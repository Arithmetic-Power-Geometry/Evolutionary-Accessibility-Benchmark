"""Matched approximation and finite-population reference models.

The primary endpoint in this first recovery experiment is FIXATION of the all-mutant
target genotype by generation T. This differs deliberately from the earlier manuscript's
"at least one target individual appears" endpoint. Fixation makes the origin-fixation
and Wright-Fisher models answer the same target question.

M0-O is a sequential origin-fixation continuous-time approximation with instantaneous
substitutions. M1 is a haploid Wright-Fisher simulation. Agreement is expected only
when mutation waiting times dominate sweep times; that is a hypothesis to test, not
an assumption that results will confirm.
"""

from __future__ import annotations
import numpy as np
from scipy.linalg import expm
from .state import fitness_vector, forward_mutation_matrix, target_genotype


def fixation_probability_diffusion(relative_fitness: float, N: int) -> float:
    """Diffusion approximation for fixation of one haploid mutant.

    Uses p = (1-exp(-2*s))/(1-exp(-2*N*s)), with s = relative_fitness-1.
    The neutral limit is 1/N. This is an approximation used consistently in M0-O.
    """
    if N < 2:
        raise ValueError("N must be >= 2")
    if relative_fitness <= 0:
        raise ValueError("relative_fitness must be > 0")
    s = relative_fitness - 1.0
    if abs(s) < 1e-12:
        return 1.0 / N
    num = -np.expm1(-2.0 * s)
    den = -np.expm1(-2.0 * N * s)
    return float(num / den)


def origin_fixation_generator(k: int, N: int, mu: float, s: float) -> np.ndarray:
    """Generator over monomorphic genotypes for one-step forward substitutions."""
    if mu < 0:
        raise ValueError("mu must be >= 0")
    w = fitness_vector(k, s)
    n = 2**k
    Q = np.zeros((n, n), dtype=float)
    target = target_genotype(k)
    for g in range(n):
        if g == target:
            continue
        for bit in range(k):
            if (g >> bit) & 1:
                continue
            h = g | (1 << bit)
            pfix = fixation_probability_diffusion(w[h] / w[g], N)
            # N*mu mutant origins per generation at this locus, thinned by fixation.
            Q[g, h] = N * mu * pfix
        Q[g, g] = -Q[g].sum()
    return Q


def origin_fixation_probability(k: int, N: int, mu: float, s: float, T: int) -> float:
    """Probability target genotype has fixed by time T under M0-O."""
    if T < 0:
        raise ValueError("T must be >= 0")
    Q = origin_fixation_generator(k, N, mu, s)
    p0 = np.zeros(2**k)
    p0[0] = 1.0
    pT = p0 @ expm(Q * float(T))
    return float(pT[target_genotype(k)])


def wright_fisher_probability(
    k: int,
    N: int,
    mu: float,
    s: float,
    T: int,
    replicates: int,
    seed: int,
) -> tuple[float, int]:
    """Monte Carlo probability of target fixation by T under haploid Wright-Fisher M1.

    Selection acts through parental sampling weights; offspring then mutate independently
    at unreached loci. No back mutation or recombination is used in the recovery model.
    Returns (estimated probability, number of successful replicates).
    """
    if N < 2 or T < 0 or replicates < 1:
        raise ValueError("invalid N, T, or replicates")
    rng = np.random.default_rng(seed)
    nstates = 2**k
    target = target_genotype(k)
    w = fitness_vector(k, s)
    M = forward_mutation_matrix(k, mu)
    successes = 0

    for _ in range(replicates):
        counts = np.zeros(nstates, dtype=np.int64)
        counts[0] = N
        for _t in range(T):
            if counts[target] == N:
                successes += 1
                break
            weighted = counts * w
            parent_p = weighted / weighted.sum()
            offspring_p = parent_p @ M
            offspring_p = np.maximum(offspring_p, 0.0)
            offspring_p /= offspring_p.sum()
            counts = rng.multinomial(N, offspring_p)
        else:
            if counts[target] == N:
                successes += 1
    return successes / replicates, successes
