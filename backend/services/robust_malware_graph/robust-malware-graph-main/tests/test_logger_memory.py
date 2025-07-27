import logging

from src.common.utils import get_logger


def test_logger_adds_memory_usage(caplog):
    logger = get_logger("test_mem")
    caplog.set_level("INFO", logger=logger.name)
    logger.info("hello")
    assert "RAM" in caplog.text and "VRAM" in caplog.text
