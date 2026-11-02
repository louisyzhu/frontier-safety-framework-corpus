#!/usr/bin/env python3
"""Krippendorff's alpha (nominal) for the second coding, the blind re-coding and the re-runs.

Usage:
  python compute_agreement.py second  RETURNED.csv [KEY.csv] [SHEET.csv]
      agreement between a returned second-coder sheet and the final codes on the 50-unit sample
  python compute_agreement.py pair    RETURNED_A.csv RETURNED_B.csv
      agreement between two returned second-coder sheets
  python compute_agreement.py blind   [SHEET.csv]
      agreement between the blind re-coding (BLIND_* columns) and the re-examined codes before
      the review, on the 249 re-examined rows; the pre-review codes are recovered from the
      REVIEW_notes column, which records every change the review made
  python compute_agreement.py reruns  [SHEET.csv]
      agreement between each re-run (RERUN{1,2,3}_* columns) and the final codes

Defaults: KEY.csv = coding/second_coder_returns/SECOND_CODER_SAMPLE_KEY.csv,
SHEET.csv = coding/tracing_FINAL_v3.csv, both relative to the repository root.
The final code of each variable is the re-examined code where READJ_mode begins with
"re-examined", otherwise the adjudicated code where filled, otherwise the first-pass code.
Announcement status is compared on all rows and on the three-way rows (final code ANN,
ANN-P or SIL); the second figure is the one the paper weighs."""
import csv, sys, os, random, re
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEF_KEY = os.path.join(ROOT, 'coding', 'second_coder_returns', 'SECOND_CODER_SAMPLE_KEY.csv')
DEF_SHEET = os.path.join(ROOT, 'coding', 'tracing_FINAL_v3.csv')
THREE = ('ANN', 'ANN-P', 'SIL')


def alpha_nominal(pairs):
    vals = [v for p in pairs for v in p]; n = len(vals)
    if n < 2: return float('nan')
    Do = sum(1 for a, b in pairs if a != b) * 2 / (len(pairs) * 2)
    c = Counter(vals); De = sum(c[x] * c[y] for x in c for y in c if x != y) / (n * (n - 1))
    return 1 - Do / De if De > 0 else float('nan')


def bootstrap(pairs, B=2000, seed=1):
    random.seed(seed); est = []
    for _ in range(B):
        s = [random.choice(pairs) for _ in pairs]; est.append(alpha_nominal(s))
    est = [e for e in est if e == e]; est.sort()
    return est[int(0.025 * len(est))], est[int(0.975 * len(est))]


def norm(v): return (v or '').strip().upper()


def final(r, k):
    if (r.get('READJ_mode') or '').startswith('re-examined'): return norm(r['READJ_' + k])
    return norm(r.get('ADJ_' + k)) or norm(r.get(k))


def report(name, pairs):
    if not pairs: print(f'{name}: no units'); return
    al = alpha_nominal(pairs); lo, hi = bootstrap(pairs)
    print(f'{name}: n={len(pairs)}  alpha={al:.3f}  95% CI [{lo:.3f}, {hi:.3f}]  raw agreement={sum(a == b for a, b in pairs) / len(pairs):.2f}')


def load_sheet(path): return {r['commitment_id']: r for r in csv.DictReader(open(path, encoding='utf-8'))}


def mode_second(returned, key_path, sheet_path):
    key = {r['unit_id']: r['commitment_id'] for r in csv.DictReader(open(key_path, encoding='utf-8'))}
    fin = load_sheet(sheet_path); E = list(csv.DictReader(open(returned, encoding='utf-8')))
    for name, k, ek, filt in [('materiality', 'material', 'E_material', lambda a: True),
                              ('outcome', 'outcome', 'E_outcome', lambda a: True),
                              ('announcement, all rows', 'announcement', 'E_announcement', lambda a: True),
                              ('announcement, three-way rows', 'announcement', 'E_announcement', lambda a: a in THREE)]:
        pairs = []
        for e in E:
            r = fin[key[e['unit_id']]]; a = final(r, k); b = norm(e[ek])
            if k == 'announcement' and a == 'NA': b = b or 'NA'
            if a and b and filt(a): pairs.append((a, b))
        report(name, pairs)


