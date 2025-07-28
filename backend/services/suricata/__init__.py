# services/suricata/__init__.py

from .suricata_extractor import extract_rules_from_meta

__all__ = [
    "extract_rules_from_meta",
]