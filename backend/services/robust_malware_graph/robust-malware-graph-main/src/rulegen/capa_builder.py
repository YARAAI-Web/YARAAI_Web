#  ───────────────────────────────────────────────────────────────
#  robust-malware-graph / src / rulegen / capa_builder.py
#  ───────────────────────────────────────────────────────────────
"""
CAPA Rule Builder
=================

• 주요 기능
    1. `tokens_to_capa(tokens: Iterable[str]) -> str`
       ‑ RL‑토큰 시퀀스를 **CAPA YAML** 룰 텍스트로 역‑변환
    2. `CapaBuilder`
       ‑ 룰 이름·scope·condition 방식(any/all/percentage) 구성 가능
       ‑ `validate()`로 PyYAML 기반 구문 간이 검사(선택 의존)
    3. CLI 스모크‑테스트
       ‑ `python -m rulegen.capa_builder "call : CreateFileW import : WS2_32 . dll"`

• CAPA 룰 최소 구조
    rule:
      meta:
        name: <auto>
        scope: file             # file/function/basic_block
        authors: [RL‑Agent]
        date: YYYY‑MM‑DD
      features:
        - and:
          - <feature1>
          - <feature2>
          ...
"""
from __future__ import annotations

import argparse
import datetime as _dt
import logging
import random
import re
import string
import uuid
import json
import subprocess
import shutil
from pathlib import Path
from typing import Iterable, List, Optional, Sequence, Tuple

try:
    import yaml  # type: ignore
except ModuleNotFoundError:  # optional
    yaml = None

try:
    from transformers import PreTrainedTokenizer
except ModuleNotFoundError:
    PreTrainedTokenizer = None

# ──────────────────────────────────────── 로깅
_LOG = logging.getLogger(__name__)
if not _LOG.handlers:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")

# ╔══════════════════════════════════════════════════════════════╗
# ║                 토큰 → 피처 추출 공통 유틸                    ║
# ╚══════════════════════════════════════════════════════════════╝
_PUNCT_CLOSE = {":", ".", ",", ")", "]", "}"}
_PUNCT_OPEN = {"(", "[", "{"}


def _token_is_atom(tok: str) -> bool:
    """CAPA feature가 될 만한 원자적 토큰 여부."""
    if len(tok) < 3 or any(c in string.whitespace for c in tok):
      return False
    return True


def _gather_atoms(tokens: Sequence[str]) -> List[str]:
    """
    RL‑토큰 시퀀스에서 'call : CreateFileW' → 'call:CreateFileW' 식으로 복원.
    구두점·중복 제거 & 순서 유지.
    """
    atoms: List[str] = []
    i, N = 0, len(tokens)
    while i < N:
        tok = tokens[i]
        # 패턴 ① '<A>' ':' '<B>' → 'A:B'
        if i + 2 < N and tokens[i + 1] == ":" and _token_is_atom(tok):
            atoms.append(f"{tok}:{tokens[i + 2]}")
            i += 3
            continue
        # 패턴 ② '<A>' '.' '<B>' → 'A.B'  (kernel32 ! CreateFileW ⇒ kernel32.CreateFileW 와 같이)
        if i + 2 < N and tokens[i + 1] == "." and _token_is_atom(tok):
            atoms.append(f"{tok}.{tokens[i + 2]}")
            i += 3
            continue
        if _token_is_atom(tok) and tok not in _PUNCT_CLOSE and tok not in _PUNCT_OPEN:
            atoms.append(tok)
        i += 1
    # 중복 제거 (stable)
    seen = set()
    uniq = []
    for a in atoms:
        if a not in seen:
            uniq.append(a)
            seen.add(a)
    return uniq


