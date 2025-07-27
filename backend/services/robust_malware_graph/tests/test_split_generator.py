import csv
from pathlib import Path

import json
import pytest

pytest.importorskip("numpy")

from src.graphs.dataset.split_generator import split_by_time, build_time_splits


def _make_graph_files(tmp_path: Path, shas: list[str]):
    graph_dir = tmp_path / "graphs"
    graph_dir.mkdir()
    for sha in shas:
        (graph_dir / f"{sha}.pt").write_text("")
    return graph_dir


def _write_meta(tmp_path: Path, rows: list[dict[str, str]]):
    meta = tmp_path / "meta.csv"
    with meta.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    return meta


def test_split_by_time_missing_date_skip(tmp_path):
    rows = [
        {"sha256": "a", "collected_at": "2023-01-01"},
        {"sha256": "b", "collected_at": "BAD"},
        {"sha256": "c", "collected_at": "2024-01-02"},
    ]
    meta = _write_meta(tmp_path, rows)
    graph_dir = _make_graph_files(tmp_path, ["a", "b", "c"])
    out = tmp_path / "splits"

    split_by_time(meta, graph_dir, out, cut_date="2024-01-01", fallback="skip")

    lists = []
    for s in ["train", "val", "test"]:
        lst = (out / s / f"{s}_list.txt").read_text().splitlines()
        lists.extend(lst)
    assert "b" not in lists


def test_split_by_time_missing_date_random(tmp_path):
    rows = [
        {"sha256": "a", "collected_at": "2023-01-01"},
        {"sha256": "b", "collected_at": "BAD"},
        {"sha256": "c", "collected_at": "2024-01-02"},
    ]
    meta = _write_meta(tmp_path, rows)
    graph_dir = _make_graph_files(tmp_path, ["a", "b", "c"])
    out = tmp_path / "splits"

    split_by_time(meta, graph_dir, out, cut_date="2024-01-01", fallback="random")

    lists = []
    for s in ["train", "val", "test"]:
        lst = (out / s / f"{s}_list.txt").read_text().splitlines()
        lists.extend(lst)
    assert "b" in lists


def test_split_by_time_overwrite(tmp_path):
    """Running split_by_time twice should not raise FileExistsError."""
    rows = [{"sha256": "a", "collected_at": "2023-01-01"}]
    meta = _write_meta(tmp_path, rows)
    graph_dir = _make_graph_files(tmp_path, ["a"])
    out = tmp_path / "splits"

    split_by_time(meta, graph_dir, out, cut_date="2024-01-01")
    # rerun with existing output files
    split_by_time(meta, graph_dir, out, cut_date="2024-01-01")


def test_build_time_splits_json(tmp_path):
    rows = [
        {"sha256": "x", "collected_at": "2023-01-01", "label": "0"},
        {"sha256": "y", "collected_at": "2024-01-02", "label": "1"},
    ]
    meta = _write_meta(tmp_path, rows)
    graph_dir = _make_graph_files(tmp_path, ["x", "y"])
    out = tmp_path / "splits"

    json_path = tmp_path / "split.json"
    train, val, test = build_time_splits(
        hetero_dir=graph_dir,
        splits_dir=out,
        meta_csv=meta,
        json_out=json_path,
    )

    assert json_path.is_file()
    js = json.loads(json_path.read_text())
    assert js["train"] == train
    assert js["val"] == val
    assert js["test"] == test

    # labels.csv should exist for each split
    for split, shas in {"train": train, "val": val, "test": test}.items():
        csv_path = out / split / "labels.csv"
        assert csv_path.is_file()
        rows = csv_path.read_text().strip().splitlines()
        assert rows[0] == "sha256,label"
        csv_shas = {r.split(",")[0] for r in rows[1:]}
        assert csv_shas == set(shas)

