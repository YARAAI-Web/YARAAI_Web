import inspect
import pytest

pytest.importorskip("networkx")

from src.extract.extractors.view_registry import (
    list_views,
    get_extractor,
    ViewRegistrationError,
)
from src.extract.base import ExtractorBase
from src.extract.constants import DEFAULT_VIEWS_DIR, VIEW_CFG
from src.extract.extractors.cfg_extractor import CFGExtractor
from src.extract.extractors.syscall_extractor import SysCallExtractor
from src.extract.constants import VIEW_SYSCALL


def test_extractors_concrete():
    for view_id in list_views():
        try:
            cls = get_extractor(view_id)
        except ViewRegistrationError as exc:
            pytest.skip(f"dependency missing for {view_id}: {exc}")
        assert not inspect.isabstract(cls), f"{view_id} still abstract"


def test_cfg_extractor_default_out_dir():
    ext = CFGExtractor()
    assert ext.out_dir == DEFAULT_VIEWS_DIR / VIEW_CFG


def test_syscall_extractor_run(tmp_path):
    pytest.importorskip("angr")

    asm = tmp_path / "exit.s"
    asm.write_text(
        """
        .global _start
    _start:
        mov $60, %rax
        xor %rdi, %rdi
        syscall
        """
    )
    bin_path = tmp_path / "exit"
    import subprocess

    subprocess.check_call(["gcc", "-nostdlib", "-static", "-o", str(bin_path), str(asm)])

    ext = SysCallExtractor(cache_dir=tmp_path)
    result = ext.run(bin_path)

    assert result["view"] == VIEW_SYSCALL
    assert result.get("binary_sha256")

