# src/models/gnn/encoder.py
"""
RGCNEncoder
-----------
Heterogeneous graph encoder that maps a `torch_geometric.data.HeteroData`
object to a fixed
size embedding per graph. It is the backbone used in the
Self
GCL 
 SupCon 
 RES
GCL pipeline.

Pipeline
~~~~~~~~
1. Per
node
type **input projection**  
 `hidden_dim`
2. Stacked **RGCNConv** layers (`num_layers`)
   
 optional **Residual + Norm** via `ResidualNorm`
3. **Global mean
pool** over a chosen `target_node` type
4. Final **linear projection**  
 `out_dim` (default 256)

Example
~~~~~~~
```python
encoder = RGCNEncoder(
    metadata=data.metadata(),
    in_dims={"bb": 128, "fn": 64, "str": 32},
    hidden_dim=128,
    num_layers=3,
    out_dim=256,
    target_node="bb",
)
emb = encoder(data)  # (batch, 256)
```
"""
from __future__ import annotations

import logging
from src.common.utils import get_logger

LOGGER = get_logger(__name__)
from typing import Callable, Dict, Optional

import torch
import torch.nn.functional as F
from torch import Tensor, nn
from torch_geometric.nn import GraphConv, global_mean_pool, HeteroConv
from src.graphs.normalizers.schema import NodeType, EdgeRel

try:
    from .layers.residual_norm import ResidualNorm
except ImportError:
    ResidualNorm = None

