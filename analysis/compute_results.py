#!/usr/bin/env python3
"""Recompute every statistic, table and figure input in the paper from the coding sheet.

Usage: python compute_results.py SHEET.csv OUTDIR [--codes adj|readj]

--codes readj (default) uses the re-adjudicated codes (READJ_* where the row was re-examined,
otherwise ADJ_* where filled, otherwise the first-pass code). --codes adj stops at the
adjudicated codes and reproduces the numbers of the analysis that preceded the re-examination.

Only the standard library and scipy.stats (Fisher's exact test, Spearman) are used.
"""
import csv, sys, os, math, itertools, collections, argparse
from scipy.stats import fisher_exact, spearmanr

ap = argparse.ArgumentParser()
ap.add_argument('sheet'); ap.add_argument('outdir'); ap.add_argument('--codes', default='readj', choices=['adj', 'readj'])
A = ap.parse_args()
os.makedirs(A.outdir, exist_ok=True)
rows = list(csv.DictReader(open(A.sheet, encoding='utf-8')))

PAIRS = [  # pair_id, label (table), short label (robustness table), regime, provider, later-version date
    ('ANT-1', 'Anthropic RSP 1.0\\textrightarrow2.0', 'Anthropic 1.0\\textrightarrow2.0', 'itemised', 'Anthropic', '2024-10-15'),
    ('ANT-2', 'Anthropic RSP 2.2\\textrightarrow3.0', 'Anthropic 2.2\\textrightarrow3.0', 'narrative', 'Anthropic', '2026-02-24'),
    ('OAI-1', 'OpenAI PF Beta\\textrightarrow2', 'OpenAI Beta\\textrightarrow2', 'itemised', 'OpenAI', '2025-04-15'),
    ('GDM-1', 'DeepMind FSF 2.0\\textrightarrow3.0', 'DeepMind 2.0\\textrightarrow3.0', 'narrative', 'Google DeepMind', '2025-09-22'),
    ('GDM-2', 'DeepMind FSF 3.0\\textrightarrow3.1', 'DeepMind 3.0\\textrightarrow3.1', 'itemised', 'Google DeepMind', '2026-04-17'),
    ('META-1', 'Meta 1.1\\textrightarrow2', 'Meta 1.1\\textrightarrow2', 'itemised', 'Meta', '2026-04-07'),
    ('MSFT-1', 'Microsoft v1\\textrightarrow2026', 'Microsoft v1\\textrightarrow2026', 'itemised', 'Microsoft', '2026-02-01'),
    ('NAV-1', 'Naver 2024\\textrightarrow2.0', 'Naver 2024\\textrightarrow2.0', 'narrative', 'Naver', '2026-07-07'),
    ('XAI-1', 'xAI draft Feb10\\textrightarrow Feb20', 'xAI Feb10\\textrightarrow Feb20', 'none', 'xAI', '2025-02-20'),
    ('XAI-2', 'xAI Feb\\textrightarrow Aug 2025', 'xAI Feb\\textrightarrow Aug 2025', 'none', 'xAI', '2025-08-20'),
    ('XAI-3', 'xAI Aug\\textrightarrow Dec 2025', 'xAI Aug\\textrightarrow Dec 2025', 'none', 'xAI', '2025-12-01'),
    ('XAI-4', 'xAI Dec 2025\\textrightarrow Jun 2026', 'xAI Dec 2025\\textrightarrow Jun 2026', 'none', 'xAI', '2026-06-01'),
]
PLAIN = {'ANT-1': 'Anthropic 1.0→2.0', 'ANT-2': 'Anthropic 2.2→3.0', 'OAI-1': 'OpenAI Beta→2', 'GDM-1': 'DeepMind 2.0→3.0',
         'GDM-2': 'DeepMind 3.0→3.1', 'META-1': 'Meta 1.1→2', 'MSFT-1': 'Microsoft v1→2026', 'NAV-1': 'Naver 2024→2.0',
         'XAI-1': 'xAI Feb10→Feb20', 'XAI-2': 'xAI Feb→Aug 2025', 'XAI-3': 'xAI Aug→Dec 2025', 'XAI-4': 'xAI Dec 2025→Jun 2026'}
