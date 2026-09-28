from eab.exact import exact_wf_one_locus_fixation_probability


def test_exact_zero_mutation_zero_fixation():
    assert exact_wf_one_locus_fixation_probability(20, 0.0, 0.01, 100) == 0.0


def test_exact_probability_bounds():
    p = exact_wf_one_locus_fixation_probability(20, 1e-3, 0.01, 100)
    assert 0.0 <= p <= 1.0


def test_exact_probability_increases_with_horizon():
    p1 = exact_wf_one_locus_fixation_probability(20, 1e-3, 0.01, 20)
    p2 = exact_wf_one_locus_fixation_probability(20, 1e-3, 0.01, 100)
    assert p2 >= p1