class RGCNEncoder(nn.Module):
    def __init__(self, *, metadata, in_dims: Dict[str, int], attr_names: Dict[str, list[str]] | None = None, vocab_size: int = 0, attr_dim: int = 32, hidden_dim: int = 128, num_layers: int = 2, out_dim: int = 256, dropout: float = 0.1, residual: bool = True, target_node: Optional[str] = None, **kwargs):
        super().__init__()
        # **kwargs를 통해 이전 버전의 불필요한 파라미터(codebert_dim, token_original_dim 등)를 받아 무시합니다.
        if kwargs:
            LOGGER.warning(f"[RGCNEncoder.__init__] 사용되지 않는 파라미터가 전달되었습니다: {list(kwargs.keys())}")

        node_types, edge_types_raw = metadata
        self.metadata = (list(node_types), list(edge_types_raw))
        self.node_types = list(node_types)
        
        if isinstance(metadata, tuple) and len(metadata) == 2:
            node_types, edge_types_raw = metadata
        else:
            node_types = metadata.node_types
            edge_types_raw = metadata.edge_types

        self.edge_types = []
        for et in edge_types_raw:
            converted_et = tuple(e.value if hasattr(e, 'value') else e for e in et)
            self.edge_types.append(converted_et)
        
        self.node_types = [nt.value if hasattr(nt, 'value') else nt for nt in node_types]
        LOGGER.debug(f"[RGCNEncoder.__init__] Converted self.edge_types: {self.edge_types}")
        self.target_node = target_node or self.node_types[0]
        
        self.input_proj = nn.ModuleDict()
        self.attr_names = attr_names or {nt: [] for nt in node_types}
        logging.debug(f"[RGCNEncoder.__init__] Final self.attr_names: {self.attr_names}")
        self.attr_dim = attr_dim
        self.meta_embed = nn.Embedding(vocab_size, attr_dim) if vocab_size > 0 else None
        logging.debug(f"[RGCNEncoder.__init__] vocab_size: {vocab_size}, attr_dim: {attr_dim}, self.meta_embed is None: {self.meta_embed is None}")
        
        # --- [파이프라인 재설계] __init__의 책임 단일화 ---
        for nt in node_types:
            base_feat_dim = in_dims.get(nt, 0)
            
            # --- [최종 수정] ---
            # meta_embed 계층이 실제로 존재할 때만 차원을 더하도록 수정합니다.
            # 이를 통해 __init__과 forward의 논리를 완벽하게 동기화합니다.
            if self.meta_embed is not None:
                num_meta_attrs = len(self.attr_names.get(nt, []))
                total_input_dim = base_feat_dim + num_meta_attrs * self.attr_dim
            else:
                total_input_dim = base_feat_dim

            if total_input_dim == 0:
                logging.debug(f"[RGCNEncoder.__init__] 경고: 노드 타입 '{nt}'의 최종 계산된 입력 차원이 0입니다.")

            proj = nn.Linear(total_input_dim, hidden_dim)
            nn.init.xavier_uniform_(proj.weight)
            nn.init.zeros_(proj.bias)
            self.input_proj[nt] = proj
            
            # 로그 메시지를 더 명확하게 수정합니다.
            if self.meta_embed is not None:
                num_meta_attrs = len(self.attr_names.get(nt, []))
                logging.debug(f"[RGCNEncoder.__init__] 노드 타입 '{nt}': 프로젝션 계층이 최종 입력 차원 {total_input_dim} (순수+임베딩: {base_feat_dim}, 메타: {num_meta_attrs}*{self.attr_dim})으로 초기화되었습니다.")
            else:
                logging.debug(f"[RGCNEncoder.__init__] 노드 타입 '{nt}': 프로젝션 계층이 최종 입력 차원 {total_input_dim} (메타데이터 임베딩 없음)으로 초기화되었습니다.")

        self.convs = nn.ModuleList()
        for _ in range(num_layers):
            conv = HeteroConv({
                et: GraphConv(hidden_dim, hidden_dim) for et in self.edge_types
            }, aggr='sum')
            self.convs.append(conv)

        self.act = F.relu
        self.drop = nn.Dropout(dropout) if dropout > 0.0 else nn.Identity()
        self.out_proj = nn.Linear(hidden_dim, out_dim)
        nn.init.xavier_uniform_(self.out_proj.weight)
        nn.init.zeros_(self.out_proj.bias)
        self.out_dim = out_dim

    def forward(
        self,
        g: HeteroData,
        edge_weight_dict: dict[str, Tensor] | None = None,
    ) -> Tensor:
        device = next(self.parameters()).device
        g = g.to(device, non_blocking=True)
        if edge_weight_dict is not None:
            edge_weight_dict = {k: v.to(device) for k, v in edge_weight_dict.items()}

        x_dict = {}
        for nt in g.node_types:
            # --- [파이프라인 재설계] forward의 역할 단순화 ---
            # forward는 .x 특징과 메타데이터 임베딩을 조합하여 최종 특징 텐서를 만들고,
            # 준비된 프로젝션 계층에 전달하는 역할만 수행합니다.
            
            # 1. 베이스 특징(.x)을 가져옵니다. GraphDataset에서 이미 모든 특징이 통합되었습니다.
            if hasattr(g[nt], "x") and g[nt].x is not None:
                feats_to_combine = [g[nt].x]
            else:
                LOGGER.warning(f"[RGCNEncoder.forward] 경고: 노드 타입 '{nt}'에 '.x' 특징이 없습니다. 건너뜁니다.")
                continue

            # 2. 메타데이터 임베딩을 가져와 합칩니다.
            if self.meta_embed:
                for name in self.attr_names.get(nt, []):
                    attr_key = f"{name}_id"
                    attr = getattr(g[nt], attr_key, None)
                    if attr is not None and attr.numel() > 0:
                        feats_to_combine.append(self.meta_embed(attr))
                    else:
                        # ID가 없는 경우, 0으로 채워진 임베딩을 추가하여 차원을 맞춥니다.
                        num_nodes = g[nt].num_nodes
                        padding_indices = torch.zeros(num_nodes, dtype=torch.long, device=feats_to_combine[0].device)
                        feats_to_combine.append(self.meta_embed(padding_indices))

            # 3. 모든 특징을 최종적으로 하나로 합칩니다.
            # 이 로직은 __init__에서 total_input_dim을 계산한 방식과 완벽하게 일치합니다.
            final_feat = torch.cat(feats_to_combine, dim=-1) if len(feats_to_combine) > 1 else feats_to_combine[0]
            
            # 4. 준비된 프로젝션 계층에 전달하기 전, 차원 불일치에 대응하는 방어 코드를 추가합니다.
            proj_layer = self.input_proj[nt]
            expected_dim = proj_layer.in_features
            actual_dim = final_feat.size(-1)

            if actual_dim != expected_dim:
                log_message = (
                    f"[RGCNEncoder.forward] 노드 타입 '{nt}'의 차원 불일치 발견! "
                    f"모델 기대 차원: {expected_dim}, 실제 입력 차원: {actual_dim}. "
                    "차원을 동적으로 조정합니다."
                )
                LOGGER.debug(log_message)

                if actual_dim < expected_dim:
                    # 실제 차원이 더 작으면 0으로 패딩합니다.
                    padding_size = expected_dim - actual_dim
                    final_feat = F.pad(final_feat, (0, padding_size), "constant", 0)
                else:
                    # 실제 차원이 더 크면 기대 차원에 맞게 자릅니다.
                    final_feat = final_feat[:, :expected_dim]
            
            final_feat = final_feat.to(proj_layer.weight.device)
            x_dict[nt] = proj_layer(final_feat)

        for i, conv in enumerate(self.convs):
            try:
                if edge_weight_dict is None:
                    collected_weights = {
                        et: g[et].edge_weight
                        for et in g.edge_types
                        if hasattr(g[et], "edge_weight")
                    }
                else:
                    collected_weights = edge_weight_dict

                if collected_weights:
                    x_dict = conv(
                        x_dict,
                        g.edge_index_dict,
                        edge_weight_dict=collected_weights,
                    )
                else:
                    x_dict = conv(x_dict, g.edge_index_dict)
            except Exception as e:
                LOGGER.info(f"오류 발생: conv 레이어 {i} 실행 중 에러가 발생했습니다: {e}")
                LOGGER.info("오류 발생 시점의 데이터 정보:")
                LOGGER.info("========================================")
                LOGGER.info("x_dict 정보 (노드 타입별 특징 텐서):")
                for nt_err, x_err in x_dict.items():
                    LOGGER.info(f"  - 노드 타입: {nt_err}, 특징 텐서 shape: {x_err.shape}")
                
                LOGGER.info("\ndata.edge_index_dict 정보 (엣지 타입별 인덱스):")
                for et, edge_index in g.edge_index_dict.items():
                    try:
                        edge_index_cpu = edge_index.cpu()
                        min_idx = edge_index_cpu.min().item() if edge_index_cpu.numel() > 0 else 'N/A'
                        max_idx = edge_index_cpu.max().item() if edge_index_cpu.numel() > 0 else 'N/A'
                        src_node_type, _, dst_node_type = et
                        src_num_nodes = g.num_nodes_dict.get(src_node_type, 'N/A')
                        dst_num_nodes = g.num_nodes_dict.get(dst_node_type, 'N/A')

                        LOGGER.info(f"  - 엣지 타입: {et}")
                        LOGGER.info(f"    - shape: {edge_index.shape}")
                        LOGGER.info(f"    - min/max: {min_idx} / {max_idx}")
                        LOGGER.info(f"    - 출발 노드({src_node_type}) 수: {src_num_nodes}, 도착 노드({dst_node_type}) 수: {dst_num_nodes}")
                        
                        if isinstance(max_idx, int) and isinstance(src_num_nodes, int) and max_idx >= src_num_nodes:
                            LOGGER.warning(f"    - [경고] 출발 노드 인덱스({max_idx})가 노드 수({src_num_nodes})의 범위를 벗어났습니다!")
                        if isinstance(max_idx, int) and isinstance(dst_num_nodes, int) and max_idx >= dst_num_nodes:
                             LOGGER.warning(f"    - [경고] 도착 노드 인덱스({max_idx})가 노드 수({dst_num_nodes})의 범위를 벗어났습니다!")

                    except Exception as cpu_e:
                        LOGGER.info(f"  - 엣지 타입: {et}")
                        LOGGER.info(f"    - [오류] edge_index를 CPU로 옮기는 중 에러 발생: {cpu_e}")
                        LOGGER.info(f"    - edge_index shape: {edge_index.shape if hasattr(edge_index, 'shape') else 'N/A'}")

                LOGGER.info("\ndata.num_nodes_dict 정보 (노드 타입별 노드 수):")
                LOGGER.info(f"  {g.num_nodes_dict}")
                LOGGER.info("========================================")
                LOGGER.info("오류 로깅을 마치고 학습을 중단합니다.")
                raise e
            x_dict = {key: self.drop(self.act(x)) for key, x in x_dict.items()}

        target_feats = x_dict.get(self.target_node)
        if target_feats is None:
            num_graphs = g.num_graphs if hasattr(g, 'num_graphs') else 1
            if not x_dict:
                 device = next(self.parameters()).device
                 return torch.zeros((num_graphs, self.out_dim), device=device)
            return x_dict[list(x_dict.keys())[0]].new_zeros((num_graphs, self.out_dim))

        batch_vec = g[self.target_node].batch if hasattr(g[self.target_node], 'batch') else None

        g_emb = global_mean_pool(target_feats, batch_vec, size=g.num_graphs if hasattr(g, 'num_graphs') else None)
        
        return self.out_proj(g_emb)
    
    @classmethod
    def load_from_checkpoint(cls, path, *, map_location=None, **kwargs):
        raise NotImplementedError("Loading from old checkpoint is not supported after HeteroConv change.")