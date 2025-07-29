from __future__ import annotations

import torch
from typing import Mapping, Any


class CategoricalOptimizer:
    """Simple optimizer for discrete rule parameters."""

    CONDITION_TYPES = ["any", "all", "percentage", "count", "combo"]
    COMBINE_MODES = ["or", "and"]

    FREQ_MIN = -1.0
    FREQ_MAX = 100.0
    GROUP_MIN_MIN = 0.0
    GROUP_MIN_MAX = 10.0

    def __init__(self, lr: float = 0.1, beta: float = 0.5) -> None:
        """Initialize parameters with logits matching default CLI values."""

        # condition_type defaults to "combo"
        cond_init = torch.zeros(len(self.CONDITION_TYPES))
        cond_init[self.CONDITION_TYPES.index("combo")] = 1.0
        self.condition_type_logits = torch.nn.Parameter(cond_init)

        # combine_mode defaults to "or" -> zeros so argmax selects first element
        self.combine_mode_logits = torch.nn.Parameter(torch.zeros(len(self.COMBINE_MODES)))

        # boolean options default to False except auto_relax which defaults True
        self.dynamic_k_logit = torch.nn.Parameter(torch.tensor(0.0))
        self.auto_relax_logit = torch.nn.Parameter(torch.tensor(10.0))
        self.adjust_group_percentage_logit = torch.nn.Parameter(torch.tensor(0.0))

        # ratio defaults
        self.group_min_ratio_logit = torch.nn.Parameter(torch.logit(torch.tensor(1e-3)))
        self.combine_min_ratio_logit = torch.nn.Parameter(torch.logit(torch.tensor(0.7)))

        self.freq_threshold_logit = torch.nn.Parameter(
            torch.logit(
                torch.tensor(
                    (10.0 - self.FREQ_MIN) / (self.FREQ_MAX - self.FREQ_MIN)
                )
            )
        )
        self.group_min_count_logit = torch.nn.Parameter(
            torch.logit(
                torch.tensor(
                    (0.0 - self.GROUP_MIN_MIN)
                    / (self.GROUP_MIN_MAX - self.GROUP_MIN_MIN)
                    if self.GROUP_MIN_MAX > self.GROUP_MIN_MIN
                    else 0.0
                )
            )
        )

        self._params = [
            self.condition_type_logits,
            self.combine_mode_logits,
            self.dynamic_k_logit,
            self.auto_relax_logit,
            self.adjust_group_percentage_logit,
            self.group_min_ratio_logit,
            self.combine_min_ratio_logit,
            self.freq_threshold_logit,
            self.group_min_count_logit,
        ]
        self.beta = beta
        self.optimizer = torch.optim.AdamW(self._params, lr=lr)

    # ------------------------------------------------------------------
    def state_dict(self) -> dict:
        return {
            "logits": {k: p.detach().cpu() for k, p in self._logit_map().items()},
            "optimizer": self.optimizer.state_dict(),
            "beta": float(self.beta),
        }

    def load_state_dict(self, state: dict) -> None:
        logits = state.get("logits", {})
        for name, param in self._logit_map().items():
            if name in logits:
                param.data.copy_(torch.tensor(logits[name]))
        if "optimizer" in state:
            self.optimizer.load_state_dict(state["optimizer"])
        if "beta" in state:
            self.beta = float(state["beta"])

    def _logit_map(self) -> dict[str, torch.nn.Parameter]:
        return {
            "condition_type": self.condition_type_logits,
            "combine_mode": self.combine_mode_logits,
            "dynamic_k": self.dynamic_k_logit,
            "auto_relax": self.auto_relax_logit,
            "adjust_group_percentage": self.adjust_group_percentage_logit,
            "group_min_ratio": self.group_min_ratio_logit,
            "combine_min_ratio": self.combine_min_ratio_logit,
            "freq_threshold": self.freq_threshold_logit,
            "group_min_count": self.group_min_count_logit,
        }

    # ------------------------------------------------------------------
    def discrete_params(self) -> dict[str, object]:
        cond = self.CONDITION_TYPES[int(torch.argmax(self.condition_type_logits).item())]
        comb = self.COMBINE_MODES[int(torch.argmax(self.combine_mode_logits).item())]
        dynamic_k = torch.sigmoid(self.dynamic_k_logit).item() > 0.5
        auto_relax = torch.sigmoid(self.auto_relax_logit).item() > 0.5
        adjust_gp = torch.sigmoid(self.adjust_group_percentage_logit).item() > 0.5
        g_ratio = torch.sigmoid(self.group_min_ratio_logit).item()
        c_ratio = torch.sigmoid(self.combine_min_ratio_logit).item()
        freq = (
            torch.sigmoid(self.freq_threshold_logit).item()
            * (self.FREQ_MAX - self.FREQ_MIN)
            + self.FREQ_MIN
        )
        g_count_f = (
            torch.sigmoid(self.group_min_count_logit).item()
            * (self.GROUP_MIN_MAX - self.GROUP_MIN_MIN)
            + self.GROUP_MIN_MIN
        )
        g_count = int(round(g_count_f))
        if g_count <= 0:
            g_count_val: int | None = None
        else:
            g_count_val = g_count
        return {
            "condition_type": cond,
            "combine_mode": comb,
            "dynamic_k": dynamic_k,
            "auto_relax": auto_relax,
            "adjust_group_percentage": adjust_gp,
            "group_min_ratio": g_ratio,
            "combine_min_ratio": c_ratio,
            "freq_threshold": freq,
            "group_min_count": g_count_val,
        }

    # ------------------------------------------------------------------
    def step(
        self,
        trial_or_loss: torch.Tensor | float | Mapping[str, Any] | Sequence[Mapping[str, Any]],
        fp_ratio_benign: float = 0.0,
    ) -> None:
        """Perform one optimizer step.

        ``trial_or_loss`` may be a loss ``Tensor``/``float`` or a result mapping
        from :func:`evaluate_single`.  When a sequence of mappings is provided,
        the mean loss over the batch is used for the update.
        """

        from collections.abc import Sequence
        from .explainer_rule_eval import _optimizer_loss

        if isinstance(trial_or_loss, Mapping) or (
            isinstance(trial_or_loss, Sequence)
            and trial_or_loss
            and isinstance(trial_or_loss[0], Mapping)
        ):
            loss = _optimizer_loss(trial_or_loss, self, fp_ratio_benign, beta=self.beta)
        else:
            loss = trial_or_loss
            if not isinstance(loss, torch.Tensor):
                loss = torch.tensor(float(loss), device=self.condition_type_logits.device)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

    # ------------------------------------------------------------------
    def load_discrete_params(self, params: Mapping[str, Any]) -> None:
        """Load discrete parameters into optimizer logits."""

        if (val := params.get("condition_type")) in self.CONDITION_TYPES:
            idx = self.CONDITION_TYPES.index(val)
            self.condition_type_logits.data.zero_()
            self.condition_type_logits.data[idx] = 10.0
        if (val := params.get("combine_mode")) in self.COMBINE_MODES:
            idx = self.COMBINE_MODES.index(val)
            self.combine_mode_logits.data.zero_()
            self.combine_mode_logits.data[idx] = 10.0
        if "dynamic_k" in params:
            self.dynamic_k_logit.data.fill_(10.0 if params["dynamic_k"] else -10.0)
        if "auto_relax" in params:
            self.auto_relax_logit.data.fill_(10.0 if params["auto_relax"] else -10.0)
        if "adjust_group_percentage" in params:
            self.adjust_group_percentage_logit.data.fill_(
                10.0 if params["adjust_group_percentage"] else -10.0
            )
        if "group_min_ratio" in params:
            val = float(params["group_min_ratio"])
            val = min(max(val, 0.0), 1.0)
            self.group_min_ratio_logit.data.copy_(torch.logit(torch.tensor(val)))
        if "combine_min_ratio" in params:
            val = float(params["combine_min_ratio"])
            val = min(max(val, 0.0), 1.0)
            self.combine_min_ratio_logit.data.copy_(torch.logit(torch.tensor(val)))
        if "freq_threshold" in params:
            val = float(params["freq_threshold"])
            val = min(max(val, self.FREQ_MIN), self.FREQ_MAX)
            norm = (val - self.FREQ_MIN) / (self.FREQ_MAX - self.FREQ_MIN)
            self.freq_threshold_logit.data.copy_(torch.logit(torch.tensor(norm)))
        if "group_min_count" in params:
            gval = params["group_min_count"]
            if gval is None:
                norm = 0.0
            else:
                gval = float(min(max(int(gval), self.GROUP_MIN_MIN), self.GROUP_MIN_MAX))
                norm = (gval - self.GROUP_MIN_MIN) / (self.GROUP_MIN_MAX - self.GROUP_MIN_MIN)
            self.group_min_count_logit.data.copy_(torch.logit(torch.tensor(norm)))