def mode_pair(a_path, b_path):
    A = list(csv.DictReader(open(a_path, encoding='utf-8'))); B = list(csv.DictReader(open(b_path, encoding='utf-8')))
    assert [x['unit_id'] for x in A] == [x['unit_id'] for x in B]
    for name, ek, filt in [('materiality', 'E_material', lambda a, b: True), ('outcome', 'E_outcome', lambda a, b: True),
                           ('announcement, three-way rows', 'E_announcement', lambda a, b: a in THREE and b in THREE)]:
        pairs = [(norm(x[ek]), norm(y[ek])) for x, y in zip(A, B)]
        pairs = [(a, b) for a, b in pairs if a and b and filt(a, b)]
        report(name, pairs)


def pre_review(r, k):
    """Code before the review, recovered from the REVIEW_notes 'Changed m/o/f/a to m/o/f/a.' record."""
    m = re.match(r'Changed (\S+)/(\S+)/(\S+)/(\S+) to ', r.get('REVIEW_notes') or '')
    if not m: return final(r, k)
    return norm({'material': m.group(1), 'outcome': m.group(2), 'flags': m.group(3), 'announcement': m.group(4)}[k])


def mode_blind(sheet_path):
    fin = load_sheet(sheet_path)
    rows = [r for r in fin.values() if (r.get('READJ_mode') or '').startswith('re-examined')]
    for label, ref in [('against the re-examined codes before the review', pre_review), ('against the final codes', final)]:
        print('==', label)
        for name, k, bk, filt in [('materiality', 'material', 'BLIND_material', lambda a: True),
                                  ('outcome', 'outcome', 'BLIND_outcome', lambda a: True),
                                  ('announcement, three-way rows', 'announcement', 'BLIND_announcement', lambda a: a in THREE)]:
            pairs = [(ref(r, k), norm(r[bk])) for r in rows]
            pairs = [(a, b) for a, b in pairs if a and b and filt(a)]
            report(name, pairs)


def mode_reruns(sheet_path):
    fin = load_sheet(sheet_path); rows = list(fin.values())
    for i in (1, 2, 3):
        print('== re-run', i, 'against the final codes')
        for name, k, filt in [('materiality', 'material', lambda a: True), ('outcome', 'outcome', lambda a: True),
                              ('announcement, all rows', 'announcement', lambda a: True),
                              ('announcement, three-way rows', 'announcement', lambda a: a in THREE)]:
            pairs = [(final(r, k), norm(r[f'RERUN{i}_{k}'])) for r in rows]
            pairs = [(a, b) for a, b in pairs if a and b and filt(a)]
            report(name, pairs)
    for i, j in [(1, 2), (1, 3), (2, 3)]:
        pairs = [(norm(r[f'RERUN{i}_announcement']), norm(r[f'RERUN{j}_announcement'])) for r in rows]
        report(f'announcement, run {i} against run {j}, all rows', [(a, b) for a, b in pairs if a and b])
        report(f'announcement, run {i} against run {j}, three-way rows', [(a, b) for a, b in pairs if a in THREE and b in THREE])


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'second'
    if mode == 'second': mode_second(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else DEF_KEY, sys.argv[4] if len(sys.argv) > 4 else DEF_SHEET)
    elif mode == 'pair': mode_pair(sys.argv[2], sys.argv[3])
    elif mode == 'blind': mode_blind(sys.argv[2] if len(sys.argv) > 2 else DEF_SHEET)
    elif mode == 'reruns': mode_reruns(sys.argv[2] if len(sys.argv) > 2 else DEF_SHEET)
    else: print(__doc__)
