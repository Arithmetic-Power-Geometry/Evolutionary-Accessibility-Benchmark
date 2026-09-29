# K=2 adequacy-boundary experiment — predeclared protocol

## Purpose
Move from the exact K=1 mechanism result to the smallest genuinely multi-step target problem. The experiment asks whether finite-horizon sweep-time error remains sufficient, or whether mutation supply and overlapping/segregating lineages create additional approximation discrepancy.

## Models
M0-O: sequential origin-fixation CTMC.
M1: explicit haploid Wright-Fisher population process.
Both use the same two-locus binary genotype space, forward mutation, no recombination, multiplicative fitness w(g)=(1+s)^k(g), wild-type initial state, and fixation of genotype 11 by T as the endpoint.

## Factors
N in {100, 300}
s in {0.005, 0.02}
T in {5000, 20000}
lambda = N*mu in {0.001, 0.005, 0.02, 0.05}

Thus mu=lambda/N. Total: 32 parameter cells.

This grid deliberately crosses mutation supply and horizon rather than holding mu*T fixed.

## Replication
2,000 Wright-Fisher replicates per cell, fixed deterministic seed derived from the cell index.
Wilson 95% intervals are reported for P1.

## Quantities
For every cell report P0, P1, E_log, E_abs, Wilson interval, N*mu, N*s, phi=t_sweep/T, and the number of target-fixation hits.

The same logistic benchmark used in the K=1 hold-out is retained:
t_sweep = 2*log(N-1)/log(1+s).

## Predeclared questions
1. Does |E_log| decrease with smaller phi at fixed N,s,lambda?
2. At comparable phi, does increasing lambda=N*mu introduce residual error beyond the K=1 sweep-time pattern?
3. Does the sign remain predominantly negative, or do multi-step finite-population dynamics generate both under- and over-estimation?
4. Are there cells in which the M0-O estimate lies inside the M1 Wilson interval (recovery cells)?
5. Is phi alone insufficient once mutation supply becomes appreciable?

## Analysis discipline
All 32 cells are retained. No adequacy threshold is selected after viewing the data. No universal scaling claim is made from this grid. If computation is expensive, implementation is optimized or cells are sharded; the scientific grid is not silently reduced.

## External data
None required.


## Outcome note

The completed 32-cell benchmark found both discrepancy signs (20 negative, 11 positive, one numerically zero), `Spearman(phi,|E_log|)=0.5761` (`p=5.60e-4`), and 15/16 matched horizon extensions reduced `|E_log|`. The pooled `N*mu` association is not interpreted causally because high-supply cells often saturate near probability one.
