"""Exact one-locus time-scale diagnostic, predeclared before execution."""

from __future__ import annotations
import csv, math
from pathlib import Path
from eab.models import fixation_probability_diffusion, origin_fixation_probability
from eab.exact import exact_wf_one_locus_fixation_probability
from eab.metrics import error_metrics

TARGET_P0 = 0.5
EPSILON = 1e-12
NS = (100, 200, 500)
TS = (500, 1000, 2000, 5000, 10000, 20000)
S = 0.01


def main():
    rows = []
    for N in NS:
        pfix = fixation_probability_diffusion(1.0 + S, N)
        for T in TS:
            # Choose mu so M0-O has the same target probability in every cell:
            # 1-exp(-N*mu*pfix*T)=TARGET_P0.
            mu = -math.log(1.0 - TARGET_P0) / (N * pfix * T)
            p0 = origin_fixation_probability(k=1, N=N, mu=mu, s=S, T=T)
            p1 = exact_wf_one_locus_fixation_probability(N=N, mu=mu, s=S, T=T)
            m = error_metrics(p0, p1, EPSILON)
            rows.append({
                "N": N, "s": S, "T": T, "mu": mu, "N_mu": N*mu,
                "pfix_diffusion": pfix, "p0_origin_fixation": p0,
                "p1_exact_wf": p1, "e_log": m["e_log"], "e_abs": m["e_abs"],
                "target_p0": TARGET_P0, "epsilon": EPSILON,
            })
    out = Path("results/timescale_diagnostic.csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader(); w.writerows(rows)
    print(f"Wrote {len(rows)} exact diagnostic cells to {out}")


if __name__ == "__main__":
    main()
