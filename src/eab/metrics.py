"""Model-comparison metrics with strict floating-point boundary handling."""

from __future__ import annotations
import math


def _probability(x: float, tol: float = 1e-12) -> float:
    x=float(x)
    if not math.isfinite(x):
        raise ValueError("probabilities must be finite")
    if x < -tol or x > 1.0 + tol:
        raise ValueError(f"probabilities must lie in [0,1]; got {x!r}")
    return min(1.0,max(0.0,x))


def error_metrics(p0: float,p1: float,epsilon: float) -> dict[str,float]:
    if epsilon <= 0:
        raise ValueError("epsilon must be > 0")
    p0=_probability(p0); p1=_probability(p1)
    elog=math.log10((p1+epsilon)/(p0+epsilon))
    return {"p0":p0,"p1":p1,"e_log":elog,"e_abs":abs(p1-p0)}
