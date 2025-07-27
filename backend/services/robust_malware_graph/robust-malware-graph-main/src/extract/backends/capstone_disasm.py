"""
robust-malware-graph – CapstoneDisasm backend
─────────────────────────────────────────────
Pure-Python disassembly helper built on top of **Capstone**.  It provides a
very lightweight, Angr-free fallback that still yields AST- and CFG-compatible
JSON objects so that the higher-level Extractors can keep a uniform
interface.

✔ Use-cases
~~~~~~~~~~~
* Embedded / stripped binaries where full symbolic analysis is overkill.
* Minimal Docker images where installing the entire angr stack is expensive.
* Quick triage during data collection to filter obviously broken samples.

✗ Limitations
~~~~~~~~~~~~~
* No lifter → *no* data-flow analysis (types, arguments, …).
* CFG construction relies on naïve basic-block boundaries (branch, ret).  It
  is **best-effort** and not verifier-grade.
* FCG extraction is heuristic and may miss indirect calls.

Example
~~~~~~~
>>> from pathlib import Path
>>> from src.extract.backends.capstone_disasm import CapstoneDisasm
>>> eng = CapstoneDisasm(Path("/bin/echo"), arch="x86_64")
>>> print(len(eng.build_ast()["nodes"]) , "instructions parsed")
"""

from __future__ import annotations

import logging
import mmap
import struct
import warnings
from pathlib import Path
from typing import Any, Dict, List, Tuple

try:
    import capstone as cs  # type: ignore – external
except ModuleNotFoundError as exc:  # pragma: no cover
    raise ImportError("capstone is required for CapstoneDisasm backend") from exc

try:
    import lief  # type: ignore – optional, for arch detection
except ModuleNotFoundError:  # pragma: no cover
    lief = None  # fallback

# ────────────────────────────────────────────────────────────────
# Logger helper (same style as other backends)
# ────────────────────────────────────────────────────────────────
try:
    from src.common.utils import get_logger
except ModuleNotFoundError:  # standalone fallback
    def get_logger(name: str):  # noqa: D401 (simple)
        logging.basicConfig(level=logging.INFO,
                            format="[%(levelname)s] %(name)s: %(message)s")
        return logging.getLogger(name)

_LOG = get_logger(__name__)

# ────────────────────────────────────────────────────────────────
# Capstone arch / mode mapping helper
# ────────────────────────────────────────────────────────────────
_CAPSTONE_TABLE: Dict[str, Tuple[int, int]] = {
    # name     (arch,          mode)
    "x86":     (cs.CS_ARCH_X86, cs.CS_MODE_32),
    "x86_64": (cs.CS_ARCH_X86, cs.CS_MODE_64),
    "arm":     (cs.CS_ARCH_ARM, cs.CS_MODE_ARM),
    "arm_thumb": (cs.CS_ARCH_ARM, cs.CS_MODE_THUMB),
    "aarch64": (cs.CS_ARCH_ARM64, cs.CS_MODE_ARM),
    "mips":    (cs.CS_ARCH_MIPS, cs.CS_MODE_MIPS32),
}

_BRANCH_MNEMONICS = {
    "jmp", "je", "jne", "jg", "jge", "jl", "jle", "ja", "jae", "jb", "jbe", "jo",
    "jno", "jp", "jnp", "js", "jns", "jcxz", "jecxz", "call", "ret", "retq", "br", "blr",
}

_SYSCALL_MNEMONICS = {"syscall", "int", "svc"}


# ╔═══════════════════════════════════════════════════════════════╗
# ║  Core Engine (stateless)                                      ║
# ╚═══════════════════════════════════════════════════════════════╝

