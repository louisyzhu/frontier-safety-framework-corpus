#!/usr/bin/env python3
"""Write the verbatim-text appendix for a list of commitment identifiers.
Usage: python make_examples.py SHEET.csv OUT.tex ID [ID ...]
Each entry quotes both versions, the account pointer and every adjudication note from the sheet."""
import csv, sys, re

sheet, out, ids = sys.argv[1], sys.argv[2], sys.argv[3:]
rows = {r['commitment_id']: r for r in csv.DictReader(open(sheet, encoding='utf-8'))}
LAB = {'ANT-1': 'Anthropic v1.0 \\textrightarrow\\ v2.0', 'ANT-2': 'Anthropic v2.2 \\textrightarrow\\ v3.0', 'OAI-1': 'OpenAI beta \\textrightarrow\\ v2',
       'GDM-1': 'Google DeepMind v2.0 \\textrightarrow\\ v3.0', 'GDM-2': 'Google DeepMind v3.0 \\textrightarrow\\ v3.1', 'META-1': 'Meta v1.1 \\textrightarrow\\ v2',
       'MSFT-1': 'Microsoft v1 \\textrightarrow\\ feb-2026', 'NAV-1': 'Naver 2024 \\textrightarrow\\ v2.0', 'XAI-1': 'xAI draft-2025-02-10 \\textrightarrow\\ draft-2025-02-20',
       'XAI-2': 'xAI draft-2025-02-20 \\textrightarrow\\ 2025-08-20', 'XAI-3': 'xAI 2025-08-20 \\textrightarrow\\ 2025-12-30', 'XAI-4': 'xAI 2025-12-30 \\textrightarrow\\ 2026-06-30'}

COMPANION = {
    'ANT-2-038': "Frontier Compliance Framework v2, section 3: Security control monitoring, testing, and assessments: Security controls are regularly tested and independently reviewed to ensure effectiveness. Penetration testing, vulnerability disclosure programs, third party risk assessments, and incident response tabletop exercises aim to help defenses remain robust, and insights from these activities are used to strengthen the company's security posture over time.",
    'ANT-2-015': "Frontier Compliance Framework v2: Prior to launching a model, we estimate the probability and severity of harm for CBRN, sabotage and loss of control, harmful manipulation and cyber offense risks.",
    'ANT-2-050': "Frontier Compliance Framework v2: When an AI Event is identified, a member of our Security or Safeguards team (the AI Incident Commander) will be promptly notified and will be responsible for our investigation and response, including assembling an incident response team with appropriate subject matter expert support.",
}

def tex(t):
    t = t.replace('\\', '\\textbackslash{}')
    for a, b in [('&', '\\&'), ('%', '\\%'), ('$', '\\$'), ('#', '\\#'), ('_', '\\_'), ('{', '\\{'), ('}', '\\}'), ('~', '\\textasciitilde{}'), ('^', '\\textasciicircum{}')]:
        t = t.replace(a, b)
    t = t.replace('“', '``').replace('”', "''").replace('‘', '`').replace('’', "'").replace('→', '\\textrightarrow\\ ').replace('–', '--').replace('—', '--').replace('●', '$\\bullet$').replace('​', '')
    return re.sub(r'\s+', ' ', t).strip()

def final(r, k):
    if r.get('READJ_mode', '').startswith('re-examined'): return r['READJ_' + k].strip()
    return ((r.get('ADJ_' + k) or '').strip() or r[k].strip())

def clip(t, n=90):
    w = t.split()
    return ' '.join(w[:n]) + (' [\\ldots]' if len(w) > n else '')

L = []
for c in ids:
    r = rows[c]
    out_, ann, flags = final(r, 'outcome'), final(r, 'announcement'), final(r, 'flags')
    code = f"{r['category']}; {out_}{' (MIX)' if 'MIX' in flags.upper() else ''}; {ann}"
    L.append(f"\\paragraph{{{c} ({code}).}} \\emph{{{LAB[r['pair_id']]}.}}\\\\")
    L.append(f"\\textbf{{Earlier:}} {tex(clip(r['v_i_text']))}\\\\")
    later = r['v_next_text']
    if out_ == 'L' and later.strip().upper() == 'NONE' and c in COMPANION:
        L.append(f"\\textbf{{Later (companion document):}} {tex(clip(COMPANION[c]))}\\\\")
    else:
        L.append(f"\\textbf{{Later:}} {tex(clip(later))}\\\\")
    ptr = r['changelog_pointer'].strip()
    L.append(f"\\textbf{{Provider's account:}} {tex(clip(ptr, 70)) if ptr and ptr.upper() not in ('NONE FOUND', 'NA') else 'none found'}\\\\")
    notes = []
    if r.get('ADJ_notes', '').strip(): notes.append(r['ADJ_notes'].strip())
    if r.get('READJ_notes', '').strip(): notes.append('Re-examination: ' + r['READJ_notes'].strip())
    L.append(f"\\textbf{{Adjudication:}} {tex(' '.join(notes)) if notes else 'first-pass code accepted.'}")
    L.append('')
open(out, 'w', encoding='utf-8').write('\n'.join(L))
print('wrote', len(ids), 'entries to', out)
