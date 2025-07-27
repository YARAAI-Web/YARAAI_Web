"""
src.graphs.dataset.split_generator
==================================

대규모 그래프 샘플을 **train / val / test** 세 부분으로 분할하고
<out_root>/{train,val,test}/graphs/ 디렉토리 구조를 생성한다.

◎ 지원 분할 방식
────────────────────────────────────────────────────────────
1) 시간 순(Time-aware)  : split_by_time()
   • 기준 열(date_col) 값을 기준으로 cut_date 이전 → train,
     이후 → {val|test} 비율대로 나눔

2) 임의(Stratified k-fold) : split_random()
   • 라벨별 균형을 유지하며 k-fold 분할
   • val, test 는 서로 다른 fold 사용 (기본 k=5)

◎ 메타 CSV 형식
────────────────────────────────────────────────────────────
sha256,collected_at,label,[any other columns …]

◎ 파일 이동/복사 옵션
────────────────────────────────────────────────────────────
op = {'symlink' (기본), 'copy', 'move'}

CLI 예시
────────────────────────────────────────────────────────────
python -m graphs.dataset.split_generator \
    --meta /data/meta.csv --graphs /data/graphs --out /data/splits \
    --by-time --cut 2024-06-01 --val-ratio 0.1 --test-ratio 0.1
"""

from __future__ import annotations

import argparse
import csv
import json
import shutil
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Sequence, Tuple
import itertools

from ..utils import ensure_dir, get_logger

_LOG = get_logger("dataset.split_gen")

########################################################################
# 내부 헬퍼
########################################################################
def _link_copy_move(src: Path, dst: Path, op: str = "symlink") -> None:
    """그래프 파일을 dst에 symlink / copy / move.

    기존 파일이 있으면 덮어써 FileExistsError 를 방지한다.
    """
    if dst.exists():
        dst.unlink()  # overwrite existing file/link

    if op == "symlink":
        dst.symlink_to(src.resolve())
    elif op == "copy":
        shutil.copy2(src, dst)
    elif op == "move":
        shutil.move(src, dst)
    else:
        raise ValueError(f"Unknown op '{op}'")


def _make_split_dirs(root: Path) -> Dict[str, Path]:
    paths = {
        "train": root / "train" / "graphs",
        "val": root / "val" / "graphs",
        "test": root / "test" / "graphs",
    }
    for p in paths.values():
        ensure_dir(p)
    return paths


def _write_split_list(root: Path, split: str, shas: Sequence[str]) -> None:
    """train/val/test 폴더 안에 리스트 파일 작성."""
    lst = root / split / f"{split}_list.txt"
    lst.write_text("\n".join(shas))


########################################################################
# 분할 로직
########################################################################
def split_by_time(
    meta_csv: Path,
    graph_dir: Path,
    out_root: Path,
    *,
    date_col: str = "collected_at",
    id_col: str = "sha256",
    label_col: str | None = None,
    cut_date: str | datetime = "2024-01-01",
    val_ratio: float = 0.1,
    test_ratio: float = 0.1,
    fallback: str = "skip",
    op: str = "symlink",
) -> Tuple[List[str], List[str], List[str]]:
    """
    cut_date 이전은 train, 이후는 (val:test) 비율로 랜덤 분할.
    """
    cut_dt = datetime.fromisoformat(cut_date) if isinstance(cut_date, str) else cut_date

    train, post_cut, missing_date = [], [], []
    labels: Dict[str, int] = {}
    alt_names: Dict[str, str] = {}

    with meta_csv.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            sha = row[id_col]
            if "filename" in row:
                alt_names[sha] = row["filename"]
            elif "name" in row:
                alt_names[sha] = row["name"]
            if label_col:
                labels[sha] = int(row[label_col])
            try:
                dt = datetime.fromisoformat(row[date_col])
            except (KeyError, ValueError):
                _LOG.warning("missing %s for %s", date_col, sha)
                missing_date.append(sha)
                continue
            (train if dt < cut_dt else post_cut).append(sha)

    # post_cut → val / test
    rng = sorted(post_cut)
    val_cnt = int(len(rng) * val_ratio / (val_ratio + test_ratio))
    val = rng[:val_cnt]
    test = rng[val_cnt:]

    if missing_date:
        _LOG.warning("%d samples missing dates", len(missing_date))
        if fallback == "random":
            total = len(train) + len(val) + len(test)
            if total == 0:
                ratios = (1.0, 0.0, 0.0)
            else:
                ratios = (
                    len(train) / total,
                    len(val) / total,
                    len(test) / total,
                )
            rng_md = sorted(missing_date)
            n_train = int(len(rng_md) * ratios[0])
            n_val = int(len(rng_md) * ratios[1])
            train.extend(rng_md[:n_train])
            val.extend(rng_md[n_train : n_train + n_val])
            test.extend(rng_md[n_train + n_val :])
        elif fallback != "skip":
            raise ValueError(f"Unknown fallback '{fallback}'")

    _LOG.info("split_by_time  train=%d  val=%d  test=%d", len(train), len(val), len(test))
    return _apply_split(graph_dir, out_root, train, val, test, op, alt_names)


