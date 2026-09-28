"""Run the predeclared Stage-5 experiment, shardable by frozen baseline."""
from __future__ import annotations
import argparse,csv,math
from pathlib import Path
from eab.stress import origin_fixation_target_probability, wright_fisher_target_probability
from eab.metrics import error_metrics

BASE=[
 ("B1",100,.005,5000,.005),("B2",100,.02,5000,.005),
 ("B3",300,.005,20000,.005),("B4",300,.02,20000,.001)]
COND=[
 ("baseline",(3,),0.,1.),("epi_pos",(3,),.02,1.),("epi_neg",(3,),-.02,1.),
 ("mut_hi",(3,),0.,5.),("mut_lo",(3,),0.,.2),("route_multi",(1,2),0.,1.),
 ("route_epi_pos",(1,2),.02,1.),("route_mut_hi",(1,2),0.,5.),
 ("epi_pos_mut_hi",(3,),.02,5.)]
R=5000; TAU=math.log10(2); EPS=1/(2*R)

def wilson(h,n,z=1.959963984540054):
 p=h/n; d=1+z*z/n; c=(p+z*z/(2*n))/d
 q=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/d
 return c-q,c+q

def main(selected=None):
 bases=[x for x in BASE if selected is None or x[0]==selected]
 if not bases: raise ValueError("unknown baseline")
 od=Path("results/stage5_outcomes"); od.mkdir(parents=True,exist_ok=True)
 rows=[]
 for b,N,s,T,lam in bases:
  bi=[x[0] for x in BASE].index(b); mu=lam/N
  for ci,(name,targets,eta,h) in enumerate(COND):
   cell=bi*len(COND)+ci+1; seed=51000+cell
   p0=origin_fixation_target_probability(N,mu,s,T,targets,eta,h)
   p1,y=wright_fisher_target_probability(N,mu,s,T,R,seed,targets,eta,h,True)
   met=error_metrics(p0,p1,EPS); lo,hi=wilson(int(y.sum()),R)
   (od/f"{b}_{name}.txt").write_text("".join(f"{int(v)}\n" for v in y))
   rows.append(dict(cell=cell,baseline=b,condition=name,N=N,s=s,T=T,lambda_Nmu=lam,
    mu=mu,targets=";".join(map(str,targets)),eta=eta,h=h,replicates=R,seed=seed,
    p0=met["p0"],p1=met["p1"],e_log=met["e_log"],abs_e_log=abs(met["e_log"]),
    e_abs=met["e_abs"],hits=int(y.sum()),wf_ci_low=lo,wf_ci_high=hi,tau=TAU,
    adequate_factor2=abs(met["e_log"])<=TAU,epsilon=EPS))
 suffix=f"_{selected}" if selected else ""
 out=Path(f"results/stage5_primary{suffix}.csv")
 with out.open("w",newline="") as f:
  w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)

if __name__=="__main__":
 ap=argparse.ArgumentParser(); ap.add_argument("--baseline",choices=[x[0] for x in BASE])
 a=ap.parse_args(); main(a.baseline)
