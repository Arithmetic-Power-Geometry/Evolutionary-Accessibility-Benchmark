"""Predeclared K=2 adequacy-boundary grid."""

from __future__ import annotations
import csv, math
from pathlib import Path
from eab.models import origin_fixation_probability, wright_fisher_probability
from eab.metrics import error_metrics

NS=(100,300)
SS=(0.005,0.02)
TS=(5000,20000)
LAMBDAS=(0.001,0.005,0.02,0.05)
R=2000
EPS=1/(2*R)

def wilson(hits,n,z=1.959963984540054):
    p=hits/n; d=1+z*z/n
    c=(p+z*z/(2*n))/d
    h=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/d
    return c-h,c+h

def main():
    rows=[]; idx=0
    for N in NS:
      for s in SS:
        sweep=2*math.log(N-1)/math.log1p(s)
        for T in TS:
          for lam in LAMBDAS:
            idx+=1; mu=lam/N; seed=21000+idx
            p0=origin_fixation_probability(k=2,N=N,mu=mu,s=s,T=T)
            p1,hits=wright_fisher_probability(k=2,N=N,mu=mu,s=s,T=T,replicates=R,seed=seed)
            m=error_metrics(p0,p1,EPS); lo,hi=wilson(hits,R)
            rows.append(dict(cell=idx,N=N,s=s,T=T,lambda_Nmu=lam,mu=mu,Ns=N*s,
                t_sweep=sweep,phi=sweep/T,replicates=R,seed=seed,p0=p0,p1=p1,
                e_log=m["e_log"],abs_e_log=abs(m["e_log"]),e_abs=m["e_abs"],
                hits=hits,wf_ci_low=lo,wf_ci_high=hi,
                p0_inside_wf_ci=(lo<=p0<=hi),epsilon=EPS))
    out=Path("results/k2_boundary.csv"); out.parent.mkdir(exist_ok=True)
    with out.open("w",newline="",encoding="utf-8") as f:
      w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    print(f"Wrote {len(rows)} K=2 cells to {out}")

if __name__=="__main__":
    main()
