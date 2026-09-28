"""Shared genotype-space definitions used by approximation and reference models."""

from __future__ import annotations
import numpy as np


def genotypes(k: int) -> np.ndarray:
    if k < 1:
        raise ValueError("k must be >= 1")
    return np.arange(2**k, dtype=np.int64)


def mutation_count(g: int) -> int:
    return int(g).bit_count()


def fitness_vector(k: int, s: float) -> np.ndarray:
    if s <= -1:
        raise ValueError("s must be > -1")
    return np.array([(1.0 + s) ** mutation_count(g) for g in genotypes(k)], dtype=float)


def target_genotype(k: int) -> int:
    return (1 << k) - 1


def forward_mutation_matrix(k: int, mu: float) -> np.ndarray:
    """Independent forward mutation at each unreached locus; no back mutation."""
    if not (0.0 <= mu <= 1.0):
        raise ValueError("mu must lie in [0,1]")
    n = 2**k
    M = np.zeros((n, n), dtype=float)
    for g in range(n):
        missing = [b for b in range(k) if not (g >> b) & 1]
        m = len(missing)
        for mask in range(1 << m):
            h = g
            changed = 0
            for j, b in enumerate(missing):
                if (mask >> j) & 1:
                    h |= 1 << b
                    changed += 1
            M[g, h] += (mu**changed) * ((1.0 - mu) ** (m - changed))
    return M
