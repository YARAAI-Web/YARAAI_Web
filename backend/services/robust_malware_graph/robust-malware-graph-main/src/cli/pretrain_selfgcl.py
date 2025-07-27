#!/usr/bin/env python3
"""robust
malware
graph 
 SelfGraphCL Pre
training CLI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This script pre
trains the 
SelfGraphCL
 contrastive learner (ICML
20 GraphCL
variant) on heterogeneous malware graphs *offline* before supervised fine
tuning.

Highlights
----------
* **torch_geometric**
native pipeline (no DGL) compliant with project utils
* Drop
in augmentations from ``src/augment`` (**GraphCL default** + domain
specific)
* Supports **multi
GPU** training via `torch.nn.DataParallel`
* YAML **Hydra** config override friendly (see ``configs/self_gcl.yaml``)

Example
~~~~~~~
.. code:: bash

   python -m cli.pretrain_selfgcl \
          data/hetero \
          --splits data/splits/time_split_fold0.json \
          --config configs/self_gcl.yaml \
          --epochs 100 --batch-size 256 --lr 1e-3 \
          --output models/gnn/encoder.pt
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence
import warnings
from collections import defaultdict
import logging
import gc
import numpy as np

import torch
import torch.multiprocessing as mp
torch.multiprocessing.set_sharing_strategy('file_system')
from torch.serialization import add_safe_globals
from torch.utils.data import DataLoader, Dataset
from torch_geometric.data import Data, HeteroData, InMemoryDataset, Batch
import torch_geometric
import torch.nn.functional as F
from torch_geometric.loader import DataLoader as PyGLoader, DataListLoader
from tqdm import tqdm

# Project internal imports ----------------------------------------------------
from common.utils import set_random_seed, get_logger, ensure_dir
from graphs.features.cache import load_tensor, clear_memory_cache
from src.graphs.normalizers.schema import NodeType, EdgeRel, NODE_ATTRS
from augment.ops.inject_call import InjectAPICall
from augment import auto_aug  # noqa: F401 (registers policies)
from augment.basic import get_default_graphcl_transforms
from models.contrast.self_gcl import SelfGraphCL
from models.gnn.encoder import RGCNEncoder
from evaluation.metrics import Alignment, Uniformity
from graphs.dataset import collect_dataset_metadata
import matplotlib.pyplot as plt

LOGGER = get_logger(__name__)


# --------------------------------------------------------------------------- #
# Dataset stub (thin wrapper around saved PyG Data objects)
# --------------------------------------------------------------------------- #


class HeteroGraphDiskDataset(InMemoryDataset):
    """Lazy
