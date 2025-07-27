from __future__ import annotations

from typing import Sequence, Tuple

import logging
import json
import subprocess
import tempfile
from pathlib import Path

try:
    import yara  # type: ignore
except ModuleNotFoundError:  # pragma: no cover - optional dependency
    yara = None

import torch
from torch_geometric.data import HeteroData

from .metrics import Metric

class RuleEvaluator:
    """Placeholder rule evaluator used by :class:`RuleGenEnv`."""

    def __init__(self, *, clf: torch.nn.Module, device: str | torch.device = "cpu", batch_size: int = 128):
        self.clf = clf
        self.device = device
        self.batch_size = batch_size

    def evaluate_rule(
        self,
        rule_text: str,
        clean_set: Sequence[HeteroData],
        dummy_set: Sequence[HeteroData],
    ) -> Tuple[float, float, float, Tuple[int, int, int, int]]:
        """Evaluate ``rule_text`` on provided datasets.

        Parameters
        ----------
        rule_text : str
            YARA or CAPA rule text.
        clean_set : sequence of :class:`HeteroData`
            Clean (negative) samples.
        dummy_set : sequence of :class:`HeteroData`
            Dummy/malicious (positive) samples.

        Returns
        -------
        tuple
            ``(f1_clean, f1_dummy, certified_r, (TP, FP, FN, TN))``
        """

        log = logging.getLogger(__name__)

        try:
            rule_type = "capa" if rule_text.lstrip().startswith("rule:") else "yara"
            rule_path = None

            if rule_type == "yara":
                if yara is None:
                    raise RuntimeError("yara module not available")
                compiled = yara.compile(source=rule_text)

                def _match(path: Path) -> bool:
                    try:
                        return bool(compiled.match(str(path)))
                    except Exception:  # pragma: no cover - yara errors
                        return False

            else:  # capa rule
                with tempfile.NamedTemporaryFile("w", suffix=".yml", delete=False) as tmp:
                    tmp.write(rule_text)
                    tmp.flush()
                    rule_path = tmp.name

                def _match(path: Path) -> bool:
                    try:
                        proc = subprocess.run(
                            ["capa", str(path), "-r", rule_path, "--json"],
                            capture_output=True,
                            text=True,
                            check=False,
                        )
                    except FileNotFoundError as exc:  # pragma: no cover - capa missing
                        raise RuntimeError("capa executable not available") from exc

                    if proc.returncode != 0:
                        return False
                    try:
                        js = json.loads(proc.stdout)
                    except Exception:
                        return False
                    return bool(js.get("rules"))

        except Exception as exc:
            log.warning("Rule compilation failed: %s", exc)
            return 0.0, 0.0, -1.0, (0, 0, 0, 0)

        TP = FP = FN = TN = 0

        def _get_path(g: HeteroData) -> Path | None:
            p = getattr(g, "file_path", None)
            if p is not None:
                return Path(p)
            sha = getattr(g, "sha256", None)
            if sha is not None:
                return Path(str(sha))
            return None

        try:
            for g in dummy_set:
                path = _get_path(g)
                matched = _match(path) if path is not None else False
                if matched:
                    TP += 1
                else:
                    FN += 1

            for g in clean_set:
                path = _get_path(g)
                matched = _match(path) if path is not None else False
                if matched:
                    FP += 1
                else:
                    TN += 1

            # F1 for positive (dummy)
            denom = 2 * TP + FP + FN
            f1_dummy = 0.0 if denom == 0 else 2 * TP / denom

            # F1 for negative (clean) – treat label 0 as positive
            denom_clean = 2 * TN + FP + FN
            f1_clean = 0.0 if denom_clean == 0 else 2 * TN / denom_clean

            certified_r = 0.0
            calc_r = getattr(self.clf, "calc_certified_radius", None)
            if callable(calc_r):
                try:
                    certified_r = float(calc_r())
                except Exception as exc:  # pragma: no cover - robustness errors
                    log.warning("certified radius computation failed: %s", exc)
                    certified_r = 0.0

            counts = (TP, FP, FN, TN)
            return f1_clean, f1_dummy, certified_r, counts
        except Exception as exc:  # pragma: no cover - unexpected evaluation errors
            log.warning("rule evaluation failed: %s", exc)
            return 0.0, 0.0, -1.0, (0, 0, 0, 0)
        finally:
            if rule_path is not None:
                try:
                    Path(rule_path).unlink(missing_ok=True)
                except Exception:
                    pass
