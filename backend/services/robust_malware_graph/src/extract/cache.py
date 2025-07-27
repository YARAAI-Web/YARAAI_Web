from __future__ import annotations

"""src.extract.cache
====================
디스크에 저장된 캐시를 점검하고 용량을 계산하며 정리하기 위한 보조 기능을 제공합니다.
:pyclass:`src.extract.base.ExtractorBase`에서 사용하는 캐시는 내용 기반 주소 체계를 따릅니다.

```
  data/views/<VIEW>/<sha256>.<fmt>
```

이 모듈은 추출기 내부 구조를 다루지 않고 단순한 파일 시스템 작업만 수행합니다.
따라서 다른 프로세스가 캐시에 쓰기 중이더라도 안전하게 사용할 수 있습니다(최선의 노력 수준이며 잠금은 사용하지 않습니다).
주요 사용 예시는 다음과 같습니다.

* "How much disk space does the *AST* view consume right now?"
* "Remove everything older than 90 days across all views."
* Cron‑job that keeps overall cache size below a hard limit.
"""

from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Dict, Iterator, List, Tuple
import argparse
import logging
import os
import shutil

from .constants import DEFAULT_VIEWS_DIR, SUPPORTED_FMTS

__all__ = [
    "cache_path",
    "iter_cache_files",
    "cache_size",
    "purge_cache",
]

log = logging.getLogger("extract.cache")
if not log.handlers:
    logging.basicConfig(
        level=logging.INFO, format="[%(asctime)s] %(levelname)s %(name)s: %(message)s"
    )

# --------------------------------------------------------------------------- #
# 핵심 도우미
# --------------------------------------------------------------------------- #

def cache_path(view: str, sha256: str, *, fmt: str = "json", root: Path = DEFAULT_VIEWS_DIR) -> Path:  # noqa: D401
    """*(view, sha256, fmt)* 조합에 대한 표준 캐시 경로를 반환합니다."""
    if fmt not in SUPPORTED_FMTS:
        raise ValueError(f"Unsupported fmt: {fmt} — choose from {sorted(SUPPORTED_FMTS)}")
    return root / view / f"{sha256}.{fmt}"


def iter_cache_files(
    view: str | None = None,
    *,
    older_than: datetime | None = None,
    root: Path = DEFAULT_VIEWS_DIR,
) -> Iterator[Path]:  # noqa: D401
    """*view*와/또는 *mtime* 기준으로 필터링된 캐시 파일 경로를 차례로 제공합니다.

    Parameters
    ----------
    view
        특정 추출기 뷰만 대상으로 제한합니다(예: ``"cfg"``). *None*이면 모든 뷰를 의미합니다.
    older_than
        지정하면 *mtime*이 이 시간보다 **엄격히 이전**인 항목만 반환합니다(UTC).
    """
    if not root.exists():
        return

    view_dirs = [root / view] if view else [d for d in root.iterdir() if d.is_dir()]
    for vdir in view_dirs:
        for p in vdir.iterdir():
            if not p.is_file():
                continue
            if older_than is not None:
                mtime = datetime.fromtimestamp(p.stat().st_mtime, timezone.utc)
                if mtime >= older_than:
                    continue
            yield p


def cache_size(view: str | None = None) -> Tuple[int, str]:  # noqa: D401
    """지정한 뷰 또는 전체 캐시의 크기를 *(바이트, 사람이 읽기 쉬운 형식)*으로 반환합니다."""
    total = sum(p.stat().st_size for p in iter_cache_files(view=view))
    return total, _sizeof_fmt(total)


def purge_cache(
    view: str | None = None,
    *,
    older_than: datetime | timedelta | None = None,
    dry_run: bool = False,
) -> Dict[str, int]:  # noqa: D401
    """캐시 파일을 삭제하고 통계 정보를 반환합니다.

    Parameters
    ----------
    view
        이 뷰로 범위를 제한합니다. *None*이면 모든 뷰를 대상으로 합니다.
    older_than
        절대(`datetime`) 또는 상대(`timedelta`) 시각을 지정하면, 이보다 새로운 항목만 유지합니다.
    dry_run
        *True*이면 실제 삭제 대신 영향만 계산합니다.
    """
    if isinstance(older_than, timedelta):
        older_than = datetime.now(timezone.utc) - older_than

    deleted = 0
    freed = 0
    for p in list(iter_cache_files(view=view, older_than=older_than)):
        freed += p.stat().st_size
        deleted += 1
        if not dry_run:
            try:
                p.unlink()
            except OSError as exc:
                log.warning("Failed to delete %s: %s", p, exc)
    return {"deleted": deleted, "bytes_freed": freed}


# --------------------------------------------------------------------------- #
# CLI 진입점
# --------------------------------------------------------------------------- #

def _parse_args() -> argparse.Namespace:  # noqa: D401
    ap = argparse.ArgumentParser(description="캐시 점검 및 정리 도구")
    ap.add_argument("--view", help="Restrict to a single view id")
    ap.add_argument("--older-than", type=int, metavar="DAYS", help="Purge entries older than N days")
    ap.add_argument("--purge", action="store_true", help="Delete matched cache entries")
    ap.add_argument("--dry-run", action="store_true", help="Compute impact without deleting")
    return ap.parse_args()


def main() -> None:  # noqa: D401
    args = _parse_args()
    threshold: datetime | None = None
    if args.older_than is not None:
        threshold = datetime.now(timezone.utc) - timedelta(days=args.older_than)

    if args.purge:
        stats = purge_cache(args.view, older_than=threshold, dry_run=args.dry_run)
        log.info("%s entries → %.1f MB freed%s", stats["deleted"], stats["bytes_freed"] / 1_048_576, " (dry‑run)" if args.dry_run else "")
    else:
        size_bytes, size_h = cache_size(args.view)
        log.info("Cache size%s: %s (%d bytes)", f" for '{args.view}'" if args.view else "", size_h, size_bytes)


# --------------------------------------------------------------------------- #
# 기타 유틸리티
# --------------------------------------------------------------------------- #

def _sizeof_fmt(num: int, suffix: str = "B") -> str:  # noqa: D401
    for unit in ("", "K", "M", "G", "T", "P", "E", "Z"):
        if abs(num) < 1024:
            return f"{num:.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Y{suffix}"


if __name__ == "__main__":  # pragma: no cover
    main()