# ╔══════════════════════════════════════════════════════════════╗
# ║                    CAPA Feature 매핑 로직                    ║
# ╚══════════════════════════════════════════════════════════════╝
def _map_atom_to_feature(atom: str) -> Tuple[str, str]:
    """
    atom → (feat_type, value) 쌍 반환.
    CAPA syntax 예)
      - api: CreateFile
      - string: "%TEMP%"
      - import: WS2_32.dll
      - bytes: 4d 5a
    """
    # 1) call:XYZ  → api
    if atom.lower().startswith("call:"):
        val = atom.split(":", 1)[1]
        # kernel32!CreateFileW → CreateFileW
        if "!" in val:
            val = val.split("!", 1)[1]
        return "api", val

    # 2) syscall:NtOpenProcess → api
    if atom.lower().startswith("syscall:"):
        val = atom.split(":", 1)[1]
        return "api", val

    # 3) import:ws2_32.dll → import
    if atom.lower().startswith("import:"):
        return "import", atom.split(":", 1)[1]

    # 4) string literals  → string
    if atom.startswith('"') and atom.endswith('"'):
        # strip quotes, remove CAPA‑불가 옵션(wide/ascii 등)
        val = atom.strip('"')
        # 첫 200 byte 제한(가독성)
        return "string", val[:200]

    # 5) byte[..]:4D 5A …  → bytes
    if atom.lower().startswith("byte"):
        # {...}:{HEX...}
        try:
            hex_pat = atom.split(":", 1)[1]
        except IndexError:
            hex_pat = atom
        return "bytes", hex_pat.lower()

    # 6) path|reg|url:VALUE → string
    if atom.lower().startswith(("path:", "reg:", "url:")):
        return "string", atom.split(":", 1)[1]

    # fallback: treat as string (best‑effort)
    return "string", atom


