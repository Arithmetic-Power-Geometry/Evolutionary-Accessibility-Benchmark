"""Generate and evaluate the predeclared exact hold-out time-scale grid."""

from __future__ import annotations
import csv, math
from pathlib import Path
import numpy as np
from scipy.stats import spearmanr
from eab.models import fixation_probability_diffusion, origin_fixation_probability
from eab.exact import exact_wf_one_locus_fixation_probability
from eab.metrics import error_metrics

NS=(75,150,300)
SS=(0.005,0.02)
TS=(1000,5000,20000)
QS=(0.25,0.50,0.75)
EPS=1e-12

def corr(rows,key,q=None):
    z=[r for r in rows if q is None or r["target_q"]==q]
    res=spearmanr([r[key] for r in z],[r["abs_e_log"] for r in z])
    return float(res.statistic), float(res.pvalue), len(z)

def main():
    rows=[]
    for N in NS:
      for s in SS:
        pfix=fixation_probability_diffusion(1+s,N)
        sweep=2*math.log(N-1)/math.log1p(s)
        for q in QS:
          for T in TS:
            mu=-math.log(1-q)/(N*pfix*T)
            p0=origin_fixation_probability(k=1,N=N,mu=mu,s=s,T=T)
            p1=exact_wf_one_locus_fixation_probability(N=N,mu=mu,s=s,T=T)
            m=error_metrics(p0,p1,EPS)
            wait=1/(N*mu*pfix)
            rows.append(dict(N=N,s=s,T=T,target_q=q,mu=mu,N_mu=N*mu,
                pfix_diffusion=pfix,t_wait=wait,t_sweep=sweep,rho=wait/sweep,
                phi=sweep/T,p0=p0,p1=p1,e_log=m["e_log"],
                abs_e_log=abs(m["e_log"]),e_abs=m["e_abs"]))
    out=Path("results/timescale_holdout.csv"); out.parent.mkdir(exist_ok=True)
    with out.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)

    summary=[]
    for key in ("phi","rho"):
        stat,p,n=corr(rows,key)
        summary.append(dict(predictor=key,stratum="all",spearman=stat,p_value=p,n=n))
        for q in QS:
            stat,p,n=corr(rows,key,q)
            summary.append(dict(predictor=key,stratum=f"q={q}",spearman=stat,p_value=p,n=n))
    # Within-series contraction: T increases should not increase |E_log|.
    groups={}
    for r in rows: groups.setdefault((r["N"],r["s"],r["target_q"]),[]).append(r)
    monotone=0
    for z in groups.values():
        z=sorted(z,key=lambda x:x["T"])
        if all(z[i+1]["abs_e_log"] <= z[i]["abs_e_log"]+1e-12 for i in range(len(z)-1)):
            monotone+=1
    sout=Path("results/timescale_holdout_summary.csv")
    with sout.open("w",newline="",encoding="utf-8") as f:
        fields=["predictor","stratum","spearman","p_value","n"]
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(summary)
        w.writerow(dict(predictor="monotone_T_series",stratum="all",
                        spearman=monotone,p_value="",n=len(groups)))
    print(f"Wrote {len(rows)} hold-out cells; monotone series {monotone}/{len(groups)}")

if __name__=="__main__":
    main()
