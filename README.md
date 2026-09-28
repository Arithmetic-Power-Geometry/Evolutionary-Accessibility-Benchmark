# Evolutionary Accessibility Benchmark

This repository implements a matched-model benchmark for asking a precise population-genetic question: **when does a sequential origin-fixation approximation reproduce the finite-horizon probability of target fixation in an explicit finite population?**

The project treats Wright-Fisher dynamics, fixation probabilities, origin-fixation theory, genotype findability, fitness landscapes, epistasis, and evolutionary accessibility as established foundations. The contribution is narrower: finite-horizon target-event probabilities are matched across models, approximation discrepancy is signed, an explicit tolerance can define endpoint-specific adequacy, and controlled assumption perturbations are tested without filtering out agreement or negative results.

## Core estimands

For matched models (M_0) and (M_1), target set (A), and horizon (T),

[
P_j(\theta)=\Pr_{M_j}(\tau_A\le T\mid X_0,\theta),\qquad j\in\{0,1\}.
]

The primary signed discrepancy is

[
E_{\log}(\theta)=\log_{10}\!\left(\frac{P_1(\theta)+\varepsilon}{P_0(\theta)+\varepsilon}\right).
]

Thus (E_{\log}>0) means the approximation underestimates the finite-population reference and (E_{\log}<0) means it overestimates it. The companion absolute discrepancy is (E_{\rm abs}=|P_1-P_0|).

Stage 5 used the predeclared analytical tolerance (	au=\log_{10}(2)), corresponding to a factor-two probability ratio. This tolerance is an analysis convention, not a biological constant.

## Models

- **M0-O:** sequential origin-fixation continuous-time Markov chain over monomorphic genotypes. Allowed substitutions occur at rate (N\mu p_{\rm fix}), and successful substitutions are instantaneous in the reduced process.
- **M1:** explicit haploid Wright-Fisher finite population with selection, mutation, and multinomial sampling.
- **Exact K=1 reference:** mutant-count Wright-Fisher Markov chain used to remove Monte Carlo noise from the finite-time mechanism diagnostic.
- **Stress extension:** matched two-locus fitness and mutation specifications supporting epistasis, state-dependent mutation, alternative targets, and paired perturbations.

The primary benchmark endpoint is **fixation of the declared target by generation (T)**.

## Completed evidence chain

1. **Recovery diagnostic:** six matched K=2 cells established the initial finite-horizon discrepancy pattern.
2. **Exact time-scale diagnostic:** 18 exact K=1 cells showed systematic contraction of discrepancy as the horizon became long relative to sweep time.
3. **Independent hold-out validation:** across 54 unseen cells, Spearman((\phi,|E_{\log}|)=0.9226) with (p=3.67\times10^{-23}), and all 18 matched series contracted monotonically with increasing horizon.
4. **K=2 benchmark:** 32 cells showed that sweep-time fraction remains informative but is not sufficient once multistep population dynamics enter; signed discrepancies occurred in both directions.
5. **Predeclared biological stress test:** all 36 cells remained within the factor-two tolerance. This negative result is retained. Several paired perturbations produced reproducible non-additive changes in signed approximation error.
6. **LTEE stress evidence:** generation-50,000 populations showed a 15.13-fold mutator/nonmutator median mutation-burden contrast, mutation-spectrum entropy medians 0.514 versus 1.236, and 14 independently listed Cit+ mutants distributed across two source-declared structural route classes (8 variant cit duplications and 6 IS3 insertions).

The LTEE results establish that assumption-stressing biological features occur in a long-term experimental system. They are not treated as causal validation of the approximation-error framework.

## Reproduce the software checks

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[test]"
pytest -q
```

Run individual computational stages:

```bash
python scripts/run_recovery.py
python scripts/run_timescale_diagnostic.py
python scripts/run_timescale_holdout.py
python scripts/run_k2_boundary.py

# Stage 5 can be sharded without altering the frozen design:
python scripts/run_stage5.py --baseline B1
python scripts/run_stage5.py --baseline B2
python scripts/run_stage5.py --baseline B3
python scripts/run_stage5.py --baseline B4
```

## Repository map

- `src/eab/` - model, exact-reference, metric, and stress-test implementations.
- `tests/` - unit and numerical-regression tests.
- `configs/` - frozen recovery configuration.
- `theory/` - predeclared definitions, hypotheses, protocols, and novelty/claim-discipline records.
- `results/` - frozen machine-readable results and diagnostic summaries.
- `.github/workflows/` - automated tests and reproducible computational workflows.

## Empirical data

The empirical stage uses publicly archived LTEE datasets:

- Tenaillon et al. / LTEE genomic data: Dryad DOI **10.5061/dryad.6226d**
- Blount et al. Cit+ data: Dryad DOI **10.5061/dryad.8q6n4**

The source archives should be obtained from Dryad rather than silently modified or redistributed.

## Reproducibility provenance

The successful sharded Stage-5 workflow is GitHub Actions run **36424797701**. All four predeclared baseline jobs completed successfully. An earlier unsharded run, **36403211328**, reached the 180-minute infrastructure timeout during simulation after its tests passed. The subsequent sharding changed execution only; scientific conditions, seeds, endpoints, and replicate counts were unchanged.

## Scope and claim discipline

This repository does **not** claim to introduce evolutionary accessibility, genotype findability, Wright-Fisher dynamics, Markov evolutionary dynamics, fixation probabilities, origin-fixation theory, epistasis, or route multiplicity. Those ideas have substantial prior literatures. The benchmark focuses on the model- and endpoint-specific magnitude and direction of finite-horizon target-probability approximation error.