# Provider-published account length in words and discrete items (counted by hand from the revision-account files).
ACCT = {'ANT-1': (4710, 11), 'ANT-2': (14274, 3), 'OAI-1': (1971, 12), 'GDM-1': (863, 3), 'GDM-2': (358, 6),
        'META-1': (1353, 7), 'MSFT-1': (291, 6), 'NAV-1': (2139, 3)}
CATS = [('EC1', 'Scope of evaluation'), ('EC2', 'Trigger and threshold'), ('EC3', 'Method'), ('EC4', 'Third-party involvement'),
        ('EC5', 'Disclosure'), ('EC6', 'Consequence of a result'), ('G', 'Governance'), ('S', 'Security'), ('M', 'Mitigation')]
ACCOUNTED = [p for p in PAIRS if p[3] != 'none']
regime = {p[0]: p[3] for p in PAIRS}; provider = {p[0]: p[4] for p in PAIRS}; vdate = {p[0]: p[5] for p in PAIRS}

def final(r, k):
    """Final code for variable k (material, outcome, announcement, flags)."""
    if A.codes == 'readj' and r.get('READJ_mode', '').startswith('re-examined'):
        return (r['READJ_' + k] or '').strip()
    v = (r.get('ADJ_' + k) or '').strip()
    if v: return v
    return (r.get(k) or '').strip()

for r in rows:
    r['_mat'] = final(r, 'material').lower() == 'yes'
    r['_out'] = final(r, 'outcome').upper()
    r['_ann'] = final(r, 'announcement').upper()
    r['_mix'] = 'MIX' in final(r, 'flags').upper()
    r['_acct'] = regime[r['pair_id']] != 'none'
    r['_added'] = r['v_i_text'].strip().upper() == 'NONE'
    r['_weak'] = r['_out'] in ('W', 'X', 'L')

def wilson(k, n, z=1.96):
    if n == 0: return (float('nan'), float('nan'))
    p = k / n; d = 1 + z * z / n; c = p + z * z / (2 * n); h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return ((c - h) / d, (c + h) / d)
def f2(x): return '--' if x != x else f'{x:.2f}'
def strict_sil(r): return r['_ann'] in ('SIL', 'ANN-P')
def lenient_sil(r): return r['_ann'] == 'SIL'

mat = [r for r in rows if r['_mat']]
acc = [r for r in mat if r['_acct']]
out = {}
L = []
def say(s=''): L.append(s); print(s)

say(f'# Results ({A.codes} codes), sheet {os.path.basename(A.sheet)}, rows {len(rows)}, material {len(mat)}')

# ---------------- Table 1 and per-pair figures ----------------
t1 = []; fig1 = []; fig2 = []; perpair = {}
for pid, lab, short, reg, prov, d in PAIRS:
    pr = [r for r in rows if r['pair_id'] == pid]; pm = [r for r in pr if r['_mat']]
    n_vi = sum(1 for r in pr if not r['_added'])
    c = collections.Counter(r['_out'] for r in pm); a = collections.Counter(r['_ann'] for r in pm)
    W = c['W'] + c['X'] + c['L']; S = c['S']; Ad = c['A']
    ann, annp, sil, ncl = a['ANN'], a['ANN-P'], a['SIL'], a['NCL']
    M = len(pm)
    if reg != 'none':
        ss, ls = (sil + annp) / M, sil / M
        srr_s, srr_l = f2(ss), f2(ls)
    else:
        ss = ls = float('nan'); srr_s = srr_l = '--'
    perpair[pid] = dict(M=M, ann=ann, annp=annp, sil=sil, ncl=ncl, ss=ss, ls=ls, W=c['W'], X=c['X'], Lr=c['L'], S=S, A=Ad, mix=sum(r['_mix'] for r in pm))
    t1.append(f'{lab} & {reg} & {n_vi} & {M} & {W} & {S} & {Ad} & {ann} & {annp} & {sil} & {srr_s} & {srr_l} \\\\')
    fig1.append([PLAIN[pid], reg, M, ss, ls, ann, annp, sil, ncl])
    fig2.append([PLAIN[pid], reg, c['W'], c['X'], c['L'], S, Ad, perpair[pid]['mix']])