def split_random(
    meta_csv: Path,
    graph_dir: Path,
    out_root: Path,
    *,
    id_col: str = "sha256",
    label_col: str = "label",
    k_fold: int = 5,
    seed: int = 42,
    op: str = "symlink",
) -> Tuple[List[str], List[str], List[str]]:
    """
    label 균형을 유지한 stratified k-fold → train/val/test.
    """
    import random

    random.seed(seed)
    buckets: Dict[int, List[str]] = defaultdict(list)
    alt_names: Dict[str, str] = {}

    with meta_csv.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            sha = row[id_col]
            if "filename" in row:
                alt_names[sha] = row["filename"]
            elif "name" in row:
                alt_names[sha] = row["name"]
            buckets[int(row[label_col])].append(sha)

    folds: List[List[str]] = [[] for _ in range(k_fold)]
    for lab, shas in buckets.items():
        random.shuffle(shas)
        for i, sha in enumerate(shas):
            folds[i % k_fold].append(sha)

    random.shuffle(folds)
    test, val, *tr_folds = folds
    train = list(itertools.chain.from_iterable(tr_folds))
    _LOG.info("split_random  train=%d  val=%d  test=%d", len(train), len(val), len(test))
    return _apply_split(graph_dir, out_root, train, val, test, op, alt_names)


########################################################################
# 공통 적용 함수
########################################################################
def _apply_split(
    graph_dir: Path,
    out_root: Path,
    train: Sequence[str],
    val: Sequence[str],
    test: Sequence[str],
    op: str,
    alt_names: Dict[str, str] | None = None,
) -> Tuple[List[str], List[str], List[str]]:
    paths = _make_split_dirs(out_root)
    mapping = [("train", list(train)), ("val", list(val)), ("test", list(test))]
    result = {}

    for split_name, lst in mapping:
        dst_dir = paths[split_name]
        kept: List[str] = []
        for sha in lst:
            src_files = list(graph_dir.glob(f"{sha}.*"))
            if not src_files and alt_names:
                alt = alt_names.get(sha)
                if alt:
                    src_files = list(graph_dir.glob(alt))
                    if not src_files:
                        stem = Path(alt).stem
                        src_files = list(graph_dir.glob(f"{stem}.*"))
            if not src_files:
                _LOG.warning("graph %s.* not found, skip", sha)
                continue
            kept.append(sha)
            for src in src_files:
                _link_copy_move(src, dst_dir / src.name, op)
        _write_split_list(out_root, split_name, kept)
        result[split_name] = kept

    return result["train"], result["val"], result["test"]


########################################################################
# CLI
########################################################################
def _build_argparser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Generate train/val/test splits")
    p.add_argument("--meta", required=True, type=Path, help="meta CSV path")
    p.add_argument("--graphs", required=True, type=Path, help="directory of graph files")
    p.add_argument("--out", required=True, type=Path, help="output root for splits")
    p.add_argument("--op", choices=["symlink", "copy", "move"], default="symlink")

    mode = p.add_mutually_exclusive_group(required=True)
    mode.add_argument("--by-time", action="store_true")
    mode.add_argument("--random", action="store_true")

    # time-split params
    p.add_argument("--cut", type=str, default="2024-01-01", help="cut date YYYY-MM-DD")
    p.add_argument("--val-ratio", type=float, default=0.1)
    p.add_argument("--test-ratio", type=float, default=0.1)
    p.add_argument("--date-col", type=str, default="collected_at")
    p.add_argument("--fallback", choices=["random", "skip"], default="skip")

    # random-split params
    p.add_argument("--k-fold", type=int, default=5)
    p.add_argument("--seed", type=int, default=42)

    return p


