"""
src.graphs.normalizers.schema
=============================

프로젝트 전반에서 **공통으로 쓰는 그래프 스키마 정의**.

1. NodeType / EdgeRel  ── Enum 기반 문자열 상수
2. NODE_TYPE_ID, EDGE_REL_ID  ── 정수 매핑(dict)
3. EDGE_TYPES          ── PyG HeteroData용 (src, rel, dst) 튜플 모음
4. NODE_ATTRS          ── 노드 타입별 허용/권장 속성 키 화이트리스트
5. 헬퍼                ── `is_valid_node_type`, `edge_rel_id`, …

모든 서브모듈(AST/CFG/FCG/SysCall 등)의 **정규화 단계**에서
이 스키마를 참조해 노드·엣지 타입 및 속성 이름을 맞춥니다.
"""

from __future__ import annotations

from enum import Enum
from typing import Dict, Final, Sequence, Tuple

# --------------------------------------------------------------------------- #
# 1. 노드 / 엣지 열거
# --------------------------------------------------------------------------- #
class NodeType(str, Enum):
    TOKEN     = "token"     # AST 토큰
    BB        = "bb"        # BasicBlock
    FUNCTION  = "function"
    SYSCALL   = "syscall"
    IMPORT    = "import"    # 외부 API / DLL
    EXPORT    = "export"
    PEHEADER  = "pe_header" # PE/ELF 헤더 필드
    SECTION   = "section"   # .text, .data …
    STRING    = "string"
    API       = "api"       # 구체적 API 노드 (printf 등)


class EdgeRel(str, Enum):
    CHILD        = "child"        # AST 부모→자식
    CFG          = "cfg"          # 제어 흐름
    CALLS        = "calls"        # 함수 호출
    HAS          = "has"          # 포함 관계 (fn→bb)
    SEQ          = "seq"          # 순차 (syscall trace)
    IMPORTS      = "imports"      # 함수→import/API
    REF          = "ref"          # 간접 참조(사용)
    JUMP         = "jump"         # 무조건 분기
    COND         = "conditional"  # 조건 분기
    FALLTHROUGH  = "fallthrough"  # 조건 미충족 직행


# --------------------------------------------------------------------------- #
# 2. 문자열 ↔ 정수 ID 매핑
#    - GNN Embedding (edge_type embedding 등)에 활용
# --------------------------------------------------------------------------- #
NODE_TYPE_ID: Final[Dict[str, int]] = {
    t.value: i for i, t in enumerate(NodeType)
}

EDGE_REL_ID: Final[Dict[str, int]] = {
    r.value: i for i, r in enumerate(EdgeRel)
}


# --------------------------------------------------------------------------- #
# 3. PyG HeteroData edge 튜플 정의
# --------------------------------------------------------------------------- #
EDGE_TYPES: Final[Tuple[Tuple[str, str, str], ...]] = (
    (NodeType.TOKEN,     EdgeRel.CHILD,    NodeType.TOKEN),
    (NodeType.BB,        EdgeRel.CFG,      NodeType.BB),
    (NodeType.FUNCTION,  EdgeRel.CALLS,    NodeType.FUNCTION),
    (NodeType.FUNCTION,  EdgeRel.HAS,      NodeType.BB),
    (NodeType.SYSCALL,   EdgeRel.SEQ,      NodeType.SYSCALL),
    (NodeType.FUNCTION,  EdgeRel.IMPORTS,  NodeType.API),
    (NodeType.BB,        EdgeRel.REF,      NodeType.STRING),
    (NodeType.FUNCTION,  EdgeRel.CHILD,    NodeType.TOKEN),
    (NodeType.TOKEN,     EdgeRel.CHILD,    NodeType.FUNCTION),
    (NodeType.SYSCALL,   EdgeRel.CHILD,    NodeType.TOKEN), # 추가된 부분
    # 필요 시 추가 …
)


# --------------------------------------------------------------------------- #
# 4. 노드 타입별 허용/권장 속성 키
#    - 정규화 시 해당 키만 남기거나, 누락 시 zero-vector 채움
# --------------------------------------------------------------------------- #
NODE_ATTRS: Final[Dict[NodeType, Sequence[str]]] = {
    NodeType.TOKEN:    ("tok_id", "pos", "feat", "addr", "text", "num_nodes"),
    NodeType.BB:       ("feat", "addr", "inst_cnt", "num_nodes"),
    NodeType.FUNCTION: ("feat", "addr", "name", "is_external", "num_nodes"),
    NodeType.SYSCALL:  ("feat", "addr", "name", "num_nodes"),
    NodeType.IMPORT:   ("dll", "ordinal", "num_nodes"),
    NodeType.SECTION:  ("name", "size", "num_nodes"),
    NodeType.STRING:   ("slen", "num_nodes"),
    NodeType.PEHEADER: ("numeric", "num_nodes"),
    NodeType.EXPORT:   ("num_nodes",),
    NodeType.API:      ("num_nodes",),
}


# --------------------------------------------------------------------------- #
# 5. 헬퍼 함수
# --------------------------------------------------------------------------- #
def is_valid_node_type(t: str) -> bool:
    """주어진 문자열이 정의된 NodeType 인가?"""
    return t in NODE_TYPE_ID


def is_valid_edge_rel(r: str) -> bool:
    """주어진 문자열이 정의된 EdgeRel 인가?"""
    return r in EDGE_REL_ID


def node_type_id(t: str) -> int:
    """NodeType 문자열 → int (KeyError 발생 가능)"""
    return NODE_TYPE_ID[t]


def edge_rel_id(r: str) -> int:
    """EdgeRel 문자열 → int"""
    return EDGE_REL_ID[r]