open(f'{A.outdir}/table1_rows.tex', 'w').write('\n'.join(t1) + '\n\\bottomrule\n')
with open(f'{A.outdir}/fig1_srr_by_pair.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['pair', 'regime', 'n_material_with_account', 'srr_strict', 'srr_lenient', 'n_ann', 'n_annp', 'n_sil', 'n_ncl']); w.writerows(fig1)
with open(f'{A.outdir}/fig2_direction_by_pair.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['pair', 'regime', 'weakened', 'removed', 'relocated', 'strengthened', 'added', 'mix']); w.writerows(fig2)

# ---------------- Headline rates ----------------
n = len(acc); ks = sum(strict_sil(r) for r in acc); kl = sum(lenient_sil(r) for r in acc)
say(f'\n## RQ1 pooled (8 accounted pairs): strict {ks}/{n} = {ks/n:.3f} CI {wilson(ks,n)}; lenient {kl}/{n} = {kl/n:.3f} CI {wilson(kl,n)}')
ev = [r for r in acc if r['category'].startswith('EC')]; ne = [r for r in acc if not r['category'].startswith('EC')]
say(f'evidentiary: strict {sum(map(strict_sil,ev))}/{len(ev)} = {sum(map(strict_sil,ev))/len(ev):.3f}, lenient {sum(map(lenient_sil,ev))/len(ev):.3f}; non-evidentiary strict {sum(map(strict_sil,ne))/len(ne):.3f}, lenient {sum(map(lenient_sil,ne))/len(ne):.3f}')
say('per pair strict (min/max over accounted pairs): ' + ', '.join(f"{pid} {perpair[pid]['ss']:.2f}" for pid, *_ in ACCOUNTED))
say('per pair intervals strict: ' + '; '.join(f"{PLAIN[pid]} {perpair[pid]['ss']:.2f} ({wilson(perpair[pid]['sil']+perpair[pid]['annp'],perpair[pid]['M'])[0]:.2f}, {wilson(perpair[pid]['sil']+perpair[pid]['annp'],perpair[pid]['M'])[1]:.2f})" for pid, *_ in ACCOUNTED))
say('per pair intervals lenient: ' + '; '.join(f"{PLAIN[pid]} {perpair[pid]['ls']:.2f} ({wilson(perpair[pid]['sil'],perpair[pid]['M'])[0]:.2f}, {wilson(perpair[pid]['sil'],perpair[pid]['M'])[1]:.2f})" for pid, *_ in ACCOUNTED))
byprov = collections.defaultdict(list)
for r in acc: byprov[provider[r['pair_id']]].append(r)
say('provider aggregates strict: ' + ', '.join(f'{p} {sum(map(strict_sil,v))/len(v):.2f} ({sum(map(strict_sil,v))}/{len(v)})' for p, v in sorted(byprov.items(), key=lambda kv: sum(map(strict_sil, kv[1])) / len(kv[1]))))

# ---------------- Section granularity ----------------
units = collections.defaultdict(list)
for r in acc:
    key = (r['pair_id'], r['v_next_section'] if r['_added'] else r['v_i_section'])
    units[key].append(r)
U = len(units)
u_strict = sum(1 for v in units.values() if not any(r['_ann'] == 'ANN' for r in v))
u_len = sum(1 for v in units.values() if not any(r['_ann'] in ('ANN', 'ANN-P') for r in v))
u_maj = sum(1 for v in units.values() if sum(strict_sil(r) for r in v) > len(v) / 2)
say(f'\n## Section granularity: {U} units; strict {u_strict}/{U} = {u_strict/U:.2f} CI {wilson(u_strict,U)}; lenient {u_len}/{U} = {u_len/U:.2f} CI {wilson(u_len,U)}; majority rule {u_maj/U:.2f}')

# ---------------- RQ2 regime ----------------
narr = [r for r in acc if regime[r['pair_id']] == 'narrative']; item = [r for r in acc if regime[r['pair_id']] == 'itemised']
ns, nn = sum(map(strict_sil, narr)), len(narr); is_, ni = sum(map(strict_sil, item)), len(item)
orr, p = fisher_exact([[ns, nn - ns], [is_, ni - is_]])
say(f'\n## RQ2: narrative strict {ns}/{nn} = {ns/nn:.3f} CI {wilson(ns,nn)}; itemised {is_}/{ni} = {is_/ni:.3f} CI {wilson(is_,ni)}; Fisher OR {orr:.2f} p = {p:.3f}')
nl, il = sum(map(lenient_sil, narr)), sum(map(lenient_sil, item))
orl, pl = fisher_exact([[nl, nn - nl], [il, ni - il]])
say(f'lenient: narrative {nl}/{nn} = {nl/nn:.3f}, itemised {il}/{ni} = {il/ni:.3f}; OR {orl:.2f} p = {pl:.3f}')
pids = [p_[0] for p_ in ACCOUNTED]
def pooled_diff(narr_ids):
    a = [r for r in acc if r['pair_id'] in narr_ids]; b = [r for r in acc if r['pair_id'] not in narr_ids]
    return sum(map(strict_sil, a)) / len(a) - sum(map(strict_sil, b)) / len(b)
def mean_diff(narr_ids):
    a = [perpair[x]['ss'] for x in narr_ids]; b = [perpair[x]['ss'] for x in pids if x not in narr_ids]
    return sum(a) / len(a) - sum(b) / len(b)
obs_n = {x for x in pids if regime[x] == 'narrative'}
od, om = pooled_diff(obs_n), mean_diff(obs_n)
combos = list(itertools.combinations(pids, 3))
pp = sum(1 for c in combos if pooled_diff(set(c)) >= od - 1e-12) / len(combos)
pm = sum(1 for c in combos if mean_diff(set(c)) >= om - 1e-12) / len(combos)
say(f'permutation (56 assignments): observed pooled diff {od:.3f}, p = {pp:.3f}; per-pair mean diff {om:.3f}, p = {pm:.3f}')
# account length correlations
xs = [perpair[x]['ss'] for x in pids]
words = [ACCT[x][0] for x in pids]; items = [ACCT[x][1] for x in pids]
wpc = [ACCT[x][0] / perpair[x]['M'] for x in pids]; ipc = [ACCT[x][1] / perpair[x]['M'] for x in pids]
say(f'Spearman strict rate vs words {spearmanr(xs,words)[0]:.2f}, items {spearmanr(xs,items)[0]:.2f}, words/change {spearmanr(xs,wpc)[0]:.2f}, items/change {spearmanr(xs,ipc)[0]:.2f}')

# ---------------- RQ3 direction ----------------
traced = [r for r in mat if not r['_added']]
wk = sum(r['_weak'] for r in traced)
say(f'\n## RQ3: weakening share {wk}/{len(traced)} = {wk/len(traced):.3f} CI {wilson(wk,len(traced))}')
tnm = [r for r in traced if not r['_mix']]; say(f'excluding MIX ({sum(r["_mix"] for r in traced)}): {sum(r["_weak"] for r in tnm)}/{len(tnm)} = {sum(r["_weak"] for r in tnm)/len(tnm):.3f} CI {wilson(sum(r["_weak"] for r in tnm),len(tnm))}')
tnl = [r for r in traced if r['_out'] != 'L']; say(f'excluding L: {sum(r["_weak"] for r in tnl)}/{len(tnl)} = {sum(r["_weak"] for r in tnl)/len(tnl):.3f}')
c = collections.Counter(r['_out'] for r in mat); say(f'outcomes among material: {dict(c)}; additions {c["A"]}')
addp = collections.Counter(r['pair_id'] for r in mat if r['_added']); say(f'additions by pair: {dict(addp)}')
wmaj = 0; pairshare = {}
for pid, *_ in PAIRS:
    t = [r for r in traced if r['pair_id'] == pid]
    sh = sum(r['_weak'] for r in t) / len(t) if t else float('nan'); pairshare[pid] = (sum(r['_weak'] for r in t), len(t), sh)
    if t and sh > 0.5: wmaj += 1
say(f'pairs with weakening majority: {wmaj} of {len(PAIRS)}; per pair: ' + ', '.join(f'{pid} {pairshare[pid][2]:.2f}' for pid, *_ in PAIRS))
loo = []
for pv in ['Anthropic', 'Google DeepMind', 'Meta', 'Microsoft', 'Naver', 'OpenAI', 'xAI']:
    t = [r for r in traced if provider[r['pair_id']] != pv]; loo.append((pv, sum(r['_weak'] for r in t), len(t)))
say('leave-one-provider-out: ' + ', '.join(f'{pv} {k}/{n_} = {k/n_:.2f}' for pv, k, n_ in loo))
open(f'{A.outdir}/appendixM2_loo.tex', 'w').write('\\begin{tabular}{lrrr}\\toprule Provider dropped & Weakening & Traced & Share \\\\ \\midrule\n' + '\n'.join(f'{pv} & {k} & {n_} & {k/n_:.2f} \\\\' for pv, k, n_ in loo) + '\n\\bottomrule\\end{tabular}\n')
# silence by direction (accounted pairs)
aw = [r for r in acc if r['_weak']]; as_ = [r for r in acc if r['_out'] == 'S']; aa = [r for r in acc if r['_out'] == 'A']
kw, ks_ = sum(map(strict_sil, aw)), sum(map(strict_sil, as_))
ord_, pd_ = fisher_exact([[kw, len(aw) - kw], [ks_, len(as_) - ks_]])
say(f'strict silence: weakenings {kw}/{len(aw)} = {kw/len(aw):.3f}, strengthenings {ks_}/{len(as_)} = {ks_/len(as_):.3f}, OR {ord_:.2f} p = {pd_:.3f}; additions {sum(map(strict_sil,aa))}/{len(aa)} = {sum(map(strict_sil,aa))/len(aa):.3f}')
byout = {o: (sum(strict_sil(r) for r in acc if r['_out'] == o), sum(1 for r in acc if r['_out'] == o)) for o in 'WXLSA'}
say('by outcome strict silence: ' + ', '.join(f'{o} {k}/{n_}' for o, (k, n_) in byout.items()))
lw, ls_ = sum(map(lenient_sil, aw)), sum(map(lenient_sil, as_)); orl2, pl2 = fisher_exact([[lw, len(aw) - lw], [ls_, len(as_) - ls_]])
say(f'lenient silence: weakenings {lw}/{len(aw)} = {lw/len(aw):.3f}, strengthenings {ls_}/{len(as_)} = {ls_/len(as_):.3f}, OR {orl2:.2f} p = {pl2:.3f}')
# within-pair asymmetry
asym = []
for pid, *_ in ACCOUNTED:
    w_ = [r for r in acc if r['pair_id'] == pid and r['_weak']]; s_ = [r for r in acc if r['pair_id'] == pid and r['_out'] == 'S']
    rw = sum(map(strict_sil, w_)) / len(w_) if w_ else float('nan'); rs = sum(map(strict_sil, s_)) / len(s_) if s_ else float('nan')
    asym.append((pid, rw, rs, len(w_), len(s_)))
say('within-pair strict silence W vs S: ' + '; '.join(f'{pid} {rw:.2f} vs {rs:.2f} ({nw}/{ns_})' for pid, rw, rs, nw, ns_ in asym))
say(f'pairs with weakenings more often silent: {sum(1 for _, rw, rs, nw, ns_ in asym if nw and ns_ and rw > rs)} of {sum(1 for _, rw, rs, nw, ns_ in asym if nw and ns_)}; margins ' + ', '.join(f'{pid} {rw-rs:+.2f}' for pid, rw, rs, nw, ns_ in asym if nw and ns_))
# robustness table M1
m1 = ['\\begin{tabular}{llrrrrrrrr}\\toprule Pair & Regime & Words & Items & Mat.\\ (acct) & ANN & $\\srr_s$ & Traced & Weak.\\ share & Silent W / S \\\\ \\midrule']
for pid, lab, short, reg, prov, d in PAIRS:
    pp_ = perpair[pid]; k, n_, sh = pairshare[pid]
    if reg != 'none':
        a_ = [x for x in asym if x[0] == pid][0]
        m1.append(f"{short} & {reg} & {ACCT[pid][0]} & {ACCT[pid][1]} & {pp_['M']} & {pp_['ann']} & {pp_['ss']:.2f} & {n_} & {sh:.2f} & {f2(a_[1])} / {f2(a_[2])} ({a_[3]}/{a_[4]}) \\\\")
    else:
        m1.append(f'{short} & {reg} & -- & -- & -- & -- & -- & {n_} & {sh:.2f} & -- \\\\')
m1.append('\\bottomrule\\end{tabular}')
open(f'{A.outdir}/appendixM1_pairs.tex', 'w').write('\n'.join(m1) + '\n')

# ---------------- Pre/post TFAIA ----------------
before = [r for r in acc if vdate[r['pair_id']] < '2026-01-01']; after = [r for r in acc if vdate[r['pair_id']] >= '2026-01-01']
say(f'\n## TFAIA split (accounted): before strict {sum(map(strict_sil,before))}/{len(before)} = {sum(map(strict_sil,before))/len(before):.2f}, lenient {sum(map(lenient_sil,before))/len(before):.2f}; after strict {sum(map(strict_sil,after))}/{len(after)} = {sum(map(strict_sil,after))/len(after):.2f}, lenient {sum(map(lenient_sil,after))/len(after):.2f}')
tb = [r for r in traced if vdate[r['pair_id']] < '2026-01-01']; ta = [r for r in traced if vdate[r['pair_id']] >= '2026-01-01']
say(f'weakening share all pairs: before {sum(r["_weak"] for r in tb)}/{len(tb)} = {sum(r["_weak"] for r in tb)/len(tb):.2f}, after {sum(r["_weak"] for r in ta)}/{len(ta)} = {sum(r["_weak"] for r in ta)/len(ta):.2f}')

# ---------------- Categories ----------------
t2 = []; fig3 = []; cis = []
for code, name in CATS:
    allm = [r for r in mat if r['category'] == code]; am = [r for r in acc if r['category'] == code]
    ks3, kl3, n3 = sum(map(strict_sil, am)), sum(map(lenient_sil, am)), len(am)
    t2.append(f'{code} & {name} & {len(allm)} & {n3} & {ks3/n3:.2f} & {kl3/n3:.2f} \\\\' + ('\n\\midrule' if code == 'EC6' else ''))
    fig3.append([code, n3, round(ks3 / n3, 3), round(kl3 / n3, 3)]); lo, hi = wilson(ks3, n3); cis.append(f'{code} ({lo:.2f}, {hi:.2f})')
open(f'{A.outdir}/table2_category.tex', 'w').write('\n'.join(t2) + '\n\\bottomrule\n')
with open(f'{A.outdir}/fig3_srr_by_category.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['category', 'n', 'srr_strict', 'srr_lenient']); w.writerows(fig3)
say('\n## categories strict intervals: ' + ', '.join(cis))
e4 = [r for r in mat if r['category'] == 'EC4']; e4a = [r for r in e4 if r['_acct']]; e2 = [r for r in mat if r['category'] == 'EC2']
say(f'EC2 material {len(e2)}; EC4 material {len(e4)}, with account {len(e4a)}, strict silent {sum(map(strict_sil,e4a))}/{len(e4a)}')

# ---------------- Adjudication statistics ----------------
fp_out = collections.Counter(); fp_ann = collections.Counter(); n_adj = sum(1 for r in rows if r.get('ADJ_mode') == 'adjudicated')
for r in rows:
    if r.get('ADJ_outcome') and r['ADJ_outcome'] != r['outcome']: fp_out[(r['outcome'], r['ADJ_outcome'])] += 1
    if r.get('ADJ_announcement') and r['ADJ_announcement'] != r['announcement']: fp_ann[(r['announcement'], r['ADJ_announcement'])] += 1
conf = collections.Counter(r['confidence'] for r in rows)
lines = ['\\begin{tabular}{lr}\\toprule Quantity & Value \\\\ \\midrule', f'Rows in first pass & {len(rows)} \\\\', f'Rows adjudicated individually & {n_adj} \\\\',
         f'Rows accepted after spot-check & {len(rows)-n_adj} \\\\', 'Spot-check sample (accepted rows) & 45 \\\\', 'Spot-check changes & 1 \\\\',
         f"First-pass confidence high / medium / low & {conf['high']} / {conf['medium']} / {conf['low']} \\\\",
         f'Outcome codes changed by adjudication & {sum(fp_out.values())} \\\\', f'Announcement codes changed by adjudication & {sum(fp_ann.values())} \\\\',
         f"\\quad of which SIL \\textrightarrow\\ ANN-P & {fp_ann[('SIL','ANN-P')]} \\\\", f"\\quad of which ANN \\textrightarrow\\ ANN-P & {fp_ann[('ANN','ANN-P')]} \\\\"]
if A.codes == 'readj':
    re_ = [r for r in rows if r.get('READJ_mode', '').startswith('re-examined')]
    def adjv(r, k): return ((r.get('ADJ_' + k) or '') or r[k]).strip().upper()
    cm = sum(1 for r in re_ if r['READJ_material'].upper() != adjv(r, 'material')); co = sum(1 for r in re_ if r['READJ_outcome'].upper() != adjv(r, 'outcome'))
    ca = collections.Counter((adjv(r, 'announcement'), r['READJ_announcement'].upper()) for r in re_ if r['READJ_announcement'].upper() != adjv(r, 'announcement'))
    say(f'\n## Re-adjudication: {len(re_)} rows re-examined; materiality changed {cm}; outcome changed {co}; announcement changed {sum(ca.values())}: {dict(ca)}')
    lines += ['\\midrule', f'Rows re-examined after the independent re-runs & {len(re_)} \\\\', f'\\quad materiality codes changed & {cm} \\\\', f'\\quad outcome codes changed & {co} \\\\',
              f'\\quad announcement codes changed & {sum(ca.values())} \\\\', f"\\quad\\quad SIL \\textrightarrow\\ ANN-P & {ca[('SIL','ANN-P')]} \\\\", f"\\quad\\quad ANN-P \\textrightarrow\\ ANN & {ca[('ANN-P','ANN')]} \\\\",
              f"\\quad\\quad SIL \\textrightarrow\\ ANN & {ca[('SIL','ANN')]} \\\\", f"\\quad\\quad ANN \\textrightarrow\\ ANN-P & {ca[('ANN','ANN-P')]} \\\\", f"\\quad\\quad ANN-P \\textrightarrow\\ SIL & {ca[('ANN-P','SIL')]} \\\\"]
lines.append('\\bottomrule\\end{tabular}')
open(f'{A.outdir}/adjudication_stats.tex', 'w').write('\n'.join(lines) + '\n')
say(f'first pass -> adjudication: outcome {dict(fp_out)}, announcement {dict(fp_ann)}')
open(f'{A.outdir}/results.md', 'w').write('\n'.join(L) + '\n')
