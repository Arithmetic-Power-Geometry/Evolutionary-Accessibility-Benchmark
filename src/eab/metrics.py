"""Model-comparison metrics."""

from __future__ import annotations
import math


def error_metrics(p0: float, p1: float, epsilon: float) -> dict[str, float]:
    if not (0 <= p0 <= 1 and 0 <= p1 <= 1):
        raise ValueError("probabilities must lie in [0,1]")
    if epsilon <= 0:
        raise ValueError("epsilon must be > 0")
    elog = math.log10((p1 + epsilon) / (p0 + epsilon))
    return {
        "p0": p0,
        "p1": p1,
        "e_log": elog,
        "e_abs": abs(p1 - p0),
    }
