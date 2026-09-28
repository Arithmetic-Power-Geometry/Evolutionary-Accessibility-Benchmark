import numpy as np
from eab.state import forward_mutation_matrix, target_genotype
from eab.models import fixation_probability_diffusion, origin_fixation_probability, wright_fisher_probability
from eab.metrics import error_metrics


def test_mutation_matrix_is_stochastic():
    M = forward_mutation_matrix(k=4, mu=1e-3)
    assert np.allclose(M.sum(axis=1), 1.0)
    assert np.all(M >= 0)


def test_target_is_absorbing_under_forward_mutation():
    k = 4
    M = forward_mutation_matrix(k, 1e-3)
    t = target_genotype(k)
    assert np.isclose(M[t, t], 1.0)


def test_neutral_fixation_limit():
    assert np.isclose(fixation_probability_diffusion(1.0, 200), 1/200)


def test_zero_mutation_zero_target_probability():
    assert origin_fixation_probability(k=2, N=100, mu=0.0, s=0.01, T=100) == 0.0
    p, hits = wright_fisher_probability(k=2, N=50, mu=0.0, s=0.01, T=20, replicates=20, seed=1)
    assert p == 0.0 and hits == 0


def test_probability_bounds():
    p0 = origin_fixation_probability(k=2, N=100, mu=1e-3, s=0.01, T=100)
    p1, _ = wright_fisher_probability(k=2, N=100, mu=1e-3, s=0.01, T=100, replicates=20, seed=2)
    assert 0 <= p0 <= 1
    assert 0 <= p1 <= 1


def test_error_sign():
    assert error_metrics(0.1, 0.2, 1e-9)["e_log"] > 0
    assert error_metrics(0.2, 0.1, 1e-9)["e_log"] < 0
