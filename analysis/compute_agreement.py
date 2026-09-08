#!/usr/bin/env python3
"""Krippendorff's alpha (nominal) between adjudicated coder-1 codes and the second coder, on the 50-unit sample.
Usage: python compute_agreement.py SECOND_CODER_SAMPLE_returned.csv
Needs tracing_FINAL.csv and SECOND_CODER_SAMPLE_KEY.csv in the same folder."""
import csv, sys, random
from collections import Counter
def alpha_nominal(pairs):
    # pairs: list of (a,b) with both non-missing
    vals=[v for p in pairs for v in p]; n=len(vals)
    if n<2: return float('nan')
    # observed disagreement
    Do=sum(1 for a,b in pairs if a!=b)*2  # each unit contributes 2 ordered pairs
    Do/= (len(pairs)*2)
    c=Counter(vals); De=sum(c[x]*c[y] for x in c for y in c if x!=y)/(n*(n-1))
    return 1-Do/De if De>0 else float('nan')
def bootstrap(pairs,B=2000,seed=1):
    random.seed(seed); est=[]
    for _ in range(B):
        s=[random.choice(pairs) for _ in pairs]; est.append(alpha_nominal(s))
    est=[e for e in est if e==e]; est.sort()
    return est[int(0.025*len(est))],est[int(0.975*len(est))]
key={r['unit_id']:r['commitment_id'] for r in csv.DictReader(open('SECOND_CODER_SAMPLE_KEY.csv'))}
fin={r['commitment_id']:r for r in csv.DictReader(open('tracing_FINAL.csv',encoding='utf-8'))}
E=list(csv.DictReader(open(sys.argv[1],encoding='utf-8')))
def norm(v): return (v or '').strip().upper()
for name,c1,c2,filt in [('materiality (yes/no)','ADJ_material','E_material',lambda r:True),
                        ('outcome (R/S/W/X/L/A)','ADJ_outcome','E_outcome',lambda r:True),
                        ('announcement (ANN/ANN-P/SIL)','ADJ_announcement','E_announcement',lambda r:r['ADJ_announcement'] in ('ANN','ANN-P','SIL'))]:
    pairs=[]
    for e in E:
        r=fin[key[e['unit_id']]]
        if not filt(r): continue
        a,b=norm(r[c1]),norm(e[c2])
        if a and b and a!='NA': pairs.append((a,b))
    al=alpha_nominal(pairs); lo,hi=bootstrap(pairs)
    print(f"{name}: n={len(pairs)}  alpha={al:.3f}  95% CI [{lo:.3f}, {hi:.3f}]  raw agreement={sum(a==b for a,b in pairs)/len(pairs):.2f}")
