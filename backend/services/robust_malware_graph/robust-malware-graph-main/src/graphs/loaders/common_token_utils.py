import re

TOKEN_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")
MAX_TOKENS = 1024


def split_name(name: str) -> list[str]:
    name = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", name)
    return [t.lower() for t in re.split(r"[_\s]+", name) if t]