loads torch_geometric ``Data``/``HeteroData`` pickles from ``root``."""

    #: Shared vocabulary path used when encoding string metadata.
    VOCAB_PATH = Path("models/token_vocab.json")

    def __init__(
        self,
        root: str | Path,
        sha_list: Sequence[str] | None = None,
        *,
        load_embeds: bool = True,
        embed_dir: Path | None = None,
    ):
        self.sha_list = set(sha_list) if sha_list else None
        self.load_embeds = load_embeds
        self.embed_dir = (
            Path(embed_dir) if embed_dir is not None else Path(root) / "embeds"
        )
        super().__init__(root)
        if self.VOCAB_PATH.is_file():
            with open(self.VOCAB_PATH, "r", encoding="utf-8") as f:
                self.vocab = json.load(f)
        else:
            self.vocab = {}
        meta_file = Path(self.processed_dir) / "metadata.pkl"
        if meta_file.is_file():
            try:
                add_safe_globals([NodeType])
                self._metadata = torch.load(meta_file, weights_only=False)
            except Exception:
                self._metadata = None
        else:
            self._metadata = None

        loaded = torch.load(self.processed_paths[0], weights_only=False)
        if isinstance(loaded, (list, tuple)) and len(loaded) == 4:
            self._data, self.slices, self.graph_meta, self.names = loaded
        elif isinstance(loaded, (list, tuple)) and len(loaded) == 3:
            self._data, self.slices, self.graph_meta = loaded
            self.names = [p.stem for p in sorted(Path(self.root).glob("*.pt"))]
        else:  # Backwards compatibility
            self._data, self.slices = loaded
            self.graph_meta = None
            self.names = [p.stem for p in sorted(Path(self.root).glob("*.pt"))]

        # Ensure every stored graph has an ``.x`` attribute for each node type.
        # Some legacy datasets only provide ``.feat`` which breaks newer
        # modules that expect ``.x``.  We patch the collated ``self._data`` in
        # place so that ``self.get()`` will yield graphs with the expected
        # attribute available.
        if isinstance(self._data, HeteroData):
            for ntype in self._data.node_types:
                store = self._data[ntype]
                if not hasattr(store, "x") and hasattr(store, "feat"):
                    store.x = store.feat
        else:
            if not hasattr(self._data, "x") and hasattr(self._data, "feat"):
                self._data.x = self._data.feat

    def get(self, idx):  # type: ignore[override]
        LOGGER.debug("Dataset get: index %d", idx)
        data = super().get(idx)
        if self.graph_meta is not None:
            meta = self.graph_meta[idx]
            if isinstance(data, HeteroData):
                for nt in data.node_types:
                    if nt in meta:
                        data[nt].meta = meta[nt]
            else:
                if "" in meta:
                    data.meta = meta[""]

        if isinstance(data, HeteroData):
            for nt in data.node_types:
                store = data[nt]
                if hasattr(store, "meta") and isinstance(store.meta, str):
                    try:
                        store.meta = json.loads(store.meta)
                    except json.JSONDecodeError:
                        pass
                if not hasattr(store, "x") and hasattr(store, "feat"):
                    store.x = store.feat
        else:
            if hasattr(data, "meta") and isinstance(data.meta, str):
                try:
                    data.meta = json.loads(data.meta)
                except json.JSONDecodeError:
                    pass
            if not hasattr(data, "x") and hasattr(data, "feat"):
                data.x = data.feat
        sha = self.names[idx] if idx < len(self.names) else None
        if sha is not None:
            data = self._attach_embeds(sha, data)
            data.sha256 = sha
        LOGGER.debug("Dataset get: sha=%s types=%s", sha, getattr(data, 'node_types', 'homo'))
        # 디버그 로그 추가
        if isinstance(data, HeteroData) and NodeType.TOKEN.value in data.node_types:
            token_store = data[NodeType.TOKEN.value]
            if hasattr(token_store, 'x') and token_store.x is not None and token_store.x.shape[-1] == 2:
                LOGGER.debug(f"in HeteroGraphDiskDataset.get() for {sha}:")
                LOGGER.debug(f"  token_store.x shape: {token_store.x.shape}")
                LOGGER.debug(f"  token_store.x_codebert shape: {token_store.x_codebert.shape if hasattr(token_store, 'x_codebert') else 'N/A'}")
        
        return data

    def _attach_embeds(self, sha: str, g: Data | HeteroData) -> Data | HeteroData:
        if not self.load_embeds:
            return g
        embed_file = self.embed_dir / f"{sha}.ftr"
        if not embed_file.is_file():
            return g
        if not isinstance(g, HeteroData) or NodeType.TOKEN.value not in g.node_types:
            return g
        # ``load_tensor`` uses memory mapping by default for faster feature
        # retrieval. Disable mmap to avoid hitting OS file descriptor limits.
        try:
            feat = load_tensor(sha, self.embed_dir, mmap=False)
        except Exception as exc:  # pragma: no cover - unexpected I/O errors
            warnings.warn(f"failed to load embed for {sha}: {exc}")
            return g
        store = g[NodeType.TOKEN.value]
        
        # --- [파이프라인 재설계] 임베딩을 원본 특징에 즉시 통합 ---
        if hasattr(store, "x") and store.x is not None:
            store.x = torch.cat([store.x, feat], dim=-1)
        else:
            store.x = feat
        
        if hasattr(store, "x_codebert"):
            del store.x_codebert
            
        return g

    @property
    def processed_file_names(self) -> list[str]:
        return ["graph_dataset.pt"]

    @property
    def metadata(self) -> tuple | None:
        return self._metadata

    def process(self):
        paths = sorted(Path(self.root).glob("*.pt"))
        data_list = []
        source_paths: list[Path] = []
        max_dim: dict[tuple[str, str], int] = defaultdict(int)
        meta_list: list[dict[str, str]] = []
        attr_union: dict[str, set[str]] = defaultdict(set)
        attr_example: dict[tuple[str, str], object] = {}
        meta_keys: dict[str, set[str]] = defaultdict(set)
        node_types: list[str] = []
        edge_types: list[tuple[str, str, str]] = []

        # ------------------------------------------------------------------
        # Build or load token vocabulary
        # ------------------------------------------------------------------
        if self.VOCAB_PATH.is_file():
            vocab = json.loads(self.VOCAB_PATH.read_text())
        else:
            counter: dict[str, int] = defaultdict(int)

            def _scan_strings(g: Data | HeteroData):
                if isinstance(g, HeteroData):
                    stores = [g[nt] for nt in g.node_types]
                else:
                    stores = [g]
                for st in stores:
                    for _, val in st.items():
                        if isinstance(val, str):
                            counter[val] += 1
                        elif (
                            isinstance(val, Sequence)
                            and val
                            and all(isinstance(x, str) for x in val)
                        ):
                            for t in val:
                                counter[t] += 1

            for p in paths:
                g = torch.load(p, weights_only=False)
                _scan_strings(g)

            vocab = {"<PAD>": 0}
            for tok, _ in sorted(counter.items(), key=lambda x: -x[1]):
                if tok not in vocab:
                    vocab[tok] = len(vocab)
            ensure_dir(self.VOCAB_PATH.parent)
            self.VOCAB_PATH.write_text(json.dumps(vocab))

        self.vocab = vocab

        def _encode_metadata(g: Data | HeteroData):
            """Convert string and sequence attributes to tensors or metadata.

            Every sequence attribute becomes either a tensor (numeric) or is
            serialized to ``meta``. The returned graph contains no raw Python
            lists.  Attributes not defined in :data:`NODE_ATTRS` are moved to
            ``meta`` regardless of type.
            """

            if isinstance(g, HeteroData):
                stores = {nt: g[nt] for nt in g.node_types}
            else:
                stores = {"": g}

            for ntype, st in stores.items():
                if ntype:
                    try:
                        allowed = set(NODE_ATTRS.get(NodeType(ntype), ()))
                    except ValueError:
                        allowed = None
                else:
                    allowed = None
                meta = getattr(st, "meta", {})
                if isinstance(meta, str):
                    try:
                        meta = json.loads(meta)
                    except json.JSONDecodeError:
                        meta = {}
                for attr, val in list(st.items()):
                    if allowed is not None and attr not in allowed:
                        try:
                            meta[attr] = json.dumps(val)
                        except TypeError:
                            meta[attr] = repr(val)
                        delattr(st, attr)
                        continue
                    if isinstance(val, str):
                        if attr == "addr" and val.lower().startswith("0x"):
                            try:
                                st[attr] = torch.tensor(
                                    [int(val, 16)], dtype=torch.long
                                )
                            except ValueError:
                                meta[attr] = val
                                st[attr + "_id"] = torch.tensor(
                                    [vocab.get(val, 0)], dtype=torch.long
                                )
                                delattr(st, attr)
                        else:
                            meta[attr] = val
                            st[attr + "_id"] = torch.tensor(
                                [vocab.get(val, 0)], dtype=torch.long
                            )
                            delattr(st, attr)
                    elif isinstance(val, torch.Tensor):
                        st[attr] = val.clone()
                        continue
                    elif isinstance(val, np.ndarray):
                        st[attr] = torch.as_tensor(val)
                        continue
                    elif isinstance(val, (list, tuple)):
                        if val and all(isinstance(x, str) for x in val):
                            if attr == "addr":
                                parsed: list[int] | None = []
                                for x in val:
                                    try:
                                        parsed.append(
                                            int(x, 16 if x.lower().startswith("0x") else 10)
                                        )
                                    except ValueError:
                                        parsed = None
                                        break
                                if parsed is not None:
                                    st[attr] = torch.tensor(parsed, dtype=torch.long)
                                    continue
                            meta[attr] = list(val)
                            st[attr + "_id"] = torch.tensor(
                                [vocab.get(x, 0) for x in val],
                                dtype=torch.long,
                            )
                            delattr(st, attr)
                        elif val and all(isinstance(x, (int, float)) for x in val):
                            st[attr] = torch.as_tensor(val)
                        else:
                            try:
                                meta[attr] = json.dumps(list(val))
                            except TypeError:
                                meta[attr] = repr(list(val))
                            delattr(st, attr)
                st.meta = json.dumps(meta)
            return g

        # --- load graphs & collect maximum feature dimensions ---
        for p in paths:
            sha = p.stem
            if self.sha_list and sha not in self.sha_list:
                continue
            data: Data | HeteroData = torch.load(p, weights_only=False)
            # --- migrate legacy token embedding attribute ---
            if isinstance(data, HeteroData) and NodeType.TOKEN.value in data.node_types:
                store = data[NodeType.TOKEN.value]
                if "emb" in store and "feat" not in store:
                    store.feat = store.pop("emb")
            data = _encode_metadata(data)
            data = self._attach_embeds(sha, data) # 추가된 라인

            graph_meta: dict[str, str] = {}
            if isinstance(data, HeteroData):
                for ntype in data.node_types:
                    if ntype not in node_types:
                        node_types.append(ntype)
                    store = data[ntype]
                    mval = getattr(store, "meta", "")
                    if mval:
                        try:
                            m_dict = json.loads(mval) if isinstance(mval, str) else mval
                            meta_keys[ntype].update(m_dict.keys())
                        except json.JSONDecodeError:
                            pass
                    graph_meta[ntype] = mval
                    if "meta" in store:
                        del store["meta"]
                for et in data.edge_types:
                    if et not in edge_types:
                        edge_types.append(et)
            else:
                graph_meta[""] = getattr(data, "meta", "")
                if hasattr(data, "meta"):
                    delattr(data, "meta")

            meta_list.append(graph_meta)
            data_list.append(data)
            source_paths.append(p)

            # record attribute union and example per node type
            if isinstance(data, HeteroData):
                for ntype in data.node_types:
                    store = data[ntype]
                    attr_union[ntype].update(store.keys())
                    for attr, val in store.items():
                        key = (ntype, attr)
                        if key not in attr_example:
                            attr_example[key] = val
                        if isinstance(val, torch.Tensor) and val.dim() == 2:
                            max_dim[key] = max(max_dim[key], val.size(1))
            else:
                if "" not in node_types:
                    node_types.append("")
                attr_union[""] .update(data.keys())
                for attr, val in data.items():
                    key = (
"", attr)
                    if key not in attr_example:
                        attr_example[key] = val
                    if isinstance(val, torch.Tensor) and val.dim() == 2:
                        max_dim[key] = max(max_dim[key], val.size(1))

        LOGGER.info("Loaded %d graphs from %s", len(data_list), self.root)

        # --- fill missing metadata keys ---
        for meta in meta_list:
            for ntype, keys in meta_keys.items():
                mval = meta.get(ntype, "{}")
                try:
                    m_dict = json.loads(mval) if isinstance(mval, str) else mval
                except json.JSONDecodeError:
                    m_dict = {}
                changed = False
                for k in keys:
                    if k not in m_dict:
                        m_dict[k] = None
                        changed = True
                if changed or not isinstance(mval, str):
                    meta[ntype] = json.dumps(m_dict)

        # --- fill missing attributes with defaults ---
        for g, path in zip(data_list, source_paths):
            if isinstance(g, HeteroData):
                for ntype in g.node_types:
                    store = g[ntype]
                    num_nodes = store.num_nodes if "num_nodes" in store else 0
                    for attr in attr_union[ntype]:
                        if attr in store:
                            continue
                        tmpl = attr_example.get((ntype, attr))
                        if isinstance(tmpl, torch.Tensor):
                            if tmpl.dim() == 2:
                                dim = max_dim.get((ntype, attr), tmpl.size(1))
                                store[attr] = torch.zeros(
                                    (num_nodes, dim), dtype=tmpl.dtype
                                )
                            else:
                                store[attr] = torch.zeros(
                                    (num_nodes,), dtype=tmpl.dtype
                                )
                        elif isinstance(tmpl, Sequence):
                            store[attr] = []
                        else:
                            store[attr] = torch.zeros((num_nodes,), dtype=torch.long)
                        msg = "Filled missing attribute '%s' for node type '%s' in graph %s"
                        LOGGER.warning(msg, attr, ntype, path)
                        logging.getLogger().warning(msg, attr, ntype, path)
                    try:
                        allowed = set(NODE_ATTRS.get(NodeType(ntype), ()))
                    except ValueError:
                        allowed = set()
                    if "addr" in allowed and "addr" not in store:
                        store["addr"] = torch.zeros((num_nodes,), dtype=torch.long)
                        msg = "Added missing attribute 'addr' for node type '%s' in graph %s"
                        LOGGER.warning(msg, ntype, path)
                        logging.getLogger().warning(msg, ntype, path)
            else:
                num_nodes = g.num_nodes if hasattr(g, "num_nodes") else 0
                for attr in attr_union[""]:
                    if attr in g:
                        continue
                    tmpl = attr_example.get(("", attr))
                    if isinstance(tmpl, torch.Tensor):
                        if tmpl.dim() == 2:
                            dim = max_dim.get(("", attr), tmpl.size(1))
                            g[attr] = torch.zeros((num_nodes, dim), dtype=tmpl.dtype)
                        else:
                            g[attr] = torch.zeros((num_nodes,), dtype=tmpl.dtype)
                    elif isinstance(tmpl, Sequence):
                        g[attr] = []
                    else:
                        g[attr] = torch.zeros((num_nodes,), dtype=torch.long)
                    LOGGER.warning(
                        "Filled missing attribute '%s' in graph %s",
                        attr,
                        path,
                    )

        # --- [FIX] Add 'api' to schema to prevent UserWarning ---
        if NodeType.API.value not in node_types:
            node_types.append(NodeType.API.value)

        # --- ensure num_nodes recorded for all node types ---
        for g in data_list:
            if isinstance(g, HeteroData):
                for ntype in node_types:
                    store = g[ntype]
                    if "num_nodes" not in store:
                        store.num_nodes = 0
            else:
                if "num_nodes" not in g:
                    g.num_nodes = 0

        # --- ensure all graphs have every edge type ---
        for g in data_list:
            if not isinstance(g, HeteroData):
                continue
            for et in edge_types:
                if et not in g.edge_types:
                    g[et].edge_index = torch.empty((2, 0), dtype=torch.long)
                    g[et].edge_type = torch.empty((0,), dtype=torch.long)

        # --- pad each tensor attribute to the maximum dimension ---
        for g in data_list:
            if isinstance(g, HeteroData):
                for ntype in g.node_types:
                    store = g[ntype]
                    for attr, val in list(store.items()):
                        if isinstance(val, torch.Tensor) and val.dim() == 2:
                            target = max_dim[(ntype, attr)]
                            if val.size(1) < target:
                                pad = target - val.size(1)
                                store[attr] = F.pad(val, (0, pad))
            else:
                for attr, val in list(g.items()):
                    if isinstance(val, torch.Tensor) and val.dim() == 2:
                        target = max_dim[("", attr)]
                        if val.size(1) < target:
                            pad = target - val.size(1)
                            g[attr] = F.pad(val, (0, pad))

        try:
            data, slices = self.collate(data_list)
        except KeyError as exc:
            missing_attr = exc.args[0]
            LOGGER.error("Collation failed: missing attribute '%s'", missing_attr)
            for path, g in zip(source_paths, data_list):
                if isinstance(g, HeteroData):
                    for ntype in g.node_types:
                        if missing_attr not in g[ntype]:
                            LOGGER.error(
                                "Graph %s missing attribute '%s' for node type '%s'",
                                path,
                                missing_attr,
                                ntype,
                            )
                else:
                    if missing_attr not in g:
                        LOGGER.error(
                            "Graph %s missing attribute '%s'", path, missing_attr
                        )
            raise KeyError(
                f"Collation failed due to missing attribute '{missing_attr}'. "
                "Some node features may be missing."
            ) from exc
        names = [p.stem for p in source_paths]
        torch.save((data, slices, meta_list, names), self.processed_paths[0])
        meta_path = Path(self.processed_dir) / "metadata.pkl"
        self._metadata = (tuple(node_types), tuple(edge_types))
        try:
            torch.save(self._metadata, meta_path)
        except Exception as exc:  # pragma: no cover - safeguard
            LOGGER.warning("Failed to save metadata: %s", exc)
        self.graph_meta = meta_list
        self.names = names


def validate_dataset(dataset: HeteroGraphDiskDataset) -> bool:
    """Return ``True`` if all graphs share the same attribute set and relation indices."""
    paths = sorted(Path(dataset.root).glob("*.pt"))
    ref: dict[str, set[str]] | None = None
    ok = True
    max_rel_index = -1
    for p in paths:
        g = torch.load(p, weights_only=False)
        attrs: dict[str, set[str]] = {}
        if isinstance(g, HeteroData):
            for nt in g.node_types:
                a = set(g[nt].keys())
                a.discard("meta")
                attrs[nt] = a
            for et in g.edge_types:
                store = g[et]
                if hasattr(store, "edge_type") and store.edge_type.numel() > 0:
                    max_rel_index = max(max_rel_index, int(store.edge_type.max()))
        else:
            a = set(g.keys())
            a.discard("meta")
            attrs[""] = a
            if hasattr(g, "edge_type") and g.edge_type.numel() > 0:
                max_rel_index = max(max_rel_index, int(g.edge_type.max()))
        if ref is None:
            ref = attrs
        elif attrs != ref:
            LOGGER.warning("Attribute set mismatch in %s", p)
            ok = False
    if not ok:
        LOGGER.warning(
            "Dataset has inconsistent attributes. Run with --reprocess to rebuild."
        )
    if dataset.metadata is not None and max_rel_index >= 0:
        num_relations = len(dataset.metadata[1])
        if max_rel_index >= num_relations:
            LOGGER.error(
                "Edge relation index %d out of range (metadata defines %d relations). "
                "Re-run with --reprocess to rebuild metadata.",
                max_rel_index,
                num_relations,
            )
            logging.getLogger().error(
                "Edge relation index %d out of range (metadata defines %d relations). "
                "Re-run with --reprocess to rebuild metadata.",
                max_rel_index,
                num_relations,
            )
            ok = False
    return ok


# --------------------------------------------------------------------------- #
# Training utilities
# --------------------------------------------------------------------------- #


def train_epoch(
    model: SelfGraphCL,
    loader: DataLoader,
    device: torch.device,
    args: argparse.Namespace,
    *,
    optimizer: torch.optim.Optimizer,
    epoch: int,
    transform,
    target_node: str | None,
    log_interval: int = 50,
):
    model.train()
    total_loss = 0.0
    align = Alignment()
    uni = Uniformity()
    LOGGER.debug(f"--- train_epoch {epoch} started ---")
    progress_bar = tqdm(loader, desc=f"Epoch {epoch}", leave=False)
    for step, batch_data in enumerate(progress_bar):
        LOGGER.debug(f"Batch {step}: Loaded from DataLoader.")

        graphs: list[Data | HeteroData] = []
        first_item = batch_data[0] if isinstance(batch_data, list) else batch_data

        if isinstance(batch_data, list):
            if args.list_loader:
                graphs = [itm[0] for itm in batch_data] # Extract graph from (graph, label, sha) tuple
            else:
                for itm in batch_data:
                    if isinstance(itm, (Data, HeteroData)):
                        graphs.append(itm)
                    elif isinstance(itm, (tuple, list)) and len(itm) == 3:
                        graphs.append(itm[0])
                    elif isinstance(itm, dict) and "graph" in itm:
                        graphs.append(itm["graph"])
                    else:
                        LOGGER.warning(
                            "Batch %d: Unexpected item type %s; skipping", step, type(itm)
                        )
            if not graphs:
                LOGGER.warning("Batch %d: No valid graphs found, skipping", step)
                continue
        else:
            batch = batch_data
            if not isinstance(batch, (Data, HeteroData)):
                if isinstance(batch, dict) and "graph" in batch:
                    batch = batch["graph"]
                else:
                    LOGGER.error(
                        f"Batch {step}: Unexpected data type from loader: {type(batch)}"
                    )
                    continue
            graphs = batch.to_data_list()

        sha = None
        if isinstance(first_item, (tuple, list)) and len(first_item) == 3:
            sha = first_item[2]
        elif isinstance(first_item, dict):
            if "ids" in first_item and isinstance(first_item["ids"], Sequence):
                sha = first_item["ids"][0]
            elif "sha256" in first_item:
                sha = first_item["sha256"]
        if sha is None and hasattr(graphs[0], "sha256"):
            sha = getattr(graphs[0], "sha256")
        if sha is None:
            sha = f"unknown_sha_at_step_{step}"
        LOGGER.debug(f"Batch {step}: Processing graph {sha}. Applying transforms...")

        view1_list = []
        view2_list = []
        try:
            for g in graphs:
                v1, v2 = transform(g)
                view1_list.append(v1)
                view2_list.append(v2)
            LOGGER.debug(f"Batch {step}: Graph {sha} transformed successfully.")
        except Exception as e:
            LOGGER.error(f"CRASH during transform of graph {sha}: {e}", exc_info=True)
            raise

        LOGGER.debug(f"Batch {step}: Collating augmented views for graph {sha}...")
        view1 = Batch.from_data_list(view1_list).to(device)
        view2 = Batch.from_data_list(view2_list).to(device)
        LOGGER.debug(f"Batch {step}: Views moved to device. Executing model forward pass for {sha}...")
        
        optimizer.zero_grad(set_to_none=True)
        
        out = model(view1, view2, return_emb=True)
        loss = out["loss"]
        emb = out["emb"]
        LOGGER.debug(f"Batch {step}: Forward pass for {sha} complete. Loss: {loss.item()}.")

        # --- [표현 붕괴 진단] ---
        # 임베딩의 표준 편차를 로깅하여, 출력이 모두 동일해지는 현상을 감지합니다.
        # 표준 편차가 0에 가��우면, 모델이 의미있는 학습을 하지 못하고 있다는 신호입니다.
        emb_std = emb.std().item()
        # tqdm 진행률 표시줄에 정보 업데이트
        progress_bar.set_postfix(loss=loss.item(), emb_std=emb_std)

        # 기존 로그는 DEBUG 레벨로 변경
        LOGGER.debug(
            "Epoch %d | Step %d/%d | Loss %.4f | Emb Std: %.6f",
            epoch,
            step + 1,
            len(loader),
            loss.item(),
            emb_std
        )

        B = emb.size(0) // 2
        align.update(emb[:B], emb[B:])
        uni.update(emb)
        
        LOGGER.debug(f"Batch {step}: Backward pass for {sha} starting...")
        loss.backward()
        LOGGER.debug(f"Batch {step}: Backward pass for {sha} complete.")
        
        optimizer.step()

        total_loss += loss.item()

        # Explicitly free GPU memory to avoid accumulation
        del view1, view2, out, emb, loss
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        clear_memory_cache()

    clear_memory_cache()
    avg = total_loss / len(loader)
    return avg, {"alignment": align.compute(), "uniformity": uni.compute()}


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser("SelfGraphCL pretraining")
    p.add_argument("graph_dir", type=Path, help="Directory with *.pt Graph pickles")
    p.add_argument(
        "--splits",
        type=Path,
        required=True,
        help="JSON dict with keys train/val/test [sha]",
    )
    p.add_argument("--config", type=Path, default=Path("configs/self_gcl.yaml"))
    p.add_argument("--epochs", type=int, default=100)
    p.add_argument("--batch-size", type=int, default=256)
    p.add_argument("--lr", type=float, default=1e-3)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--gpu", type=int, default=0, help="CUDA device id (1 CPU)")
    p.add_argument("--num-workers", type=int, default=4)
    p.add_argument(
        "--list-loader",
        action="store_true",
        help="Use DataListLoader instead of PyGLoader (workaround for batch crashes)",
    )
    p.add_argument(
        "--embed-dir",
        type=Path,
        default=None,
        help="Directory with cached token embeddings (default: <graph_dir>/embeds)",
    )
    p.add_argument(
        "--strict-metadata",
        action="store_true",
        help="Raise error on invalid edge_type indices in graphs",
    )
    p.add_argument(
        "--output", type=Path, required=True, help="Path to save encoder weights (\.pt)"
    )
    p.add_argument("--plot-path", type=Path, help="Path to save training plot (.png)")
    p.add_argument(
        "--save-every", type=int, default=10, help="Checkpoint interval (epochs)"
    )
    p.add_argument(
        "--reprocess",
        action="store_true",
        help="Rebuild processed dataset when attribute mismatch is detected",
    )
    return p.parse_args()


def main():
    args = parse_args()
    # PyArrow can segfault with fork; ensure safer spawn start method
    mp.set_start_method("spawn", force=True)
    set_random_seed(args.seed)
    logging.getLogger().setLevel(logging.INFO) # 루트 로거 레벨을 INFO로 설정

    # --------------------------------------------------------------------- #
    # Device & Logging
    # --------------------------------------------------------------------- #
    LOGGER.info("--- Starting Pre-training ---")
    LOGGER.info(f"Graph directory: {args.graph_dir}")
    LOGGER.info(f"Embeddings directory: {args.embed_dir}")
    LOGGER.info(f"Batch size: {args.batch_size}, Epochs: {args.epochs}")

    device = torch.device(
        f"cuda:{args.gpu}" if args.gpu >= 0 and torch.cuda.is_available() else "cpu"
    )
    LOGGER.info("Using device: %s", device)
    LOGGER.info("PyTorch version: %s", torch.__version__)
    LOGGER.info("PyG version: %s", getattr(torch_geometric, "__version__", "n/a"))

    # --------------------------------------------------------------------- #
    # Dataset & Loader
    # --------------------------------------------------------------------- #
    LOGGER.info("Step 1: Loading splits file...")
    if not args.splits.is_file():
        LOGGER.error(
            "Splits file %s not found. Generate it using split_generator.py (e.g. `python -m graphs.dataset.split_generator`).",
            args.splits,
        )
        raise SystemExit(1)
    split_json = json.loads(Path(args.splits).read_text())
    train_shas = split_json["train"]
    val_shas = split_json.get("val")
    LOGGER.info(f"Loaded {len(train_shas)} train samples and {len(val_shas) if val_shas else 0} validation samples.")

    LOGGER.info("Step 2: Initializing training dataset...")
    try:
        train_ds = HeteroGraphDiskDataset(
            args.graph_dir, sha_list=train_shas, embed_dir=args.embed_dir
        )
        LOGGER.info("Training dataset initialized.")
    except Exception as e:
        LOGGER.error(f"Error initializing training dataset: {e}", exc_info=True)
        raise

    val_ds = None
    if val_shas:
        LOGGER.info("Step 2b: Initializing validation dataset...")
        try:
            val_ds = HeteroGraphDiskDataset(
                args.graph_dir, sha_list=val_shas, embed_dir=args.embed_dir
            )
            LOGGER.info("Validation dataset initialized.")
        except Exception as e:
            LOGGER.error(f"Error initializing validation dataset: {e}", exc_info=True)
            raise

    LOGGER.info("Step 3: Validating and potentially reprocessing dataset...")
    if not validate_dataset(train_ds):
        if args.reprocess:
            LOGGER.info("Attribute mismatch detected. Reprocessing dataset...")
            try:
                train_ds.process()
                train_ds = HeteroGraphDiskDataset(
                    args.graph_dir, sha_list=train_shas, embed_dir=args.embed_dir
                )
                LOGGER.info("Dataset reprocessed successfully.")
            except Exception as e:
                LOGGER.error(f"Error during dataset reprocessing: {e}", exc_info=True)
                raise
        else:
            LOGGER.warning(
                "Attribute mismatch detected. Re-run with --reprocess to rebuild"
            )

    LOGGER.info("Step 4: Creating DataLoader...")
    try:
        loader_cls = DataListLoader if args.list_loader else PyGLoader
        train_loader = loader_cls(
            train_ds,
            batch_size=args.batch_size,
            shuffle=True,
            num_workers=args.num_workers,
            pin_memory=(device.type == "cuda"),
        )
        LOGGER.info("DataLoader created successfully.")
    except Exception as e:
        LOGGER.error(f"Error creating DataLoader: {e}", exc_info=True)
        raise

    # --------------------------------------------------------------------- #
    # Model & Optimizer
    # --------------------------------------------------------------------- #
    LOGGER.info("Step 5: Setting up the model...")
    try:
        datasets = [train_ds]
        if val_ds is not None:
            datasets.append(val_ds)
        
        params, target_node, meta_info = _load_model_hparams(
            args.config,
            datasets, # train_ds와 val_ds를 모두 전달
            vocab_size=len(train_ds.vocab),
            strict=args.strict_metadata,
            use_embed_dir=args.embed_dir is not None
        )
        model = SelfGraphCL(**params)
        LOGGER.info("SelfGCL model created.")

        if device.type == "cuda" and torch.cuda.device_count() > 1:
            LOGGER.info(f"Using {torch.cuda.device_count()} GPUs for DataParallel.")
            model = torch.nn.DataParallel(model)
        
        model.to(device)
        LOGGER.info("Model moved to device.")

        optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr)
        scheduler = _build_scheduler(args.config, optimizer, args.epochs)
        LOGGER.info("Optimizer and scheduler created.")
    except Exception as e:
        LOGGER.error(f"Error during model setup: {e}", exc_info=True)
        raise

    # --------------------------------------------------------------------- #
    # Training Loop
    # --------------------------------------------------------------------- #
    LOGGER.info("Step 6: Starting training loop...")
    best_loss = float("inf")
    best_encoder_state = None
    ensure_dir(args.output.parent)
    plot_path = args.plot_path if args.plot_path else args.output.with_suffix(".png")
    ensure_dir(plot_path.parent)
    loss_hist, align_hist, uni_hist = [], [], []
    schedule = _load_aug_schedule(args.config)

    try:
        for epoch in range(1, args.epochs + 1):
            LOGGER.info(f"--- Epoch {epoch}/{args.epochs} Started ---")
            ops = _ops_for_epoch(schedule, epoch)
            transform = (
                _make_transform(ops, target_node)
                if ops
                else get_default_graphcl_transforms(target_node=target_node)
            )
            LOGGER.info("Using augmentation ops: %s", ops if ops else ["default"])
            train_ds.transform = transform
            
            # Re-create loader to apply new transform
            loader_cls = DataListLoader if args.list_loader else PyGLoader
            train_loader = loader_cls(
                train_ds,
                batch_size=args.batch_size,
                shuffle=True,
                num_workers=args.num_workers,
                pin_memory=(device.type == "cuda"),
            )

            epoch_loss, metrics = train_epoch(
                model,
                train_loader,
                device,
                args,
                optimizer=optimizer,
                epoch=epoch,
                transform=transform,
                target_node=target_node,
            )
            LOGGER.info(
                "Epoch %d finished | AvgLoss %.4f Alignment %.4f Uniformity %.4f",
                epoch,
                epoch_loss,
                metrics["alignment"],
                metrics["uniformity"],
            )
            loss_hist.append(epoch_loss)
            align_hist.append(metrics["alignment"])
            uni_hist.append(metrics["uniformity"])

            if epoch % args.save_every == 0 or epoch == args.epochs:
                ckpt_path = args.output.with_suffix(f".e{epoch}.pt")
                torch.save(model.state_dict(), ckpt_path)
                LOGGER.info("Saved checkpoint %s", ckpt_path)
            
            if epoch_loss < best_loss:
                best_loss = epoch_loss
                # Save the best model state in memory
                best_encoder_state = (model.module.encoder if hasattr(model, "module") else model.encoder).state_dict()
                LOGGER.info(f"New best loss: {best_loss:.4f}. Best model state updated.")

            if scheduler is not None:
                if isinstance(scheduler, torch.optim.lr_scheduler.ReduceLROnPlateau):
                    scheduler.step(epoch_loss)
                else:
                    scheduler.step()
                LOGGER.info("Scheduler step taken.")

    except KeyboardInterrupt:
        LOGGER.warning("--- Training interrupted by user ---")
    except Exception as e:
        LOGGER.error(f"An unexpected error occurred during training: {e}", exc_info=True)
        raise
    finally:
        LOGGER.info("--- Pre-training Finished or Interrupted ---")

        # --------------------------------------------------------------------- #
        # Plotting and Saving
        # --------------------------------------------------------------------- #
        if loss_hist:
            LOGGER.info(f"Step 7: Saving training plot to {plot_path}")
            plt.figure()
            epochs_range = range(1, len(loss_hist) + 1)
            plt.plot(epochs_range, loss_hist, label="Loss")
            plt.plot(epochs_range, align_hist, label="Alignment")
            plt.plot(epochs_range, uni_hist, label="Uniformity")
            plt.xlabel("Epoch")
            plt.legend()
            plt.savefig(plot_path)
            LOGGER.info("Plot saved.")
        else:
            LOGGER.info("No training history to plot.")

        if best_encoder_state:
            LOGGER.info("Saving best encoder weights...")
            torch.save({"model": best_encoder_state, "attr_names": meta_info.get("attr_names")}, args.output)
            
            meta_output_path = Path(args.output).with_suffix(".meta.pkl")
            try:
                torch.save(meta_info, meta_output_path)
                LOGGER.info(f"Meta info saved to {meta_output_path}")
            except Exception as exc:
                LOGGER.warning("Failed to save meta snapshot: %s", exc)
            LOGGER.info("Pretraining completed  BestLoss %.4f  Saved %s", best_loss, args.output)
        else:
            LOGGER.warning("No best model state to save. Was training started?")


# --------------------------------------------------------------------------- #
# Helper
# --------------------------------------------------------------------------- #


def _load_model_hparams(
    cfg_path: Path,
    datasets: Sequence[Dataset],
    *,
    vocab_size: int = 0,
    strict: bool = False,
    use_embed_dir: bool = False
) -> tuple[dict, str | None, dict]:
    """Return ``SelfGraphCL`` kwargs loaded from ``cfg_path`` and datasets.

    Expected YAML ``model`` keys are a subset of
    ``hidden_dim``, ``num_layers``, ``out_dim``, ``dropout``, ``proj_dim``,
    ``temperature``, ``gather_distributed`` and ``target_node``.  Unknown keys
    (e.g. ``name`` or ``backbone``) are ignored.

    Node feature dimensions are inferred from ``datasets`` using
    :func:`collect_dataset_metadata`.  When an API node type required by
    augmentation is missing, it is added automatically.
    """
    LOGGER.info(">> Entering _load_model_hparams...")
    try:
        import yaml  # Lazy import (PyYAML optional)

        with open(cfg_path, "r", encoding="utf-8") as f:
            cfg = yaml.safe_load(f) or {}
        LOGGER.info("YAML config loaded.")
    except ModuleNotFoundError:
        LOGGER.warning("PyYAML not installed - using default hyper-params")
        cfg = {}

    model_cfg = dict(cfg.get("model", {}))
    for key in ("name", "backbone"):
        model_cfg.pop(key, None)

    encoder_args = {}
    for k in (
        "hidden_dim",
        "num_layers",
        "out_dim",
        "dropout",
        "residual",
        "target_node",
    ):
        if k in model_cfg:
            encoder_args[k] = model_cfg.pop(k)

    attr_dim = int(model_cfg.get("attr_dim", 32))
    
    LOGGER.info(">> Calling collect_dataset_metadata...")
    metadata, in_dims, raw_feat_dim, attr_names, max_ids = collect_dataset_metadata(
        datasets,
        attr_dim=attr_dim,
        strict=strict,
    )
    LOGGER.info("<< collect_dataset_metadata finished.")
    LOGGER.info(f"[METADATA] `in_dims` from collector: {in_dims}")
    LOGGER.info(f"[METADATA] `attr_names` from collector: {attr_names}")

    # ensure API node/edge types for augmentation
    if metadata[0]:
        node_types, edge_types = map(list, metadata)
        api_nt = NodeType.API.value
        if api_nt not in node_types:
            node_types.append(api_nt)
            in_dims[api_nt] = InjectAPICall.DEFAULT_FEAT_DIM
        api_edge = (NodeType.BB.value, EdgeRel.CALLS.value, api_nt)
        if api_edge not in edge_types:
            edge_types.append(api_edge)
        metadata = (tuple(node_types), tuple(edge_types))
    
    LOGGER.info(">> Creating RGCNEncoder instance...")
    target_node = encoder_args.get("target_node")
    
    # --- [강건성 개선 최종안] ---
    # Gated Fusion 경로에서 사용하는 "원본 피처"의 차원은, 모든 속성 임베딩이 합쳐진
    # '최종' 차원입니다. 이 정보는 `in_dims`에 이미 정확하게 계산되어 있습니다.
    # 따라서 `token_original_dim`에 `raw_feat_dim`이 아닌 `in_dims`의 값을 전달하여
    # 모델의 모든 경로가 일관된 차원 정보를 사용하도록 합니다.
    token_original_dim = in_dims.get(NodeType.TOKEN.value) if use_embed_dir else None

    encoder = RGCNEncoder(
        metadata=metadata,
        in_dims=in_dims,
        attr_names=attr_names if attr_names else None,
        vocab_size=vocab_size,
        attr_dim=attr_dim,
        codebert_dim=768 if use_embed_dir else None,
        token_original_dim=token_original_dim, # 'token'의 '최종' 원본 피처 차원(예: 66)을 명시적으로 전달
        **encoder_args,
    )
    LOGGER.info("<< RGCNEncoder instance created.")

    params = {
        "encoder": encoder,
        "proj_dim": model_cfg.pop("proj_dim", 256),
        "temperature": cfg.get("loss", {}).get("temperature", 0.2),
        "gather_distributed": model_cfg.pop("gather_distributed", False),
    }
    meta_info = {
        "node_types": list(metadata[0]),
        "edge_types": [tuple(e) for e in metadata[1]],
        "in_dims": {k: int(v) for k, v in in_dims.items()},
        "num_relations": len(metadata[1]),
        "vocab_size": vocab_size,
        "attr_names": attr_names,
        "attr_dim": attr_dim,
        "max_ids": {k: int(v) for k, v in max_ids.items()},
        "hidden_dim": encoder_args.get("hidden_dim", 128),
        "num_layers": encoder_args.get("num_layers", 2),
        "out_dim": encoder_args.get("out_dim", 256),
        "target_node": target_node,
    }
    LOGGER.info("<< Exiting _load_model_hparams.")
    return params, target_node, meta_info


def _build_scheduler(
    cfg_path: Path,
    optimizer: torch.optim.Optimizer,
    epochs: int
) -> torch.optim.lr_scheduler.LRScheduler | None:
    """Instantiate LR scheduler from YAML configuration.

    Supported scheduler names are ``cosine``, ``cyclic`` and ``plateau``.  Any
    additional keys in the ``scheduler`` section of ``cfg_path`` are passed to
    the underlying PyTorch scheduler.
    """
    try:
        import yaml

        with open(cfg_path, "r", encoding="utf-8") as f:
            cfg = yaml.safe_load(f) or {}
    except ModuleNotFoundError:
        LOGGER.warning("PyYAML not installed - no scheduler configured")
        return None

    sched_cfg = cfg.get("scheduler")
    if not sched_cfg:
        return None

    name = str(sched_cfg.get("name", "")).lower()
    params = {k: v for k, v in sched_cfg.items() if k != "name"}

    if name == "cosine":
        warmup = int(params.pop("warmup_epochs", 0))
        total = int(params.pop("total_epochs", epochs))
        eta_min = float(params.pop("eta_min", 0.0))
        cosine = torch.optim.lr_scheduler.CosineAnnealingLR(
            optimizer, T_max=max(1, total - warmup), eta_min=eta_min, **params
        )
        if warmup > 0:
            linear = torch.optim.lr_scheduler.LinearLR(
                optimizer, start_factor=1e-6, end_factor=1.0, total_iters=warmup
            )
            scheduler = torch.optim.lr_scheduler.SequentialLR(
                optimizer, schedulers=[linear, cosine], milestones=[warmup]
            )
        else:
            scheduler = cosine
    elif name == "cyclic":
        scheduler = torch.optim.lr_scheduler.CyclicLR(optimizer, **params)
    elif name == "plateau":
        scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, **params)
    else:
        LOGGER.warning("Unknown scheduler '%s'", name)
        return None
    return scheduler


def _load_aug_schedule(cfg_path: Path) -> list[dict]:
    """Return augmentation schedule from YAML or empty list."""
    try:
        import yaml

        with open(cfg_path, "r", encoding="utf-8") as f:
            cfg = yaml.safe_load(f) or {}
    except ModuleNotFoundError:
        LOGGER.warning("PyYAML not installed - using default augmentation")
        return []

    schedule = cfg.get("aug_schedule", [])
    if not isinstance(schedule, list):
        LOGGER.warning("aug_schedule must be a list of entries")
        return []
    schedule.sort(key=lambda x: int(x.get("start", 0)))
    return schedule


def _make_transform(ops: list[str], target_node: str | None):
    """Return ``StandardPair`` with only selected ops enabled."""
    from augment.basic import get_default_graphcl_transforms
    from augment.view_generators.standard_pair import StandardPair

    base = get_default_graphcl_transforms(target_node=target_node)

    all_names = {op.__class__.__name__ for op in base.ops_a + base.ops_b}
    for name in ops:
        if name not in all_names:
            LOGGER.warning("unknown op %s in schedule", name)

    def filter_ops(op_list):
        return [op for op in op_list if op.__class__.__name__ in ops]

    pair = StandardPair(filter_ops(base.ops_a), filter_ops(base.ops_b))
    LOGGER.info("Transform ops: %s", ops)
    return pair


def _ops_for_epoch(schedule: list[dict], epoch: int) -> list[str]:
    """Return list of op names active for ``epoch``."""
    for item in schedule:
        start = int(item.get("start", 0))
        end = int(item.get("end", 10**9))
        if start <= epoch <= end:
            ops = item.get("ops", [])
            return [str(op) for op in ops]
    return []

if __name__ == "__main__":    main()