def main(argv: Sequence[str] | None = None) -> None:
    args = _build_argparser().parse_args(argv)

    if args.by_time:
        split_by_time(
            meta_csv=args.meta,
            graph_dir=args.graphs,
            out_root=args.out,
            cut_date=args.cut,
            val_ratio=args.val_ratio,
            test_ratio=args.test_ratio,
            date_col=args.date_col,
            fallback=args.fallback,
            op=args.op,
        )
    else:
        split_random(
            meta_csv=args.meta,
            graph_dir=args.graphs,
            out_root=args.out,
            k_fold=args.k_fold,
            seed=args.seed,
            op=args.op,
        )
    _LOG.info("✔ Done")
# ════════════════════════════════════════════════════════════════
# build_time_splits  –  split-only helper  (re-entrant)
# ----------------------------------------------------------------
from datetime import datetime
from typing import Tuple

def build_time_splits(
    *,
    hetero_dir : Path,                # <sha>.pt 가 있는 디렉터리
    splits_dir : Path,                # 결과 train/val/test 루트
    strategy   : str        = "time", # {"time", "random"}
    # time-split 옵션
    cut_date   : str|datetime = "2024-01-01",
    val_ratio  : float       = 0.1,
    test_ratio : float       = 0.1,
    date_col   : str         = "collected_at",
    fallback   : str         = "skip",
    # random-split 옵션
    k_fold     : int         = 5,
    # 공통
    meta_csv   : Path|None   = None,  # 지정 없으면 hetero_dir.parent / "meta.csv"
    id_col     : str         = "sha256",
    label_col  : str         = "label",
    seed       : int         = 42,
    op         : str         = "symlink",
    json_out   : Path | None  = None,
) -> Tuple[List[str], List[str], List[str]]:
    """
    이미 생성된 *.pt 헤테로그래프를 train/val/test 로 배분한다.

    hetero_dir/
        ├─ a1b2c3.pt
        ├─ d4e5f6.pt
        └─ …
    splits_dir/
        ├─ train/graphs/
        ├─ val/graphs/
        └─ test/graphs/

    strategy
    --------
    • "time"   : cut_date 기준 → split_by_time()
    • "random" : 라벨 균형 stratified k-fold → split_random()
    """
    meta_csv = meta_csv or (hetero_dir.parent / "meta.csv")
    if not meta_csv.is_file():
        raise FileNotFoundError(f"meta CSV not found: {meta_csv}")

    ensure_dir(splits_dir)

    if strategy == "time":
        train, val, test = split_by_time(
            meta_csv   = meta_csv,
            graph_dir  = hetero_dir,
            out_root   = splits_dir,
            date_col   = date_col,
            id_col     = id_col,
            cut_date   = cut_date,
            val_ratio  = val_ratio,
            test_ratio = test_ratio,
            fallback   = fallback,
            op         = op,
        )
    elif strategy in {"random", "stratified"}:
        train, val, test = split_random(
            meta_csv  = meta_csv,
            graph_dir = hetero_dir,
            out_root  = splits_dir,
            id_col    = id_col,
            label_col = label_col,
            k_fold    = k_fold,
            seed      = seed,
            op        = op,
        )
    else:
        raise ValueError(f"Unknown strategy '{strategy}' (expect 'time' or 'random')")

    if json_out is not None:
        with json_out.open("w", encoding="utf-8") as f:
            json.dump({"train": train, "val": val, "test": test}, f)

    # ── split별 labels.csv 작성 ────────────────────────────────────────
    label_map: Dict[str, str] = {}
    with meta_csv.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            sha = row[id_col]
            if label_col in row:
                label_map[sha] = row[label_col]

    for split_name, sha_list in {
        "train": train,
        "val": val,
        "test": test,
    }.items():
        path = splits_dir / split_name / "labels.csv"
        with path.open("w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["sha256", "label"])
            for sha in sha_list:
                label = label_map.get(sha)
                if label is not None:
                    writer.writerow([sha, label])

    _LOG.info("✔ build_time_splits complete → %s", splits_dir)
    return train, val, test



if __name__ == "__main__":  # pragma: no cover
    main(sys.argv[1:])
