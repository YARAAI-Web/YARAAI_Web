#!/usr/bin/env python3
"""
robust‑malware‑graph – End‑to‑End *Pre‑processing* CLI (refactored)
──────────────────────────────────────────────────────────────────
* 주요 개선: 안정적 예외처리, 경로 보장, YAML 구성, spawn‑safe 멀티프로세싱,
  공통 로깅 레벨 동기화 등. 자세한 변경점은 README 참조.
"""
from __future__ import annotations

import argparse
import logging
import multiprocessing as mp
import os
import sys
from pathlib import Path

from src.graphs.builders import OverLengthPolicy
from typing import Callable, Dict, Sequence

# ────────────────────────────────────────────────────────────────
# 0. 공통 유틸
# ────────────────────────────────────────────────────────────────
LOGGER: logging.Logger | None = None              # 싱글턴
STAGES: Dict[str, Callable[[argparse.Namespace], None]] = {}  # stage registry

class StageError(RuntimeError):
    """단일 Stage 실패 시 throw; run_all 에서 캐치한다."""

def _get_logger(level: str = "INFO") -> logging.Logger:  # noqa: D401
    """전역 로거(싱글턴) 반환 및 root 레벨 동기화."""
    global LOGGER  # pylint: disable=global-statement
    if LOGGER is None:
        logging.basicConfig(
            level=getattr(logging, level),
            format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        from src.common.logger import get_logger  # lazy import (light)
        LOGGER = get_logger(name="preprocessing", level=level)
    return LOGGER

def ensure_dir(p: Path) -> None:
    """디렉터리 미존재 시 재귀 생성."""
    p.mkdir(parents=True, exist_ok=True)

def register_stage(name: str) -> Callable[[Callable], Callable]:
    """데코레이터: stage 함수를 STAGES dict에 자동 등록."""
    def _wrap(fn: Callable) -> Callable:
        STAGES[name] = fn
        return fn
    return _wrap

def load_yaml_cfg(path: Path) -> dict:
    """YAML → dict  (OmegaConf 우선, PyYAML fallback)."""
    if not path.exists():
        raise FileNotFoundError(path)
    try:
        from omegaconf import OmegaConf  # type: ignore
        return OmegaConf.to_container(OmegaConf.load(path), resolve=True)  # type: ignore
    except ModuleNotFoundError:
        import yaml  # pyright: ignore
        with path.open("r", encoding="utf-8") as f:
            return yaml.safe_load(f)


def _get_nested(js: dict, path: str) -> str | None:
    """Retrieve nested value via dotted ``path``."""
    cur = js
    for key in path.split("."):
        if isinstance(cur, dict) and key in cur:
            cur = cur[key]
        else:
            return None
    if isinstance(cur, (str, int, float)):
        return str(cur)
    return None

# ────────────────────────────────────────────────────────────────
# labels.csv 생성
# ────────────────────────────────────────────────────────────────
@register_stage("labels")
def run_labels(args: argparse.Namespace) -> None:
    """Generate or update ``labels.csv`` from raw JSON files."""
    import csv
    import json

    logger = _get_logger(args.log_level)

    src_dir = Path(args.input_dir)
    csv_path = Path(args.csv or (Path(args.out_dir) / "labels.csv"))
    ensure_dir(csv_path.parent)

    existing: dict[str, str] = {}
    if csv_path.is_file():
        with csv_path.open("r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                existing[row["sha256"]] = row["label"]

    new_rows: list[dict[str, str]] = []
    for fp in src_dir.glob("*.json"):
        try:
            js = json.loads(fp.read_text())
        except Exception as exc:  # noqa: BLE001
            logger.error("Failed to read %s: %s", fp, exc)
            continue

        sha = js.get("virustotal", {}).get("sha256")
        if not sha:
            logger.warning("sha256 not found in %s", fp.name)
            continue
        if sha in existing:
            logger.debug("%s already in CSV", sha)
            continue

        row = {"sha256": sha, "label": str(args.label), "filename": fp.name}
        if args.date_key:
            date_val = _get_nested(js, args.date_key)
            if date_val is None:
                logger.warning("%s missing date key '%s'", fp.name, args.date_key)
            else:
                row["collected_at"] = date_val
        new_rows.append(row)

    if not new_rows:
        logger.info("[LABELS] no new entries for %s", csv_path)
        return

    mode = "a" if csv_path.exists() else "w"
    fieldnames = ["sha256", "label", "filename"]
    if args.date_key:
        fieldnames.append("collected_at")
    with csv_path.open(mode, encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if mode == "w":
            writer.writeheader()
        for row in new_rows:
            writer.writerow(row)

    logger.info("[LABELS] %d new entries written to %s", len(new_rows), csv_path)

# ────────────────────────────────────────────────────────────────
# 1. EXTRACT
# ────────────────────────────────────────────────────────────────
@register_stage("extract")
def run_extract(args: argparse.Namespace) -> None:  # noqa: D401
    """Stage 1 – Graph *views* 추출."""
    from src.extract.pipelines.extract_pipeline import ExtractPipeline

    logger = _get_logger(args.log_level)
    n_files = len(list(Path(args.input_dir).iterdir()))
    logger.info("[EXTRACT] %d file(s) → views=%s", n_files, ",".join(args.views))
    try:
        views_dir = Path(args.out_dir, "data", "views")
        ensure_dir(views_dir)
        pipeline = ExtractPipeline(
            views=list(args.views),
            out_dir=views_dir,
            workers=args.workers,
            overwrite=args.overwrite,
        )
        pipeline.run(Path(args.input_dir))
    except Exception as exc:  # noqa: BLE001
        logger.exception("Extract stage failed")
        raise StageError from exc

# ────────────────────────────────────────────────────────────────
# 2. JSON → VIEWS
# ────────────────────────────────────────────────────────────────
@register_stage("json")
def run_json(args: argparse.Namespace) -> None:
    """Stage 2 – PE metadata JSON → view JSONs."""
    import json
    from src.graphs.loaders.ast_loader import ASTLoader
    from src.graphs.loaders.cfg_loader import CFGLoader
    from src.graphs.loaders.fcg_loader import FCGLoader
    from src.graphs.loaders.syscall_loader import SysCallLoader

    logger = _get_logger(args.log_level)
    converters = {
        "ast": ASTLoader._convert_pejson_to_ast,
        "cfg": CFGLoader._convert_pejson_to_cfg,
        "fcg": FCGLoader._convert_pejson_to_fcg,
        "syscall": SysCallLoader._convert_pejson_to_syscalls,
    }

    input_dir = Path(args.input_dir)
    views_dir = Path(args.out_dir, "data", "views")
    ensure_dir(views_dir)

    # --- remove legacy AST caches -------------------------------------------
    if "ast" in args.views:
        ast_dir = views_dir / "ast"
        if ast_dir.exists():
            for fp in ast_dir.glob("*.json"):
                try:
                    with fp.open("r", encoding="utf-8") as f:
                        js = json.load(f)
                    if "nodes" not in js:
                        logger.debug("Removing legacy AST file %s", fp)
                        fp.unlink()
                except Exception:  # noqa: BLE001
                    logger.debug("Removing unparsable AST file %s", fp)
                    fp.unlink()
    files = list(input_dir.glob("*.json"))
    logger.info("[JSON] %d file(s) → views=%s", len(files), ",".join(args.views))

    for fp in files:
        try:
            js = json.loads(fp.read_text())
        except Exception as exc:  # noqa: BLE001
            logger.error("Failed to read %s: %s", fp, exc)
            continue

        sha = js.get("get_metadata", {}).get("sha256", fp.stem)

        for view in args.views:
            conv = converters.get(view)
            if conv is None:
                continue
            try:
                data_dict = conv(js)
            except Exception as exc:  # noqa: BLE001
                logger.error("[%s/%s] convert error: %s", fp.name, view, exc)
                continue

            dst = views_dir / view / f"{sha}.json"
            if dst.exists() and not args.overwrite:
                logger.debug("%s exists; skip", dst)
                continue
            ensure_dir(dst.parent)
            try:
                with dst.open("w", encoding="utf-8") as f:
                    json.dump(data_dict, f, indent=2)
            except Exception as exc:  # noqa: BLE001
                logger.error("[%s/%s] save error: %s", fp.name, view, exc)


# ────────────────────────────────────────────────────────────────
# 3. GRAPHS
# ────────────────────────────────────────────────────────────────
@register_stage("graphs")
def run_graphs(args: argparse.Namespace) -> None:
    """Stage 3 – View 통합 → Hetero Graph."""
    from src.graphs.builders.hetero_builder import build_hetero_dataset

    logger = _get_logger(args.log_level)
    logger.info(
        "[GRAPHS] rebuild=%s  clean=%s  normalise=%s  with_feats=%s  feat_policy=%s",
        args.rebuild,
        args.clean,
        args.normalise,
        args.with_feats,
        args.feat_policy,
    )
    try:
        hetero_dir = Path(args.out_dir, "data", "hetero")
        ensure_dir(hetero_dir)
        build_hetero_dataset(
            views_dir=Path(args.out_dir, "data", "views"),
            hetero_dir=hetero_dir,
            normalise=args.normalise,
            rebuild=args.rebuild,
            clean=args.clean,
            workers=args.workers,
            with_feats=args.with_feats,
            feat_policy=OverLengthPolicy[args.feat_policy],
        )
    except Exception as exc:  # noqa: BLE001
        logger.exception("Graphs stage failed")
        raise StageError from exc


# ────────────────────────────────────────────────────────────────
# 4. SPLITS
# ────────────────────────────────────────────────────────────────
@register_stage("splits")
def run_splits(args: argparse.Namespace) -> None:
    """Stage 4 – 시간 기반 Train/Val/Test 분할."""
    from src.graphs.dataset.split_generator import build_time_splits

    logger = _get_logger(args.log_level)
    logger.info(
        "[SPLITS] strategy=%s  val=%.2f  test=%.2f  fallback=%s",
        args.strategy,
        args.val_ratio,
        args.test_ratio,
        args.fallback,
    )
    try:
        splits_dir = Path(args.out_dir, "data", "splits")
        ensure_dir(splits_dir)
        train, val, test = build_time_splits(
            hetero_dir=Path(args.out_dir, "data", "hetero"),
            splits_dir=splits_dir,
            strategy=args.strategy,
            val_ratio=args.val_ratio,
            test_ratio=args.test_ratio,
            fallback=args.fallback,
            seed=args.seed,
            json_out=args.json_out,
        )
        if args.json_out:
            logger.info("[SPLITS] JSON saved to %s", args.json_out)
    except Exception as exc:  # noqa: BLE001
        logger.exception("Splits stage failed")
        raise StageError from exc

# ────────────────────────────────────────────────────────────────
# 4. EMBEDS
# ────────────────────────────────────────────────────────────────
@register_stage("embeds")
def run_embeds(args: argparse.Namespace) -> tuple[int, int]:
    """Stage 4 – Code‑LLM 임베딩 캐시.

    Returns the number of created and skipped embeddings.
    """
    from src.models.llm_embed import CodeLLMNodeFeat, embed_corpus

    logger = _get_logger(args.log_level)
    logger.debug("[EMBEDS] model=%s  device=%s", args.model_name, args.device)
    try:
        hetero_dir = Path(args.out_dir, "data", "hetero")
        if args.input_dir:
            user_dir = Path(args.input_dir, "hetero")
            if user_dir.resolve() != hetero_dir.resolve():
                logger.error(
                    "[EMBEDS] input-dir %s does not match expected %s",
                    user_dir,
                    hetero_dir,
                )
                raise StageError("Incorrect input directory for embed stage")
        encoder = CodeLLMNodeFeat(model_name=args.model_name)
        encoder.to(args.device)
        embeds_dir = Path(args.out_dir, "data", "embeds")
        ensure_dir(embeds_dir)
        processed, skipped = embed_corpus(
            encoder,
            hetero_dir=hetero_dir,
            out_dir=embeds_dir,
            batch_size=args.batch_size,
            overwrite=args.overwrite,
        )
        logger.info("[EMBEDS] created=%d skipped=%d", processed, skipped)
        return processed, skipped
    except Exception as exc:  # noqa: BLE001
        logger.exception("Embeds stage failed")
        raise StageError from exc

# ────────────────────────────────────────────────────────────────
# 5. Umbrella – run *all*
# ────────────────────────────────────────────────────────────────
@register_stage("all")
def run_all(args: argparse.Namespace) -> None:
    """extract → graphs → splits → embeds 순차 실행."""
    # Populate stage-specific defaults when called via the "all" subcommand.
    defaults = {
        "views": ["ast", "cfg", "fcg", "syscall"],
        "normalise": False,
        "rebuild": False,
        "clean": False,
        "with_feats": False,
        "feat_policy": "TRIM",
        "strategy": "time",
        "val_ratio": 0.1,
        "test_ratio": 0.1,
        "fallback": "skip",
        "seed": 42,
        "json_out": None,
        "model_name": "microsoft/codebert-base",
        "batch_size": 64,
        "device": "cuda",
    }
    for key, val in defaults.items():
        if not hasattr(args, key):
            setattr(args, key, val)

    for name in ("extract", "graphs", "splits", "embeds"):
        _get_logger(args.log_level).info("=== [%s] stage ===", name.upper())
        try:
            STAGES[name](args)
        except StageError:
            _get_logger(args.log_level).error("Pipeline aborted at [%s]", name)
            sys.exit(1)

# ────────────────────────────────────────────────────────────────
# 6. Argparse
# ────────────────────────────────────────────────────────────────
def build_parser() -> argparse.ArgumentParser:  # noqa: C901
    parser = argparse.ArgumentParser(
        prog="robust-malware-graph.preprocessing",
        description="End‑to‑end dataset preparation for malware graphs.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # --- 글로벌 공통 옵션 -------------------------------------------------
    parser.add_argument("--input-dir", required=True, help="Path to raw samples")
    parser.add_argument("--out", dest="out_dir", default="./", help="Project root (data/* will live here)")
    parser.add_argument("--workers", type=int, default=os.cpu_count() or 8)
    parser.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR"])
    parser.add_argument("--overwrite", action="store_true", help="Overwrite cached artifacts")

    # 새 옵션: YAML 설정
    parser.add_argument("--config", type=str, help="YAML config merging into CLI args (OmegaConf/PyYAML)")

    sub = parser.add_subparsers(dest="command", required=True)

    # ---------------- labels ---------------- #
    p = sub.add_parser("labels", help="Generate labels.csv from raw JSONs")
    p.add_argument("--label", type=int, choices=[0, 1], required=True,
                   help="Label for all samples (0=benign, 1=malicious)")
    p.add_argument("--csv", type=str,
                   help="Output CSV path (default: OUT/labels.csv)")
    p.add_argument("--date-key", type=str, default=None,
                   help="Dotted JSON path for sample collection date")
    p.set_defaults(func=run_labels)

    # ---------------- extract ---------------- #
    p = sub.add_parser("extract", help="Generate AST/CFG/FCG/SysCall views")
    p.add_argument("--views", nargs="+", default=["ast", "cfg", "fcg", "syscall"],
                   choices=["ast", "cfg", "fcg", "syscall"])
    p.set_defaults(func=run_extract)

    # ---------------- json ---------------- #
    p = sub.add_parser("json", help="Convert PE JSON → view JSONs")
    p.add_argument("--views", nargs="+", default=["ast", "cfg", "fcg", "syscall"],
                   choices=["ast", "cfg", "fcg", "syscall"])
    p.set_defaults(func=run_json)

    # ---------------- graphs ---------------- #
    p = sub.add_parser("graphs", help="Merge views into hetero graphs")
    p.add_argument("--normalise", action="store_true")
    p.add_argument("--rebuild", action="store_true")
    p.add_argument("--clean", action="store_true", help="Remove existing *.pt when rebuilding")
    p.add_argument("--with-feats", action="store_true", help="Pad missing node features")
    p.add_argument(
        "--feat-policy",
        choices=["ERROR", "TRIM", "EXPAND", "MASKPAD"],
        default="TRIM",
        help="Policy for over-length node features",
    )
    p.set_defaults(func=run_graphs)

    # ---------------- splits ---------------- #
    p = sub.add_parser("splits", help="Create temporal train/val/test splits")
    p.add_argument("--strategy", default="time", choices=["time", "stratified", "random"])
    p.add_argument("--val-ratio", type=float, default=0.1)
    p.add_argument("--test-ratio", type=float, default=0.1)
    p.add_argument("--fallback", choices=["random", "skip"], default="skip")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--json-out", type=Path)
    p.set_defaults(func=run_splits)

    # ---------------- embeds ---------------- #
    p = sub.add_parser(
        "embeds",
        help="Encode token nodes with a Code‑LLM and cache under data/embeds",
    )
    p.add_argument("--model-name", default="microsoft/codebert-base")
    p.add_argument("--batch-size", type=int, default=64, help="Encoding batch size")
    p.add_argument("--device", default="cuda", help="Torch device for inference")
    p.set_defaults(func=run_embeds)

    # ---------------- all ---------------- #
    p = sub.add_parser("all", help="Run *all* pre‑processing stages sequentially")
    p.add_argument("--views", nargs="+", default=["ast", "cfg", "fcg", "syscall"],
                   choices=["ast", "cfg", "fcg", "syscall"],
                   help="Views to extract and convert")
    p.add_argument("--normalise", action="store_true", help="Normalise features")
    p.add_argument("--rebuild", action="store_true", help="Rebuild existing graphs")
    p.add_argument("--clean", action="store_true", help="Remove existing *.pt when rebuilding")
    p.add_argument("--with-feats", action="store_true", help="Pad missing node features")
    p.add_argument(
        "--feat-policy",
        choices=["ERROR", "TRIM", "EXPAND", "MASKPAD"],
        default="TRIM",
        help="Policy for over-length node features",
    )
    p.add_argument("--strategy", default="time", choices=["time", "stratified", "random"],
                   help="Splitting strategy")
    p.add_argument("--val-ratio", type=float, default=0.1, help="Validation split ratio")
    p.add_argument("--test-ratio", type=float, default=0.1, help="Test split ratio")
    p.add_argument("--fallback", choices=["random", "skip"], default="skip",
                   help="Fallback policy if no timestamp")
    p.add_argument("--seed", type=int, default=42, help="Random seed")
    p.add_argument("--json-out", type=Path, help="Save split info as JSON")
    p.add_argument("--model-name", default="microsoft/codebert-base", help="LLM model name")
    p.add_argument("--batch-size", type=int, default=64, help="Encoding batch size")
    p.add_argument("--device", default="cuda", help="Torch device for inference")
    p.set_defaults(func=run_all)

    return parser

# ────────────────────────────────────────────────────────────────
# 7. Main
# ────────────────────────────────────────────────────────────────
def main(argv: Sequence[str] | None = None) -> None:  # noqa: D401
    mp.set_start_method("spawn", force=True)  # cross‑platform safety
    parser = build_parser()
    args = parser.parse_args(argv)

    # YAML 구성 파일 병합
    if args.config:
        cfg = load_yaml_cfg(Path(args.config))
        parser.set_defaults(**cfg)        # CLI 인자 < YAML < 코드 default
        args = parser.parse_args(argv)    # 재‑파싱

    _get_logger(args.log_level).debug("robust‑malware‑graph stage: %s", args.command.upper())
    try:
        STAGES[args.command](args)
    except StageError:
        sys.exit(1)

if __name__ == "__main__":  # pragma: no cover
    main()
