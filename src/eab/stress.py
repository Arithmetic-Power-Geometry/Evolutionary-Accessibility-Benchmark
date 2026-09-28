"""General K=2 stress-test engines for Stage 5."""

from __future__ import annotations
import numpy as np
from scipy.linalg import expm
from .models import fixation_probability_diffusion


def k2_fitness(s: float, eta: float = 0.0) -> np.ndarray:
    if s <= -1:
        raise ValueError("s must be > -1")
    w1 = 1.0 + s
    return np.array([1.0, w1, w1, w1*w1*np.exp(eta)], dtype=float)


def k2_state_mutation_matrix(mu: float, h: float = 1.0) -> np.ndarray:
    """Forward mutation; after one derived allele the remaining-locus rate is h*mu."""
    if mu < 0 or h < 0 or mu > 1 or h*mu > 1:
        raise ValueError("mutation probabilities must lie in [0,1]")
    M=np.zeros((4,4),float)
    M[0]=[(1-mu)**2, mu*(1-mu), mu*(1-mu), mu**2]
    M[1,1]=1-h*mu; M[1,3]=h*mu
    M[2,2]=1-h*mu; M[2,3]=h*mu
    M[3,3]=1.0
    return M


def _targets(targets) -> tuple[int,...]:
    t=tuple(sorted(set(int(x) for x in targets)))
    if not t or any(x<0 or x>3 for x in t):
        raise ValueError("targets must be nonempty K=2 genotype indices")
    return t


def origin_fixation_target_probability(N:int, mu:float, s:float, T:int,
                                          targets=(3,), eta:float=0.0,
                                          h:float=1.0) -> float:
    """M0 probability of hitting any declared monomorphic target by T."""
    targets=_targets(targets); w=k2_fitness(s,eta)
    Q=np.zeros((4,4),float)
    for g in range(4):
        if g in targets: continue
        rate=mu if g==0 else h*mu
        for bit in range(2):
            if (g>>bit)&1: continue
            z=g|(1<<bit)
            Q[g,z]=N*rate*fixation_probability_diffusion(w[z]/w[g],N)
        Q[g,g]=-Q[g].sum()
    p=np.zeros(4); p[0]=1
    return float((p@expm(Q*T))[list(targets)].sum())


def wright_fisher_target_probability(N:int, mu:float, s:float, T:int,
                                         replicates:int, seed:int, targets=(3,),
                                         eta:float=0.0, h:float=1.0,
                                         return_successes:bool=False):
    """M1 probability that any declared target genotype fixes by T.

    Target-fixed populations are counted at first fixation. Replicate-level binary
    outcomes can be returned for reproducible bootstrap contrasts.
    """
    if N<2 or T<0 or replicates<1: raise ValueError("invalid N, T, or replicates")
    targets=_targets(targets); target_set=set(targets)
    w=k2_fitness(s,eta); M=k2_state_mutation_matrix(mu,h)
    rng=np.random.default_rng(seed); y=np.zeros(replicates,dtype=np.uint8)
    for r in range(replicates):
        c=np.array([N,0,0,0],dtype=np.int64)
        for _ in range(T):
            fixed=int(np.argmax(c)) if c.max()==N else -1
            if fixed in target_set:
                y[r]=1; break
            pp=(c*w); pp=pp/pp.sum(); q=pp@M
            q=np.maximum(q,0); q=q/q.sum()
            c=rng.multinomial(N,q)
        else:
            fixed=int(np.argmax(c)) if c.max()==N else -1
            if fixed in target_set: y[r]=1
    p=float(y.mean())
    return (p,y) if return_successes else (p,int(y.sum()))
