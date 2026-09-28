import numpy as np
from eab.stress import (
    k2_fitness,k2_state_mutation_matrix,
    origin_fixation_target_probability,wright_fisher_target_probability,
)
from eab.models import origin_fixation_probability, wright_fisher_probability

def test_k2_mutation_rows_stochastic():
    M=k2_state_mutation_matrix(1e-3,5)
    assert np.allclose(M.sum(axis=1),1)
    assert np.all(M>=0)

def test_k2_epistasis_map():
    s=.02
    w0=k2_fitness(s,0)
    wp=k2_fitness(s,.02)
    wm=k2_fitness(s,-.02)
    assert np.isclose(w0[3],(1+s)**2)
    assert wp[3]>w0[3]>wm[3]
    assert np.allclose(wp[:3],w0[:3])

def test_h_one_matches_baseline_m0():
    args=dict(N=100,mu=5e-5,s=.01,T=1000)
    a=origin_fixation_target_probability(**args,targets=(3,),eta=0,h=1)
    b=origin_fixation_probability(k=2,**args)
    assert np.isclose(a,b,rtol=1e-12,atol=1e-14)

def test_h_one_matches_baseline_m1_seeded():
    args=dict(N=40,mu=2e-4,s=.01,T=100,replicates=40,seed=991)
    a=wright_fisher_target_probability(**args,targets=(3,),eta=0,h=1)
    b=wright_fisher_probability(k=2,**args)
    assert a==b

def test_multiple_targets_absorbing_m0():
    p=origin_fixation_target_probability(N=100,mu=1e-4,s=.01,T=10000,targets=(1,2))
    assert 0<=p<=1

def test_replicate_outputs_binary_and_reproducible():
    kw=dict(N=30,mu=1e-3,s=.01,T=100,replicates=30,seed=123,targets=(1,2))
    p1,y1=wright_fisher_target_probability(**kw,return_successes=True)
    p2,y2=wright_fisher_target_probability(**kw,return_successes=True)
    assert np.array_equal(y1,y2)
    assert set(np.unique(y1)).issubset({0,1})
    assert p1==p2==y1.mean()

def test_zero_mutation_zero_target():
    assert origin_fixation_target_probability(100,0,.01,1000)==0
    p,hits=wright_fisher_target_probability(30,0,.01,100,20,4)
    assert p==0 and hits==0
