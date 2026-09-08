"""Phase B: recall-oriented extraction of candidate commitment sentences.

Operational test (from the brief): the sentence refers to the provider as actor (we/our/us, the company name,
or a named internal role) AND contains a commitment-strength verb or modal
(will, must, commit, shall, intend, aim, expect, may, could, consider, plan). Conditional commitments included.
No classification or paraphrase. Over-inclusion accepted; omission not.

Usage: python extract_candidates.py manifest.csv documents/ candidates.csv
"""
import csv, re, sys, unicodedata
from collections import Counter


def clean(text):
    """Strip Unicode format characters (bidi marks, soft hyphens, zero-width) and normalise spaces."""
    text = "".join(ch for ch in text if unicodedata.category(ch) != "Cf")
    return text.replace("\u00a0", " ")

MODALS = r"\b(will|won't|must|commits?|committed|commitment|commitments|shall|intends?|intended|intend|aims?|aimed|expects?|expected|may|could|considers?|considered|plans?|planned)\b"
ROLE_TERMS = {
    "generic": [r"\bwe\b", r"\bour\b", r"\bus\b", r"\bourselves\b", r"\bthe company\b", r"\bthe Company\b",
                r"\bthe Board\b", r"\bBoard of Directors\b", r"\bCEO\b", r"\bChief Executive\b", r"\bexecutive leadership\b"],
    "Anthropic": [r"\bAnthropic\b", r"\bResponsible Scaling Officer\b", r"\bRSO\b", r"\bLong-Term Benefit Trust\b", r"\bLTBT\b"],
    "OpenAI": [r"\bOpenAI\b", r"\bSafety Advisory Group\b", r"\bSAG\b", r"\bPreparedness team\b", r"\bSafety and Security Committee\b", r"\bSSC\b"],
    "Google DeepMind": [r"\bGoogle DeepMind\b", r"\bDeepMind\b", r"\bGoogle\b", r"\bFrontier Safety team\b", r"\bAGI Safety Council\b", r"\bResponsibility and Safety Council\b", r"\bRSC\b"],
    "xAI": [r"\bxAI\b", r"\bGrok\b"],
    "Meta": [r"\bMeta\b"],
    "Amazon": [r"\bAmazon\b", r"\bAWS\b"],
    "Microsoft": [r"\bMicrosoft\b"],
    "NVIDIA": [r"\bNVIDIA\b", r"\bNvidia\b"],
    "Cohere": [r"\bCohere\b"],
    "G42": [r"\bG42\b"],
    "Naver": [r"\bNAVER\b", r"\bNaver\b", r"\bFuture AI Center\b"],
    "Magic": [r"\bMagic\b"],
}
ABBREV = ["e.g.", "i.e.", "etc.", "vs.", "cf.", "No.", "Fig.", "Sec.", "approx.", "U.S.", "U.K.", "Dr.", "Mr.", "Ms.",
          "Inc.", "Ltd.", "Co.", "Corp.", "St.", "al.", "Vol.", "pp.", "p.", "Jan.", "Feb.", "Mar.", "Apr.", "Jun.", "Jul.",
          "Aug.", "Sep.", "Sept.", "Oct.", "Nov.", "Dec.", "v.", "ver."]


def protect(text):
    for a in ABBREV:
        text = text.replace(a, a.replace(".", "\u2024"))  # one-dot leader as placeholder
    text = re.sub(r"(\d)\.(\d)", "\\1\u2024\\2", text)  # decimals and version numbers 2.1
    text = re.sub(r"\b([A-Z])\.(?=\s?[A-Z]\.)", "\\1\u2024", text)  # initials
    return text


def unprotect(text):
    return text.replace("\u2024", ".")


def blocks_from_txt(text):
    """Yield (heading, paragraph_text). Rebuilds paragraphs from the toolkit's line-oriented .txt."""
    heading = "(none)"
    para = []
    text = clean(text)
    # running headers/footers: heading lines repeated on 3+ pages are dropped entirely
    hcount = Counter(l.strip() for l in text.splitlines() if l.startswith("## "))
    running = {h for h, c in hcount.items() if c >= 3}
    for raw in text.splitlines():
        line = raw.strip()
        if line in running:
            continue
        if re.fullmatch(r"\[\[page \d+\]\]", line):
            continue
        if line.startswith("## "):
            if para:
                yield heading, " ".join(para)
                para = []
            heading = line[3:].strip()
            continue
        if not line:
            if para:
                yield heading, " ".join(para)
                para = []
            continue
        # de-hyphenate line-break hyphens
        if para and para[-1].endswith("-") and line and line[0].islower():
            para[-1] = para[-1][:-1] + line
        else:
            para.append(line)
    if para:
        yield heading, " ".join(para)


def split_sentences(par):
    p = protect(par)
    # split after terminal punctuation (optionally followed by a closing quote/bracket) when the next token starts a sentence
    parts = re.split(r"(?:(?<=[.!?])|(?<=[.!?][\"'\)\]]))\s+(?=[\"'\(\[]?[A-Z0-9])", p)
    return [unprotect(s).strip() for s in parts if s.strip()]


def extract(provider, text):
    pats = ROLE_TERMS["generic"] + ROLE_TERMS.get(provider, [])
    role_re = re.compile("|".join(pats))
    modal_re = re.compile(MODALS, re.IGNORECASE)
    out = []
    idx = 0
    for heading, par in blocks_from_txt(text):
        for s in split_sentences(par):
            idx += 1
            if len(s) < 15:
                continue
            modals = modal_re.findall(s)
            if modals and role_re.search(s):
                out.append({"section_heading": heading, "sentence_index": idx, "sentence_verbatim": s,
                            "modal_verbs_found": ";".join(sorted(set(m.lower() for m in modals)))})
    return out, idx


def main(manifest_path, docs_dir, out_path, log_path=None):
    rows = list(csv.DictReader(open(manifest_path, encoding="utf-8")))
    cands, stats = [], []
    for r in rows:
        if r.get("is_companion", "").strip().lower() == "yes":
            continue
        txt = r.get("txt_filename", "").strip()
        if not txt:
            stats.append((r["provider"], r["version"], "skipped: no txt"))
            continue
        if "-ko" in r["version"] or "korean" in r.get("notes", "").lower()[:80]:
            stats.append((r["provider"], r["version"], "skipped: Korean-language rendering"))
            continue
        path = f"{docs_dir}/{txt.split('/')[-1]}"
        text = open(path, encoding="utf-8").read()
        found, n = extract(r["provider"], text)
        for f in found:
            cands.append({"provider": r["provider"], "document": r["document"], "version": r["version"], **f})
        stats.append((r["provider"], r["version"], f"{len(found)} candidates / {n} sentences"))
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["provider", "document", "version", "section_heading", "sentence_index", "sentence_verbatim", "modal_verbs_found"])
        w.writeheader()
        w.writerows(cands)
    if log_path:
        with open(log_path, "w", encoding="utf-8") as f:
            for s in stats:
                f.write(" | ".join(map(str, s)) + "\n")
    return cands, stats


if __name__ == "__main__":
    main(*sys.argv[1:])
