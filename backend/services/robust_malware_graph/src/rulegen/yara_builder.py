#  ───────────────────────────────────────────────────────────────
#  robust-malware-graph / src / rulegen / yara_builder.py
#  ───────────────────────────────────────────────────────────────
"""
YARA Rule Builder
=================

• 핵심 기능
    1. **`tokens_to_yara(tokens: List[str]) -> str`**
       ‑ 토큰 시퀀스를 YARA룰 문자열로 변환
       ‑ 프로젝트의 RL‑에이전트가 바로 호출해 사용
    2. **`YaraBuilder`클래스**
       ‑ 룰 이름·조건 방식(ANY/ALL/포함 퍼센트) 등 파라미터화
       ‑ `validate(rule)`: yara‑python(선택)으로 구문 검사
    3. **CLI**
       ‑ `python -m rulegen.yara_builder "call : CreateFileW import : WS2_32 . dll"`
         → 완성된 룰 프린트 + 컴파일 OK여부

• 설계 원칙
    ─────────────────────────────────────────────────────────────
    *프로젝트 요구*: RL토큰화(`RuleGenEnv._rule_tokenize`)와 **역변환** 가능해야 함
    →토큰 사이 간격·구두점 복원 로직 포함.

    *YARA 간단 skeleton*
        rule auto_rule_<timestamp> {
          strings:
            $s0 = "token0" nocase ascii
            ...
          condition:
            <cond_type> of them
        }

    *의존성 최소화*: yara‑python은 선택 사항. 설치되어 있지 않을 경우
    `validate()`는`False, "yara module not available"` 반환.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import logging
import random
import re
import string
import math
import itertools
from pathlib import Path
from typing import Iterable, List, Optional, Sequence, Tuple

try:
    import yara  # type: ignore
except ModuleNotFoundError:  # optional
    yara = None

try:
    from transformers import PreTrainedTokenizer
except ModuleNotFoundError:
    PreTrainedTokenizer = None

# ──────────────────────────────────────── 로깅 헬퍼
_LOG = logging.getLogger(__name__)
if not _LOG.handlers:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")


# ╔══════════════════════════════════════════════════════════════╗
# ║                  핵심 유틸: 토큰 ↔ 텍스트 복원                 ║
# ╚══════════════════════════════════════════════════════════════╝
_PUNCT = {":", ",", ".", ";", ")", "]", "}", "?", "!"}
_OPEN_PUNCT = {"(", "[", "{"}
_WHITESPACE_RX = re.compile(r"\s+")

# Pre-existing YARA string literal with allowed modifiers
_YARA_STR_MOD_RX = re.compile(
    r'^"(?P<content>(?:[^"\\]|\\.)*)"(?P<mods>(?:\s+(?:wide|ascii|nocase))*)$'
)


def _token_is_feature(tok: str) -> bool:
    """Return True if ``tok`` resembles a feature string.

    The original logic rejected tokens shorter than three characters and
    filtered out anything containing whitespace.  This caused perfectly
    valid short hints such as ``pe`` to be dropped.  Tokens are now trimmed
    and allowed when at least two characters long, ignoring spaces but still
    excluding control characters.
    """

    tok = tok.strip()
    if len(tok) < 2:
        return False
    if not any(c.isalnum() for c in tok):
        return False
    if any(ord(c) < 32 for c in tok):
        return False
    return True


# ╔══════════════════════════════════════════════════════════════╗
# ║                     YaraBuilder 클래스                       ║
# ╚══════════════════════════════════════════════════════════════╝
class YaraBuilder:
    """
    token 시퀀스를 YARA룰 문자열로 변환.
    """

    def __init__(
        self,
        *,
        rule_name_prefix: str = "auto_rule",
        condition_type: str = "any",  # "any" | "all" | "percentage" | "count" | "combo"
        percentage: int = 70,  # condition_type=="percentage" 일 때
        min_count: int | None = None,
        group_percentage: int | None = None,
        group_min_count: int | None = None,
        group_min_count_ratio: float = 0.0,
        auto_group_min: bool = True,
        adjust_group_percentage: bool = False,
        tokenizer: Optional[PreTrainedTokenizer] = None,
        strip_prefix: bool = True,
    ) -> None:
        self.rule_name_prefix = rule_name_prefix
        self.condition_type = condition_type
        self.percentage = percentage
        self.min_count = min_count
        if self.condition_type not in {"any", "all", "percentage", "count", "combo"}:
            raise ValueError("condition_type must be any|all|percentage|count|combo")
        if self.condition_type == "combo" and group_percentage is not None and group_min_count is not None:
            raise ValueError("Specify only one of group_percentage or group_min_count")
        self.tokenizer = tokenizer
        self.strip_prefix = strip_prefix
        self.group_percentage = group_percentage
        self.group_min_count = group_min_count
        self.group_min_count_ratio = group_min_count_ratio
        self.auto_group_min = auto_group_min
        self.adjust_group_percentage = adjust_group_percentage

    def _scaled_group_percentage(self, n_feats: int) -> int:
        """Return adjusted group percentage based on feature count."""
        if not self.adjust_group_percentage or self.group_percentage is None:
            return self.group_percentage or 0
        if n_feats <= 0:
            return self.group_percentage
        scaled = int(round(self.group_percentage / math.sqrt(n_feats)))
        scaled = max(1, min(self.group_percentage, scaled))
        return scaled

    def _group_required(self, n_feats: int) -> int:
        """Return minimum required matches for a feature group."""
        if n_feats <= 0:
            return 0

        if self.auto_group_min and self.group_min_count_ratio > 0:
            req = max(1, math.ceil(n_feats * self.group_min_count_ratio))
            if self.group_min_count is not None:
                req = max(req, self.group_min_count)
            if n_feats <= 3:
                req = min(req, 1 if n_feats <= 2 else 2)
            return min(req, n_feats)

        if self.group_min_count is not None:
            req = max(int(n_feats * self.group_min_count_ratio), self.group_min_count or 0)
            return min(req, n_feats)

        if self.group_min_count_ratio > 0:
            req = max(1, math.ceil(n_feats * self.group_min_count_ratio))
            return min(req, n_feats)

        return 1

    def _detokenize(self, tokens: Sequence[str]) -> str:
        """
        RL 토큰 시퀀스 → 사람이 읽는 단일 문자열.
        간단한 규칙:
          • 여는 괄호 앞 공백 제거
          • 닫는 구두점 앞 공백 제거
          • 기타 토큰은 한 칸 공백으로 구분
        """
        if self.tokenizer:
            # Use the tokenizer's convert_tokens_to_string for better accuracy
            return self.tokenizer.convert_tokens_to_string(list(tokens))

        out: List[str] = []
        for i, tok in enumerate(tokens):
            if i == 0:
                out.append(tok)
                continue
            prev = tokens[i - 1]
            if tok in _PUNCT:
                # 직전 단어와 붙임
                out[-1] = out[-1] + tok
            elif tok in _OPEN_PUNCT:
                # 여는 괄호는 뒤에 붙임
                out.append(tok)
            elif prev in _OPEN_PUNCT:
                # 괄호 바로 뒤 토큰 – 앞에 공백 X
                out.append(tok)
            else:
                out.append(" " + tok)
        return "".join(out)

    # ──────────────────────────────────────────── public api ──
    def build(
        self, tokens: Sequence[str], *, return_map: bool = False
    ) -> str | Tuple[str, dict[str, str]]:
        """Return a YARA rule text assembled from ``tokens``.

        Parameters
        ----------
        tokens : Sequence[str]
            Input token sequence.
        return_map : bool, optional
            When ``True`` also return a mapping from generated string
            identifiers (e.g. ``"$s0"``) to the originating feature.
        """
        # 1) rule name
        ts = _dt.datetime.utcnow().strftime("%Y%m%d%H%M%S")
        rand = random.randint(0, 9999)
        rule_name = f"{self.rule_name_prefix}_{ts}_{rand:04}"

        # 2) feature 선정
        unique_feats = self._extract_features(tokens)
        if not unique_feats:
            for tok in tokens:
                if _token_is_feature(tok):
                    unique_feats = [tok]
                    break
        if not unique_feats:
            unique_feats = ["dummy_token_unlikely_to_match"]

        # chain 처리 – "chain:A→B" 를 분리해 call prefix 보정
        processed: List[str] = []
        for feat in unique_feats:
            if feat.startswith("chain:") and "→" in feat:
                rest = feat[len("chain:") :]
                partA, partB = rest.split("→", 1)
                if not partA.startswith("call:"):
                    partA = "call:" + partA
                if not partB.startswith("call:"):
                    partB = "call:" + partB
                processed.extend([partA, partB])
            else:
                processed.append(feat)

        # 중복 제거, 순서 유지
        seen = set()
        unique_feats = []
        for f in processed:
            if f not in seen:
                unique_feats.append(f)
                seen.add(f)

        # 3) strings section
        strings_section_lines = []
        groups: dict[str, list[str]] = {}
        id_map: dict[str, str] = {}
        if self.condition_type == "combo":
            prefix_map = {"call:": "c", "import:": "i", "marker:": "m"}
            for feat in unique_feats:
                tag = "o"
                for p, t in prefix_map.items():
                    if feat.startswith(p):
                        tag = t
                        break
                idx = len(groups.setdefault(tag, []))
                ident = f"${tag}{idx}"
                yara_str = self._to_yara_string(feat)
                strings_section_lines.append(f"    {ident} = {yara_str}")
                groups[tag].append(feat)
                id_map[ident] = feat
        else:
            for idx, feat in enumerate(unique_feats):
                yara_str = self._to_yara_string(feat)
                ident = f"$s{idx}"
                strings_section_lines.append(f"    {ident} = {yara_str}")
                id_map[ident] = feat

        # 4) condition
        n_feats = len(unique_feats)
        if n_feats == 1 and self.condition_type != "combo":
            cond_line = "    all of them"
        elif self.condition_type == "any":
            cond_line = "    any of them"
        elif self.condition_type == "all":
            cond_line = "    all of them"
        elif self.condition_type == "percentage":
            thresh = max(1, math.ceil(n_feats * self.percentage / 100.0))
            cond_line = f"    {thresh} of them"
        elif self.condition_type == "count":
            required = self.min_count if self.min_count is not None else n_feats
            required = min(required, n_feats)
            required = max(1, required)
            cond_line = f"    {required} of them"
        else:  # combo
            group_count = sum(1 for v in groups.values() if v)
            feat_count = n_feats
            if feat_count <= 2:
                if group_count == 1:
                    tag = next(t for t, v in groups.items() if v)
                    feats_list = groups[tag]
                    if tag == "m":
                        cond_line = f"    {len(feats_list)} of ($m*)"
                    elif self.group_percentage is not None:
                        pct = self.group_percentage
                        if self.adjust_group_percentage:
                            pct = self._scaled_group_percentage(len(feats_list))
                        required = max(1, math.ceil(len(feats_list) * pct / 100.0))
                        cond_line = f"    {required} of (${tag}*)"
                    elif self.group_min_count is not None or self.group_min_count_ratio > 0:
                        required = self._group_required(len(feats_list))
                        cond_line = f"    {required} of (${tag}*)"
                    else:
                        required = max(2, len(feats_list))
                        cond_line = f"    {required} of (${tag}*)"
                else:
                    parts = []
                    for tag, feats_list in groups.items():
                        if not feats_list:
                            continue
                        if tag == "m":
                            parts.append(f"{len(feats_list)} of ($m*)")
                            continue
                        if self.group_min_count is not None or self.group_min_count_ratio > 0:
                            required = self._group_required(len(feats_list))
                        elif self.group_percentage is not None:
                            pct = self.group_percentage
                            if self.adjust_group_percentage:
                                pct = self._scaled_group_percentage(len(feats_list))
                            required = max(1, math.ceil(len(feats_list) * pct / 100.0))
                        else:
                            required = 2 if len(feats_list) >= 2 else 1
                        parts.append(f"{required} of (${tag}*)")
                    cond_line = "    " + " and ".join(parts)
            elif group_count <= 1:
                # Single feature group but more than two features: require all
                tag = next(t for t, v in groups.items() if v)
                feats_list = groups[tag]
                if tag == "m":
                    cond_line = f"    {len(feats_list)} of ($m*)"
                elif self.group_min_count is not None or self.group_min_count_ratio > 0:
                    required = self._group_required(len(feats_list))
                    cond_line = f"    {required} of (${tag}*)"
                elif self.group_percentage is not None:
                    pct = self.group_percentage
                    if self.adjust_group_percentage:
                        pct = self._scaled_group_percentage(len(feats_list))
                    n = max(1, math.ceil(len(feats_list) * pct / 100.0))
                    cond_line = f"    {n} of (${tag}*)"
                else:
                    cond_line = "    all of them"
            else:
                parts = []
                for tag, feats_list in groups.items():
                    if not feats_list:
                        continue
                    if tag == "m":
                        parts.append(f"{len(feats_list)} of ($m*)")
                        continue
                    if self.group_min_count is not None or self.group_min_count_ratio > 0:
                        required = self._group_required(len(feats_list))
                        parts.append(f"{required} of (${tag}*)")
                    elif self.group_percentage is not None:
                        pct = self.group_percentage
                        if self.adjust_group_percentage:
                            pct = self._scaled_group_percentage(len(feats_list))
                        n = max(1, math.ceil(len(feats_list) * pct / 100.0))
                        parts.append(f"{n} of (${tag}*)")
                    else:
                        required = 2 if len(feats_list) >= 2 else 1
                        parts.append(f"{required} of (${tag}*)")
                cond_line = "    " + " and ".join(parts)

        # 5) join
        rule_lines = [
            f"rule {rule_name} {{",
            "  strings:",
            *strings_section_lines,
            "  condition:",
            f"{cond_line}",
            "}",
        ]
        text = "\n".join(rule_lines)
        if return_map:
            return text, id_map
        return text

    def validate(self, rule_text: str) -> Tuple[bool, str | None]:
        """
        yara‑python을 통해 구문 검증.
        Returns
        -------
        ok   : bool
        info : None or error str
        """
        if yara is None:
            return False, "yara‑python module not available"

        try:
            yara.compile(source=rule_text)
            return True, None
        except Exception as e:  # pylint:disable=broad-except
            return False, str(e)

    def load(self, path: Path) -> None:
        """Load rules from a file and compile if yara-python is available."""
        text = Path(path).read_text(encoding="utf-8")
        self.rule_count = text.count("rule ")
        self._compiled = None
        if yara is not None:
            try:
                self._compiled = yara.compile(filepath=str(path))
            except Exception as exc:  # pragma: no cover - best effort
                _LOG.warning("yara compile failed: %s", exc)

    def match_file(self, sample_path: Path) -> bool:
        """Return True if any rule matches the given file."""
        if yara is None or self._compiled is None:
            return False
        try:
            return bool(self._compiled.match(sample_path))
        except Exception as exc:  # pragma: no cover - best effort
            _LOG.warning("yara match failed for %s: %s", sample_path, exc)
            return False

    def combine_rules(
        self,
        rules: List[str],
        mode: str = "or",
        min_match_ratio: float = 0.7,
        wrapper_name: str | None = None,
        private: bool = False,
    ) -> str:
        """Return a YARA file combining ``rules`` with a wrapper rule.

        Parameters
        ----------
        rules : List[str]
            Individual rule texts to combine.
        mode : str, optional
            "or" (default) creates a wrapper rule that triggers if any rule
            matches.  ``"and"`` requires all rules to match.
        min_match_ratio : float, optional
            Minimum fraction of rules that must match when ``mode`` is ``"or"``.
            Default is ``0.7``.
            When the ratio results in more than one but fewer than all rules,
            the wrapper condition is formed by OR'ing together every
            combination of ``k`` rules joined with AND, where
            ``k = ceil(n * min_match_ratio)`` and ``n`` is the number of input
            rules.

        Notes
        -----
        The returned text contains the original rules followed by a final wrapper
        rule referencing them.  The wrapper rule name can be customized via
        ``wrapper_name``; when omitted a unique name is automatically generated.
        """

        if mode not in {"or", "and"}:
            raise ValueError("mode must be 'or' or 'and'")

        if len(rules) <= 1:
            return rules[0].strip() if rules else ""

        if wrapper_name is None:
            ts = _dt.datetime.utcnow().strftime("%Y%m%d%H%M%S")
            rand = random.randint(0, 9999)
            wrapper_name = f"combined_rule_{ts}_{rand:04}"

        names: List[str] = []
        cleaned: List[str] = []
        for idx, text in enumerate(rules):
            text = text.strip()
            cleaned.append(text)
            m = re.search(r"rule\s+(\w+)", text)
            names.append(m.group(1) if m else f"rule_{idx}")

        cond = "false"
        if names:
            if mode == "or":
                k = max(1, math.ceil(len(names) * min_match_ratio))
                if k <= 1:
                    cond = " or ".join(names)
                elif k >= len(names):
                    cond = " and ".join(names)
                else:
                    parts = [
                        "(" + " and ".join(c) + ")" for c in itertools.combinations(names, k)
                    ]
                    cond = " or ".join(parts) if parts else "false"
            else:  # mode == "and"
                cond = " and ".join(names)
        header = "rule"
        if private:
            header = "private " + header
        wrapper = [
            f"{header} {wrapper_name} {{",
            "  condition:",
            f"    {cond}",
            "}",
        ]
        return "\n\n".join(cleaned + ["\n".join(wrapper)])

    # ─────────────────────────────────── helpers ───────────────
    def _extract_features(self, tokens: Sequence[str]) -> List[str]:
        """
        • 토큰들 중 구두점/예약어를 제외하고 <특징 후보>를 추출
        • ':'·'.' 앞뒤 토큰을 붙여 'call:CreateFileW' 복원
        """
        feats: List[str] = []
        i = 0
        N = len(tokens)
        while i < N:
            tok = tokens[i]
            # case 1: "<X>" ":" "<Y>"  ⇒  "X:Y"
            if i + 2 < N and tokens[i + 1] == ":" and _token_is_feature(tok):
                combined = f"{tok}:{tokens[i + 2]}"
                feats.append(combined)
                i += 3
                continue
            # default
            if _token_is_feature(tok):
                feats.append(tok)
            i += 1
        # 중복 제거, 순서 유지
        seen = set()
        uniq = []
        for f in feats:
            if f not in seen:
                uniq.append(f)
                seen.add(f)
        return uniq

    def _to_yara_string(self, feat: str) -> str:
        """
        • feat 자체가 정규식/16진 패턴 등이면 그대로
        • 아니면 → `"<feat>" nocase ascii`
        """
        if self.strip_prefix:
            lowered = feat.lower()
            for prefix in ("call:", "syscall:", "import:", "marker:"):
                if lowered.startswith(prefix):
                    feat = feat.split(":", 1)[1]
                    lowered = feat.lower()
                    break
            if "!" in feat:
                feat = feat.split("!", 1)[1]

        m = _YARA_STR_MOD_RX.fullmatch(feat)
        if m:
            escaped = m.group("content").replace("\\", r"\\").replace('"', r'\"')
            mods = m.group("mods") or ""
            return f'"{escaped}"{mods}'

        if feat.startswith("/") and feat.endswith("/"):
            return feat
        if feat.startswith("{") and feat.endswith("}"):
            return feat
        if feat.startswith('"') and feat.endswith('"'):
            return feat
        # handle unmatched quote/braces/regex delimiters
        if feat.count('"') == 1:
            feat = feat.replace('"', '')
        if feat.startswith('{') and not feat.endswith('}'):
            feat = feat.lstrip('{')
        elif feat.endswith('}') and not feat.startswith('{'):
            feat = feat.rstrip('}')
        if feat.startswith('/') and not feat.endswith('/'):
            feat = feat.lstrip('/')
        elif feat.endswith('/') and not feat.startswith('/'):
            feat = feat.rstrip('/')
        # 기본: ASCII+nocase
        escaped = feat.replace("\\", r"\\").replace('"', r'\"')
        return f"\"{escaped}\" nocase ascii"


# ╔══════════════════════════════════════════════════════════════╗
# ║                    외부 사용자를 위한 함수                   ║
# ╚══════════════════════════════════════════════════════════════╝
def tokens_to_yara(tokens: Iterable[str], tokenizer: Optional[PreTrainedTokenizer] = None) -> str:
    """
    편의 함수–Builder인스턴스 생성 & rule 반환
    """
    builder = YaraBuilder(tokenizer=tokenizer)
    return builder.build(list(tokens))


# ╔══════════════════════════════════════════════════════════════╗
# ║                          CLI Entry                          ║
# ╚══════════════════════════════════════════════════════════════╗
def _cli():
    """
    예시
    ----
    >>> python -m rulegen.yara_builder "call : CreateFileW import : WS2_32 . dll"
    """
    parser = argparse.ArgumentParser(description="YARA Builder CLI")
    parser.add_argument("tokens", nargs="+", help="space‑separated token list")
    parser.add_argument(
        "--condition-type",
        choices=["any", "all", "percentage", "count", "combo"],
        default="any",
        help="Condition aggregation strategy",
    )
    parser.add_argument("--percentage", type=int, default=70, help="percentage value")
    parser.add_argument("--min-count", type=int, default=None, help="minimum count value")
    parser.add_argument("--group-percentage", type=int, help="combo mode: group percentage")
    parser.add_argument("--group-min-count", type=int, help="combo mode: group min count")
    parser.add_argument(
        "--adjust-group-percentage",
        action="store_true",
        help="lower group percentage automatically for many features",
    )
    args = parser.parse_args()

    builder = YaraBuilder(
        condition_type=args.condition_type,
        percentage=args.percentage,
        min_count=args.min_count,
        group_percentage=args.group_percentage,
        group_min_count=args.group_min_count,
        adjust_group_percentage=args.adjust_group_percentage,
    )
    rule_text = builder.build(args.tokens)
    print(rule_text)
    ok, err = builder.validate(rule_text)
    if ok:
        print("\n[validate] YARA syntax")
    else:
        print(f"\n[validate] skipped/failed: {err}")


if __name__ == "__main__":
    _cli()
