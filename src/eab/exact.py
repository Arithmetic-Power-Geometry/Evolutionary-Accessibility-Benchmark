"""Exact small-state Wright-Fisher calculations for diagnostic experiments."""

from __future__ import annotations
import numpy as np
from scipy.stats import binom


def exact_wf_one_locus_fixation_probability(N: int, mu: float, s: float, T: int) -> float:
    """Exact probability of mutant fixation by generation T for one forward-mutating locus.

    States are mutant counts 0..N. Selection acts before reproduction; wild-type
    offspring mutate forward with probability mu; there is no back mutation.
    State N is absorbing. Matrix exponentiation removes Monte Carlo error from this
    diagnostic and isolates model/time-scale discrepancy.
    """
    if N < 2 or T < 0 or not (0 <= mu <= 1) or s <= -1:
        raise ValueError("invalid N, mu, s, or T")
    counts = np.arange(N + 1)
    P = np.empty((N + 1, N + 1), dtype=float)
    w = 1.0 + s
    for i in range(N + 1):
        if i == N:
            P[i] = 0.0
            P[i, N] = 1.0
            continue
        q_sel = (i * w) / ((N - i) + i * w)
        q_off = q_sel + (1.0 - q_sel) * mu
        P[i] = binom.pmf(counts, N, q_off)
        P[i] /= P[i].sum()
    PT = np.linalg.matrix_power(P, T)
    return float(PT[0, N])
