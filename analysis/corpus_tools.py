"""Shared helpers for building the safety-framework corpus.

Usage (python kernel, in the sub-agent's own workspace):
    exec(open(PATH_TO_THIS_FILE).read())
Then call the functions below. Nothing here spoofs a User-Agent; requests' default UA is used.
"""
import csv, hashlib, json, os, re, time
import requests

MANIFEST_COLUMNS = [
    "provider", "document", "version", "is_companion", "publication_date", "date_source",
    "currently_hosted", "retrieved_from", "retrieval_url", "wayback_capture_timestamp",
    "local_filename", "sha256", "txt_filename", "revision_account_exists",
    "revision_account_filename", "revision_account_source", "saferai_quote_check", "notes",
]

WB = "https://web.archive.org"
_session = requests.Session()


def _get(url, retries=6, backoff=8, **kw):
    """GET with retry on 429/5xx (Wayback rate-limits shared across parallel workers)."""
    last = None
    for i in range(retries):
        r = _session.get(url, **kw)
        if r.status_code in (429, 502, 503, 504):
            last = r
            wait = backoff * (2 ** i)
            ra = r.headers.get("Retry-After")
            if ra and ra.isdigit():
                wait = max(wait, int(ra))
            time.sleep(min(wait, 300))
            continue
        return r
    return last


def slug(s):
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9.\-]+", "-", s)
    return re.sub(r"-+", "-", s).strip("-")


def make_filename(provider, document, version, date_yyyy_mm_dd, ext):
    """{provider}_{document}_{version}_{YYYY-MM-DD}.{ext} per the brief's layout."""
    assert re.fullmatch(r"\d{4}-\d{2}-\d{2}|unknown-date", date_yyyy_mm_dd), date_yyyy_mm_dd
    return f"{slug(provider)}_{slug(document)}_{slug(version)}_{date_yyyy_mm_dd}.{ext.lstrip('.')}"


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def cdx(url, prefix=False, status="200", collapse_digest=True, limit=5000, pause=1.0):
    """Wayback CDX capture history. Returns list of dicts {timestamp,statuscode,digest,length,original}."""
    params = {"url": url, "output": "json", "fl": "timestamp,statuscode,digest,length,original", "limit": limit}
    if status:
        params["filter"] = f"statuscode:{status}"
    if collapse_digest:
        params["collapse"] = "digest"
    if prefix:
        params["matchType"] = "prefix"
    r = _get(f"{WB}/cdx/search/cdx", params=params, timeout=60)
    r.raise_for_status()
    time.sleep(pause)
    rows = r.json()
    if not rows:
        return []
    keys = rows[0]
    return [dict(zip(keys, row)) for row in rows[1:]]


def wayback_raw_url(timestamp, url):
    """Raw (unmodified) archived bytes: the id_ flag strips the Wayback toolbar/rewriting."""
    return f"{WB}/web/{timestamp}id_/{url}"


def fetch(url, out_path, timeout=90, pause=1.0):
    """Download url to out_path. Returns dict {status, content_type, bytes, sha256, final_url}."""
    r = _get(url, timeout=timeout, allow_redirects=True)
    time.sleep(pause)
    info = {"status": r.status_code, "content_type": r.headers.get("Content-Type", ""),
            "final_url": r.url, "bytes": len(r.content)}
    if r.status_code == 200:
        os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
        with open(out_path, "wb") as f:
            f.write(r.content)
        info["sha256"] = sha256(out_path)
        info["path"] = out_path
    return info


def fetch_wayback(url, timestamp, out_path, **kw):
    """Fetch the raw archived copy of url at timestamp. Wayback may redirect to the nearest capture;
    the actual capture timestamp is parsed from final_url and returned as 'capture_timestamp'."""
    info = fetch(wayback_raw_url(timestamp, url), out_path, **kw)
    m = re.search(r"/web/(\d{14})", info.get("final_url", ""))
    info["capture_timestamp"] = m.group(1) if m else timestamp
    info["capture_url"] = info.get("final_url")
    return info


def neighbour_captures(url, timestamp, n=3):
    """Digests of the n captures before and after `timestamp` for url, so a reader can see
    whether earlier/later captures differ in content. Returns {before:[...], after:[...]}."""
    rows = cdx(url, collapse_digest=False)
    before = [r for r in rows if r["timestamp"] < timestamp][-n:]
    after = [r for r in rows if r["timestamp"] > timestamp][:n]
    return {"before": before, "after": after}


# ---------- text extraction ----------

def pdf_to_text(pdf_path, txt_path):
    """Extract text with PyMuPDF. Emits '[[page N]]' markers and prefixes probable headings with '## '
    (spans whose font size exceeds 1.15x the modal body size and that are short). Returns page count."""
    import fitz
    from collections import Counter
    doc = fitz.open(pdf_path)
    sizes = Counter()
    for page in doc:
        for b in page.get_text("dict")["blocks"]:
            for l in b.get("lines", []):
                for s in l.get("spans", []):
                    if s["text"].strip():
                        sizes[round(s["size"], 1)] += len(s["text"])
    body = sizes.most_common(1)[0][0] if sizes else 10.0
    out = []
    for i, page in enumerate(doc, 1):
        out.append(f"\n[[page {i}]]\n")
        for b in page.get_text("dict")["blocks"]:
            for l in b.get("lines", []):
                line_txt = "".join(s["text"] for s in l.get("spans", [])).strip()
                if not line_txt:
                    continue
                mx = max(s["size"] for s in l["spans"])
                if mx >= body * 1.15 and len(line_txt) <= 120:
                    out.append("## " + line_txt)
                else:
                    out.append(line_txt)
            out.append("")
    text = "\n".join(out)
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(text)
    return len(doc)


def html_to_text(html_path, txt_path):
    """Extract visible text from HTML; headings become '## ' lines; scripts/styles/nav dropped."""
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(open(html_path, "rb").read(), "lxml")
    for t in soup(["script", "style", "noscript", "svg", "nav", "footer", "header"]):
        t.decompose()
    lines = []
    for el in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "td", "th", "blockquote", "pre"]):
        txt = " ".join(el.get_text(" ", strip=True).split())
        if not txt:
            continue
        lines.append(("## " + txt) if el.name.startswith("h") else txt)
    text = "\n".join(lines)
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(text)
    return len(lines)


def _norm(s):
    s = s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\u2013", "-").replace("\u2014", "-").replace("\u00ad", "")
    return re.sub(r"\s+", " ", s).strip().lower()


def find_quote(txt_path, phrase):
    """Whitespace/quote-insensitive search. Returns list of page numbers where phrase occurs (from [[page N]] markers)."""
    text = open(txt_path, encoding="utf-8").read()
    pages = re.split(r"\[\[page (\d+)\]\]", text)
    hits = []
    if len(pages) > 1:
        for i in range(1, len(pages), 2):
            if _norm(phrase) in _norm(pages[i + 1]):
                hits.append(int(pages[i]))
    else:
        if _norm(phrase) in _norm(text):
            hits.append(0)
    return hits


# ---------- manifest ----------

def write_manifest_rows(rows, path):
    """rows: list of dicts with MANIFEST_COLUMNS keys (missing -> ''). Writes CSV."""
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=MANIFEST_COLUMNS, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in MANIFEST_COLUMNS})