# ╔══════════════════════════════════════════════════════════════╗
# ║                       Builder 클래스                         ║
# ╚══════════════════════════════════════════════════════════════╝
class CapaBuilder:
    """
    RL‑토큰 시퀀스 → 간단 CAPA YAML 룰 생성기
    """

    def __init__(
        self,
        *,
        rule_name_prefix: str = "auto_capa",
        scope: str = "file",  # file | function | basic_block
        tokenizer: Optional[PreTrainedTokenizer] = None,
    ) -> None:
        self.rule_name_prefix = rule_name_prefix
        self.scope = scope
        if self.scope not in {"file", "function", "basic_block"}:
            raise ValueError("scope must be file|function|basic_block")
        self.tokenizer = tokenizer

    # ───────────────────────────────────────── public API ───────
    def build(self, tokens: Sequence[str]) -> str:
        """
        토큰 시퀀스 → CAPA YAML 문자열
        """
        atoms = _gather_atoms(tokens)
        if not atoms:
            atoms = ["dummy_feature_that_never_matches"]

        # chain:FeatureA→FeatureB pattern → sequence feature
        seq_pairs: List[List[Tuple[str, str]]] = []
        rest_atoms: List[str] = []
        for atom in atoms:
            if atom.startswith("chain:") and "→" in atom:
                partA, partB = atom[len("chain:") :].split("\u2192", 1)
                if not partA.startswith("call:"):
                    partA = "call:" + partA
                if not partB.startswith("call:"):
                    partB = "call:" + partB
                seq_pairs.append([
                    _map_atom_to_feature(partA),
                    _map_atom_to_feature(partB),
                ])
            else:
                rest_atoms.append(atom)

        atoms = rest_atoms
        features_yaml: List[str] = []
        for seq in seq_pairs:
            features_yaml.append("      - sequence:")
            for ftype, val in seq:
                if any(c in val for c in ":{}[]#,&*?|-<>=!%@`\\\"' \t"):
                    val = f'"{val}"'
                features_yaml.append(f"        - {ftype}: {val}")

        features_yaml.extend(self._atoms_to_features_yaml(atoms))

        # 메타정보
        ts = _dt.datetime.utcnow().strftime("%Y-%m-%d")
        rand = random.randint(0, 9999)
        rule_name = f"{self.rule_name_prefix}_{rand:04}"

        meta_yaml = (
            f"  meta:\n"
            f"    id: {uuid.uuid4()}\n"
            f"    name: {rule_name}\n"
            f"    scope: {self.scope}\n"
            f"    authors: [RL-Agent]\n"
            f"    date: {ts}\n"
        )

        # 조립
        rule_yaml_lines = ["rule:", meta_yaml, "  features:", "    - and:"]
        rule_yaml_lines.extend(features_yaml)
        # ensure newline at end
        return "\n".join(rule_yaml_lines) + "\n"

    def validate(self, rule_text: str) -> Tuple[bool, str | None]:
        """
        PyYAML 파싱으로 구문 오류만 간단 체크.
        capa‑py 엔진 전체 의존성은 요구하지 않음.
        """
        if yaml is None:
            return False, "PyYAML not installed"

        try:
            yaml.safe_load(rule_text)
            return True, None
        except Exception as e:  # pylint: disable=broad-except
            return False, str(e)

    def load(self, path: Path) -> None:
        """Load CAPA rules from a YAML file."""
        text = Path(path).read_text(encoding="utf-8")
        if yaml is not None:
            try:
                docs = [d for d in yaml.safe_load_all(text) if d]
                self.rule_count = len(docs)
            except Exception as exc:  # pragma: no cover - best effort
                _LOG.warning("capa yaml parse failed: %s", exc)
                self.rule_count = text.count("rule:")
        else:
            self.rule_count = text.count("rule:")
        self._loaded = text

    def match_file(self, sample_path: Path) -> bool:
        """Return ``True`` if any loaded rule matches ``sample_path``."""

        if not getattr(self, "_loaded", None):
            return False

        rule_text = self._loaded

        # Try the python API first as it's faster than spawning a process.
        try:  # pragma: no cover - optional dependency
            import capa.main as capa_main  # type: ignore
        except Exception:  # pragma: no cover - python API missing
            capa_main = None

        if capa_main is not None:
            import io
            import sys
            import tempfile
            rule_path = None
            try:
                with tempfile.NamedTemporaryFile("w", suffix=".yml", delete=False) as tmp:
                    tmp.write(rule_text)
                    tmp.flush()
                    rule_path = tmp.name

                buf = io.StringIO()
                old_out = sys.stdout
                sys.stdout = buf
                rc = 0
                try:
                    capa_main.main([str(sample_path), "-r", rule_path, "--json"])
                except SystemExit as e:  # pragma: no cover - capa exits normally
                    rc = int(e.code) if isinstance(e.code, int) else 1
                finally:
                    sys.stdout = old_out

                if rc != 0:
                    return False

                try:
                    js = json.loads(buf.getvalue())
                except Exception:
                    return False
                finally:
                    if rule_path:
                        Path(rule_path).unlink(missing_ok=True)

                return bool(js.get("rules"))
            finally:
                if rule_path:
                    Path(rule_path).unlink(missing_ok=True)

        # Fallback to capa CLI
        exe = shutil.which("capa")
        if not exe:
            return False

        import tempfile

        with tempfile.NamedTemporaryFile("w", suffix=".yml", delete=False) as tmp:
            tmp.write(rule_text)
            tmp.flush()
            rule_path = tmp.name

        try:
            proc = subprocess.run(
                [exe, str(sample_path), "-r", rule_path, "--json"],
                capture_output=True,
                text=True,
                check=False,
            )
        except FileNotFoundError:
            return False
        finally:
            Path(rule_path).unlink(missing_ok=True)

        if proc.returncode != 0:
            return False
        try:
            js = json.loads(proc.stdout)
        except Exception:
            return False
        return bool(js.get("rules"))

    # ────────────────────────────── 내부 헬퍼 ───────────────────
    def _atoms_to_features_yaml(self, atoms: List[str]) -> List[str]:
        """
        • 각 atom → '- <type>: <value>' YAML 라인
        • 들여쓰기 8 칸 유지
        """
        lines: List[str] = []
        for atom in atoms:
            ftype, val = _map_atom_to_feature(atom)
            # YAML 문자열에서 따옴표 필요 여부 판별
            if any(c in val for c in ":{}[]#,&*?|-<>=!%@`\\\"' \t"):
                val = f'"{val}"'  # 안전하게 감싸기
            lines.append(f"      - {ftype}: {val}")
        return lines


# ╔══════════════════════════════════════════════════════════════╗
# ║                 외부 노출 편의 함수 (tokens→rule)            ║
# ╚══════════════════════════════════════════════════════════════╝
def tokens_to_capa(tokens: Iterable[str], tokenizer: Optional[PreTrainedTokenizer] = None) -> str:
    """
    즉시 사용 가능한 helper
    """
    builder = CapaBuilder(tokenizer=tokenizer)
    return builder.build(list(tokens))


# ╔══════════════════════════════════════════════════════════════╗
# ║                          CLI 테스트                          ║
# ╚══════════════════════════════════════════════════════════════╗
def _cli():
    """
    사용 예
    -------
    $ python -m rulegen.capa_builder "call : CreateFileW import : WS2_32 . dll"
    """
    parser = argparse.ArgumentParser(description="CAPA Builder CLI")
    parser.add_argument("tokens", nargs="+", help="space‑separated token list")
    args = parser.parse_args()

    builder = CapaBuilder(scope="file")
    rule_text = builder.build(args.tokens)
    print(rule_text)

    ok, err = builder.validate(rule_text)
    if ok:
        print("[validate] YAML syntax")
    else:
        print(f"[validate] skipped / failed: {err}")


if __name__ == "__main__":
    _cli()
