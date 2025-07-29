from __future__ import annotations

import argparse
import json
import shutil
import sys
import tempfile
from pathlib import Path
from typing import Sequence

__all__ = ["classify_from_json", "main"]

repo_root = Path(__file__).resolve().parents[1]
# Insert the project root directory so the CLI packages can be imported when
# running this script from outside the repository root.
sys.path.insert(0, str(repo_root))

import torch
from torch_geometric.loader import DataLoader as GeoDataLoader
from torch_geometric.data import InMemoryDataset, HeteroData
import torch_geometric.transforms as T

from src.common.logger import get_logger

logger = get_logger(__name__)

from src.graphs.features.cache import load_tensor
from src.cli.preprocessing import run_json, run_graphs, run_embeds
from src.cli.detect import collate_graphs, infer
from src.graphs.dataset import GraphDataset
from src.models.gnn.res_wrapper import RESGCLClassifier


class SingleGraphDataset(InMemoryDataset):
    def __init__(self, graph_path: Path, embed_dir: Path | None, *, load_embeds: bool = True):
        self.graph_path = graph_path
        self.embed_dir = embed_dir
        self.load_embeds = load_embeds
        self._normalizer = T.NormalizeFeatures()
        super().__init__(None, None, None, None)

    def len(self) -> int:  # type: ignore[override]
        return 1

    def get(self, idx: int) -> HeteroData:  # type: ignore[override]
        g = torch.load(self.graph_path, map_location="cpu", weights_only=False)
        sha = self.graph_path.stem
        if self.embed_dir and self.load_embeds:
            embed_file = self.embed_dir / f"{sha}.ftr"
            if embed_file.is_file():
                feat = load_tensor(sha, self.embed_dir, mmap=False)
                store = g["token"]
                if hasattr(store, "x") and store.x is not None:
                    store.x = torch.cat([store.x, feat], dim=-1)
                else:
                    store.x = feat
            else:
                logger.warning("Embedding file missing: %s", embed_file)
        g.sha256 = sha
        g = GraphDataset._ensure_num_nodes(g)
        g = GraphDataset._ensure_x(g)
        g = GraphDataset._sanitize_edges(g)
        g = self._normalizer(g)
        return g


def preprocess(
    json_path: Path,
    work_dir: Path,
    device: str,
    *,
    model_name: str = "microsoft/codebert-base",
    attr_dim: int = 32,
    vocab_size: int = 0,
    use_embeds: bool = True,
) -> tuple[Path, str]:
    """Run preprocessing stages for a single JSON sample.

    Returns the path to the generated ``.pt`` graph file along with the sample's
    SHA256 hash.
    """
    raw_dir = work_dir / "raw"
    views_dir = work_dir / "data" / "views"
    hetero_dir = work_dir / "data" / "hetero"

    # Remove leftovers from previous runs
    for fp in raw_dir.glob("*.json"):
        fp.unlink()
    if views_dir.exists():
        for fp in views_dir.rglob("*.json"):
            fp.unlink()
    if hetero_dir.exists():
        for fp in hetero_dir.glob("*.pt"):
            fp.unlink()

    raw_dir.mkdir(parents=True, exist_ok=True)
    dst = raw_dir / json_path.name
    shutil.copy2(json_path, dst)

    with dst.open("r", encoding="utf-8") as f:
        sha = json.load(f).get("get_metadata", {}).get("sha256", dst.stem)

    common = dict(
        input_dir=str(raw_dir),
        out_dir=str(work_dir),
        workers=1,
        log_level="INFO",
        overwrite=True,
    )

    run_json(argparse.Namespace(views=["ast", "cfg", "fcg", "syscall"], **common))
    run_graphs(
        argparse.Namespace(
            normalise=True,
            rebuild=True,
            clean=True,
            with_feats=True,
            feat_policy="TRIM",
            **common,
        )
    )
    processed = skipped = 0
    if use_embeds:
        processed, skipped = run_embeds(
            argparse.Namespace(
                input_dir=None,
                model_name=model_name,
                batch_size=32,
                device=device,
                attr_dim=attr_dim,
                vocab_size=vocab_size,
                **{k: v for k, v in common.items() if k != "input_dir"},
            )
        )
        logger.info(
            "[PREPROCESS] embed creation: created=%d skipped=%d", processed, skipped
        )

    hetero_dir = work_dir / "data" / "hetero"
    graph_path = hetero_dir / f"{sha}.pt"
    if not graph_path.is_file():
        raise RuntimeError(f"Expected graph not generated: {graph_path}")
    return graph_path, sha


def classify(
    graph: Path,
    model: RESGCLClassifier,
    work_dir: Path,
    device: str,
    threshold: float,
    amp: bool,
    *,
    load_embeds: bool = True,
) -> tuple[int, float, float]:
    device_t = torch.device(device)
    model = model.to(device_t)
    model.eval()
    attr = getattr(getattr(model, "encoder", None), "attr_names", None)

    ds = SingleGraphDataset(graph, work_dir / "data" / "embeds", load_embeds=load_embeds)
    loader = GeoDataLoader(
        ds,
        batch_size=1,
        shuffle=False,
        num_workers=0,
        pin_memory=device_t.type == "cuda",
        collate_fn=lambda batch: collate_graphs(batch, attr_names=attr),
    )

    for _, pred, prob, radius in infer(model, loader, device_t, threshold, amp):
        return pred, prob, radius
    raise RuntimeError("Inference returned no results")


