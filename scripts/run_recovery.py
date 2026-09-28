"""Run the predeclared recovery benchmark and write machine-readable output."""

from __future__ import annotations
import argparse, csv, math
from pathlib import Path
from eab.models import origin_fixation_probability, wright_fisher_probability
from eab.metrics import error_metrics


def wilson_interval(x: int, n: int, z: float = 1.959963984540054):
    if n <= 0:
        raise ValueError("n must be positive")
    phat = x / n
    den = 1 + z*z/n
    center = (phat + z*z/(2*n))/den
    half = z*math.sqrt(phat*(1-phat)/n + z*z/(4*n*n))/den
    return center-half, center+half


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="configs/recovery.csv")
    ap.add_argument("--output", default="results/recovery.csv")
    args = ap.parse_args()

    rows = []
    with open(args.config, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            k,N,T,R,seed = map(int, [r["k"],r["N"],r["T"],r["replicates"],r["seed"]])
            mu,s = float(r["mu"]),float(r["s"])
            p0 = origin_fixation_probability(k,N,mu,s,T)
            p1,hits = wright_fisher_probability(k,N,mu,s,T,R,seed)
            eps = 1/(2*R)
            m = error_metrics(p0,p1,eps)
            lo,hi = wilson_interval(hits,R)
            rows.append({**r, **m, "wf_hits":hits, "wf_ci_low":lo, "wf_ci_high":hi, "epsilon":eps})

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader(); w.writerows(rows)
    print(f"Wrote {len(rows)} rows to {out}")


if __name__ == "__main__":
    main()
