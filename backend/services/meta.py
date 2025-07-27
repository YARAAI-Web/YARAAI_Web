# backend/services/meta.py
import os, json

META_DIR = os.path.join(os.path.dirname(__file__), '..', 'meta_json')

def _load_meta(base):
    path = os.path.join(META_DIR, f"{base}.json")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Meta JSON not found: {path}")
    with open(path, encoding='utf-8') as f:
        return json.load(f)

def get_metadata(base):
    return _load_meta(base).get("get_metadata", {})

def get_current_address(base):
    return _load_meta(base).get("get_current_address")

def get_current_function(base):
    return _load_meta(base).get("get_current_function", {})

def get_entry_points(base):
    return _load_meta(base).get("get_entry_points", [])

def file_entropy(base):
    return _load_meta(base).get("file_entropy")

def string_stats(base):
    return _load_meta(base).get("string_stats", {})

def pe_headers(base):
    return _load_meta(base).get("pe_headers", {})
