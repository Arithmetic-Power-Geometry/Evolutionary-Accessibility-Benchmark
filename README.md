# When Does Origin–Fixation Approximate Finite-Population Evolution?

## A Finite-Horizon Target-Probability Benchmark with Exact Diagnostics, Stress Tests, and Long-Term Evolution Evidence

This repository contains the software, frozen configurations, tests, machine-readable results, and analysis records supporting the study by **Mohammad Amir Khusru Akhtar (2026)**.

The study asks a specific population-genetic question: **when does a sequential origin–fixation approximation reproduce the finite-horizon probability of target fixation in an explicit finite population?** The approximation is compared with a haploid Wright–Fisher reference for the same target event and observation horizon.

The work treats Wright–Fisher dynamics, fixation probabilities, origin–fixation theory, genotype findability, fitness landscapes, epistasis, and evolutionary accessibility as established foundations. Its contribution is an endpoint-specific comparison framework built around matched finite-horizon target probabilities, signed approximation error, explicit tolerance-defined adequacy, exact diagnostics, held-out time-scale validation, and controlled biological stress tests.

## Main quantities

For matched models \(M_0\) and \(M_1\), target set \(A\), and horizon \(T\),

\[
P_j(\theta)=\Pr_{M_j}(\tau_A\le T\mid X_0,\theta),\qquad j\in\{0,1\}.
\]

The primary signed discrepancy is

\[
E_{\log}(\theta)=\log_{10}\left(\frac{P_1(\theta)+\varepsilon}{P_0(\theta)+\varepsilon}\right).
\]

Thus \(E_{\log}>0\) means the origin–fixation approximation underestimates the finite-population reference, whereas \(E_{\log}<0\) means it overestimates it. The companion absolute discrepancy is \(E_{\rm abs}=|P_1-P_0|\).

For a declared tolerance \(\tau\), adequacy is endpoint- and horizon-specific:

\[
\mathcal{A}_{\tau}=\{\theta:|E_{\log}(\theta)|\le\tau\}.
\]

Stage 5 used the predeclared convention \(\tau=\log_{10}(2)=0.30103\), corresponding to a factor-two probability ratio. It is an analytical convention, not a universal biological threshold.

## Model hierarchy

- **M0-O:** sequential origin–fixation continuous-time Markov chain over monomorphic genotypes; successful substitutions are instantaneous in the reduced process.
- **M1:** explicit haploid Wright–Fisher finite population with selection, mutation, and multinomial sampling.
- **Exact K=1 reference:** mutant-count Wright–Fisher Markov chain, used to remove Monte Carlo error from the finite-time mechanism test.
- **K=2 stress extension:** matched two-locus fitness and mutation specifications supporting epistasis, mutation-process heterogeneity, alternative target sets, and paired perturbations.

The primary benchmark endpoint is fixation of the declared target by generation \(T\).

## Evidence chain

1. **Recovery benchmark:** six matched K=2 cells established the initial finite-horizon discrepancy pattern.
2. **Exact one-locus diagnostic:** all 18 exact cells showed contraction of signed error toward zero as the observation horizon increased. The calculation isolates the finite time consumed by segregation and selective sweep.
3. **Independent hold-out validation:** across 54 unseen cells, the sweep-time fraction \(\phi=t_{\rm sweep}/T\) strongly tracked absolute log-error (Spearman \(\rho=0.9226\), \(p=3.67\times10^{-23}\)); all 18 matched series contracted monotonically with increasing \(T\).
4. **Two-locus benchmark:** 32 cells showed that sweep time remains informative but is not sufficient once mutation supply and multistep dynamics enter. Signed discrepancies included both over- and under-estimation; extending the horizon reduced \(|E_{\log}|\) in 15 of 16 matched pairs.
5. **Predeclared biological stress test:** all 36 cells remained within the factor-two tolerance. The largest \(|E_{\log}|\) was 0.17996. Route multiplicity, epistasis, and mutation-process heterogeneity shifted signed error, and selected paired perturbations produced non-additive approximation-error responses.
6. **Long-term E. coli evidence:** at generation 50,000, mutator and nonmutator LTEE populations showed a 15.13-fold difference in median mutation burden, strong differences in mutation-spectrum entropy, and 14 independently listed Cit+ mutants across two source-declared structural-event classes (8 variant cit duplications and 6 IS3 insertions).

The LTEE analysis is independent empirical evidence that approximation-relevant heterogeneity and alternative routes occur in a real long-term evolutionary system. It is not used as causal proof of the simulated error patterns.

## Reproducibility

The implementation is written in Python and uses NumPy, SciPy, and Matplotlib. Unit and numerical-regression tests cover mutation matrices, absorbing target states, neutral fixation limits, zero-mutation controls, probability bounds, exact one-locus behavior, replicate reproducibility, and floating-point boundary tolerance.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[test]"
pytest -q
```

Run the principal computational stages:

```bash
python scripts/run_recovery.py
python scripts/run_timescale_diagnostic.py
python scripts/run_timescale_holdout.py
python scripts/run_k2_boundary.py

python scripts/run_stage5.py --baseline B1
python scripts/run_stage5.py --baseline B2
python scripts/run_stage5.py --baseline B3
python scripts/run_stage5.py --baseline B4
```

The successful sharded Stage-5 GitHub Actions run was **36424797701**. An earlier unsharded run **36403211328** reached the 180-minute infrastructure timeout after tests passed. Sharding changed execution only; the scientific grid, parameter values, deterministic seeds, endpoint, and replicate counts were unchanged.

## Repository structure

- `src/eab/` — model, exact-reference, metric, and stress-test implementations.
- `tests/` — unit and numerical-regression tests.
- `configs/` — frozen computational configuration.
- `theory/` — definitions, hypotheses, protocols, and claim-boundary records.
- `results/` — frozen machine-readable results and diagnostic summaries.
- `data/` — source inventories and provenance records for the empirical stage.
- `.github/workflows/` — automated tests and reproducible computational workflows.

## Empirical data

The empirical stage uses publicly archived LTEE data:

- Good et al. genomic data — Dryad DOI: **10.5061/dryad.6226d**
- Blount et al. citrate-innovation data — Dryad DOI: **10.5061/dryad.8q6n4**

Source archives should be obtained from their archival repositories rather than silently modified or redistributed.

## Citation

**Akhtar, M. A. K. (2026). _When Does Origin–Fixation Approximate Finite-Population Evolution?: A Finite-Horizon Target-Probability Benchmark with Exact Diagnostics, Stress Tests, and Long-Term Evolution Evidence_ (Version V1). Zenodo. https://doi.org/10.5281/zenodo.23019878**

DOI: https://doi.org/10.5281/zenodo.23019878

Citation metadata are also provided in `CITATION.cff`.

## Scope

This repository does not claim to introduce evolutionary accessibility, genotype findability, Wright–Fisher dynamics, Markov evolutionary dynamics, fixation probability, origin–fixation theory, epistasis, or route multiplicity. The study focuses on the model- and endpoint-specific magnitude and direction of finite-horizon target-probability approximation error.

## License

Licensed under the **Apache License 2.0**.

Copyright © 2026 Mohammad Amir Khusru Akhtar