def classify_from_json(
    json_obj: dict,
    ckpt: Path,
    *,
    device: str = "cuda" if torch.cuda.is_available() else "cpu",
    threshold: float = 0.5,
    amp: bool = False,
    use_embeds: bool = True,
) -> tuple[int, float, float]:
    """Classify a single JSON object and return (label, prob, cert_radius)."""
    device_t = torch.device(device)
    model = RESGCLClassifier.load_from_checkpoint(ckpt, map_location=device_t)
    meta_path = ckpt.with_suffix(".meta.pkl")
    meta = {}
    if meta_path.is_file():
        try:
            from torch.serialization import add_safe_globals
            from src.graphs.normalizers.schema import NodeType

            add_safe_globals([NodeType])
            meta = torch.load(meta_path, weights_only=False)
        except Exception:
            meta = {}

    with tempfile.TemporaryDirectory() as tmpdir:
        work_dir = Path(tmpdir)
        json_path = work_dir / "sample.json"
        with json_path.open("w", encoding="utf-8") as f:
            json.dump(json_obj, f)

        graph, _ = preprocess(
            json_path,
            work_dir,
            device,
            model_name=meta.get("model_name", "microsoft/codebert-base"),
            attr_dim=int(meta.get("attr_dim", 32)),
            vocab_size=int(meta.get("vocab_size", 0)),
            use_embeds=use_embeds,
        )

        # Re-init encoder if feature dimensions do not match
        in_dims = meta.get("in_dims")
        if in_dims:
            mismatch = False
            for nt, dim in in_dims.items():
                proj = model.encoder.input_proj[nt] if nt in model.encoder.input_proj else None
                if proj is None or proj.in_features != int(dim):
                    mismatch = True
                    break
            if mismatch:
                model.reinit_input_dims(
                    in_dims,
                    attr_names=meta.get("attr_names"),
                    vocab_size=meta.get("vocab_size", 0),
                )

        pred, prob, radius = classify(
            graph,
            model,
            work_dir,
            device,
            threshold,
            amp,
            load_embeds=use_embeds,
        )
        return pred, prob, radius


def main(argv: Sequence[str] | None = None) -> None:
    p = argparse.ArgumentParser(description="Classify a single sample JSON")
    p.add_argument("--json", type=Path, help="Path to PE JSON")
    p.add_argument("--json-dir", type=Path, help="Directory of JSON samples")
    p.add_argument("--meta-csv", type=Path, help="CSV with sha256,label mapping")
    p.add_argument("--model", type=Path, required=True, help="Classifier checkpoint")
    p.add_argument("--out", type=Path, required=True, help="Output CSV path")
    p.add_argument(
        "--work-dir",
        type=Path,
        default=Path("./single_work"),
        help="Directory for intermediate files",
    )
    p.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    p.add_argument("--threshold", type=float, default=0.5)
    p.add_argument("--amp", action="store_true")
    p.add_argument(
        "--no-embeds",
        action="store_true",
        help="Skip creating and loading token embeddings",
    )
    args = p.parse_args(argv)

    if not args.json_dir and not args.json:
        p.error("--json or --json-dir required")

    json_files = []
    if args.json_dir:
        json_files.extend(sorted(Path(args.json_dir).glob("*.json")))
    if args.json:
        json_files.append(args.json)

    labels = {}
    if args.meta_csv and args.meta_csv.is_file():
        import csv

        with args.meta_csv.open("r", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                labels[row["sha256"]] = int(row["label"])

    args.out.parent.mkdir(parents=True, exist_ok=True)
    y_true = []
    y_pred = []
    use_embeds = not args.no_embeds

    with args.out.open("w", encoding="utf-8") as f:
        f.write("sha256,pred,prob,cert_radius\n")
        for json_fp in json_files:
            with json_fp.open("r", encoding="utf-8") as jf:
                js = json.load(jf)
            pred, prob, radius = classify_from_json(
                js,
                args.model,
                device=args.device,
                threshold=args.threshold,
                amp=args.amp,
                use_embeds=use_embeds,
            )
            sha = js.get("get_metadata", {}).get("sha256", json_fp.stem)
            f.write(f"{sha},{pred},{prob:.6f},{radius}\n")
            if sha in labels:
                y_true.append(labels[sha])
                y_pred.append(pred)

    if y_true:
        from sklearn.metrics import accuracy_score, f1_score

        acc = accuracy_score(y_true, y_pred)
        f1 = f1_score(y_true, y_pred)
        print(f"Accuracy: {acc:.4f}  F1: {f1:.4f}")

    print(f"[OK] saved predictions -> {args.out}")


if __name__ == "__main__":  # pragma: no cover
    main()