class CapstoneDisasm:  # noqa: D101 – full docstring at top

    def __init__(self,
                 binary: Path | str,
                 *,
                 arch: str | None = None,
                 base_addr: int = 0x0,
                 section: str | None = None,
                 max_insns: int = 10_000_000):
        self.binary = Path(binary)
        if not self.binary.is_file():
            raise FileNotFoundError(self.binary)
        self.max_insns = max_insns
        self.base_addr = base_addr

        if arch is None:
            arch = self._auto_detect_arch(self.binary)
        if arch not in _CAPSTONE_TABLE:
            raise ValueError(f"unsupported/unknown arch: {arch}")
        self.arch_name = arch
        self.cs_arch, self.cs_mode = _CAPSTONE_TABLE[arch]
        self._md = cs.Cs(self.cs_arch, self.cs_mode)
        self._md.detail = True  # enable operand info

        self.section = section  # if None→ whole file
        _LOG.debug("CapstoneDisasm: arch=%s, section=%s", arch, section or "<all>")

    # ------------------------------------------------------------------
    @staticmethod
    def _auto_detect_arch(bin_path: Path) -> str:
        """Best-effort architecture detection using **lief** (if available)."""
        if lief is None:
            _LOG.warning("lief not installed – defaulting to x86_64")
            return "x86_64"
        try:
            binary = lief.parse(str(bin_path))
            if binary is None:  # corrupted file
                raise RuntimeError("lief.parse returned None")
            if binary.format in {lief.EXE_FORMATS.ELF, lief.EXE_FORMATS.PE, lief.EXE_FORMATS.MACHO}:
                if binary.machine_type in {lief.ELF.ARCH.x86_64, lief.PE.MACHINE_TYPES.AMD64, lief.MachO.CPU_TYPES.X86_64}:
                    return "x86_64"
                if binary.machine_type in {lief.ELF.ARCH.i386, lief.PE.MACHINE_TYPES.I386, lief.MachO.CPU_TYPES.I386}:
                    return "x86"
                if binary.machine_type in {lief.ELF.ARCH.ARM, lief.MachO.CPU_TYPES.ARM}:
                    return "arm"
                if binary.machine_type in {lief.ELF.ARCH.AARCH64, lief.MachO.CPU_TYPES.ARM64}:
                    return "aarch64"
                if binary.machine_type == lief.ELF.ARCH.MIPS:
                    return "mips"
        except Exception as exc:  # pylint: disable=broad-except
            _LOG.warning("LIEF failed to parse %s: %s", bin_path.name, exc)
        _LOG.warning("falling back to x86_64 – unable to detect arch")
        return "x86_64"

    # ------------------------------------------------------------------
    def _load_bytes(self) -> Tuple[bytes, int]:
        """Load target *section* (or full file) into memory.

        Returns (bytearray, real_base_addr)
        """
        with self.binary.open("rb") as fp:
            mm = mmap.mmap(fp.fileno(), 0, access=mmap.ACCESS_READ)
            data = bytes(mm)
        if self.section and lief is not None:
            try:
                binobj = lief.parse(str(self.binary))
                sec = next((s for s in binobj.sections if s.name == self.section), None)
                if sec:
                    _LOG.debug("disassembling section %s@0x%x", self.section, sec.virtual_address)
                    return bytes(sec.content), sec.virtual_address
            except Exception as exc:  # pylint: disable=broad-except
                _LOG.warning("failed to extract section via LIEF: %s", exc)
        return data, self.base_addr

    # ════════════════════════════════════════════════════════════
    #  Disassembly helpers
    # ════════════════════════════════════════════════════════════
    def _iter_instructions(self):  # noqa: D401
        blob, base = self._load_bytes()
        count = 0
        for ins in self._md.disasm(blob, base):
            yield ins
            count += 1
            if count >= self.max_insns:
                _LOG.warning("max_insns reached (%d) – truncating", self.max_insns)
                break

    # ════════════════════════════════════════════════════════════
    #  Public adapters (AST / CFG / FCG / Syscalls)
    # ════════════════════════════════════════════════════════════
    def build_ast(self) -> Dict[str, Any]:
        """Linear instruction stream → AST-like token list."""
        nodes: List[Dict[str, Any]] = []
        parent: int | None = None
        for idx, ins in enumerate(self._iter_instructions()):
            tokens = [ins.mnemonic] + [op.strip() for op in ins.op_str.split(',')] if ins.op_str else [ins.mnemonic]
            nodes.append({
                "id": idx,
                "type": "inst",
                "tokens": tokens,
                "parent": parent,
            })
            parent = idx  # next instruction links back
        return {"nodes": nodes, "entry": 0 if nodes else None}

    # ------------------------------------------------------------------
    def build_cfg(self) -> Dict[str, Any]:
        """Very rough basic-block graph via branch mnemonic heuristics."""
        blocks: List[Tuple[int, List[cs.CsInsn]]] = []  # (start_addr, insns)
        current: List[cs.CsInsn] = []
        start_addr = None
        for ins in self._iter_instructions():
            if start_addr is None:
                start_addr = ins.address
            current.append(ins)
            if ins.mnemonic.lower() in _BRANCH_MNEMONICS:
                blocks.append((start_addr, current))
                current = []
                start_addr = None
        if current and start_addr is not None:
            blocks.append((start_addr, current))

        nlist: List[Dict[str, Any]] = []
        elist: List[Dict[str, Any]] = []
        addr2idx: Dict[int, int] = {}
        for idx, (baddr, insns) in enumerate(blocks):
            addr2idx[baddr] = idx
            nlist.append({
                "id": idx,
                "addr": hex(baddr),
                "size": len(insns),
            })

        for idx, (_, insns) in enumerate(blocks):
            last = insns[-1]
            mnem = last.mnemonic.lower()
            if mnem.startswith("j") or mnem == "br" or mnem == "b":  # branch
                # immediate target only
                if last.operands and last.operands[0].type == cs.x86.X86_OP_IMM:
                    tgt = last.operands[0].imm
                    if tgt in addr2idx:
                        elist.append({"src": idx, "dst": addr2idx[tgt], "type": "cond"})
            if mnem == "call":
                # fall-through edge
                if idx + 1 < len(blocks):
                    elist.append({"src": idx, "dst": idx + 1, "type": "fall"})
            elif mnem not in {"ret", "retq"}:
                # not terminal → sequential edge
                if idx + 1 < len(blocks):
                    elist.append({"src": idx, "dst": idx + 1, "type": "seq"})

        return {
            "nodes": nlist,
            "edges": elist,
            "entry": 0,
        }

    # ------------------------------------------------------------------
    def build_fcg(self) -> Dict[str, Any]:
        """Heuristic function-call graph (direct *call* imm32 targets)."""
        functions: Dict[int, Dict[str, Any]] = {}
        calls: List[Dict[str, Any]] = []
        addr2id: Dict[int, int] = {}
        next_id = 0

        for ins in self._iter_instructions():
            if ins.mnemonic.lower() == "call":
                if ins.operands and ins.operands[0].type == cs.x86.X86_OP_IMM:
                    dst = ins.operands[0].imm
                    if dst not in addr2id:
                        addr2id[dst] = next_id
                        functions[next_id] = {
                            "id": next_id,
                            "name": f"sub_{dst:x}",
                            "addr": hex(dst),
                            "external": False,
                        }
                        next_id += 1
                    if ins.address not in addr2id:
                        addr2id[ins.address] = next_id
                        functions[next_id] = {
                            "id": next_id,
                            "name": f"sub_{ins.address:x}",
                            "addr": hex(ins.address),
                            "external": False,
                        }
                        next_id += 1
                    calls.append({
                        "src": addr2id[ins.address],
                        "dst": addr2id[dst],
                        "type": "direct",
                    })
        fn_list = list(functions.values())
        return {
            "functions": fn_list,
            "calls": calls,
            "entry": 0,
        }

    # ------------------------------------------------------------------
    def extract_syscalls(self) -> List[Dict[str, Any]]:
        """Scan for explicit syscall-style instructions."""
        syscalls: List[Dict[str, Any]] = []
        for ins in self._iter_instructions():
            mnem = ins.mnemonic.lower()
            if mnem in _SYSCALL_MNEMONICS:
                syscalls.append({
                    "name": mnem,
                    "addr": hex(ins.address),
                    "args": [],
                })
        return syscalls


__all__ = [
    "CapstoneDisasm",
]
# 파일 맨 아래 추가 ────────────────────────────────────────────────
from types import SimpleNamespace

def extract_ast(                       # noqa: D401
    sample_path: str | Path,
    *,
    timeout: int = 120,                # capstone 은 실시간 → 파라미터만 맞춤
    normalize_unicode: bool = True,
    keep_tmp: bool = False,
):
    """
    CapstoneDisasm 전용 AST 추출 헬퍼.
    """
    eng = CapstoneDisasm(sample_path)
    ast_dict = eng.build_ast()
    return [
        SimpleNamespace(
            name="global",
            nodes=[
                SimpleNamespace(
                    type=n["type"],
                    tokens=n["tokens"],
                    parent=n["parent"],
                )
                for n in ast_dict["nodes"]
            ],
        )
    ]

__all__.append("extract_ast")
