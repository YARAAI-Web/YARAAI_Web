import argparse
import json
import pytest

pytest.importorskip("numpy")

from src.cli.preprocessing import run_labels


def test_run_labels(tmp_path):
    raw_dir = tmp_path / "raw"
    raw_dir.mkdir()
    data = {"virustotal": {"sha256": "deadbeef"}}
    (raw_dir / "sample.json").write_text(json.dumps(data))

    args = argparse.Namespace(
        input_dir=str(raw_dir),
        out_dir=str(tmp_path),
        workers=1,
        log_level="INFO",
        overwrite=False,
        command="labels",
        label=1,
        csv=str(tmp_path / "labels.csv"),
        date_key=None,
    )

    run_labels(args)

    csv_path = tmp_path / "labels.csv"
    text = csv_path.read_text().strip().splitlines()
    assert text[0] == "sha256,label,filename"
    assert "deadbeef,1,sample.json" in text[1]


def test_run_labels_with_date_key(tmp_path):
    raw_dir = tmp_path / "raw"
    raw_dir.mkdir()
    data = {
        "virustotal": {"sha256": "deadbeef"},
        "meta": {"date": "2024-01-02"},
    }
    (raw_dir / "sample.json").write_text(json.dumps(data))

    args = argparse.Namespace(
        input_dir=str(raw_dir),
        out_dir=str(tmp_path),
        workers=1,
        log_level="INFO",
        overwrite=False,
        command="labels",
        label=1,
        csv=str(tmp_path / "labels.csv"),
        date_key="meta.date",
    )

    run_labels(args)

    csv_path = tmp_path / "labels.csv"
    text = csv_path.read_text().strip().splitlines()
    assert text[0] == "sha256,label,filename,collected_at"
    assert "deadbeef,1,sample.json,2024-01-02" in text[1]