class PopulationOptimizer:
    """Simple genetic optimizer wrapping multiple ``CategoricalOptimizer``s."""

    def __init__(
        self,
        population_size: int = 4,
        *,
        mutation_rate: float = 0.1,
        crossover_rate: float = 0.5,
        steps: int = 1,
        local_steps: int = 1,
        beta: float = 0.5,
    ) -> None:
        self.population_size = max(1, population_size)
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.steps = steps
        self.local_steps = max(1, int(local_steps))
        self.optimizers = [CategoricalOptimizer(beta=beta) for _ in range(self.population_size)]
        self.best_index = 0
    # ------------------------------------------------------------------
    def state_dict(self) -> dict:
        return {
            "population": [opt.state_dict() for opt in self.optimizers],
            "mutation_rate": self.mutation_rate,
            "crossover_rate": self.crossover_rate,
            "steps": self.steps,
            "local_steps": self.local_steps,
        }

    def load_state_dict(self, state: dict) -> None:
        pop = state.get("population", [])
        for opt, st in zip(self.optimizers, pop):
            opt.load_state_dict(st)
        self.mutation_rate = float(state.get("mutation_rate", self.mutation_rate))
        self.crossover_rate = float(state.get("crossover_rate", self.crossover_rate))
        self.steps = int(state.get("steps", self.steps))
        self.local_steps = int(state.get("local_steps", self.local_steps))

    # ------------------------------------------------------------------
    def step(self, results: list[Mapping[str, Any]]) -> None:
        from .explainer_rule_eval import _optimizer_loss

        losses: list[float] = []
        for opt, res in zip(self.optimizers, results):
            loss = _optimizer_loss(res, opt, res.get("fp_ratio_benign", 0.0))
            opt.step(loss)
            losses.append(float(loss.item()))

        if losses:
            self.best_index = int(sorted(range(len(losses)), key=lambda i: losses[i])[0])
            best_result = results[self.best_index]
        else:
            best_result = {}

        # selection based on current generation losses
        order = sorted(range(len(losses)), key=lambda i: losses[i])
        parents = [self.optimizers[i] for i in order[: max(1, len(order) // 2)]]

        import random

        current = parents
        steps = max(1, int(self.steps))
        for _ in range(steps):
            new_opts: list[CategoricalOptimizer] = []
            while len(new_opts) < self.population_size:
                parent1 = random.choice(current)
                parent2 = random.choice(current)
                child_params = parent1.discrete_params()
                other = parent2.discrete_params()
                for k in child_params.keys():
                    if random.random() < self.crossover_rate:
                        child_params[k] = other[k]
                if random.random() < self.mutation_rate:
                    key = random.choice(list(child_params.keys()))
                    self._mutate_param(child_params, key)
                child = CategoricalOptimizer(beta=parent1.beta)
                child.load_discrete_params(child_params)
                new_opts.append(child)
            current = new_opts

        # local optimization on new population using best result
        if best_result:
            for opt in current:
                for _ in range(self.local_steps):
                    loss = _optimizer_loss(best_result, opt, best_result.get("fp_ratio_benign", 0.0))
                    opt.step(loss)

        self.optimizers = current

    # ------------------------------------------------------------------
    def best_discrete_params(self) -> dict[str, object]:
        if not self.optimizers:
            return CategoricalOptimizer().discrete_params()
        return self.optimizers[self.best_index].discrete_params()

    # ------------------------------------------------------------------
    @staticmethod
    def _mutate_param(params: dict, key: str) -> None:
        import random

        if key == "condition_type":
            params[key] = random.choice(CategoricalOptimizer.CONDITION_TYPES)
        elif key == "combine_mode":
            params[key] = random.choice(CategoricalOptimizer.COMBINE_MODES)
        elif key in {"dynamic_k", "auto_relax", "adjust_group_percentage"}:
            params[key] = not params.get(key, False)
        elif key in {"group_min_ratio", "combine_min_ratio"}:
            params[key] = min(1.0, max(0.0, params.get(key, 0.5) + random.uniform(-0.1, 0.1)))
        elif key == "freq_threshold":
            val = params.get(key, 10.0) + random.uniform(-1.0, 1.0)
            params[key] = min(CategoricalOptimizer.FREQ_MAX, max(CategoricalOptimizer.FREQ_MIN, val))
        elif key == "group_min_count":
            val = int(params.get(key, 0) or 0)
            val += random.choice([-1, 1])
            val = min(int(CategoricalOptimizer.GROUP_MIN_MAX), max(int(CategoricalOptimizer.GROUP_MIN_MIN), val))
            params[key] = None if val <= 0 else val


