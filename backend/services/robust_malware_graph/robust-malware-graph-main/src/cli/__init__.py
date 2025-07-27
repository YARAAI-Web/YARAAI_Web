#!/usr/bin/env python3
"""robust‑malware‑graph ‑ CLI Package
====================================
A **unified entry‑point** that aggregates every command‑line tool under
``robust_malware_graph.cli`` so users can either

* call each script directly::

      python -m robust_malware_graph.cli.pretrain_selfgcl --help

* **or** (recommended) install the *console‑script* ``rmg-cli`` that lazily
  dispatches to the same sub‑commands::

      rmg-cli finetune-supcon --config configs/sup_con.yaml

Adding a new CLI tool is as simple as:

1. Drop a ``foo.py`` script under ``src/cli`` exposing a ``main()`` function.
2. Append ``{"foo": "foo"}`` to ``_COMMANDS`` below.

No further wiring required – the sub‑command is auto‑registered at import time.
"""
from __future__ import annotations

import ast
import importlib
import importlib.util
import sys
from types import ModuleType
from typing import Dict, List, Final, Optional

import click

__all__: list[str] = [
    "COMMANDS",
    "cli",
    "main",
]

# --------------------------------------------------------------------------- #
# 1. Sub‑command ↔ module map (lazy‑loaded)
# --------------------------------------------------------------------------- #
# Friendly CLI name → *module name* (within this package)
# NOTE: keep keys kebab‑case to match command‑line style.
_COMMANDS: Final[Dict[str, str]] = {
    "feature-mine": "rulegen_cli",
    "preprocess": "preprocessing",
    "pretrain-selfgcl": "pretrain_selfgcl",
    "finetune-supcon": "finetune_supcon",
    "detect": "detect",
    "certify-res": "certify_res",
    "train-resgcl": "train_res_gcl",
    "train-explainer": "explainer_train",
    "explain-refine": "explain_refine",
    "explainer-rule-eval": "explainer_rule_eval",
}

# Expose publicly in case external plugins need to introspect
COMMANDS: Dict[str, str] = dict(_COMMANDS)

# --------------------------------------------------------------------------- #
# 2. Helper ­– lazy import
# --------------------------------------------------------------------------- #

def _lazy_import(module_name: str) -> ModuleType:  # pragma: no cover
    """Import ``robust_malware_graph.cli.<module_name>`` on demand."""
    full_name = f"{__name__}.{module_name}"
    return importlib.import_module(full_name)


def _read_docstring(module_name: str) -> Optional[str]:  # pragma: no cover
    """Return the first line of the target module's docstring without importing."""
    spec = importlib.util.find_spec(f"{__name__}.{module_name}")
    if spec and spec.origin:
        try:
            with open(spec.origin, "r", encoding="utf-8") as fp:
                node = ast.parse(fp.read())
            doc = ast.get_docstring(node)
            if doc:
                return doc.splitlines()[0]
        except Exception:
            return None
    return None


# --------------------------------------------------------------------------- #
# 3. Build the **click** group dynamically
# --------------------------------------------------------------------------- #
@click.group(context_settings={"help_option_names": ["-h", "--help"]})
def cli() -> None:  # noqa: D401 (imperative mood)
    """Robust‑Malware‑Graph **unified** CLI.

    Use ``rmg-cli <command> --help`` to see each tool's options.
    """
    pass  # sub‑commands are attached below


def _add_proxy(cmd_name: str, module_name: str) -> None:  # pragma: no cover
    """Create a thin *proxy* command that forwards to ``module.main()``."""

    # Each script should expose a ``main(argv: list[str] | None = None)``
    @click.command(name=cmd_name, context_settings={
        "ignore_unknown_options": True,  # pass‑through
        "allow_extra_args": True,
    })
    @click.pass_context
    def _proxy(ctx: click.Context) -> None:  # noqa: WPS430 (nested)
        # Reconstruct the argv slice *after* the sub‑command token
        argv_slice: List[str] = list(sys.argv[sys.argv.index(cmd_name) + 1 :])
        module = _lazy_import(module_name)
        if not hasattr(module, "main"):
            raise AttributeError(
                f"{module.__name__!r} does not expose a callable `main()`",
            )
        module.main(argv_slice)

    # Adopt the docstring of the target module (first line only) without import
    doc = _read_docstring(module_name)
    if doc:
        _proxy.__doc__ = doc

    cli.add_command(_proxy)


for _cmd, _mod in _COMMANDS.items():
    _add_proxy(_cmd, _mod)

# --------------------------------------------------------------------------- #
# 4. *Console‑script* entry‑point
# --------------------------------------------------------------------------- #

def main(argv: List[str] | None = None) -> None:  # pragma: no cover
    """Entry‑point for *rmg-cli* (setuptools ``console_scripts``)."""
    cli.main(args=argv, standalone_mode=True)


# ``python -m robust_malware_graph.cli`` → behave like *rmg-cli*
if __name__ == "__main__":  # pragma: no cover
    main(sys.argv[1:])
