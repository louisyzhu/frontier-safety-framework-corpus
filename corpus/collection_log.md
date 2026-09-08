# Collection log

Corpus of frontier AI safety frameworks, built 1 to 2 September 2026 (UTC). All times UTC. Style note: quotations from providers are verbatim and may contain em-dashes; the log's own prose avoids them.

## 0. Order of work

1. restatement.md was written and saved before any reconnaissance or download began (artifact version 0b2e7440-5752-41f3-904a-af548db331cf, 1 September 2026 23:2x UTC).
2. Phase A1 reconnaissance ran as four parallel tracks (Anthropic; OpenAI; DeepMind, xAI and Meta; the seven single-version signatories). Each track's full search log is a separate artifact: recon_anthropic.md, recon_openai.md, recon_deepmind_xai_meta.md, recon_signatories.md. This file summarises them and records the judgement calls made when consolidating.
3. Phase A2 collection began only after the consolidated list below was written.

## 1. Access and environment

- Sandbox network access was granted per domain. Wayback Machine (web.archive.org, archive.org) answered, but rate-limited the shared sandbox IP with HTTP 429 for long stretches while four tracks ran in parallel. Consequences are recorded per track under 'Limits'.
- openai.com HTML pages return HTTP 403 to the sandbox; cdn.openai.com PDFs return 200. OpenAI web pages were therefore read from Wayback captures and web-search snippets.
- x.ai HTML pages return 403 to the sandbox; x.ai/documents/2025.02.20-RMF-Draft.pdf returns HTTP 200 with content-type application/pdf but a 131-byte Git LFS pointer body (oid sha256 89fafebb73757def5a9068105554e68799e3dcce55374a4179b7a62559b6bef9, size 230615) instead of the PDF; observed 1 September 2026 23:33 UTC with server Last-Modified 1 September 2026 17:12 GMT. The PDF itself is served from data.x.ai.
- g42.ai returns 403 to the sandbox. G42 documents come from Wayback.
- storage.googleapis.com is on the sandbox's built-in denylist. DeepMind PDFs were read from Wayback during reconnaissance; the bucket-qualified host deepmind-media.storage.googleapis.com was granted afterwards and serves the same files (checked: frontier-safety-framework_3-1.pdf, 447155 bytes, HTTP 200).
- ai.meta.com/static-resource/meta-frontier-ai-framework/ returns HTTP 500 (live and in Wayback from 24 April 2026). The 2025 Meta document comes from Wayback.
- Anthropic hosts (www.anthropic.com, www-cdn.anthropic.com, cdn.sanity.io) answered 200 throughout. A prior session had recorded 403s from Anthropic hosts; not reproduced here.
- Anthropic's Frontier Compliance Framework is hosted only inside a Vanta Trust Center app (trust.anthropic.com), which the sandbox cannot render. See judgement call J7.

## 2. Reconnaissance results by track

### 2.1 Anthropic (recon_anthropic.md)

| Provider | Document | Version identifier | Companion | Date (as recorded) | Hosted | Format | Document URL |
|---|---|---|---|---|---|---|---|
| Anthropic | Responsible Scaling Policy | v1.0 | no | 2023-09-19 | yes | pdf | https://www-cdn.anthropic.com/1adf000c8f675958c2ee23805d91aaade1cd4613/responsible-scaling-policy.pdf |
| Anthropic | Responsible Scaling Policy | v2.0 | no | 2024-10-15 | yes | pdf | https://www-cdn.anthropic.com/616dee633636e5bd309cb73aed8622e80fe47839.pdf |
| Anthropic | Responsible Scaling Policy | v2.1 | no | 2025-03-31 | yes | pdf | https://www-cdn.anthropic.com/17310f6d70ae5627f55313ed067afc1a762a4068.pdf |
| Anthropic | Responsible Scaling Policy | v2.2 | no | 2025-05-14 | yes | pdf | https://www-cdn.anthropic.com/872c653b2d0501d6ab44cf87f43e1dc4853e4d37.pdf |
| Anthropic | Responsible Scaling Policy | v3.0 | no | 2026-02-24 | yes | pdf | https://www.anthropic.com/responsible-scaling-policy/rsp-v3-0 (307 redirect to https://www-cdn.anthropic.com/e670587677525f28df69b59e5fb4c22cc5461a17.pdf) |
| Anthropic | Responsible Scaling Policy | v3.1 | no | 2026-04-02 | yes | pdf | https://www-cdn.anthropic.com/files/4zrzovbb/website/bf04581e4f329735fd90634f6a1962c13c0bd351.pdf |
| Anthropic | Responsible Scaling Policy | v3.2 | no | 2026-04-29 | yes | pdf | https://cdn.sanity.io/files/4zrzovbb/website/28c6241900d90410628a8a2003a5572faae4365a.pdf |
| Anthropic | Responsible Scaling Policy | v3.3 | no | 2026-05-26 | yes | pdf | https://cdn.sanity.io/files/4zrzovbb/website/c11e84981d0a7281a1b229f3fa6af0da66eaf43f.pdf |
| Anthropic | Responsible Scaling Policy | v3.4 | no | 2026-07-08 | yes | pdf | https://cdn.sanity.io/files/4zrzovbb/website/0bacdc8440ea96e62a8766d99ebe1d4eea6d5f3a.pdf |
| Anthropic | Frontier Compliance Framework | Frontier Compliance Framework (December 2025) | yes | 2025-12-19 | unknown | unknown | https://trust.anthropic.com/resources?s=eorilovp4wxk38nxbi7k3&name=anthropic-frontier-compliance-framework |
| Anthropic | Frontier Compliance Framework | Frontier Compliance Framework [Feb 2026] | yes | unknown (Trust Center resource name says 'Feb 2026'; earliest Wayback capture of its URL 2026-03-05) | unknown | unknown | https://trust.anthropic.com/resources?s=gi5v45ke7aezh7b04e82s&name=anthropic-frontier-compliance-framework-%5Bfeb-2026-%5D |
| Anthropic | RSP Noncompliance Reporting and Anti-Retaliation Policy | RSP Noncompliance Reporting and Anti-Retaliation Policy (file 'Final 2025.12.04') | yes | 2025-12-04 (file name) / linked publicly by 2026-02-20 (Wayback capture of rsp-updates) | yes | pdf | https://www-cdn.anthropic.com/fcf136d0f2204e2184f73c6bd082bea27f2d631b/RSP Noncompliance Reporting and Anti-Retaliation Policy (Final 2025.12.04).pdf |
| Anthropic | RSP Noncompliance Reporting and Anti-Retaliation Policy | RSP Noncompliance Reporting and Anti-Retaliation Policy (March 2026 posting; metadata 'v 3.3') | yes | 2026-03-24 (page entry) / 'released internally in February 2026' (page entry) | yes | pdf | https://www-cdn.anthropic.com/b7a5629e40b391b2adfb4cc8c0888ac9d6bfddf6/RSP Noncompliance Reporting and Anti-Retaliation Policy.pdf |
| Anthropic | Frontier Safety Roadmap | Frontier Safety Roadmap (HTML page) | yes | 2026-02-24 (first Wayback capture 20260224225537; introduced with RSP v3.0) / updated 2026-04-02 (page entry) | yes | html | https://www.anthropic.com/responsible-scaling-policy/roadmap |

Not found:
- **RSP v1.1**. Every changelog lists v1.0 (Sept 19, 2023) followed directly by v2.0 (Oct 15, 2024). No v1.1 anywhere. Sources checked:
    - https://www.anthropic.com/responsible-scaling-policy
    - https://www-cdn.anthropic.com/616dee633636e5bd309cb73aed8622e80fe47839.pdf (v2.0 changelog)
    - https://www-cdn.anthropic.com/17310f6d70ae5627f55313ed067afc1a762a4068.pdf (v2.1 changelog)
    - https://www-cdn.anthropic.com/872c653b2d0501d6ab44cf87f43e1dc4853e4d37.pdf (v2.2 changelog)
    - https://www-cdn.anthropic.com/e670587677525f28df69b59e5fb4c22cc5461a17.pdf (v3.0 changelog)
    - https://cdn.sanity.io/files/4zrzovbb/website/0bacdc8440ea96e62a8766d99ebe1d4eea6d5f3a.pdf (v3.4 cumulative changelog)
    - https://web.archive.org/web/20241104110000/https://www.anthropic.com/rsp-updates
    - https://web.archive.org/web/20250619084758/https://www.anthropic.com/rsp-updates
    - https://web.archive.org/web/20260220175916/https://www.anthropic.com/rsp-updates
    - Wayback redirect targets of https://www.anthropic.com/responsible-scaling-policy 2023-10 to 2024-10 (all v1.0 PDF, identical text)
    - https://www.anthropic.com/news/anthropics-responsible-scaling-policy
    - https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy
    - https://metr.org/fsp
- **Standalone announcement posts for v2.1, v2.2, v3.1, v3.2, v3.3, v3.4**. Provider accounts for these versions are the dated page entries, in-document changelogs and (from v2.2) redlines. Sources checked:
    - https://www.anthropic.com/responsible-scaling-policy
    - https://www.anthropic.com/news/responsible-scaling-policy-v3
    - web search
- **Post on RSP v3.0 by Buck Shlegeris**. The v3.0 reasoning post is by Holden Karnofsky. Sources checked:
    - https://www.lesswrong.com/graphql (post HzKuzrKfaDJvQqmjh: author HoldenKarnofsky; body has no 'Shlegeris'/'Buck')
    - https://www.lesswrong.com/graphql (60 most recent posts of user 'Buck', id rx7xLaHCh3m7Po385: none on RSP v3)
    - web search
- **Direct PDF URL for the Frontier Compliance Framework (either version)**. Hosted only inside the Vanta Trust Center app; not retrievable from the sandbox (assets.vanta.com not allowed). Sources checked:
    - https://www.anthropic.com/news/responsible-scaling-policy-v3
    - https://www.anthropic.com/news/compliance-framework-SB53
    - https://www.anthropic.com/transparency/voluntary-commitments
    - https://www.anthropic.com/transparency
    - Wayback CDX trust.anthropic.com/resources* (103 captures, app shells)
    - web search
- **Wayback capture of the Dec 2025 Noncompliance Policy PDF**. 0 rows. Sources checked:
    - https://web.archive.org/cdx/search/cdx?url=www-cdn.anthropic.com/fcf136d0f2204e2184f73c6bd082bea27f2d631b/*&matchType=prefix

Conflicts recorded (not resolved):
- v3.0 reasoning post authorship: brief says Buck Shlegeris; LessWrong record (GraphQL) says HoldenKarnofsky, posted 2026-02-24T20:20:47Z. Both recorded; primary record supports Karnofsky.
- RSP Noncompliance Reporting and Anti-Retaliation Policy: earlier file named 'Final 2025.12.04' and linked publicly by 2026-02-20, versus page entry (March 24, 2026) saying the policy was 'released internally in February 2026'. Current file's PDF metadata title says 'v 3.3' while its body refers to RSP 'Version 3.0'.
- v2.0 identifier: title page reads 'Responsible Scaling Policy Effective October 15, 2024' with no version number; RSP page calls it 'Version 2.0'; changelogs call it 'RSP-2024' and (from v2.1) 'RSP v2.0'.
- Frontier Compliance Framework scope: Dec 19, 2025 post lists cyber offence, CBRN, AI sabotage and loss of control; Transparency Hub (updated July 23, 2026) adds 'harmful manipulation'. Consistent with a Feb 2026 revision but the documents were not read.
- v2.1 effective date March 31, 2025 versus first Wayback evidence of the PDF on 2025-04-01 (PDF creation dates of v2.2, v3.1, v3.3, v3.4 precede their effective dates by 1-3 days). Effective dates as stated are used.
- Publication date of the current RSP page's 'Version 3.0' link: the page lists an HTML URL (/responsible-scaling-policy/rsp-v3-0) while the document is a PDF; format recorded as pdf.

Silent-version candidates:
- v2.1: two PDF files served on 2025-04-01 (www-cdn.anthropic.com/080b003762c270d033dc2ea1153b9df665078da1.pdf, Wayback 20250401013032; www-cdn.anthropic.com/f3b282f157017d08e36636bda1bf3bd4d9f23ee7.pdf, Wayback 20250401141944) are textually identical to each other and differ from the current v2.1 file (17310f6d..., Wayback 20250402134435) only in table-of-contents page numbers and the removal of the TOC line 'Changelog 17'. Same version number and effective date. Low substance. 080b now 404; f3b2 still served but unlinked.
- v2.0: the file at assets.anthropic.com/m/24a47b00f10301cd/original/Anthropic-Responsible-Scaling-Policy-2024-10-15.pdf was re-uploaded between Wayback captures 20241022154907 and 20241101012028; the only text difference from the current v2.0 file is the changelog phrase 'Initial version.' becoming 'Initial version, link here.' (hyperlink to v1.0 added). Served in that form until at least 20260428160734; the URL now returns an HTML page. The 59 distinct digests at this URL mostly reflect CDN byte variants, not content changes.
- RSP HTML page (https://www.anthropic.com/responsible-scaling-policy): 37 distinct-digest 200 captures from 20260225232904 to 20260830142047. Digest changes coincide with the dated entries and with site boilerplate changes; two spot checks found no silent edits to existing version entries (v2.1 and v2.2 entries identical between 20250619084758 and 2026-09-01). One trivial edit found on the predecessor page /rsp-updates: '15th of October, 2024' (capture 20241104110000) became 'October 15, 2024' (by 20250619084758). Not over-claimed.
- v1.0 PDF moved across three URLs (www-files 2023-09; www-cdn/files/4zrzovbb 2024-01; www-cdn/1adf.../responsible-scaling-policy.pdf 2024-03) with identical bytes (same Wayback digest DLPQADEPM5MVRQXOEOAF3ENKVXQ42RQT for the first two; identical MD5 for the second and the current file). Not a content change.

Limits declared by the track:
- Frontier Compliance Framework documents (Dec 2025 and Feb 2026) could not be read: hosted in the Vanta Trust Center whose scripts are served from assets.vanta.com (not allowed); existence and dates rest on Anthropic's announcement post, Transparency Hub text and Trust Center resource URLs/Wayback captures; content and the Feb 2026 date are provisional
- Redline PDFs: only the v2.2 redline's earliest Wayback capture was checked; the v3.1 to v3.4 redlines were downloaded and read but their Wayback capture history was not queried
- Secondary trackers: only METR (metr.org/fsp) was consulted; SaferAI, AI Lab Watch and Vorp Labs were not
- Frontier Safety Roadmap and Risk Reports: existence and capture counts recorded, but their internal revision histories were not examined
- Silent-version digest analysis of the RSP HTML page rests on two spot-check captures of the predecessor /rsp-updates page (2024-11-04, 2025-06-19) and the 2026-02-20 capture, not on a capture-by-capture diff of all 37 post-Feb-2026 captures
- www-files.anthropic.com (original 2023 v1.0 host) is not reachable from the sandbox, so its current hosting status is unknown

### 2.2 OpenAI (recon_openai.md)

| Provider | Document | Version identifier | Companion | Date (as recorded) | Hosted | Format | Document URL |
|---|---|---|---|---|---|---|---|
| OpenAI | Preparedness Framework | Beta | no | 2023-12-18 | yes | pdf | https://cdn.openai.com/openai-preparedness-framework-beta.pdf |
| OpenAI | Preparedness Framework | Version 2 (document label 'Version 2. Last updated: 15th April, 2025'; METR lists 'v2.0') | no | 2025-04-15 | yes | pdf | https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf |
| OpenAI | Preparedness Framework | Version 2, silent revision of the PDF at the same URL (no new version label) | no | unknown; bounded 2025-04-17 to 2025-06-11 by Wayback captures; server Last-Modified 2025-06-09 21:27:02 GMT; PDF CreationDate 2025-04-28 | yes | pdf | https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf |
| OpenAI | Frontier Governance Framework | unversioned (first edition; no version number or date printed in the PDF) | yes | 2026-05-28 (announcement page) / 2026-05-27 (PDF server Last-Modified) | yes | pdf | https://cdn.openai.com/pdf/e37d949b-8c9f-4d76-b99e-4272f4631a7e/openai-frontier-governance-framework.pdf |

Not found:
- **Preparedness Framework version between Beta (Dec 2023) and Version 2 (Apr 2025)**. Provisional. Beta PDF shows a single content digest throughout. CDX prefix enumeration of openai.com/* and cdn.openai.com/* could not be completed (rate limiting and timeouts), so a differently named intermediate PDF cannot be excluded by Wayback enumeration. Sources checked:
    - https://web.archive.org/cdx/search/cdx?url=https://cdn.openai.com/openai-preparedness-framework-beta.pdf&output=json&collapse=digest
    - https://metr.org/fsp
    - https://web.archive.org/web/20250416173732/https://openai.com/index/updating-our-preparedness-framework/
    - https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf (Appendix A)
    - web searches: 'OpenAI Preparedness Framework version 2 April 2025 update'; 'OpenAI Preparedness Framework beta announcement December 18 2023'
- **Preparedness Framework version after Version 2 (v2.1, v3, or a 2026 revision)**. Provisional. The v2 PDF content is unchanged since June 2025. The FGF (May 2026) describes the PF as continuing and announces no PF revision. Same prefix-enumeration caveat. Sources checked:
    - https://web.archive.org/cdx/search/cdx?url=https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf&output=json&collapse=digest (captures to 20260817145128)
    - https://web.archive.org/web/20260528180226/https://openai.com/index/openai-frontier-governance-framework/
    - https://cdn.openai.com/pdf/e37d949b-8c9f-4d76-b99e-4272f4631a7e/openai-frontier-governance-framework.pdf
    - https://metr.org/fsp
    - https://vorplabs.com/ai-regulatory-updates/frontier-ai-frameworks (snippet)
    - web search: 'OpenAI Preparedness Framework version 2.1 OR v2.1 OR version 3 update 2026'
- **PF version-history or updates page on openai.com**. None found. The Beta announcement page now redirects to openai.com/safety/. Sources checked:
    - https://web.archive.org/web/20231218182454/https://openai.com/safety/preparedness
    - https://web.archive.org/web/20240912155938/https://openai.com/preparedness/
    - https://web.archive.org/web/20250416173732/https://openai.com/index/updating-our-preparedness-framework/
    - https://web.archive.org/web/20260528180226/https://openai.com/index/openai-frontier-governance-framework/
- **Revision account for the Beta**. None found; first version. Sources checked:
    - https://cdn.openai.com/openai-preparedness-framework-beta.pdf
    - https://web.archive.org/web/20231218182454/https://openai.com/safety/preparedness
    - https://metr.org/fsp

Conflicts recorded:
- PF Version 2 date: printed 'Last updated: 15th April, 2025' versus PDF metadata CreationDate 2025-04-28 versus server Last-Modified 2025-06-09 for the currently served file (original 15 April file had CreationDate 2025-04-15 and Last-Modified 2025-04-15).
- FGF date: announcement page 2026-05-28 versus PDF server Last-Modified 2026-05-27; no date printed in the document.
- PF v2 identifier: document says 'Version 2'; METR lists 'v2.0'; commentators write '2.0'.

Silent-version candidates:
- PF Version 2 PDF at https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf: bytes changed between Wayback captures 20250415191354 (digest XL3NESO2Y74VJT7AMP7U32JNG2LPPK2B, md5 da07e86d630fed9cbe617eb02ecffa01) and 20250611025204 (digest BAJKRRWOFFAB2NJKQCYAC7DKLKRTZB2Z, md5 648b1dfe1af9fa3fe37bc17100835371, equal to the file served 2026-09-01). Server Last-Modified 2025-06-09 21:27:02 GMT. Text changes are editorial: 'e.g.' to 'e.g.,' (7x), en-dash to hyphen (1x), removal of a duplicated 'Value alignment' sentence in Appendix C. Label unchanged.
- PF Version 2 PDF: a third Wayback digest 3YPOFDZLPTMFIYNBJWJNNRDJW5CD7YRV appears in 2026 captures, but the 20260408203627 capture is byte-identical to the current file; transfer artefact, NOT a content change.
- FGF PDF at https://cdn.openai.com/pdf/e37d949b-8c9f-4d76-b99e-4272f4631a7e/openai-frontier-governance-framework.pdf: Wayback digests DMQY..., T7SO..., JOXC... differ, but captures 20260529171758 and 20260616170222 are byte-identical to the current file and 20260608044040 is a 5 MiB truncation; NOT a content change.
- Beta PDF: Wayback digest WD3OXSNT77W7DBL46GQBO6N65O527S3N at 20240226181828 is a 1 MiB truncated capture; NOT a content change.
- Announcement pages (openai.com/safety/preparedness 43 distinct digests Dec 2023 to Mar 2024; v2 post 70 distinct digests Apr 2025 to Aug 2026, of which 53 are status 200; FGF post 8 distinct digests): only the earliest capture of each was read; later digest changes not diffed and most likely site boilerplate. Not verified.

Limits declared by the track:
- Wayback CDX prefix enumeration of openai.com/* and cdn.openai.com/* could not be completed (HTTP 429 rate limiting and read timeouts); only the specific URLs were enumerated, so the absence of differently named intermediate or later PF PDFs is provisional.
- Only the earliest Wayback capture of each announcement page was read; the later distinct-digest captures (43 for the Beta page, 70 for the v2 post, 8 for the FGF post) were not diffed.
- openai.com HTML pages were read via Wayback captures and web search snippets, not directly (HTTP 403 to the sandbox).
- The parent brief's listed final outputs (restatement.md, manifest.csv, collection_log.md, documents/, changelogs/, candidates.csv) were not produced; this task was reconnaissance only and produced recon_openai.md plus this structured output.

### 2.3 Google DeepMind, xAI, Meta (recon_deepmind_xai_meta.md)

| Provider | Document | Version identifier | Companion | Date (as recorded) | Hosted | Format | Document URL |
|---|---|---|---|---|---|---|---|
| Google DeepMind | Frontier Safety Framework | Version 1.0 | no | 2024-05-17 | yes | pdf | https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/introducing-the-frontier-safety-framework/fsf-technical-report.pdf |
| Google DeepMind | Frontier Safety Framework | Version 2.0 | no | 2025-02-04 | yes | pdf | https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/updating-the-frontier-safety-framework/Frontier%20Safety%20Framework%202.0.pdf |
| Google DeepMind | Frontier Safety Framework | Version 3.0 | no | 2025-09-22 | yes | pdf | https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3.pdf |
| Google DeepMind | Frontier Safety Framework | Version 3.1 | no | 2026-04-17 | yes | pdf | https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3-1.pdf |
| xAI | Risk Management Framework (Draft) | Draft, 10 February 2025 (filename 2025.02.10-RMF-Draft; PDF title 'xAI Risk Management Framework (2.10.2025 Draft)') | no | 2025-02-10 | no | pdf | https://x.ai/documents/2025.02.10-RMF-Draft.pdf |
| xAI | Risk Management Framework (Draft) | Draft, 20 February 2025 (filename 2025.02.20-RMF-Draft; PDF title '2025.02.20 xAI Risk Management Framework Draft') | no | 2025-02-20 (filename/PDF title) / PDF CreationDate 2025-02-21 / earliest real-PDF capture 2025-02-26 | yes | pdf | https://data.x.ai/2025.02.20-RMF-Draft.pdf |
| xAI | Risk Management Framework | Last updated: August 20, 2025 (no version number) | no | 2025-08-20 (document) / 2025-08-21 (earliest capture) / 2025-08-22 (current file CreationDate and server Last-Modified) | yes | pdf | https://data.x.ai/2025-08-20-xai-risk-management-framework.pdf |
| xAI | Frontier Artificial Intelligence Framework (successor to the Risk Management Framework; retitled, no provider statement of replacement) | Last updated: December 30, 2025 (no version number) | no | 2025-12-30 (document) / 2025-12-31 (filename and server Last-Modified) | yes | pdf | https://data.x.ai/2025-12-31-xai-frontier-artificial-intelligence-framework.pdf |
| xAI | Frontier Artificial Intelligence Framework | Effective Date: 30 June 2026 (no version number) | no | 2026-06-30 (effective date in document) / server Last-Modified 2026-07-10 / earliest capture 2026-07-16 | yes | pdf | https://media.x.ai/v1/website/xai-frontier-artificial-intelligence-framework-30-june-2026-99c40684.pdf |
| Meta | Frontier AI Framework | Version 1.1 (cover label) / 'Initial version' per the 2026 change log | no | 2025-02-03 | no | pdf | https://ai.meta.com/static-resource/meta-frontier-ai-framework/ |
| Meta | Advanced AI Scaling Framework (renamed from Frontier AI Framework) | Version 2 (cover) / v2.0 (change log) | no | 2026-04-07 (in-document change log) / 2026-04-08 (blog post and earliest Wayback capture) | yes | pdf | https://ai.meta.com/static-resource/Meta_Advanced-AI-Scaling-Framework-v2 |

Not found:
- **Google DeepMind FSF version later than 3.1 (e.g. 3.2, 4.0) as of 1 Sep 2026**. Latest listed on the provider page is Version 3.1 (17 Apr 2026). Sources checked:
    - https://deepmind.google/frontier-safety/
    - https://deepmind.google/blog/strengthening-our-frontier-safety-framework/
    - https://web.archive.org/cdx/search/cdx?url=storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/*
    - https://metr.org/fsp
    - web_search: Google DeepMind Frontier Safety Framework page
    - web_search: Frontier Safety Framework 3.1 Tracked Capability Levels April 2026
- **Separate DeepMind announcement post for FSF 3.1**. 3.1 was announced by editing the 22 Sep 2025 post in place ('Updated April 17, 2026'). Sources checked:
    - https://deepmind.google/frontier-safety/
    - https://deepmind.google/blog/strengthening-our-frontier-safety-framework/
    - https://deepmind.google/blog/updating-the-frontier-safety-framework/
    - https://deepmind.google/blog/introducing-the-frontier-safety-framework/
    - web_search: Frontier Safety Framework 3.1 Tracked Capability Levels April 2026
- **xAI statement of what changed between any two framework versions (10 Feb draft, 20 Feb draft, Aug 2025 RMF, Dec 2025 FAIF, Jun 2026 FAIF)**. No in-document changelog, no x.ai news post, no version-history table found. Sources checked:
    - https://web.archive.org/web/20250210221647id_/https://x.ai/documents/2025.02.10-RMF-Draft.pdf
    - https://data.x.ai/2025.02.20-RMF-Draft.pdf
    - https://data.x.ai/2025-08-20-xai-risk-management-framework.pdf
    - https://data.x.ai/2025-12-31-xai-frontier-artificial-intelligence-framework.pdf
    - https://media.x.ai/v1/website/xai-frontier-artificial-intelligence-framework-30-june-2026-99c40684.pdf
    - https://web.archive.org/web/20250828090312id_/https://x.ai/safety
    - https://web.archive.org/web/20260203002028id_/https://x.ai/safety
    - https://web.archive.org/web/20260405054622id_/https://x.ai/safety
    - https://web.archive.org/web/20260815221302id_/https://x.ai/safety
    - https://web.archive.org/cdx/search/cdx?url=x.ai/news/*
    - web_search: xAI Risk Management Framework published August 2025 x.ai news
    - web_search: xAI Frontier AI Framework announcement December 2025 OR 30 June 2026 Grok
- **xAI framework version later than the 30 June 2026 FAIF**. x.ai/safety could not be fetched live (HTTP 403); latest Wayback capture is 15 Aug 2026. Sources checked:
    - https://web.archive.org/web/20260815221302id_/https://x.ai/safety
    - https://web.archive.org/cdx/search/cdx?url=media.x.ai/v1/website/*
    - https://web.archive.org/cdx/search/cdx?url=data.x.ai/*
    - https://web.archive.org/cdx/search/cdx?url=x.ai/documents/*
    - https://metr.org/fsp
- **xAI announcement post for any framework version on x.ai**. Not found. Sources checked:
    - https://web.archive.org/cdx/search/cdx?url=x.ai/news/*
    - https://x.ai/news (HTTP 403 live)
    - https://web.archive.org/web/20250814140938/https://x.ai/news/safety (404)
- **Meta framework version later than Advanced AI Scaling Framework Version 2**. Not found. Sources checked:
    - https://ai.meta.com/static-resource/Meta_Advanced-AI-Scaling-Framework-v2
    - https://web.archive.org/cdx/search/cdx?url=ai.meta.com/static-resource/*
    - https://metr.org/fsp
    - web_search: Meta Advanced AI Scaling Framework 2026
- **Meta statement about the March 2025 silent edit of the Frontier AI Framework PDF**. Change log of the 2026 document lists only 'February 3, 2025 ... Initial version.' Sources checked:
    - https://web.archive.org/web/20250328093937id_/https://ai.meta.com/static-resource/meta-frontier-ai-framework/
    - https://web.archive.org/web/20260825090800id_/https://about.fb.com/news/2025/02/meta-approach-frontier-ai/
    - https://ai.meta.com/blog/meta-frontier-ai-framework/ (404)
    - https://ai.meta.com/static-resource/Meta_Advanced-AI-Scaling-Framework-v2 (change log)
- **Wayback capture of the Meta Frontier AI Framework PDF between 3 Feb and 13 Feb 2025**. Earliest capture is 20250213105620; the text as first published on 3 Feb 2025 is not verified. Sources checked:
    - https://web.archive.org/cdx/search/cdx?url=ai.meta.com/static-resource/meta-frontier-ai-framework/

Conflicts recorded:
- DeepMind: secondary sources (comparativeai.org, futureagi.com) call the 17 Apr 2026 update 'v3.0'; the PDF, framework page and blog say 'Version 3.1'.
- DeepMind FSF 2.0: three byte variants of the 'Version 2.0' document (5 Feb 2025; '(1).pdf' from 13 Feb 2025; 21 Mar 2025 corrected file first captured 28 Mar 2025) with no version number change.
- DeepMind FSF 3.1: stated publication 17 Apr 2026 vs earliest Wayback capture of the PDF 25 May 2026 (coverage gap, recorded not resolved).
- xAI drafts: the brief's single 'Feb 2025 draft' is two documents with different text (2025.02.10 and 2025.02.20 filenames).
- xAI 20 Feb draft: filename date 20 Feb 2025; PDF CreationDate 21 Feb 2025; first real-PDF Wayback capture 26 Feb 2025; PDF ModDate 7 Mar 2025 (text unchanged).
- xAI Aug 2025 RMF: 'Last updated: August 20, 2025' in document; capture of 21 Aug 2025 differs in text from the current file created 22 Aug 2025 ('AISI,' removed).
- xAI Dec 2025 FAIF: 'December 30, 2025' (body) vs 2025-12-31 (filename, server Last-Modified).
- xAI Jun 2026 FAIF: PDF metadata title 'Privileged/Confidential DRAFT working FRAMEWORK DOC' vs body 'Effective Date: 30 June 2026' and its status as the framework linked from x.ai/safety; server object overwritten once (metageneration 2, Last-Modified 10 Jul 2026).
- xAI: whether the Frontier Artificial Intelligence Framework is a version of the Risk Management Framework or a new document; the provider has made no statement. Reported as successor versions.
- xAI: SaferAI Table 9 cites 'Section 5.2' of the Feb 2025 draft; the draft has no heading numbered 5.2 (the red-team commitment is on page 4).
- Meta Frontier AI Framework: cover says 'Version 1.1'; the 2026 change log calls it 'Initial version'.
- Meta Frontier AI Framework: PDF text changed between Wayback captures 20250213105620 and 20250328093937 (20 word-level changes) with no change of version label or date.
- Meta Advanced AI Scaling Framework: change log date 'April 7, 2026' vs blog post and earliest Wayback capture 8 Apr 2026; version label 'Version 2' (cover) vs 'v2.0' (change log) vs '-v2' (URL).
- Meta newsroom post dated 'February 3, 2025' also shows 'April 20, 2026' and now links the 2026 document under the link text 'Frontier AI Framework'; body text unchanged.

Silent-version candidates:
- DeepMind FSF 2.0 'Frontier Safety Framework 2.0 (1).pdf' (Wayback 20250213011843, digest UTWY...): identical to the 5 Feb 2025 file except 'Zimmerman' to 'Zimmermann'.
- DeepMind FSF 2.0 'Frontier Safety Framework 2.0.pdf' from Wayback 20250328105532 (digest CANP...): adds page 9 'Updates and changes' with correction dated 21 March 2025; provider-acknowledged non-substantive correction.
- xAI 20 Feb 2025 draft: byte change between Wayback 20250226214512 (3ORH) and 20250311152130 (4EOB), PDF ModDate 7 Mar 2025; extracted text identical.
- xAI Aug 2025 RMF: Wayback 20250821224133 (TUQE) vs 20250822181311 (CERT, current): 'AISI,' removed from page 5 list of experts; 'Last updated' line unchanged.
- xAI 30 June 2026 FAIF: server x-goog-metageneration 2, Last-Modified 10 Jul 2026; earlier generation content unknown; single Wayback capture so no comparison possible.
- Meta Frontier AI Framework: Wayback 20250213105620 (J4NA) vs 20250328093937 (45KI, regenerated 14 Mar 2025): 20 word-level changes including scope and threshold wording; both 'Version 1.1'. Full diff in log.
- Meta Advanced AI Scaling Framework v2: four CDX digests but all parseable captures are byte-identical to the live file; differing digests come from truncated captures. Not a silent version.
- HTML pages (deepmind.google, x.ai/safety, ai.meta.com blog, about.fb.com): every Wayback capture has a distinct digest because the HTML is dynamic; digest grouping is uninformative for these pages.

Limits declared by the track:
- DeepMind PDFs read only from Wayback captures (storage.googleapis.com denylisted); 'currently hosted' for DeepMind rests on live page links plus Wayback 200 captures of 28-29 Aug 2026, not a direct fetch
- x.ai and about.fb.com HTML pages read only from Wayback captures (HTTP 403 / unreachable live)
- The single Wayback capture of the 30 June 2026 xAI FAIF was not downloaded; the live file was read instead; the earlier server generation of that file could not be recovered
- Text comparisons detect wording changes only (pypdf extraction), not layout-only changes; two Meta FAF and two Meta AASF captures were truncated and could not be compared
- Which DeepMind page linked 'Frontier Safety Framework 2.0 (1).pdf', and when, not verified

### 2.4 Single-version signatories (recon_signatories.md)

| Provider | Document | Version identifier | Companion | Date (as recorded) | Hosted | Format | Document URL |
|---|---|---|---|---|---|---|---|
| Amazon | Amazon's Frontier Model Safety Framework | unversioned (single published version; file title 'PC Amazon Frontier Model Safety Framework 2.7 FINAL') | no | 2025-02-09 (amazon.science page) / 2025-02-10 (PDF CreationDate UTC, HTTP Last-Modified; METR secondary) | yes | pdf | https://cdn.amazon.science/a7/7c/8bdade5c4eda9168f3dee6434fff/pc-amazon-frontier-model-safety-framework-2-7-final-2-9.pdf |
| Microsoft | Frontier Governance Framework | Version 1 (February 2025) | no | 2025-02-08 (in-document change log '8 February 2025 – First version') / 2025-02-07 and 2025-02-11 (PDF CreationDate of the two renderings) / 2025-02-12 (HTTP Last-Modified) | yes | pdf | https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Microsoft-Frontier-Governance-Framework.pdf |
| Microsoft | Frontier Governance Framework | February 2026 (no version number in document; METR lists 'February 2026'; no provider source says 'Version 2') | no | 2026-02 (in-document 'February 2026', day not stated) / 2026-02-13 (PDF CreationDate) / 2026-03-20 (PDF ModDate) / 2026-03-24 (HTTP Last-Modified) | yes | pdf | https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/Frontier-Governance-Framework-Feb-2026.pdf |
| NVIDIA | Frontier AI Risk Assessment | unversioned (single published version; 'Applicable from August 2025') | no | 2025-02-11 (PDF CreationDate) / 2025-02-17 (HTTP Last-Modified; METR secondary 'February 17, 2025') / applicable from 2025-08 (in-document); SaferAI (secondary) 'August 2025' | yes | pdf | https://images.nvidia.com/content/pdf/NVIDIA-Frontier-AI-Risk-Assessment.pdf |
| Cohere | The Cohere Secure AI Frontier Model Framework | V1.0 (February 2025) | no | 2025-02-11 (blog datePublished) / 2025-02-07 (METR, secondary); document says 'February 2025' | yes | pdf | https://cohere.com/security/the-cohere-secure-ai-frontier-model-framework-february-2025.pdf |
| G42 | G42's Frontier AI Safety Framework | unversioned ('February 2025'; file name 'Publication_Version') | no | 2025-02-06 (g42.ai news page '06 Feb 2025' and PDF CreationDate 2025-02-06) | unknown | pdf | https://www.g42.ai/application/files/9517/3882/2182/G42_Frontier_Safety_Framework_Publication_Version.pdf |
| Naver | NAVER AI Safety Framework (ASF) | ASF (2024); no label in the June 2024 text; called 'NAVER ASF Beta' by the clova.ai Korean page and by ASF 2.0 | no | 2024-06-17 (navercorp.com story and press release) / 2024-08-07 (clova.ai Korean and English pages; METR secondary) | yes | html | https://www.navercorp.com/story/storyDetail?seq=32033 |
| Naver | NAVER AI Safety Framework (ASF) 2.0 | ASF 2.0 | no | 2026-07-07 (PDF 'Initial Publication Date: July 7, 2026'; page date 2026.07.07) / 2026-07-08 (Korean and English press releases) | yes | pdf | https://www.navercorp.com/api/article/download/c742a6dd-b5dd-4aa7-a415-93e7af6119ef |
| Magic | AGI Readiness Policy | Version 1.0 | no | 2024-07-02 (page heading 'Version 1.0 — July 2, 2024') | yes | html | https://magic.dev/agi-readiness-policy |

Not found:
- **Amazon: framework page on aws.amazon.com (aws.amazon.com/ai/responsible-ai/frontier-model-safety-framework/)**. 404 today; no Wayback captures. The framework lives on amazon.science. Sources checked:
    - https://aws.amazon.com/ai/responsible-ai/frontier-model-safety-framework/
    - https://web.archive.org/web/timemap/json?url=aws.amazon.com/ai/responsible-ai/frontier-model-safety-framework/
    - web_search: Amazon Frontier Model Safety Framework aws.amazon.com responsible AI page
- **Microsoft: HTML landing page or blog post announcing either edition of the Frontier Governance Framework**. Both PDFs are reachable only by direct CDN URL as far as this reconnaissance found. Sources checked:
    - https://www.microsoft.com/en-us/ai/responsible-ai
    - https://www.microsoft.com/en-us/ai/principles-and-approach
    - https://www.microsoft.com/en-us/corporate-responsibility/responsible-ai
    - https://www.microsoft.com/en-us/corporate-responsibility/responsible-ai-transparency-report
    - web_search x6 (queries listed in log)
- **Microsoft: a 'Version 2' label for the February 2026 edition**. Document footer reads 'February 2026 Frontier Governance Framework'; no version number. Sources checked:
    - https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/Frontier-Governance-Framework-Feb-2026.pdf
- **NVIDIA: an August 2025 revision of the Frontier AI Risk Assessment (hypothesis from SaferAI tracker)**. Current file byte-identical to the 20250224 capture, which already says 'Applicable from August 2025'. Sources checked:
    - https://images.nvidia.com/content/pdf/NVIDIA-Frontier-AI-Risk-Assessment.pdf
    - https://web.archive.org/web/timemap/json?url=images.nvidia.com/content/pdf/NVIDIA-Frontier-AI-Risk-Assessment.pdf
    - https://web.archive.org/web/timemap/json?url=images.nvidia.com/content/pdf/&matchType=prefix (filter Frontier)
    - https://www.nvidia.com/en-us/ai-trust-center/trustworthy-ai/
    - web_search: NVIDIA Frontier AI Risk Assessment August 2025 updated
- **Cohere: any version after V1.0**. Single PDF digest since 20250224. Sources checked:
    - https://cohere.com/security
    - https://cohere.com/blog/secure-model-framework
    - https://web.archive.org/web/timemap/json?url=cohere.com/security/&matchType=prefix (filter frontier)
    - web_search: Cohere Secure AI Frontier Model Framework
- **G42: any revision of the Frontier AI Safety Framework; direct confirmation of current hosting**. Single PDF capture; page text unchanged to 20260331. g42.ai blocks the sandbox. Sources checked:
    - https://www.g42.ai/resources/publications/g42-frontier-ai-safety-framework (403)
    - https://www.g42.ai/application/files/9517/3882/2182/G42_Frontier_Safety_Framework_Publication_Version.pdf (403)
    - https://web.archive.org/web/timemap/json?url=www.g42.ai/application/files/&matchType=prefix (filter Frontier)
    - https://web.archive.org/web/timemap/json?url=www.g42.ai/resources/&matchType=prefix (filter frontier-ai-safety-framework)
    - https://web.archive.org/web/timemap/json?url=www.g42.ai/resources/frontier-ai-safety-framework
- **Naver: a PDF edition of the 2024 ASF; Wayback captures of navercorp.com story/ASF 2.0/download URLs**. 2024 ASF exists only as web pages. navercorp.com query-string URLs have zero Wayback captures. Sources checked:
    - https://www.navercorp.com/story/storyDetail?seq=32033
    - https://clova.ai/tech-blog/ko-naver-ai-safety-framework-asf
    - https://clova.ai/en/tech-blog/en-navers-ai-safety-framework-asf
    - https://web.archive.org/web/timemap/json?url=www.navercorp.com/story/storyDetail?seq=32033
    - https://web.archive.org/web/timemap/json?url=www.navercorp.com/media/aiInNaver/buildingAiDetail?seq=10034455
- **Magic: any version label other than 1.0, or a provider account of the July 2024 text change**. magic.dev/safety not fetched. Sources checked:
    - https://magic.dev/agi-readiness-policy
    - https://web.archive.org/web/timemap/json?url=magic.dev/agi-readiness-policy
    - web_search: Magic AGI Readiness Policy magic.dev
- **Companion documents for any of the seven providers**. None found. Amazon's Nova Premier evaluation report (assets.amazon.science/59/0e/...) is an evaluation under the framework, not a companion policy. Sources checked:
    - provider pages and PDFs listed in the log
    - https://metr.org/fsp

Conflicts recorded:
- Amazon publication date: 2025-02-09 (amazon.science page text) vs 2025-02-10 (PDF CreationDate UTC, HTTP Last-Modified, METR).
- Microsoft v1 date: '8 February 2025' (in-document change log) vs PDF CreationDate 2025-02-07 (CSR rendering) and 2025-02-11 (current rendering) vs HTTP Last-Modified 2025-02-12 vs third-party 12 Feb 2025.
- Microsoft v1 file: two PDF renderings with different digests (PA73HQIKIMH2JXER67BTGECCGMP7G7C3 at CSR path, 20250213; FRSTQH6SVIPXZEMB46IYYPAHEHOJJNGL at microsoft-brand path, 20250226 to today); text differs by a duplicated paragraph and three typographic fixes.
- Microsoft 2026 edition identifier: document 'February 2026' (no number) vs METR 'February 2026' vs Vorp Labs (secondary) '2026 update'; no 'Version 2' anywhere. Dates: CreationDate 2026-02-13 vs ModDate 2026-03-20 vs Last-Modified 2026-03-24 vs earliest capture 2026-04-24.
- NVIDIA dates: no date in document; CreationDate 2025-02-11 vs Last-Modified/METR 2025-02-17 vs in-document 'Applicable from August 2025' vs SaferAI (secondary) 'August 2025'.
- Cohere publication date: blog 2025-02-11 vs METR (secondary) 2025-02-07; document says 'February 2025'.
- Naver 2024 ASF date: 2024-06-17 (navercorp.com story and press release) vs 2024-08-07 (clova.ai KO and EN pages; METR).
- Naver 2024 ASF identifier: no label (navercorp.com) vs 'NAVER ASF Beta' (clova.ai KO page; ASF 2.0 document and press releases).
- Naver ASF 2.0 date: 2026-07-07 (PDF 'Initial Publication Date', page) vs 2026-07-08 (press releases); PDF ModDate 2026-07-20.

Silent-version candidates:
- Microsoft FGF v1: CSR-path PDF (Wayback 20250213011748, CreationDate 2025-02-07) vs microsoft-brand PDF (Wayback 20250226161803 to today, CreationDate 2025-02-11). Same 'Version 1 (February 2025)' label; text differs (duplicated paragraph removed; 'lor' to 'low or'; 'thresh' to 'threshold'; '[8]' to '8'). Corrected re-render, not a new commitment text.
- Microsoft FGF February 2026: PDF ModDate 2026-03-20 postdates CreationDate 2026-02-13; earliest capture 20260424. A pre-20 March 2026 variant may have been served; not verified (no capture).
- Magic AGI Readiness Policy v1.0: policy body text changed between Wayback 20240710104824 and 20240720163019 (public LiveCodeBench baseline paragraph replaced: five old model scores replaced with five new ones and 'As of publishing, the best public models...' wording). Heading 'Version 1.0 — July 2, 2024' unchanged. Other 40 digest changes are boilerplate (copyright year, title string, punctuation).
- Amazon amazon.science page: 24 distinct digests 20250224 to 20260829; PDF unchanged; page-text comparison not verified (Wayback 429). Boilerplate likely.
- Cohere blog page: 11 distinct digests 20250226 to 20260412; CMS updated_at 2025-06-24; body not compared. Boilerplate likely; not verified.
- G42 publication page: 8 distinct digests 20250211 to 20260331; text compared for the first and last: only footer/copyright changed. Not a version.
- clova.ai ASF pages: EN 6 digests (20241103 to 20260829), KO 3 digests (20250426 to 20260316); earliest vs live compared: only navigation menu changed. Not a version. Whether the 'Beta' label on the KO page predates 20250426 is not verified.
- NVIDIA trustworthy-ai page: 17 digests 20250930 to 20260816; not compared (marketing page, not the framework text).
- Naver ASF 2.0 English PDF: ModDate 2026-07-20 vs stated publication 2026-07-07; no captures; not verified.

Limits declared by the track:
- Wayback CDX endpoint returned HTTP 429 throughout; the equivalent timemap endpoint was used with the same parameters, and persistent rate limiting meant some HTML-page capture comparisons (amazon.science page, Cohere blog, NVIDIA trust-center page) were not performed.
- g42.ai returned HTTP 403 to the sandbox; G42 pages and PDF were read from Wayback captures only (latest page capture 20260331, sole PDF capture 20250214), so current hosting of the G42 document is recorded as unknown, not confirmed.
- Microsoft landing page/announcement post and blogs.microsoft.com were not fetched directly (not on allowlist); only web_search and microsoft.com pages were checked.
- Magic page: 13 of 42 distinct-digest captures were fetched and compared (bisection around the one detected text change); the remaining captures were not individually inspected.
- Secondary trackers SaferAI and Vorp Labs were read only through web_search snippets, not fetched.
- Naver: bilingual comparison of the clova.ai English text against the navercorp.com Korean text was not performed; the English page is treated as a translation.

## 3. Corrections to the brief's hypotheses

| Brief hypothesis | Finding | Evidence |
|---|---|---|
| Anthropic RSP v3.1 uncertain | Exists. Effective 2 April 2026. | RSP page entry dated April 2, 2026; in-document changelog; PDF at www-cdn.anthropic.com/files/4zrzovbb/website/bf04581e4f329735fd90634f6a1962c13c0bd351.pdf |
| Anthropic RSP v1.1 uncertain | Not found. Every changelog goes v1.0 to v2.0. | 13 sources listed in 2.1 |
| Anthropic v3.0 reasoning post by Shlegeris | Post is by Holden Karnofsky (LessWrong, 24 Feb 2026, personal capacity). Anthropic's own v3.0 news post also exists. | LessWrong record; anthropic.com/news/responsible-scaling-policy-v3 |
| Anthropic FCF Dec 2025 companion | Exists (announced 19 Dec 2025). A second Trust Center resource labelled '[Feb 2026]' also exists. Neither document could be read from the sandbox. | anthropic.com/news/compliance-framework-SB53; trust.anthropic.com resource URLs |
| OpenAI PF Beta, v2 | Confirmed. v2 PDF silently re-uploaded between 15 Apr and 11 Jun 2025 (editorial text changes). | cdn.openai.com PDFs; Wayback digests |
| OpenAI FGF May 2026 replaces or supplements PF | Supplements. OpenAI: 'The PF and FGF together describe OpenAI's practices, and we will continue to use and evolve the PF'. Published 28 May 2026. | FGF PDF p.4; openai.com/index/openai-frontier-governance-framework/ |
| DeepMind FSF v1.0, v2.0, v3.0; any later? | v3.1 exists (17 April 2026, announced by editing the Sept 2025 blog post in place). v2.0 has three byte variants, one provider-acknowledged correction (21 March 2025). | FSF page; PDFs; Wayback |
| xAI draft Feb 2025 and final Aug 2025; any later? | Two different Feb 2025 drafts (10 Feb, 20 Feb). Aug 2025 RMF (two text variants). Then two documents retitled 'Frontier Artificial Intelligence Framework' (30 Dec 2025; effective 30 June 2026). No revision account anywhere. | x.ai/documents, data.x.ai, media.x.ai; Wayback |
| Meta FAF Feb 2025 and 2026 retitle | Confirmed. Cover of the 2025 PDF reads 'Version 1.1'. Silent substantive edit between 13 Feb and 28 Mar 2025 captures. 'Advanced AI Scaling Framework' Version 2 (7/8 April 2026) change log names the 2025 document as 'Initial version'. | ai.meta.com PDFs; Wayback |
| Seven single-version signatories | Microsoft has a February 2026 edition with change log. Naver has ASF 2.0 (July 2026). Magic's page text changed silently in July 2024. Others single-version. | recon_signatories.md |
| SaferAI Table 9 cites xAI draft 'Section 5.2' | The Feb 2025 drafts have no heading numbered 5.2; the red-team commitment sentence is on page 4. To be re-checked at collection. | recon_deepmind_xai_meta.md |

## 4. Judgement calls at consolidation

- **J1. Silent re-uploads with changed text are separate manifest entries.** Brief rule 6. Applied to: OpenAI PF v2 (Apr 2025 file vs Jun 2025 file); Anthropic RSP v2.0 (Oct 2024 assets.anthropic.com upload vs later file) and v2.1 (1 April 2025 files vs current); DeepMind FSF 2.0 (5 Feb, 13 Feb, 21 Mar 2025 files); xAI Aug 2025 RMF (21 Aug vs 22 Aug files); Meta FAF (13 Feb vs 28 Mar 2025 captures); Microsoft FGF v1 (CSR-path vs brand-path renderings); Magic v1.0 (pre and post 20 July 2024 page text). Each is labelled '<version> variant <letter>' with the capture timestamp in the manifest and flagged in section 6 of this log. The drift analysis may collapse editorial variants; the corpus does not.
- **J2. Byte changes with identical extracted text are not separate entries** (xAI 20 Feb draft 26 Feb vs 11 Mar 2025 files; OpenAI and Meta truncated captures). Recorded in notes only.
- **J3. OpenAI Frontier Governance Framework is a companion (is_companion = yes), not a PF version**, because OpenAI's own text says the PF continues alongside it.
- **J4. xAI's 'Frontier Artificial Intelligence Framework' documents are treated as successor versions of the RMF**, because they carry the same opening sentence and structure and x.ai/safety links them as the framework; xAI has made no statement either way. Recorded as a conflict; the retitle is flagged in the manifest notes.
- **J5. Meta's Advanced AI Scaling Framework v2 is a version of the Frontier AI Framework**, on Meta's own change log ('Renamed from Frontier AI Framework').
- **J6. Anthropic companions collected**: Frontier Compliance Framework (both Trust Center resources, if retrievable), the RSP Noncompliance Reporting and Anti-Retaliation Policy (two files), and the Frontier Safety Roadmap (HTML, first capture and current). The brief names only the FCF; the other two are separate documents Anthropic publishes alongside the RSP and are needed to check whether commitments moved. All labelled is_companion = yes.
- **J7. FCF retrieval.** The collection track will probe the Trust Center for a public download endpoint. If none works without a browser session, the FCF entries stay in the manifest with local_filename empty, retrieved_from = 'not retrieved', and a request for manual download by the author.
- **J8. Redline PDFs** (Anthropic v2.2, v3.1 to v3.4) are provider-issued tracked-change documents, i.e. a provider's own account of a revision. They are saved as revision-account material in changelogs/, not as versions.
- **J9. Multiple revision accounts per pair** are saved into one revision-account file per version with a labelled section per source (version-history entry, in-document changelog, announcement post, redline reference). The manifest's revision_account_source lists all sources.
- **J10. Announcement posts announcing a first version** (RSP v1.0, PF Beta, FSF 1.0, Cohere, Meta 2025, Naver 2024) are not revision accounts (there is no prior version). Their manifest entry reads revision_account_exists = na with the post URL in notes; a file is still written stating this.
- **J11. Dates.** publication_date takes the provider's stated effective or publication date; alternatives go in notes and date_source records which one was used. Conflicts are carried verbatim from section 2.
- **J12. Naver 2024 ASF** exists only as web pages (Korean on navercorp.com, Korean and English on clova.ai). The English clova.ai page is saved as the primary file and the two Korean pages alongside it. ASF 2.0 English PDF is primary; the Korean PDF is saved if found.
- **J13. Single-version signatories with a second version (Microsoft, Naver)**: both versions are collected and the revision account is retrieved. They may now enter the drift analysis; noted in manifest.
- **J14. HTML documents** are saved as the raw HTML served (from Wayback with the id_ flag, or live), not re-packaged with inlined assets. The brief asks for a single self-contained file; the raw page is a single file and the text extraction is what downstream work uses. Noted as a deviation from the letter of the brief.

## 5. Resolved collection list

See collection_list.json (artifact) for the machine-readable list handed to the collection tracks. Counts: see section 7 after collection.


## 6. Silent versions: prominent flag (brief rule 6)

Nine documents were found to have been served with changed text under an unchanged version label or date. Each is a separate manifest row and a separate file. The provider gave no account of any of these changes except DeepMind's 21 March 2025 link correction, which is recorded on the added 'Updates and changes' page of that file.

| Provider | Document | Manifest version | Publication date | Capture | What changed (from manifest notes) |
|---|---|---|---|---|---|
| Anthropic | Responsible Scaling Policy | v2.0-reupload-20241101 | 2024-10-15 | 20241101012028 | SILENT VARIANT of v2.0: the only extracted-text difference from the v2.0 file is the changelog line for v1.0, 'Initial version.' becoming 'Initial version, link here.' with a hyperlink to the v1.0 PDF. Captures of the assets.anthropic.com URL on 20241022154907 and 20241028110643 carry the original digest; 20241101012028 is the first capture with the new file (Wayback digest RCOS266OYENYSUELJ5Y7DZ5 |
| Anthropic | Responsible Scaling Policy | v2.1-reupload-20250402 | 2025-03-31 | live | SILENT VARIANT of v2.1: the current file (linked as 'Version 2.1' on the RSP page) differs from the 1 April 2025 file only in the table of contents on PDF page 4: page numbers for sections 3.2 to 7.2 are each one higher (e.g. '3.2. Comprehensive Assessment 5' becomes '6', '7.2. Transparency and External Input 12' becomes '13') and the line 'Changelog 17' is removed; body text is identical. Live by |
| OpenAI | Preparedness Framework | v2-reupload-20250611 | 2025-04-15 | live | SILENT VARIANT of Version 2 served at the same URL with no new label: compared with the 15 April 2025 file, 'e.g.' becomes 'e.g.,' in seven places, one en-dash becomes a hyphen, and a duplicated 'Value alignment' sentence is removed from the 'Lack of Autonomous Capability' bullet in Appendix C (verified by diffing the two text extractions; editorial only, Appendix A unchanged). Live file (170399 b |
| Google DeepMind | Frontier Safety Framework | v2.0-reupload-20250213 | 2025-02-04 | 20250213011843 | SILENT VARIANT: identical to the 5 February 2025 file except 'Roland Zimmerman' corrected to 'Roland Zimmermann' in the acknowledgements (page 8). Served under a different filename 'Frontier Safety Framework 2.0 (1).pdf' (https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/updating-the-frontier-safety-framework/Frontier%20Safety%20Framework%202.0%20(1).pdf); which DeepMind page linked  |
| Google DeepMind | Frontier Safety Framework | v2.0-reupload-20250328 | 2025-02-04 | live | SILENT VARIANT: adds a ninth page 'Updates and changes' recording 'Fixed an incorrect link to Google's AI Principles webpage (21 March 2025)' and changes the page-1 AI Principles hyperlink from https://blog.google/technology/ai/ai-principles/ to https://ai.google/responsibility/principles/; body text otherwise identical to the 13 February variant. Live file sha256 identical to Wayback capture 2025 |
| xAI | xAI Risk Management Framework | 2025-08-20-reupload-20250822 | 2025-08-20 | live | SILENT VARIANT: 'AISI,' removed from the page 5 list of external experts ('SecureBio, NIST, RAND, and EBRC'); no other text change; 'Last updated' line unchanged. Live sha256 identical to Wayback capture 20250822181311 (first capture showing it). neighbour captures before: 20250821224133 TUQEZQ47; after: 20250905165346 CERTNCX4, 20250915084821 CERTNCX4, 20250918094318 CERTNCX4. SaferAI sentence sp |
| Meta | Frontier AI Framework | v1.1-reupload-20250328 | 2025-02-03 | 20250328093937 | SILENT VARIANT: regenerated PDF (CreationDate 2025-03-14) still labelled 'Version 1.1' with 19 word-level text changes found by diff, including the scope sentence on page 4 losing 'most advanced' and 'match or' (now 'models and systems that exceed the capabilities present in the most advanced models'), 'internal' to 'closed' deployment (p7), 'catastrophic outcome' to 'threat scenario' (p17), 'risk |
| Microsoft | Frontier Governance Framework | v1-reupload-20250226 | 2025-02-08 | live | SILENT VARIANT of v1: re-rendered PDF at the microsoft-brand path in which a duplicated security paragraph ('As Microsoft operates the infrastructure ... appropriately addressed.') was removed, 'lor medium' corrected to 'low or medium', 'Capability thresh' to 'Capability threshold' (twice) and '[8] February 2025' to '8 February 2025'; version label 'Version 1 (February 2025)' and commitments uncha |
| Magic | AGI Readiness Policy | v1.0-reupload-20240720 | 2024-07-02 | 20240720163019 | SILENT VARIANT: the LiveCodeBench baseline paragraph was replaced (five scores 'GPT-4-Turbo (April 2024) – 44% ... Llama3-70B-Base – 22%' replaced by 'As of publishing, the best public models currently have the following scores' with Claude-3.5-Sonnet 48.8%, GPT-4-Turbo-2024-04-09 43.9%, GPT-4O-2024-05-13 43.4%, GPT-4-Turbo-1106 38.8%, DeepSeekCoder-V2 38.1%) while the heading 'Version 1.0 — July  |

Two further cases are recorded but not promoted to rows (J2): the xAI 20 February 2025 draft changed bytes between the 26 February and 11 March 2025 captures with identical extracted text; several Wayback captures of OpenAI, Meta and DeepMind PDFs have distinct digests because they are truncated transfers.

Unverifiable candidates: the Microsoft February 2026 PDF (ModDate five weeks after CreationDate, no capture before 24 April 2026), the Naver ASF 2.0 PDFs (ModDate after publication, no captures), and the xAI 30 June 2026 file (server object overwritten once, single capture). Whether earlier text states existed cannot be determined.

## 7. Collection results by track

Manifest: 50 rows. 48 files retrieved and hashed; 2 rows (Anthropic Frontier Compliance Framework, Dec 2025 and Feb 2026) not retrieved. Of the 50 rows: 43 framework rows and 7 companion rows; 9 silent-variant rows; 3 Korean-language renderings of Naver documents. Distinct framework versions, counting variants and renderings once: 31 (Anthropic 9, xAI 5, Google DeepMind 4, OpenAI 2, Meta 2, Microsoft 2, Naver 2, Amazon 1, Cohere 1, G42 1, NVIDIA 1, Magic 1). Retrieval source: 34 provider, 14 Wayback, 2 not retrieved.

Files: documents/ holds 48 documents and 48 text extractions; changelogs/ holds 50 revision-account files and 5 Anthropic redline PDFs; sources/ holds 45 working files the collection tracks retrieved while building revision accounts (announcement-post HTML and text, RSP page capture, x.ai/safety captures, Naver press releases). sources/ is supplementary and not referenced by the manifest; byte-identical duplicates of manifest documents were removed from it at assembly.

### 7.1 Anthropic (log_anthropic.md, appendix A)
Limits declared:
- Frontier Compliance Framework Dec 2025 and Feb 2026 documents not retrieved (Vanta Trust Center gating); their rows carry no file, hash or text, and the Feb 2026 date (2026-02-01) is provisional (month only)
- Wayback capture-history checks skipped for the Roadmap URL and the v2.2, v3.1, v3.2 redline URLs because of Wayback rate limiting (3 of 5 redlines and 1 of 2 Roadmap versions unchecked); the Roadmap first-capture timestamp relies on the reconnaissance record
- LessWrong post author taken from the GraphQL API record rather than the rendered HTML page (HTTP 429)
- Frontier Safety Roadmap archive page (/responsible-scaling-policy/updates) linked from the live Roadmap was not collected

Failures and workarounds:
- Frontier Compliance Framework (Dec 2025 and Feb 2026): not retrieved. Vanta Trust Center resource pages are JS app shells; /doc?s=<slug> endpoints return 404 for the resource slugs; the GraphQL backend requires signed requests. 10 requests used, no sign-in attempted. Rows written with local_filename empty, retrieved_from 'not retrieved', and manual-download instructions in notes.
- Wayback CDX neighbouring-capture checks not completed for the Frontier Safety Roadmap URL and the v2.2, v3.1 and v3.2 redline URLs (HTTP 429 and proxy 502 on repeated attempts). All RSP PDF URLs, the assets.anthropic.com v2.0 URL, the 080b v2.1 URL, and the v3.3/v3.4 redlines were checked before the rate limit hit.
- LessWrong HTML page returned HTTP 429; the post was retrieved via the site's GraphQL API instead (author recorded as HoldenKarnofsky from the API record, not from the rendered page).

### 7.2 OpenAI (log_openai.md, appendix B)
Limits declared:
- Announcement pages read via Wayback captures only (openai.com 403s); later captures of those pages were not diffed.
- FGF Wayback neighbour captures with differing digests (20260608044040, 20260616170613, 20260713034530) were not re-downloaded; the recon's finding that they are truncations or byte-identical transfer artefacts is relied on.
- No CDX prefix enumeration was attempted; the recon's provisional finding of no intermediate or later PF version is inherited, not re-tested.

Failures and workarounds:
- openai.com HTML returns HTTP 403 to the sandbox; the three announcement pages were read from the Wayback captures named in the recon (20231218182454, 20250416173732, 20260528180226), not live; current hosting status of the v2 and FGF posts not directly verified.
- Corrected after review: FGF revision-account section (b) initially truncated the page-20 quote before 'the PF.'; the file was rewritten with the full sentence and re-saved as version 2 (aae14712-20bb-47d1-bb4e-be4b8230adfd).

### 7.3 Google DeepMind, xAI, Meta (log_deepmind_xai_meta.md, appendix C)
Limits declared:
- Meta AASF v2 Wayback capture history beyond capture 20260408163104 not verified (CDX unreachable); manifest attributes it to recon as provisional
- Truncated Wayback captures of the Meta FAF (20250215, 20250419) and AASF (20260408173617, 20260508190541) were not downloaded; their truncated status is recon-sourced
- Which DeepMind page linked 'Frontier Safety Framework 2.0 (1).pdf', and when, not verified (carried from recon)
- The xAI announcement search relied on the recon CDX listing of x.ai/news (live 403) plus four x.ai/safety captures and two web searches; no further enumeration
- restatement.md and candidates.csv listed among the session's desired outputs were not part of this collection brief and were not produced

Failures and workarounds:
- neighbour_captures() for https://ai.meta.com/static-resource/Meta_Advanced-AI-Scaling-Framework-v2 failed: Wayback CDX unreachable through the sandbox proxy (HTTP 502) on five attempts; only capture 20260408163104 verified (sha256 identical to live); capture history for that URL is recon-sourced and provisional
- Live https://x.ai/documents/2025.02.10-RMF-Draft.pdf HTTP 404 (Wayback used)
- Live https://ai.meta.com/static-resource/meta-frontier-ai-framework/ HTTP 500 (Wayback used for both variants)
- Live x.ai/news HTTP 403 (recon CDX listing relied on for the xAI announcement search)
- Toolkit find_quote() fails on xAI PDFs because of Unicode bidi control characters and on the Aug 2025 RMF because the SaferAI sentence spans the page 7/8 break; both checks were completed with a control-character-stripped search and by reading the text across the break
- Two 60 s ReadTimeouts on Wayback CDX during DeepMind neighbour checks (retried successfully)

### 7.4 Signatories (log_signatories.md, appendix D)
Limits declared:
- Naver 2024 ASF English page saved from the live clova.ai page rather than the Wayback 20241103220646 capture; extracted text identical, bytes differ only in boilerplate; capture hash recorded in the log.
- Version slugs for the three unversioned single documents (Amazon, NVIDIA, G42) were set to the publication month '2025-02' because no other collection manifest existed to align with.
- Deliverables follow the task rules (manifest_signatories.csv, log_signatories.md) rather than the parent's generic names manifest.csv and collection_log.md; restatement.md and candidates.csv were not in this task's scope.
- Pre-publication variants of the Microsoft February 2026 PDF and the Naver ASF 2.0 PDFs (ModDate after CreationDate) could not be checked because no Wayback captures predate the files as served; presence/absence of such variants is provisional.

Failures and workarounds:
- g42.ai returned HTTP 403 for the PDF (HEAD); document taken from Wayback capture 20250214105213; currently_hosted recorded as unknown.
- Microsoft CSR-path v1 PDF URL returns HTTP 404 live; taken from Wayback capture 20250213011748.
- One Wayback CDX request (NVIDIA PDF) timed out after 60 s; retry succeeded.
- No Microsoft announcement post found for either edition of the Frontier Governance Framework (web search 2026-09-02; microsoft.com pages per reconnaissance; blogs.microsoft.com not on allowlist).
- No provider account found for Magic's July 2024 text change (page section, three Wayback captures, web search).
- No Wayback captures exist for any navercorp.com URL used, so ASF 2.0 PDFs (ModDate after publication) could not be checked against earlier states.
- Magic capture 20240720163019: local SHA-1 does not match the CDX digest (re-fetch byte-identical; attributed to content-encoding of the archived record).

### 7.5 Assembly judgement calls
- **J15. currently_hosted convention.** The field records whether the text state in that row is still served by the provider, not whether the URL is live. Magic v1.0 was changed from yes to no at assembly for consistency with the OpenAI v2 and Roadmap rows. Anthropic v2.1 (earliest file) stays yes because a text-identical copy is still served at an unlinked URL.
- **J16. Provider names** were normalised to display form (Google DeepMind, NVIDIA, xAI) in manifest.csv; the track manifests used slugs.
- **J17. Version slugs for unversioned single documents** (Amazon, NVIDIA, G42) are the publication month '2025-02'; xAI's unversioned documents use their stated dates; OpenAI's FGF uses its date. This follows the tracks' choices and is recorded here so the naming is explicable.
- **J18. Two Anthropic rows share the slug 'feb-2026'** (Frontier Compliance Framework [Feb 2026], Frontier Safety Roadmap first capture). They are different documents with different document slugs; filenames do not collide.
- **J19. SaferAI checks.** All nine applicable checks pass. I re-ran each check independently at assembly on the saved text files (control characters stripped): FSF 2.0 phrase on page 6 in all three variants; FSF 3.0 page 13; FSF 3.1 page 15; xAI drafts page 4 (and page 6); xAI Aug 2025 sentence found only when the page-7/8 break and an intervening footnote are bridged, in both variants. The 'AISI' removal between the two Aug 2025 variants is confirmed (page 5 in the 21 Aug file, absent from the 22 Aug file). SaferAI's 'Section 5.2' for the xAI draft does not correspond to any heading in either draft; the nearest headings are '2. Implementation' under 'Addressing Risks of Malicious Use'. The pass is on content, not on the section reference.
- **J20. xAI June 2026 document** contains no 'external red team' language at all (checked at assembly); the December 2025 document retains the August 2025 sentence (page 8). Recorded for the drift analysis; saferai_quote_check stays na for both.

## 8. Self-check (brief section 7)

- Every manifest row with a file has: a document file (48/48), a recomputed SHA-256 equal to the manifest value (48/48), a text extraction (48/48), a revision-account file (50/50, including the two unretrieved FCF rows).
- Every row has a revision_account_exists value: yes 22, na 18 (first versions, companions with no predecessor), no 10 (NONE files listing what was checked).
- Every SaferAI quotation check has a result: pass 9, na 41. No fail.
- Every 'not found' in sections 2 and 7 lists the sources checked.
- restatement.md was written and saved before reconnaissance began (section 0).
- Two rows are not retrieved: the Frontier Compliance Framework, Dec 2025 and Feb 2026. They need a manual download from the Trust Center URLs in their notes.

## 9. Items for the author

1. Download the two Frontier Compliance Framework PDFs from trust.anthropic.com (URLs in manifest rows 12 and 13) and add sha256 and text; the manifest rows are ready.
2. The brief's attribution of the RSP v3.0 reasoning post to Buck Shlegeris is not supported; the post is by Holden Karnofsky on LessWrong (personal capacity). Anthropic's own account is the v3.0 news post and the page entry. Both are in changelogs/anthropic_rsp_v3.0_2026-02-24_revision-account.md.
3. Four providers now have more versions than the brief assumed (Anthropic v3.1; DeepMind 3.1; xAI five documents; Microsoft and Naver second versions). Meta's 2025 PDF has a substantive silent edit (scope sentence) that the 2026 change log does not mention.
4. x.ai currently serves a Git LFS pointer instead of the 20 Feb 2025 draft PDF; its oid equals the SHA-256 of the file in this corpus.
5. Korean-language Naver renderings are in the manifest but excluded from Phase B.



---

# Appendix A. Track log: Anthropic (log_anthropic.md, verbatim)

# Collection log: Anthropic (group 'anthropic')

Date of collection: 2026-09-02. Toolkit: corpus_tools.py (fetch, fetch_wayback, cdx, pdf_to_text, html_to_text). All live fetches went to the provider's hosts; Wayback was used for variants that are no longer hosted. British spelling. Wayback CDX digests are base32 SHA-1 of the payload; where I say 'live bytes match the capture digest' I computed that digest from the downloaded file and compared it with the CDX record without downloading the capture.

## Method notes and judgement calls

- J-A. Live URL preferred. For each of the nine RSP PDFs the CDX record of the live URL (collapsed by digest) contains exactly one distinct digest, and it equals the digest of the live bytes. I therefore recorded these as retrieved_from = provider with no capture timestamp, and stated the match in notes.
- J-B. v2.0 silent variant (brief J1). The earliest capture of the original upload at assets.anthropic.com (20241022154907) has the same SHA-256 as the live www-cdn v2.0 file (cc522e27...). The re-uploaded file first appears at capture 20241101012028 (the intervening capture 20241028110643 still carries the original digest). So the live file is the original and the later assets file is the variant. Saved as v2.0 (live) and v2.0-reupload-20241101 (Wayback). Text difference: one changelog line, 'Initial version.' versus 'Initial version, link here.' (link to the v1.0 PDF).
- J-C. v2.1 silent variant (brief J1). The 1 April 2025 file (080b0037...pdf, Wayback 20250401013032) and the current file (17310f6d...pdf, first and only capture 20250402134435) differ in extracted text: on the contents page (PDF page 4) the page numbers for sections 3.2 through 7.2 are one higher in the current file, and the line 'Changelog 17' is absent from the current file. All other text is identical (22 differing lines in a normalised line diff, all on the contents page). Saved the earlier file as v2.1 and the current file as v2.1-reupload-20250402. The third 1 April file (f3b282f1...pdf, still served, unlinked) is byte-different from 080b but text-identical, so per J2 it is not a separate row; its SHA-256 is 4a22e7f0abe3da8db42a7e91ac9fb630fa3b05695e2d927874f3f1451c62093e. The 080b URL now returns HTTP 404 (66-byte JSON body). The 080b URL has two captures (20250401013032 and 20250401020540) whose CDX digests differ but whose retrieved bytes are identical (same SHA-256), presumably a transfer-encoding artefact.
- J-D. Zero-width and bidi control characters (U+200B, U+202A-U+202E) appear in the text of the Google-Docs-exported PDFs (v2.2, v3.1, v3.3, v3.4). The .txt files keep them as extracted; diffs and quoted changelog entries strip them.
- J-E. Frontier Safety Roadmap: the first capture and the live page differ substantially and the live page documents its own changes in a dated 'Updates' section, so I treated them as two documented versions (feb-2026, jul-2026), not silent variants. Version slug for the live page is 'jul-2026' with publication_date 2026-07-29 (latest dated entry on the page); the page heading says 'Our goals as of July 10th, 2026'. The archive page linked from 'here' (https://www.anthropic.com/responsible-scaling-policy/updates) was not collected (out of scope).
- J-F. Document titles: v1.0 prints 'Anthropic's Responsible Scaling Policy'; v2.0 onward print 'Responsible Scaling Policy'. Recorded as printed, with the rename noted in the v1.0 row.
- J-G. FCF dates: Dec 2025 row dated from the announcement post (Dec 19, 2025). Feb 2026 row dated 2026-02-01 because only the month is known from the Trust Center resource name; flagged provisional.
- J-H. Noncompliance Policy dates: the earlier file is dated from its file name and PDF CreationDate (2025-12-04); the later file from the RSP page entry (March 24, 2026). Neither document states a date in its body.

## RSP versions

### v1.0
- Fetched live: https://www-cdn.anthropic.com/1adf000c8f675958c2ee23805d91aaade1cd4613/responsible-scaling-policy.pdf | HTTP 200 | 527694 bytes | sha256 14785337769bee567dd488d346f9cf6e36fed7792da9656a0a8b55b2f6d21c43 | pages 22
- Wayback CDX for this URL: 1 distinct digest(s); capture(s) ['20240304173919']; live digest matches: yes (digest DLPQADEPM5MVRQXOEOAF3ENKVXQ42RQT).
- Title page:  [[page 1]]  ## Anthropic's Responsible Scaling Policy  Version 1.0 Effective September 19, 2023  As AI models become more capable, Anthropic believes that they
- Changelog: none (first version)

### v2.0
- Fetched live: https://www-cdn.anthropic.com/616dee633636e5bd309cb73aed8622e80fe47839.pdf | HTTP 200 | 336390 bytes | sha256 cc522e2770c6fec6c2808ce5abd8b757a8d7fe2078d029879295df8443185f7f | pages 22
- Wayback CDX for this URL: 1 distinct digest(s); capture(s) ['20250401073019']; live digest matches: yes (digest MFW64YZWG3S32ME4W45O3BRC5AH6I6BZ).
- Title page:  [[page 1]]  ## Responsible ## Scaling Policy  ## Effective October 15, 2024  ## Supplementary info available at www.anthropic.com/rsp-updates    [[page 2]]  ##
- Changelog: entry on PDF page(s) 21; full cumulative changelog PDF pages 21-22

### v2.1-reupload-20250402
- Fetched live: https://www-cdn.anthropic.com/17310f6d70ae5627f55313ed067afc1a762a4068.pdf | HTTP 200 | 625648 bytes | sha256 f0ac67ca61b1726cbcd159e6d2f595ce4f26de2ee29c594ba488f53f780d4ee7 | pages 22
- Wayback CDX for this URL: 1 distinct digest(s); capture(s) ['20250402134435']; live digest matches: yes (digest C4YQ63LQVZLCP5KTCPWQM6X4DJ3CUQDI).
- Title page:  [[page 1]]   ## Responsible ## Scaling Policy  ## Version 2.1  ## Effective March 31, 2025  ## Supplementary info available at www.anthropic.com/rsp-updates   
- Changelog: entry on PDF page(s) 22; full cumulative changelog PDF pages 21-22

### v2.2
- Fetched live: https://www-cdn.anthropic.com/872c653b2d0501d6ab44cf87f43e1dc4853e4d37.pdf | HTTP 200 | 342638 bytes | sha256 4807f3970c76968a75a6dffa55d8ffe547014522b63c67e261cd02f7b6fc1e39 | pages 23
- Wayback CDX for this URL: 1 distinct digest(s); capture(s) ['20250514223759']; live digest matches: yes (digest Q4WGKOZNAUA5NK2EZ6D7IPQ5YSCT4TJX).
- Title page:  [[page 1]]  ## Responsible ## Scaling Policy  ## Version 2.2  ## Effective May 14, 2025  ## Supplementary info available atwww.anthropic.com/rsp-upd
- Changelog: entry on PDF page(s) 23; full cumulative changelog PDF pages 21-23

### v3.0
- Fetched live: https://www-cdn.anthropic.com/e670587677525f28df69b59e5fb4c22cc5461a17.pdf | HTTP 200 | 473604 bytes | sha256 a71bfa08a7fa4b750b2b408b4b9c8681ad50c6b53271c314f591c59c84c38064 | pages 19
- Wayback CDX for this URL: 1 distinct digest(s); capture(s) ['20260225044800']; live digest matches: yes (digest 4ZYFQ5TXKJPSRX3JWWPF7NGCFTCUMGQX).
- Title page:  [[page 1]]   ## Responsible ## Scaling Policy  ## Version 3.0   ## Effective February 24, 2026      ## For more information, see www.anthropic.com/responsible-
- Changelog: entry on PDF page(s) 19; full cumulative changelog PDF pages 17-19

### v3.1
- Fetched live: https://www-cdn.anthropic.com/files/4zrzovbb/website/bf04581e4f329735fd90634f6a1962c13c0bd351.pdf | HTTP 200 | 268348 bytes | sha256 5aa73a3b3155ef856e429711c8d156e18d9b5ce1e28c2e0a74019a2c3c764d7b | pages 20
- Wayback CDX for this URL: 1 distinct digest(s); capture(s) ['20260407205145']; live digest matches: yes (digest X4CFQHSPGKLTL7MQMNHWUGLCYE6AXU2R).
- Title page:  [[page 1]]  ## Responsible ## Scaling Policy  ## Version 3.1  ## Effective April 2, 2026  ## For more information, seewww.anthropic.com/responsible-
- Changelog: entry on PDF page(s) 20; full cumulative changelog PDF pages 17-20

### v3.2
- Fetched live: https://cdn.sanity.io/files/4zrzovbb/website/28c6241900d90410628a8a2003a5572faae4365a.pdf | HTTP 200 | 493353 bytes | sha256 5410e3d986cf6917e9105c3d3a661ccc91bfbcb8672bca18b7752ca394e3f2a1 | pages 20
- Wayback CDX for this URL: 1 distinct digest(s); capture(s) ['20260505141510']; live digest matches: yes (digest FDDCIGIA3ECBAYUKRIQAHJKXF6VOINS2).
- Title page:  [[page 1]]   ## Responsible ## Scaling Policy  ## Version 3.2   ## Effective April 29, 2026      ## For more information, see www.anthropic.com/responsible-sca
- Changelog: entry on PDF page(s) 20; full cumulative changelog PDF pages 18-20

### v3.3
- Fetched live: https://cdn.sanity.io/files/4zrzovbb/website/c11e84981d0a7281a1b229f3fa6af0da66eaf43f.pdf | HTTP 200 | 293120 bytes | sha256 b7e7cc1e72e9371949415522ae3c9e61103cc739c5df64579af32dd941624f42 | pages 20
- Wayback CDX for this URL: 1 distinct digest(s); capture(s) ['20260528170023']; live digest matches: yes (digest YEPIJGA5BJZIDINSFHZ7U2XQ3JTOV5B7).
- Title page:  [[page 1]]  ## Responsible ## Scaling Policy  ## Version 3.3  ## Effective May 26, 2026  ## For more information, seewww.anthropic.com/responsible-s
- Changelog: entry on PDF page(s) 20; full cumulative changelog PDF pages 18-20

### v3.4
- Fetched live: https://cdn.sanity.io/files/4zrzovbb/website/0bacdc8440ea96e62a8766d99ebe1d4eea6d5f3a.pdf | HTTP 200 | 304755 bytes | sha256 6247b9e4001fd342827526fabc476c9d4dd6b2041ac00055f0ccda26f4d0b07d | pages 21
- Wayback CDX for this URL: 1 distinct digest(s); capture(s) ['20260710234036']; live digest matches: yes (digest BOWNZBCA5KLOMKUHM3MZ5PQ5J3VG2XZ2).
- Title page:  [[page 1]]  ## Responsible ## Scaling Policy  ## Version 3.4  ## Effective July 8, 2026  ## For more information, seewww.anthropic.com/responsible-s
- Changelog: entry on PDF page(s) 20; full cumulative changelog PDF pages 18-21

### v2.0-reupload-20241101 (silent variant)
- Fetched from Wayback: https://web.archive.org/web/20241101012028id_/https://assets.anthropic.com/m/24a47b00f10301cd/original/Anthropic-Responsible-Scaling-Policy-2024-10-15.pdf | HTTP 200 | 341342 bytes | sha256 22b37ecf913ea432e4c48a050a1b7fade32e155c96d7b6a9f85c2977501902f3 | capture 20241101012028.
- Earlier capture of the same URL (20241022154907): HTTP 200, 336390 bytes, sha256 cc522e2770c6fec6c2808ce5abd8b757a8d7fe2078d029879295df8443185f7f (identical to the live v2.0 file). Captures between: 20241028110643 (same digest as 20241022). The URL has 101 captures to 20260428160734; it now returns text/html (HTTP 200, 176201 bytes).
- Text diff against v2.0: 2 differing lines (see J-B).

### v2.1 (earliest file, silent-variant pair)
- Fetched from Wayback: https://web.archive.org/web/20250401013032id_/https://www-cdn.anthropic.com/080b003762c270d033dc2ea1153b9df665078da1.pdf | HTTP 200 | 627208 bytes | sha256 c239fc31d4acabba7b35437dba103fcae4c4d4b8ae25b43bdff28b63f5c40ac5 | capture 20250401013032.
- Second capture 20250401020540: same SHA-256. Live 080b URL: HTTP 404. f3b2 URL live: HTTP 200, 627152 bytes, sha256 4a22e7f0abe3da8db42a7e91ac9fb630fa3b05695e2d927874f3f1451c62093e, text identical to 080b (0 differing lines).
- Text diff 080b versus current 17310f6d: 22 differing lines, all on the contents page (see J-C).

## Revision accounts

- RSP page https://www.anthropic.com/responsible-scaling-policy fetched live: HTTP 200, 220895 bytes, sha256 389c363014e1dbb571bb0560c3c303459f1364104697dc8b171b32be27e8ea0f; page states 'Last updated Aug 14, 2026'. Dated entries present: August 14, 2026, July 8, 2026, May 26, 2026, April 29, 2026, April 2, 2026, March 24, 2026, February 24, 2026, February 10, 2026, May 14, 2025, March 31, 2025, October 15, 2024. Each version's entry copied verbatim into its revision-account file.
- In-document changelog entries copied verbatim from each PDF with PDF page and printed page numbers.
- Announcement posts fetched live (HTTP 200): v1.0 https://www.anthropic.com/news/anthropics-responsible-scaling-policy (Sep 19, 2023); v2.0 https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy (Oct 15, 2024); v3.0 https://www.anthropic.com/news/responsible-scaling-policy-v3 (Feb 24, 2026); FCF https://www.anthropic.com/news/compliance-framework-SB53 (Dec 19, 2025). Full visible text copied; 'Related content' footers dropped.
- v3.0 in-document changelog reads 'For a summary of changes and the thinking behind them, see here.' The 'see here' link annotation on PDF page 19 points to https://www.anthropic.com/news/responsible-scaling-policy-v3. The RSP page entry's 'here' points to https://anthropic.com/news/responsible-scaling-policy-v3.
- LessWrong post https://www.lesswrong.com/posts/HzKuzrKfaDJvQqmjh/responsible-scaling-policy-v3: HTML fetch returned HTTP 429; retrieved via the site's GraphQL API. Site record: user 'HoldenKarnofsky' (display name 'HoldenKarnofsky'), no coauthors, postedAt 2026-02-24T20:20:47Z. The brief's attribution to Buck Shlegeris is not supported by the site record. The post opens 'All views are my own, not Anthropic's', so it is recorded as a third-party account, not a provider account. Full text copied into the v3.0 revision-account file.
- Redline PDFs saved into changelogs/ (all HTTP 200 live from cdn.sanity.io): v2.2: 360631 bytes, sha256 3fd9544beb5c54583e249693f91c3cfe315fcda5479f34282623a0979ec4412e; v3.1: 271372 bytes, sha256 c261f86f738bc477719be1568fe7399a4d649feed9dd602ece62cb9d4b99303f; v3.2: 281517 bytes, sha256 2097ec7abacf6a6f39f58703d916e9b507ea59a48f9561a271df70ef4f6718b5; v3.3: 300484 bytes, sha256 4586970a41251128976b6fe9066b07ec4fe06fb4c7982f7cd2e08467974cfdb3; v3.4: 305618 bytes, sha256 182eb015277e7441403ddabc528e7127745710c78e2aa305f5af488856df166e.
- Redline Wayback checks: v3.3 redline has one distinct digest (capture 20260622144209) matching the live bytes; v3.4 redline has one distinct digest (capture 20260710130016) matching the live bytes; v2.2, v3.1 and v3.2 redline CDX queries failed (HTTP 429 / proxy 502) on two attempts and were not completed. The reconnaissance record gives 20250514213534 as the v2.2 redline's earliest capture.
- No announcement posts exist for v2.1, v2.2, v3.1, v3.2, v3.3, v3.4 (checked: RSP page links; reconnaissance web search). No redlines exist for v1.0 to v2.0, v2.0 to v2.1, v2.2 to v3.0.

## Companions

### RSP Noncompliance Reporting and Anti-Retaliation Policy
- 'Final 2025.12.04' file: https://www-cdn.anthropic.com/fcf136d0f2204e2184f73c6bd082bea27f2d631b/RSP%20Noncompliance%20Reporting%20and%20Anti-Retaliation%20Policy%20(Final%202025.12.04).pdf | HTTP 200 | 373298 bytes | sha256 94f403892f1461d533b31a8233b135cbc455f0f070560eb77f42272c58199075 | 8 pages | PDF CreationDate D:20251204231929Z. No date, version or changelog in the body. Not linked from the RSP page today. No Wayback capture (per reconnaissance CDX prefix query).
- March 2026 file: https://www-cdn.anthropic.com/b7a5629e40b391b2adfb4cc8c0888ac9d6bfddf6/RSP%20Noncompliance%20Reporting%20and%20Anti-Retaliation%20Policy.pdf | HTTP 200 | 251445 bytes | sha256 13eb470a35614ee286e5cc846f8776bf8b4f913555d7d7688e1810ce3c7a0782 | 9 pages | metadata title 'RSP Noncompliance Reporting and Anti-Retaliation Policy v 3.3 [REDACTED]'; body refers to RSP 'Version 3.0'. Revision account: RSP page entry of March 24, 2026 (verbatim in the file).

### Frontier Safety Roadmap
- First capture: https://web.archive.org/web/20260224225537id_/https://www.anthropic.com/responsible-scaling-policy/roadmap | HTTP 200 | 208208 bytes | sha256 bf57607b70285f4db8a5056d77f2cf81ad679c5da55cfbe100142212f638e723 | capture 20260224225537; heading 'Our goals as of February 19th, 2026'.
- Live: https://www.anthropic.com/responsible-scaling-policy/roadmap | HTTP 200 | 233195 bytes | sha256 681a531ddb31d1af523229545e0f30d2fd605f7aad2f3b50c85448dec08977f4; heading 'Our goals as of July 10th, 2026'; 'Updates' section with entries dated April 2, May 5, July 8, July 10 and July 29, 2026.
- Text diff: 43 differing lines (see J-E). Both saved.
- Neighbouring-capture check for the roadmap URL: not completed (CDX HTTP 429 / proxy 502 on three attempts).

### Frontier Compliance Framework (Dec 2025 and Feb 2026)
- Not retrieved. Bounded attempt (10 requests): (1) GET https://trust.anthropic.com/resources?s=eorilovp4wxk38nxbi7k3&name=anthropic-frontier-compliance-framework: HTTP 200, 5980 bytes, app shell for the Vanta Trust Center (title 'Anthropic Trust Center', scripts from assets.vanta.com, og:image https://app.vanta.com/doc?s=sy1uft0hltb14h4h4wwvu). (2) GET assets.vanta.com/static/index-trust-report-DZK7xX5_.js: 223966 bytes; no API routes in plain text. (3) GET assets.vanta.com/static/use-document-download-D_YhInLz.js: exposes document routes '/doc?s=<documentSlug>', '/doc?download=1&s=<documentSlug>'. (4) GET assets.vanta.com/static/resources-DckwOfmy.js: exposes '/doc/trust?rid=<resourceId>&r=<slugId>&view=true&download=true'. (5-8) GET trust.anthropic.com/doc?s=eorilovp4wxk38nxbi7k3, /doc?download=1&s=eorilovp4wxk38nxbi7k3, /doc/trust?r=eorilovp4wxk38nxbi7k3&view=true, /doc?s=gi5v45ke7aezh7b04e82s: all HTTP 404 'This document could not be found' (the resource slug is not the document slug). (9) GET assets.vanta.com/static/trust-resources-page-CCNkT6jU.js: no operation names. (10) POST trust.anthropic.com/graphql with a trivial query: HTTP 400 'Missing `signature` or `signedAt`' (signed-request gating). Stopped here; no accounts created and no gating bypassed. app.vanta.com was not requested (not on the allowlist and the same gating applies).
- Rows written with local_filename empty and retrieved_from 'not retrieved'; the Feb 2026 revision account is NONE with the sources checked.

## Failures and not-found

- LessWrong HTML page: HTTP 429 on the first attempt; content obtained via GraphQL instead. A second HTML attempt was abandoned when the cell stalled on Wayback backoff.
- Wayback CDX: proxy 502 and HTTP 429 errors from about 01:50 UTC; the roadmap URL and the v2.2, v3.1, v3.2 redline URLs could not be checked. Everything else was checked before the rate limit hit.
- Frontier Compliance Framework PDFs (both versions): not retrievable without sign-in (see above).
- No new network domains were requested.

## Dates and identifiers: conflicts carried into the manifest

- v2.0: no version number on the title page; 'Version 2.0' on the page; 'RSP-2024' and 'RSP v2.0' in changelogs.
- v2.1: effective March 31, 2025 versus first Wayback evidence 1 April 2025.
- Noncompliance Policy: file-name date 2025-12-04 versus page statement that the successor was 'released internally in February 2026' and posted March 24, 2026; metadata 'v 3.3' versus body 'Version 3.0'.
- v3.0 reasoning post authorship: brief says Buck Shlegeris; LessWrong record says HoldenKarnofsky.
- FCF Feb 2026: month-only date, provisional.


---

# Appendix B. Track log: OpenAI (log_openai.md, verbatim)

# Collection log: OpenAI (group 'openai')

Date of collection: 2 September 2026. Collector: sub-agent working from recon_openai.json (frame 653f5038). Toolkit: corpus_tools.py (fetch, fetch_wayback, neighbour_captures, pdf_to_text, html_to_text). All fetches returned HTTP 200 unless stated.

## Preparedness Framework (Beta), 2023-12-18
- Fetched live https://cdn.openai.com/openai-preparedness-framework-beta.pdf: HTTP 200, application/pdf, 27448530 bytes, sha256 c84e3a59c7dab251e45434e0b0d3e8abadcea7293f995cf92d32269e7d290398.
- Fetched Wayback capture 20231218195930 of the same URL (id_ raw): HTTP 200, 27448530 bytes, sha256 identical. Judgement: keep the live file as the collected copy (retrieved_from=provider) since bytes are identical to the earliest capture.
- Neighbour captures (CDX): none before; after: before=[]; after=[('20231218203231', 'M5QF4Z2D'), ('20231218214135', 'M5QF4Z2D'), ('20231219022320', 'M5QF4Z2D')]. All carry the single digest M5QF4Z2DYODK7GEPXCHYTDGV3RJF2NNQ. No silent variant.
- Text extraction: 27 pages. Title page reads 'December 18, 2023' then 'Preparedness Framework (Beta)'. No changelog, version-history or revision section found (searched for 'Change log', 'Version history', 'Revision').
- PDF metadata: no CreationDate or Producer embedded.
- Revision account: NA (first version). Announcement page https://openai.com/safety/preparedness fetched via Wayback 20231218182454 (HTTP 200, 93134 bytes HTML, sha256 abdc64ec73a87c4242aed51b57ae59310423eb2916545a95b92fc0f156c1bf5b); text extracted and copied verbatim into the revision-account file. The page calls the document 'the initial version' and 'the initial Beta version'. Live openai.com is HTTP 403 to the sandbox; recon states the URL now redirects to openai.com/safety/.

## Preparedness Framework, Version 2, original file, 2025-04-15
- Fetched Wayback capture 20250415191354 (id_ raw) of https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf: HTTP 200, 170525 bytes, sha256 432de80c72d039f2e93c70c481af916616676a31b867b7113f1874e5763ccac3. This is the earliest capture; the live URL no longer serves these bytes, so retrieved_from=wayback and currently_hosted=no (for these bytes; the URL itself is live).
- Neighbour captures: before=[]; after=[('20250416104253', 'XL3NESO2'), ('20250419215914', 'XL3NESO2'), ('20250423231221', 'XL3NESO2')]. No earlier capture; the three following captures share the same digest XL3NESO2Y74VJT7AMP7U32JNG2LPPK2B.
- PDF metadata: CreationDate 2025-04-15T16:32:41Z, Producer pdfTeX-1.40.26. Title page: 'Preparedness Framework / Version 2. Last updated: 15th April, 2025'. 22 PDF pages.
- Revision account (yes): (a) Appendix A 'Change log' copied verbatim from the extraction, PDF pages 15-16 (printed 14-15), twelve numbered items. (b) Announcement post 'Our updated Preparedness Framework' fetched via Wayback 20250416173732 (HTTP 200, 226732 bytes HTML, sha256 7f626b7d9dcf618cf36cce36f3ce341cc22042f8c92b3bfb6b0d973992f2cd7e); full body copied verbatim. Judgement: the html extraction duplicated the three nested bullets of the 'Sharper capability categories' item (parent list-item text already contains the nested items); the duplicates were dropped and the fact recorded in the file. Navigation header lines and footer tag words omitted. No version-history page, redline or other account found (recon sources: openai.com/safety/preparedness, openai.com/preparedness, METR /fsp).
- Identifier conflict recorded: 'Version 2' (document) vs 'v2.0' (METR) vs '2.0' (commentators). Version slug used: v2.

## Preparedness Framework, Version 2, silent re-upload (v2-reupload-20250611), publication_date 2025-04-15
- Fetched live https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf: HTTP 200, 170399 bytes, sha256 fae6e4cc6f7212a010bb9348fc0cde1fe711b9cad426c6a99db97740ee52729b.
- Fetched Wayback capture 20250611025204 (id_ raw): HTTP 200, 170399 bytes, sha256 identical. Kept the live file (retrieved_from=provider). The Wayback timestamp 20250611 dates the slug.
- Neighbour captures around 20250611025204: before=[('20250519032057', 'XL3NESO2'), ('20250602133650', 'XL3NESO2'), ('20250607005510', 'XL3NESO2')]; after=[('20250626050142', 'BAJKRRWO'), ('20250721042659', 'BAJKRRWO'), ('20250721182127', 'BAJKRRWO')]. The three earlier captures (to 20250607005510) still carry the original digest; the three later ones carry the new digest BAJKRRWOFFAB2NJKQCYAC7DKLKRTZB2Z. The swap therefore happened between 2025-06-07 and 2025-06-11, consistent with the server Last-Modified 2025-06-09 21:27:02 GMT reported by recon.
- PDF metadata: CreationDate 2025-04-28T15:11:25Z, Producer pdfTeX-1.40.26. Title page label unchanged.
- Text diff of the two extractions (difflib, line level): 21 changed lines. Changes: 'e.g.' to 'e.g.,' in seven places (pages with 'operations, e.g., those in-', 'expected access (e.g., doing finetuning', 'third party evaluations (e.g., bio wet lab', 'deployment conditions of an existing model (e.g., enabling finetuning', 'risks (e.g., biological risk)', 'across actors, e.g., rate-limits', 'filesystem (e.g., sandboxing)'); one en-dash to hyphen ('increasingly agentic – systems' to 'increasingly agentic - systems'); removal of the duplicated sentence 'Value alignment: The model consistently applies human values in novel settings (without any instructions) to avoid taking actions that cause harm, and has shown sufficiently minimal indications of misaligned behaviors like deception or scheming.' from the 'Lack of Autonomous Capability' bullet in Appendix C. This matches the recon's description exactly. Appendix A and B text (PDF pages 15-16) is identical across the two files.
- Judgement J1: text differs, so a separate manifest row and file. Judgement J2: recon's third 2026 Wayback digest for this URL was byte-identical to the current file, so it is noted, not a row. Not re-fetched here.
- Revision account: NONE. Checked the PDF (label and Appendix A unchanged; no note of a correction), the v2 announcement post (capture 20250416173732; recon checked later captures to 20260830), the FGF PDF and FGF post. Date checked 2026-09-02.

## Frontier Governance Framework, 2026-05-28 (companion)
- Fetched live https://cdn.openai.com/pdf/e37d949b-8c9f-4d76-b99e-4272f4631a7e/openai-frontier-governance-framework.pdf: HTTP 200, 6136955 bytes, sha256 33e4e118b24d56786c2292df6ed4d9ec635f8887b22986f98ce3c09896fcfffc. This equals the sha256 the recon recorded for Wayback captures 20260529171758 and 20260616170222, so retrieved_from=provider and no Wayback copy was fetched.
- Neighbour captures around 20260529171758: before=[]; after=[('20260608044040', 'T7SOI4IE'), ('20260616170613', 'JOXCCRIY'), ('20260713034530', 'DMQYYBNS')]. Digests differ from capture to capture. Recon established that 20260608044040 is a 5 MiB truncation and the others are byte-identical to the live file (transfer artefacts). Not re-verified here to limit Wayback requests; flagged in notes.
- PDF metadata: no CreationDate; Producer 'Super PDF Plugin'. No version number or date printed. 22 PDF pages. Title as printed: 'Frontier Governance Framework'.
- Judgement J3: companion, not a PF successor. The FGF (PDF p.4, printed 02) says the PF and FGF 'together describe OpenAI’s practices' and that OpenAI 'will continue to use and evolve the PF'. The announcement post says 'The Preparedness Framework remains the foundation'. Both quoted in the revision-account file and the manifest notes.
- Date: announcement page dated May 28, 2026 (Wayback capture 20260528180226, HTTP 200, 283181 bytes, sha256 ec0772c1ccf23830498980d847fb224c16d40c8baff454f35d701bedc8470b3c). Recon reports server Last-Modified 2026-05-27. publication_date set to 2026-05-28 (announcement date), conflict recorded in notes. Version slug: 2026-05-28 (unversioned document).
- Revision account: NA (first edition). Relationship passages (Sections 1, 6, 7) and the full announcement post copied verbatim under the heading 'Relationship to the Preparedness Framework (not a revision account)'.

## Failures and limitations
- openai.com HTML pages return HTTP 403 to the sandbox; all three announcement pages were read from Wayback captures (the captures named in the recon), not live. Whether the v2 post and FGF post are currently live was not verified directly; recon reports Wayback 200 captures of the v2 post to 20260830.
- No CDX prefix enumeration was attempted (rule 10); the recon's provisional finding that no intermediate or later PF version exists is inherited, not re-tested.
- The FGF Wayback neighbour captures with differing digests were not re-downloaded; the recon's finding (truncation or byte-identical) is relied on.

## Files produced
- documents/: 4 PDFs and 4 .txt extractions (see manifest).
- changelogs/: 4 revision-account .md files plus the three source HTML captures and their .txt extractions (src_openai_*_wayback.html/.txt) kept as provenance for the verbatim announcement text.
- manifest_openai.csv, log_openai.md.


---

# Appendix C. Track log: Google DeepMind, xAI, Meta (log_deepmind_xai_meta.md, verbatim)

# Collection log: Google DeepMind, xAI, Meta (group deepmind_xai_meta)

Date of collection: 2 September 2026. Toolkit: corpus_tools.py (fetch, fetch_wayback, cdx, neighbour_captures, pdf_to_text, html_to_text, find_quote). All Wayback fetches used the id_ flag. Live DeepMind files were fetched from deepmind-media.storage.googleapis.com (the storage.googleapis.com/deepmind-media/ host is denylisted); Wayback captures are of the storage.googleapis.com URLs. Fifteen manifest rows were produced for eleven recon version entries because four silent variants were saved as their own rows (J1).

## General judgement calls
- J1 applied: FSF 2.0 (three text variants), xAI RMF Aug 2025 (two), Meta FAF v1.1 (two). Each variant is its own row and file with '-reupload-YYYYMMDD' of the first Wayback capture showing it.
- J2 applied: xAI 20 Feb 2025 draft (captures 20250226214512 and 20250311152130 differ in bytes, identical text) is one row. The 12 Feb 2025 capture of the 10 Feb draft has a different CDX digest but identical sha256 to the 10 Feb capture, so it is not a variant at all.
- J4 applied: the two xAI 'Frontier Artificial Intelligence Framework' documents are treated as successor versions of the RMF (document slug faif). xAI has made no statement either way.
- J5 applied: Meta 'Advanced AI Scaling Framework' Version 2 is the successor of the 'Frontier AI Framework'; the change log says 'Renamed from "Frontier AI Framework"'.
- SaferAI quote checks: the toolkit's find_quote() does not strip Unicode bidirectional control characters (U+202A to U+202E), which the xAI PDFs contain in large numbers. A local variant of the check strips them first. Hyphen/en-dash and whitespace are normalised by the toolkit. The .txt files are left as extracted (control characters retained).
- Blog post texts are quoted as extracted by html_to_text(): navigation, header, footer and 'Related posts' blocks removed, hyperlink targets not reproduced. Datelines were read from the raw HTML and stated beside each quotation.
- publication_date for each silent variant equals the publication date of the version, as instructed.
- 'document' in the manifest is the title as printed on the document; the xAI PDFs print 'xAI Risk Management Framework' / 'xAI Frontier Artificial Intelligence Framework', and the drafts add '(Draft)'.

## Google DeepMind, Frontier Safety Framework (slug fsf)

### v1.0 (2024-05-17)
- Live: https://deepmind-media.storage.googleapis.com/DeepMind.com/Blog/introducing-the-frontier-safety-framework/fsf-technical-report.pdf: HTTP 200, 248794 bytes, sha256 3c073cd5c7a0dd03a07d0cc826fd9d5c76801f57441ac37ef6b2163e9261543d.
- Wayback: https://web.archive.org/web/20240517140902id_/https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/introducing-the-frontier-safety-framework/fsf-technical-report.pdf: HTTP 200, 248794 bytes, sha256 3c073cd5c7a0dd03a07d0cc826fd9d5c76801f57441ac37ef6b2163e9261543d, capture 20240517140902. sha256 identical to live. Saved the live file.
- neighbour captures before: none; after: 20240517141131 5CZVKYLA, 20240517201745 5CZVKYLA, 20240521161934 5CZVKYLA. Recon: single digest across 91 captures.
- Text: 7 pages; 'Version 1.0' on cover; no date in document. Date from the framework page and blog dateline (May 17, 2024).
- Revision account: NA (first version). Announcement post fetched live (HTTP 200, 142482 bytes, sha256 61f80007f75d8cef89c9553e8825febc2ceac2e72ceb3757196eeb2cf47a25c0) for the record.
- SaferAI: na.

### v2.0 (2025-02-04), three variants
- Variant A (v2.0): https://web.archive.org/web/20250205011727id_/https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/updating-the-frontier-safety-framework/Frontier%20Safety%20Framework%202.0.pdf: HTTP 200, 279970 bytes, sha256 f82534b5f9c26a700340706d8ebac7b34bbb492354465d24226bf94eb7ddd16c, capture 20250205011727. 8 pages. Cover '4th February 2025', 'Version 2.0'.
- Variant B (v2.0-reupload-20250213): https://web.archive.org/web/20250213011843id_/https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/updating-the-frontier-safety-framework/Frontier%20Safety%20Framework%202.0%20(1).pdf: HTTP 200, 279976 bytes, sha256 5d66eec33b473462d5d536674b2ef2f3ee2492ff71a2721dc2cf9fad4f4d2a84, capture 20250213011843. 8 pages. Word-level diff against A: exactly one change, 'Zimmerman,' to 'Zimmermann,' (acknowledgements, page 8). Hyperlink targets identical to A. Filename 'Frontier Safety Framework 2.0 (1).pdf'. neighbour captures before: none; after: 20250213105753 UTWYKWCP, 20250216105724 UTWYKWCP, 20250328094136 UTWYKWCP (all one digest). Which DeepMind page linked this filename, and when, is not verified (carried over from recon).
- Variant C (v2.0-reupload-20250328): live https://deepmind-media.storage.googleapis.com/DeepMind.com/Blog/updating-the-frontier-safety-framework/Frontier%20Safety%20Framework%202.0.pdf: HTTP 200, 304584 bytes, sha256 14a48e4ef052fba75b651ea23845c2e9557f5c638e2767656decc6410861aae3. Wayback 20250328105532: HTTP 200, 304584 bytes, sha256 14a48e4ef052fba75b651ea23845c2e9557f5c638e2767656decc6410861aae3, capture 20250328105532. Live sha256 identical to the 20250328105532 capture, so the live file was saved. 9 pages. Word-level diff against B: only the added page 9 'Updates and changes' (plus extraction-order noise around the page 7/8 footnote). Hyperlink diff: page-1 AI Principles link changed from https://blog.google/technology/ai/ai-principles/ to https://ai.google/responsibility/principles/, and page 9 links the v1.0 PDF. This matches the page-9 statement 'Fixed an incorrect link to Google's AI Principles webpage (21 March 2025)'.
- CDX for the main 2.0 URL (all statuses): 20250205011727 200 (7FSXTJFC); 20250205124328 404; 20250328105532 200 (CANPYOST); 20260518154755 404; 20260528082402 revisit (CANPYOST). neighbour captures before: none; after: 20250205021314 7FSXTJFC, 20250328105532 CANPYOST, 20250417020603 CANPYOST.
- No PDF CreationDate/ModDate metadata in any variant.
- Revision account (all three rows): announcement post 'Updating the Frontier Safety Framework' fetched live (HTTP 200, 142887 bytes, sha256 2fc7d543ba56a3937af55a7729a3f7b45cd5a7a016434218b7c94ee9c0ce4ba0), dateline February 4, 2025, full text quoted. Comparison with Wayback capture 20250205021259 of the /discover/blog/ URL (the deepmind.google/blog/ URL has no 200 capture before 20251105): body identical except 'Roland Zimmerman,' now reads 'Roland S. Zimmermann,'; the capture shows a byline (Allan Dafoe, Anca Dragan, Four Flynn, Helen King, Tom Lue, Lewis Ho, and Rohin Shah) that html_to_text() did not recover from the live page. The 20250328 row additionally quotes page 9 verbatim. Variants A and B contain no in-document changelog (checked).
- SaferAI: 'substantially accelerating (e.g. 2x) from 2020-2024 rates' found on page 6 in all three variants (pass). Printed with a plain hyphen in '2020-2024'.

### v3.0 (2025-09-22)
- Live: https://deepmind-media.storage.googleapis.com/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3.pdf: HTTP 200, 457871 bytes, sha256 87ebf40b747b98468226b2198442b45ff54854975f6e9882d9ece2d009082fe5. Wayback request for 20250922133155 redirected to https://web.archive.org/web/20250922134959id_/https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3.pdf: HTTP 200, 457871 bytes, sha256 87ebf40b747b98468226b2198442b45ff54854975f6e9882d9ece2d009082fe5, capture 20250922134959. sha256 identical. Saved the live file. CDX shows 20250922133155 with the same digest VJE3GZ. neighbour captures before: 20250922133155 VJE3GZLE; after: 20250922135530 VJE3GZLE, 20250923041651 VJE3GZLE, 20250923100724 VJE3GZLE.
- Cover: 'Version 3.0', 'Published: September 22, 2025'. 16 pages.
- Revision account: announcement post 'Strengthening our Frontier Safety Framework' as captured https://web.archive.org/web/20260204135940id_/https://deepmind.google/blog/strengthening-our-frontier-safety-framework/ (HTTP 200, 224111 bytes, sha256 83712901b3bce15fc253e3e10f80987f6c268e43bee34b645d2aa51236ce2a51, capture 20260204135940), dateline September 22, 2025, full text quoted. Section 5.3 'Past Updates and Changes' (page 16) quoted; it lists Version 2.0 (4 February 2025) and Version 1.0 (17 May 2024) only and contains no change description.
- Live post (HTTP 200, 144146 bytes, sha256 f9b989449bce87895e6e63d0ee0e61d04b46994c81b84405f8ef3da5c3a0c270) differs from the capture: adds 'Updated April 17, 2026', adds section 'FSF 3.1: Introducing tracked capability levels' (two paragraphs), and changes 'This latest update to our Frontier Safety Framework represents' to 'The Frontier Safety Framework represents'.
- SaferAI: 'substantially accelerating from historical rates' on page 13 (pass).

### v3.1 (2026-04-17)
- Live: https://deepmind-media.storage.googleapis.com/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3-1.pdf: HTTP 200, 447155 bytes, sha256 ad10d2d240e0d557ecad406dbccedcbb4a70295f8ba8eec46bfe01803cb9c301. Wayback: https://web.archive.org/web/20260525151112id_/https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3-1.pdf: HTTP 200, 447155 bytes, sha256 ad10d2d240e0d557ecad406dbccedcbb4a70295f8ba8eec46bfe01803cb9c301, capture 20260525151112. sha256 identical. Saved the live file. neighbour captures before: none; after: 20260616170224 XTACT2DY, 20260712154220 XTACT2DY, 20260723132341 XTACT2DY (single digest). Earliest capture is five weeks after the stated publication date; the file as it stood on 17 April 2026 is therefore not independently verified.
- Cover: 'Version 3.1', 'Published: April 17, 2026'. 20 pages.
- Revision account: section 5.3 (page 17) 'Version 3.1 (April 17, 2026)' with six sub-bullets quoted verbatim; the added blog section quoted from the live post with the 'Updated April 17, 2026' marker recorded. No separate 3.1 post exists (recon not_found; consistent with the live post's 'Related posts' list).
- Conflict recorded: secondary sources call this 'v3.0'; the PDF says 'Version 3.1'.
- SaferAI: 'substantially accelerating from historical rates' on page 15 (pass).

## xAI (slugs rmf, faif)

### draft-2025-02-10
- Wayback: https://web.archive.org/web/20250210221647id_/https://x.ai/documents/2025.02.10-RMF-Draft.pdf: HTTP 200, 190131 bytes, sha256 5ba8859b6552d5d3acc929ed22cfb7f0459deb4cf076d5d70c8cf9b9e8ee050f, capture 20250210221647. Live https://x.ai/documents/2025.02.10-RMF-Draft.pdf: HTTP 404 (text/html). Saved the Wayback file.
- neighbour captures before: none; after: 20250212084642 PTK7NOYW, 20250213011848 PTK7NOYW, 20250213105647 PTK7NOYW. The later captures have CDX digest PTK7NO versus the first capture's digest; capture 20250212084642 was downloaded (HTTP 200, 190131 bytes, sha256 5ba8859b6552d5d3acc929ed22cfb7f0459deb4cf076d5d70c8cf9b9e8ee050f, capture 20250212084642) and is byte-identical (same sha256), so the digest difference is a transfer artefact, not a content change.
- 8 pages, 'DRAFT' watermark; PDF title 'xAI Risk Management Framework (2.10.2025 Draft)'; no creation date; no date in body. Date from filename, PDF title and capture date.
- Revision account: NA (first draft). No xAI announcement located.
- SaferAI (Table 9): 'we will subject Grok to adversarially testing its safeguards utilizing both internal and qualified external red teams' found on page 4 under 'Addressing Risks of Malicious Use' / 'Implementation'. Pass. SaferAI cites 'Section 5.2'; the draft has no heading numbered 5.2 (numbered sub-headings restart within each part). Recorded as a section-number mismatch.

### draft-2025-02-20
- Live https://data.x.ai/2025.02.20-RMF-Draft.pdf: HTTP 200, 230615 bytes, sha256 89fafebb73757def5a9068105554e68799e3dcce55374a4179b7a62559b6bef9. Wayback of https://x.ai/documents/2025.02.20-RMF-Draft.pdf at 20250311152130: HTTP 200, 230615 bytes, sha256 89fafebb73757def5a9068105554e68799e3dcce55374a4179b7a62559b6bef9, capture 20250311152130. Byte-identical; saved the live file.
- Wayback 20250226214512: HTTP 200, 227316 bytes, sha256 0dd74000a037cf9e9df43bdda3b1950b91ed1bdd23a4d5d1a683fd36e1574c7d, capture 20250226214512. Text extraction identical to the live file; byte difference only (PDF ModDate 2025-03-07 in the later file; CreationDate 2025-02-21 in both). Not a separate row (J2).
- https://x.ai/documents/2025.02.20-RMF-Draft.pdf live: HTTP 200, Content-Type application/pdf, 131 bytes, body is a Git LFS pointer, not a PDF.
- neighbour captures before: 20250224201856 E5K3E7K5, 20250226214512 3ORHLATG; after: 20250320120328 4EOB2HDD, 20250403201652 4EOB2HDD, 20250426055309 4EOB2HDD. Capture 20250224201856 (810 bytes) is the LFS pointer. No captures of the data.x.ai URL exist before 20251016.
- Text differences from the 10 Feb draft (bidi characters stripped): page 2 adds ', or if such requests cover information that is already readily and easily available, including by an internet search.'; the second 'Implementation' heading is renumbered '1.' to '2.'. All other diff hits are extraction spacing.
- Date: 2025-02-20 from filename and PDF title; recon conflict (CreationDate 21 Feb, first real capture 26 Feb) recorded in the manifest date_source.
- Revision account: NONE. Checked as listed in the file.
- SaferAI: same page-4 red-team commitment, pass, same section-number mismatch.

### 2025-08-20 (two variants)
- Wayback 20250821224133: HTTP 200, 144255 bytes, sha256 31eae94d448b5b359220cbb93673e22b11adc9e27b8e8eb87e7646521f322f8a, capture 20250821224133 (variant A, saved as '2025-08-20'). Wayback 20250822181311: HTTP 200, 144214 bytes, sha256 39fab200a4b36f149c6e24ee00d3e31adc84ed59f95a734290ed80a69de73f74, capture 20250822181311. Live https://data.x.ai/2025-08-20-xai-risk-management-framework.pdf: HTTP 200, 144214 bytes, sha256 39fab200a4b36f149c6e24ee00d3e31adc84ed59f95a734290ed80a69de73f74; identical to the 20250822181311 capture; saved the live file as '2025-08-20-reupload-20250822'.
- Word-level diff A to B: one change, 'AISI,' deleted from 'SecureBio, NIST, AISI, RAND, and EBRC' (page 5). PDF CreationDate 2025-08-20 17:37 (-07:00) versus 2025-08-22 08:57 (-07:00). 'Last updated: August 20, 2025' unchanged.
- neighbour captures before: 20250821224133 TUQEZQ47; after: 20250905165346 CERTNCX4, 20250915084821 CERTNCX4, 20250918094318 CERTNCX4.
- Revision account: NONE for both rows.
- SaferAI: the sentence 'As necessities dictate, we may also provide vetted and qualified external red teams or appropriate government agencies unredacted versions.' begins on page 7 ('...we may also') and ends on page 8 ('provide vetted ... unredacted versions.') in both variants; find_quote() per page therefore returns no hit, and the pass was confirmed by reading the extracted text across the break. Pass (pages 7-8).

### faif 2025-12-30
- Live https://data.x.ai/2025-12-31-xai-frontier-artificial-intelligence-framework.pdf: HTTP 200, 251686 bytes, sha256 aa01669c19fca50c85323595141d08f98076cf0c48ed8f4a114ad6420c1a1012. Wayback 20260102171656: HTTP 200, 251686 bytes, sha256 aa01669c19fca50c85323595141d08f98076cf0c48ed8f4a114ad6420c1a1012, capture 20260102171656. Identical; saved the live file. neighbour captures before: none; after: 20260108011534 6SOPRODX, 20260213142151 6SOPRODX, 20260309074227 6SOPRODX (single digest).
- 11 pages. 'Last updated: December 30, 2025' on page 1; filename and server date say 31 December. PDF title 'xAI Frontier Artificial Intelligence Framework'.
- Revision account: NONE. The document does not mention the RMF.
- SaferAI: na; the 'vetted and qualified external red teams ... unredacted versions' sentence appears on page 8.

### faif 2026-06-30
- Live https://media.x.ai/v1/website/xai-frontier-artificial-intelligence-framework-30-june-2026-99c40684.pdf: HTTP 200, 203142 bytes, sha256 2c3c6313bd2fb6eeffcafedb38013c34d92c53331ddedbfa331821c75055df53. Wayback 20260716003429: HTTP 200, 203142 bytes, sha256 2c3c6313bd2fb6eeffcafedb38013c34d92c53331ddedbfa331821c75055df53, capture 20260716003429. Identical; saved the live file. neighbour captures before: none; after: none (only one capture exists).
- 9 pages. 'Effective Date: 30 June 2026'. PDF metadata title 'Privileged/Confidential DRAFT working FRAMEWORK DOC'. Recon: server metageneration 2, Last-Modified 10 July 2026; the earlier generation cannot be recovered.
- Revision account: NONE.
- SaferAI: na; no occurrence of 'red team' or 'unredacted' anywhere in the text.

### xAI revision-account search
- Document texts searched for 'previous version', 'prior version', 'earlier version', 'changelog', 'change log', 'revision', 'updated', 'last updated', 'supersede', 'version history', 'replace': only 'Last updated' lines and the standing 'will be continually adapted and updated' sentence.
- x.ai/safety Wayback captures 20250828090312, 20260203002028, 20260405054622, 20260815221302 fetched (HTTP 200 each); they say 'our updated Risk Management Framework', 'our updated Frontier Artificial Intelligence Framework' and 'our Frontier AI Framework' with no description of changes.
- x.ai/news: live HTTP 403; CDX listing (recon) has no framework post.
- Web search (2 September 2026): only third-party accounts (AI Lab Watch, The Midas Project, Vorp Labs, SaferAI). No xAI statement.

## Meta (slugs frontier-ai-framework, advanced-ai-scaling-framework)

### Frontier AI Framework v1.1 (2025-02-03), two variants
- Wayback 20250213105620: HTTP 200, 14652734 bytes, sha256 9fa301dfb67bf8d392abda13a2466358ffde756f14a9d55e4fe2d95f7cfecc21, capture 20250213105620 (variant A, 'v1.1'; PDF CreationDate 2025-01-31 11:57 -05:00, ModDate 2025-01-31 12:48). Wayback 20250328093937: HTTP 200, 14656123 bytes, sha256 8f88ef32bba23ea9b386231c3bf10091e73bcae17fed6a900bb0c52b98d0d58b, capture 20250328093937 (variant B, 'v1.1-reupload-20250328'; CreationDate 2025-03-14 14:04 -04:00). Live https://ai.meta.com/static-resource/meta-frontier-ai-framework/: HTTP 500.
- neighbour captures before: none; after: 20250215004405 4TI2HRRF, 20250215143054 4TI2HRRF, 20250311152132 J4NAIWWR. neighbour captures before: 20250215004405 4TI2HRRF, 20250215143054 4TI2HRRF, 20250311152132 J4NAIWWR; after: 20250406194142 45KIELWO, 20250408180041 45KIELWO, 20250419115123 HDIGW6WJ. Per recon the 20250215 (about 1 MB) and 20250419 (about 5 MB) captures are truncated files, not content variants; they were not downloaded.
- Both 21 pages, both 'Version 1.1', no date in either. Word-level wording changes A to B (control characters and glyph noise excluded), with page numbers:
- p2: 'state-of-the-art' -> 'state of the art' (context: ...innovators. We’re committed to advancing the [...] in AI, on models themselves and...)
- p3: 'biological' -> 'Biological' (context: ...two domains: Cybersecurity and Chemical & [...] risks. In this section we explain...)
- p4: 'most advanced' -> '' (context: ...AI Framework relates to our forthcoming [...] models and systems that match or...)
- p4: 'match or' -> '' (context: ...most advanced models and systems that [...] exceed the capabilities present in the...)
- p4: 'realising' -> 'realizing' (context: ...of uplift a model provides towards [...] a threat scenario. We will develop...)
- p7: 'internal' -> 'closed' (context: ...also considers the planned release (i.e. [...] deployment, limited release, or full release),...)
- p9: 'of' -> '' (context: ...GDM latter A key component of [...] our Frontier AI Framework is a...)
- p10: '' -> 'within the domains of' (context: ...most urgent catastrophic outcomes – i.e., [...] cybersecurity and chemical and biological weapons...)
- p10: 'risks' -> '' (context: ...cybersecurity and chemical and biological weapons [...] – and focus our efforts on...)
- p10: 'them' -> 'these outcomes' (context: ...and focus our efforts on avoiding [...] rather than spreading efforts across a...)
- p10: 'realise' -> 'realize' (context: ...use a frontier AI model to [...] a catastrophic outcome.5 5 We aim...)
- p11: 'realise' -> 'realize' (context: ...to note that the pathway to [...] a catastrophic outcome is often extremely...)
- p11: 'realising' -> 'realizing' (context: ...whether there are still barriers to [...] the catastrophic outcome (see Section 5.1...)
- p12: 'realising' -> 'realizing' (context: ...uplift a frontier AI provides towards [...] a threat scenario. We will develop...)
- p13: 'realising' -> 'realizing' (context: ...to determine whether other barriers to [...] the catastrophic outcome exist } If...)
- p17: 'catastrophic outcome' -> 'threat scenario' (context: ...significant uplift towards realization of a [...] we will not release the frontier...)
- p18: '' -> 'catastrophic' (context: ...our efforts to anticipate and mitigate [...] risks of catastrophic outcomes, it is...)
- p18: 'of catastrophic outcomes,' -> 'from frontier AI,' (context: ...efforts to anticipate and mitigate risks [...] it is important to emphasize that...)
- p20: 'realising' -> 'realizing' (context: ...identifies the potential causal pathways for [...] the catastrophic outcome* : Threat scenarios...)
- The diff also shows font/glyph-encoding differences in bullet characters and list markers that do not affect wording. My count of wording changes is 19 (the recon counted 20; the difference lies in how spelling changes are grouped).
- Publication date 2025-02-03 from the newsroom post (Wayback 20250203200742, time element 2025-02-03T12:00:51-08:00). The text as published on 3 February is not verified: the earliest PDF capture is 13 February.
- Revision account v1.1: NA (first version); announcement post 'Our Approach to Frontier AI' (HTTP 200, 230007 bytes, sha256 64e252196955f33b96a35ef8bdeea86940605bc680f85949795c02534f756a8b, capture 20250203200742). Live post (HTTP 200, 522450 bytes, sha256 567a8fc03c0d0481064a61b546f525641f883f6b5e1aaad53a35d6026c377162): body text identical to the February 2025 capture; a second dateline 'April 20, 2026' (2026-04-20T10:29:50-07:00) added and the 'Frontier AI Framework' link retargeted to the 2026 PDF.
- Revision account reupload: NONE (change log of the 2026 document lists only 'Initial version'; newsroom post; blog post; web search).
- SaferAI: na.

### Advanced AI Scaling Framework v2 (2026-04-07)
- Live https://ai.meta.com/static-resource/Meta_Advanced-AI-Scaling-Framework-v2: HTTP 200, 668289 bytes, sha256 d87aa9bf00456ec747e80b84216f9f2ffc427c1e98541f8b3c8f7f52c13c7b6a. Wayback 20260408163104: HTTP 200, 668289 bytes, sha256 d87aa9bf00456ec747e80b84216f9f2ffc427c1e98541f8b3c8f7f52c13c7b6a, capture 20260408163104. Identical; saved the live file.
- neighbour_captures() FAILED: the Wayback CDX endpoint became unreachable through the sandbox proxy (tunnel 502 Bad Gateway) on five attempts spread over roughly twenty minutes (three ProxyError retries, a direct diagnostic request, and a final retry returning an HTTP error), after earlier CDX calls had succeeded. The only capture verified here is 20260408163104 (downloaded; sha256 identical to live). The recon JSON reports capture 20260412083116 byte-identical to live and captures 20260408173617 and 20260508190541 truncated; I could not check those and the manifest attributes them to recon as provisional.
- 44 pages; cover 'Advanced AI Scaling Framework', 'Version 2'; change log 'v2.0'; URL '-v2'. Change-log date April 7, 2026; blog and first capture April 8, 2026. publication_date set to 2026-04-07 per the change log.
- Revision account: Appendix II Change log (page 44) verbatim; blog post 'Scaling How We Build and Test Our Most Advanced AI' (HTTP 200, 191478 bytes, sha256 130393b15339597ddeb361c2651900619675b267fba50e55b0f25282e1bfc5fd, dateline April 8, 2026) verbatim.
- SaferAI: na.

## Failures and gaps
- Wayback CDX unreachable (proxy 502) at the end of the session: neighbour_captures() for the Meta AASF URL not completed.
- Toolkit cdx() hit two ReadTimeouts (60 s) during the DeepMind neighbour checks; retried successfully.
- Live x.ai HTML (x.ai/news) returns HTTP 403; not needed beyond the recon CDX listing.
- Meta FAF live URL returns HTTP 500; both variants taken from Wayback.
- The earliest-published text of Meta FAF (3 to 13 February 2025), the 17 April 2026 state of the FSF 3.1 PDF (first capture 25 May 2026) and the first server generation of the xAI June 2026 FAIF could not be verified.
- restatement.md and candidates.csv, listed among the session's desired outputs, were not part of this collection brief and were not produced here.


---

# Appendix D. Track log: Signatories (log_signatories.md, verbatim)

# Collection log: signatories group

Date of collection: 2026-09-02. Collector: this session. Inputs: recon JSON vaba95d49_recon_sigs.json (frame 3a7f4e26), toolkit v019d4b20_corpus_tools.py.

Conventions. Files are named with make_filename(). Unversioned single documents (Amazon, NVIDIA, G42) carry the publication month as version slug ('2025-02'); no other collection manifest existed in the project to align with. SHA-1 base32 values below are computed locally for comparison with Wayback CDX digests. SaferAI quote checks are not applicable to this group (all 'na'). Wayback requests were kept to one CDX query per live PDF, one neighbour_captures() query per Wayback-sourced file, and the fetches listed. One CDX request (NVIDIA) timed out and was repeated once. Rows in manifest_signatories.csv: 14.

## Amazon: Amazon's Frontier Model Safety Framework (2025-02)

- Fetched: https://cdn.amazon.science/a7/7c/8bdade5c4eda9168f3dee6434fff/pc-amazon-frontier-model-safety-framework-2-7-final-2-9.pdf
- HTTP status: 200; bytes: 265935; SHA-256: 0628d7818d2c506df871521c6a58c83ad8e42a3322d1c942b0b69a0ec873721f
- Saved as: documents/amazon_frontier-model-safety-framework_2025-02_2025-02-09.pdf; text: documents/amazon_frontier-model-safety-framework_2025-02_2025-02-09.txt
- Revision account: changelogs/amazon_frontier-model-safety-framework_2025-02_2025-02-09_revision-account.md
- HTTP Last-Modified: Mon, 10 Feb 2025 00:35:59 GMT. PDF CreationDate D:20250210003158Z. PDF metadata title 'PC Amazon Frontier Model Safety Framework 2.7 FINAL'.
- Comparison: local SHA-1 base32 4NSNPGJAPSSG4P5LNA4YQOC4ET64LH57 equals the CDX digest for cdn.amazon.science (single capture 20260423074133) and for assets.amazon.science (single capture 20250213011856). Live bytes identical to the earliest capture; live URL used.
- Date: amazon.science page text 'This report was published on February 9, 2025.' used. Conflict with 2025-02-10 (CreationDate UTC, Last-Modified, METR) recorded in notes. Judgement: follow the provider page, per the brief.
- The page text is rendered client-side, so html_to_text() of the page returned no body; the date was read from the raw HTML.
- Revision: none published. Checked the publication page, the PDF text, CDX for both PDF hosts, and reconnaissance web search.

## Microsoft: Frontier Governance Framework v1 (CSR-path rendering)

- Fetched: https://web.archive.org/web/20250213011748id_/https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/Frontier-Governance-Framework.pdf
- HTTP status: 200; bytes: 309209; SHA-256: 56f902f1d72e20f619f68e4853c3ff45ee0e1e0a809acc218ed8cc884ca002cc; Wayback capture timestamp: 20250213011748 (requested 20250213011748; no redirect)
- Saved as: documents/microsoft_frontier-governance-framework_v1_2025-02-08.pdf; text: documents/microsoft_frontier-governance-framework_v1_2025-02-08.txt
- Revision account: changelogs/microsoft_frontier-governance-framework_v1_2025-02-08_revision-account.md
- Live status of the CSR URL today: HTTP 404 (HEAD). currently_hosted = no.
- neighbour_captures: before = none; after = 20250213105619 PA73HQIKIMH2JXER67BTGECCGMP7G7C3, 20250214143657 PA73HQIKIMH2JXER67BTGECCGMP7G7C3, 20250323121116 PA73HQIKIMH2JXER67BTGECCGMP7G7C3. Local SHA-1 base32 PA73HQIKIMH2JXER67BTGECCGMP7G7C3 equals the CDX digest; all later captures of this URL through 20250323 carry the same digest, so the CSR path never served the corrected file.
- PDF CreationDate D:20250211100853-05'00' for the re-render; D:20250207 for this rendering (per reconnaissance; not re-read here).
- Change log entry reads '[8] February 2025 – First version' in this rendering.

## Microsoft: Frontier Governance Framework v1-reupload-20250226 (microsoft-brand rendering)

- Fetched: https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Microsoft-Frontier-Governance-Framework.pdf
- HTTP status: 200; bytes: 304300; SHA-256: da0d8b1507a305fb8b5148b560d8be426549b854ca8888b999874d00e6170c4f
- Saved as: documents/microsoft_frontier-governance-framework_v1-reupload-20250226_2025-02-08.pdf; text: documents/microsoft_frontier-governance-framework_v1-reupload-20250226_2025-02-08.txt
- Revision account: changelogs/microsoft_frontier-governance-framework_v1-reupload-20250226_2025-02-08_revision-account.md
- HTTP Last-Modified: Wed, 12 Feb 2025 19:41:45 GMT. PDF CreationDate D:20250211100853-05'00'.
- Comparison: local SHA-1 base32 FRSTQH6SVIPXZEMB46IYYPAHEHOJJNGL equals the sole CDX digest (capture 20250226161803). Live bytes identical to the first capture; live URL used.
- Text diff against the CSR rendering (unified diff of non-blank extracted lines, 26 changed lines): the paragraph beginning 'As Microsoft operates the infrastructure on which its models will be trained and deployed' appeared twice in the CSR rendering and once here; 'lor medium' became 'low or medium'; 'Capability thresh' became 'Capability threshold' (two occurrences); '[8] February 2025' became '8 February 2025'. No other text changes.
- Judgement J1: saved as a separate SILENT VARIANT row because the extracted text differs. Naming per brief: v1-reupload-20250226 (first capture of the corrected file).
- Revision account: NONE. Checked the change log in both renderings (unchanged apart from the bracket), web search on 2026-09-02, and the microsoft.com pages listed by reconnaissance.

## Microsoft: Frontier Governance Framework feb-2026

- Fetched: https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/Frontier-Governance-Framework-Feb-2026.pdf
- HTTP status: 200; bytes: 831043; SHA-256: 3282e4fc65a84420f3bf1360d4716928883abce3d28b56804d0598c164111932
- Saved as: documents/microsoft_frontier-governance-framework_feb-2026_2026-02-01.pdf; text: documents/microsoft_frontier-governance-framework_feb-2026_2026-02-01.txt
- Revision account: changelogs/microsoft_frontier-governance-framework_feb-2026_2026-02-01_revision-account.md
- HTTP Last-Modified: Tue, 24 Mar 2026 09:51:00 GMT. PDF CreationDate D:20260213173212-03'00'; ModDate D:20260320151947+05'30'.
- Comparison: local SHA-1 base32 VDGBEYB3PYQUWOBETOY6FI4HE5LIMJV5 equals the sole CDX digest (capture 20260424000716). Live URL used. The secondary Vorp Labs inventory publishes SHA-256 3282e4fc65a84420f3bf1360d4716928883abce3d28b56804d0598c164111932 for this file, which matches.
- Date: publication_date 2026-02-01 with date_source 'in-document: February 2026, day not stated'. Not verified whether a variant existed before the 2026-03-20 modification; no capture predates 2026-04-24.
- Revision account: Appendix II – Change log copied verbatim from PDF page 16 (printed page 15) with pymupdf page text. Announcement post: none found. Web searches 'Microsoft Frontier Governance Framework February 2026 update' and 'Microsoft "Frontier Governance Framework" blog announcement' returned the PDF, METR's index, Vorp Labs, an unrelated Microsoft partner blog post and OpenAI's separately named Frontier Governance Framework. blogs.microsoft.com not fetched (not on the allowlist).
- J13: Microsoft has two versions (v1 and February 2026); both are hosted.

## NVIDIA: Frontier AI Risk Assessment (2025-02)

- Fetched: https://images.nvidia.com/content/pdf/NVIDIA-Frontier-AI-Risk-Assessment.pdf
- HTTP status: 200; bytes: 638458; SHA-256: 8c6aade8b0cff8797f481715cf3dc512171299790031f921c00ae60f53d0077b
- Saved as: documents/nvidia_frontier-ai-risk-assessment_2025-02_2025-02-17.pdf; text: documents/nvidia_frontier-ai-risk-assessment_2025-02_2025-02-17.txt
- Revision account: changelogs/nvidia_frontier-ai-risk-assessment_2025-02_2025-02-17_revision-account.md
- HTTP Last-Modified: Mon, 17 Feb 2025 18:46:20 GMT. PDF CreationDate D:20250211185510-08'00'. No date printed in the document; title page states 'Applicable from August 2025'.
- Comparison: local SHA-1 base32 HQFDWQDOF27ULCU5SDLCTH5KQQ5HN5I4 equals the sole CDX digest (capture 20250224223739). First CDX request timed out after 60 s; the retry succeeded.
- Date: 2025-02-17 (Last-Modified) used per the brief; CreationDate 2025-02-11 and the August 2025 applicability recorded in notes.
- Revision: none published. Checked the PDF, the trust-center page, CDX, and reconnaissance's prefix query and web search.

## Cohere: The Cohere Secure AI Frontier Model Framework V1.0

- Fetched: https://cohere.com/security/the-cohere-secure-ai-frontier-model-framework-february-2025.pdf
- HTTP status: 200; bytes: 464757; SHA-256: 9b76fb542bdacb94c62fd0e24274391baee504513ea4ee0c8ce0d93ff13eed46
- Saved as: documents/cohere_secure-ai-frontier-model-framework_v1.0_2025-02-11.pdf; text: documents/cohere_secure-ai-frontier-model-framework_v1.0_2025-02-11.txt
- Revision account: changelogs/cohere_secure-ai-frontier-model-framework_v1.0_2025-02-11_revision-account.md
- HTTP Last-Modified: Tue, 01 Sep 2026 22:52:38 GMT (a CDN value; bytes match the 2025 capture). PDF has no CreationDate.
- Comparison: local SHA-1 base32 44WAQLARJOJH2WCIQHFLSK257EQS3YBK equals the sole CDX digest (capture 20250224223911). Live URL used.
- Date: blog datePublished 2025-02-11T12:44:56-05:00 read from the raw HTML (JSON-LD). Blog body is rendered client-side; the statement 'It is the first published version and will be updated as we continue to develop new best practices to advance the safety and security of our products.' was located in the embedded page data. METR's 2025-02-07 recorded as a conflict.
- Revision: none published.

## G42: G42's Frontier AI Safety Framework (2025-02)

- Fetched: https://web.archive.org/web/20250214105213id_/https://www.g42.ai/application/files/9517/3882/2182/G42_Frontier_Safety_Framework_Publication_Version.pdf
- HTTP status: 200; bytes: 5799923; SHA-256: 36ddb6b0cc80ca7d275019c4fbd0545b51fcf875147c171eca35ccdb060a3e58; Wayback capture timestamp: 20250214105213 (requested 20250214105213; no redirect)
- Saved as: documents/g42_frontier-ai-safety-framework_2025-02_2025-02-06.pdf; text: documents/g42_frontier-ai-safety-framework_2025-02_2025-02-06.txt
- Revision account: changelogs/g42_frontier-ai-safety-framework_2025-02_2025-02-06_revision-account.md
- Live HEAD of the PDF URL: HTTP 403. currently_hosted = unknown, per the brief.
- neighbour_captures: before = none; after = 20251128113247 6P5DP6W4KVMYTPFKX4VKWQ4LVYW7TLOF, 20260204152916 6P5DP6W4KVMYTPFKX4VKWQ4LVYW7TLOF, 20260204205903 6P5DP6W4KVMYTPFKX4VKWQ4LVYW7TLOF. Local SHA-1 base32 6P5DP6W4KVMYTPFKX4VKWQ4LVYW7TLOF equals the CDX digest of the 20250214105213 capture and of the three later captures (to 20260204205903). Reconnaissance had reported a single PDF capture; three later captures now exist, all with the same digest. The file was still served unchanged on 2026-02-04.
- PDF CreationDate D:20250206055434Z. Cover prints 'February 2025'; the title is an image. Date 2025-02-06 from the g42.ai news page (Wayback 20250215005301, from reconnaissance) and CreationDate.
- Revision: none found.

## Naver: 2024 ASF, English rendering (clova.ai), slug 2024

- Fetched: https://clova.ai/en/tech-blog/en-navers-ai-safety-framework-asf
- HTTP status: 200; bytes: 79144; SHA-256: 81b60fb72ab2820fa90c260d9b0a0098830b6612e33991c4651455ed6c02aeb6
- Saved as: documents/naver_asf_2024_2024-06-17.html; text: documents/naver_asf_2024_2024-06-17.txt
- Revision account: changelogs/naver_asf_2024_2024-06-17_revision-account.md
- Wayback comparison: capture 20241103220646 fetched (SHA-256 daf4df96069dfc83d3c4280a8c31f6c45a446b8781880e9bbc7872e5e26dd7b7, 81496 bytes, local SHA-1 base32 HNLENNA4IOSOKBAO36D4WDILXQASITIU equals the CDX digest). Extracted text of the live page and the capture is identical (zero changed lines); bytes differ. Judgement: live page saved as primary (J2: byte-only difference); capture URL and timestamp recorded in notes.
- neighbour_captures: before = none; after = 20241207180357 HNLENNA4IOSOKBAO36D4WDILXQASITIU, 20250426115404 ISU7HNLTKCIZ65KENTAGWWJK7ZHELW7E, 20250808081752 3RGOA4V7RMX24RBFHK6UFRV3GW5JFBDP.
- Page dated 'Aug 7, 2024'. Publication date 2024-06-17 taken from navercorp.com, per the brief; conflict recorded.
- Revision account: NA; announcement press release seq=31855 (fetched live, HTTP 200, title '네이버, AI 안전성 실천 체계 공개…안전한 소버린 AI 생태계 구축한다', dated 2024-06-17).

## Naver: 2024 ASF, Korean rendering (navercorp.com story), slug 2024-ko-navercorp

- Fetched: https://www.navercorp.com/story/storyDetail?seq=32033
- HTTP status: 200; bytes: 224849; SHA-256: 6aeeefe81d17e684b400d1910ab3b9bef5634502b969cf06fea946f3dd04c636
- Saved as: documents/naver_asf_2024-ko-navercorp_2024-06-17.html; text: documents/naver_asf_2024-ko-navercorp_2024-06-17.txt
- Revision account: changelogs/naver_asf_2024-ko-navercorp_2024-06-17_revision-account.md
- Page date 2024.06.17 read from the raw HTML. No Wayback captures exist for this query-string URL (reconnaissance), so no capture comparison was possible.
- Title as printed: 'NAVER ASF (AI Safety Framework)'; no 'Beta' label.

## Naver: 2024 ASF, Korean rendering (clova.ai), slug 2024-ko-clova

- Fetched: https://clova.ai/tech-blog/ko-naver-ai-safety-framework-asf
- HTTP status: 200; bytes: 94586; SHA-256: ed5b53e5f1803d868bbce4b1f55c39c9fd6390b702d4caea9b859fb0b0ff640e
- Saved as: documents/naver_asf_2024-ko-clova_2024-06-17.html; text: documents/naver_asf_2024-ko-clova_2024-06-17.txt
- Revision account: changelogs/naver_asf_2024-ko-clova_2024-06-17_revision-account.md
- Page dated 'Aug 7, 2024'; text refers to 'NAVER ASF(AI Safety Framework) Beta'. Whether the 'Beta' label predates the earliest capture (20250426162747) is not verified. No Wayback request made for this page (reconnaissance already compared captures).

## Naver: ASF 2.0, English PDF, slug v2.0

- Fetched: https://www.navercorp.com/api/article/download/c742a6dd-b5dd-4aa7-a415-93e7af6119ef
- HTTP status: 200; bytes: 6431908; SHA-256: 56e5ee0dc0cf6fe358f8809db920534d5072215d111adf5d4fe1a0d2138f7496
- Saved as: documents/naver_asf_v2.0_2026-07-07.pdf; text: documents/naver_asf_v2.0_2026-07-07.txt
- Revision account: changelogs/naver_asf_v2.0_2026-07-07_revision-account.md
- No HTTP Last-Modified header. PDF CreationDate D:20260706194906+09'00'; ModDate D:20260720102619+09'00'. 14 pages. Title page: 'Initial Publication Date: July 7, 2026'.
- No Wayback captures of the download URL exist (CDX returned no rows), so no capture comparison was possible and a pre-20 July 2026 variant cannot be ruled out.
- The navercorp.com page seq=10034455 (fetched live, HTTP 200) is dated 2026.07.07 and links both PDFs.
- Revision account: section '2. The Direction of ASF 2.0' (PDF pages 4 to 5) copied verbatim with pymupdf page text; English press release seq=10034489 and Korean press release seq=10034459 copied verbatim from html_to_text() output from the headline to '(End)'/'(끝)'. The repeated headline lines produced by the responsive layout were reproduced once; this is noted in the file.
- J13: Naver has two versions (2024 ASF, ASF 2.0).

## Naver: ASF 2.0, Korean PDF, slug v2.0-ko

- Fetched: https://www.navercorp.com/api/article/download/c516533c-8aab-42ae-9ffc-81f3de71e7e1
- HTTP status: 200; bytes: 6488153; SHA-256: 6c86f799c2e3384726116fb073c49e8cd5206c547dbd9b9af354757adf1ecc44
- Saved as: documents/naver_asf_v2.0-ko_2026-07-07.pdf; text: documents/naver_asf_v2.0-ko_2026-07-07.txt
- Revision account: changelogs/naver_asf_v2.0-ko_2026-07-07_revision-account.md
- PDF CreationDate D:20260706194906+09'00'; ModDate D:20260707110836+09'00'. Title page '최초 제정일: 2026년 7월 7일'.
- Revision account: section '2. ASF 2.0의 방향성' (PDF pages 4 to 5) verbatim plus both press releases.

## Magic: AGI Readiness Policy v1.0 (Wayback 20240704164810)

- Fetched: https://web.archive.org/web/20240704164810id_/https://magic.dev/agi-readiness-policy
- HTTP status: 200; bytes: 51233; SHA-256: 0959ec36503d962d95b3ad6fcf1823d79172c794a96c6009b4648ec84202124e; Wayback capture timestamp: 20240704164810 (requested 20240704164810; no redirect)
- Saved as: documents/magic_agi-readiness-policy_v1.0_2024-07-02.html; text: documents/magic_agi-readiness-policy_v1.0_2024-07-02.txt
- Revision account: changelogs/magic_agi-readiness-policy_v1.0_2024-07-02_revision-account.md
- neighbour_captures: before = none; after = 20240710104824 GY3VXC4F424TPAT572DHL4UEWSMYLUF6, 20240720163019 NGMJGTAD6AJGPE3YTO7LOQTUSBI6QHYV, 20240808174147 PRSXLSP7WSKCXSMKVAZVU5CQ67PJZFEA. Local SHA-1 base32 LBTUB2DUZJMJKT2MCR7PQNR6ZI4PCZOS equals the CDX digest.
- Capture 20240710104824 also fetched (51233 bytes): extracted text identical to 20240704164810, so the text change occurred between 20240710104824 and 20240720163019.
- Heading 'Version 1.0 — July 2, 2024'.

## Magic: AGI Readiness Policy v1.0-reupload-20240720 (Wayback 20240720163019)

- Fetched: https://web.archive.org/web/20240720163019id_/https://magic.dev/agi-readiness-policy
- HTTP status: 200; bytes: 51670; SHA-256: e7996304e700cb5613092c34414501bedd17521a720ad7fe0dafeb51fdc8383b; Wayback capture timestamp: 20240720163019 (requested 20240720163019; no redirect)
- Saved as: documents/magic_agi-readiness-policy_v1.0-reupload-20240720_2024-07-02.html; text: documents/magic_agi-readiness-policy_v1.0-reupload-20240720_2024-07-02.txt
- Revision account: changelogs/magic_agi-readiness-policy_v1.0-reupload-20240720_2024-07-02_revision-account.md
- neighbour_captures: before = 20240704164810 LBTUB2DUZJMJKT2MCR7PQNR6ZI4PCZOS, 20240710104824 GY3VXC4F424TPAT572DHL4UEWSMYLUF6; after = 20240808174147 PRSXLSP7WSKCXSMKVAZVU5CQ67PJZFEA, 20240822123127 BXMPHUQOABLDHO5C7DFUTMSC5VSOYTTM, 20240829203910 AKLPHG7TP4RZKYHDPDMRJH3ACY2ICQYN.
- Text diff against 20240704164810 (12 changed lines): the LiveCodeBench baseline paragraph and its five model scores were replaced; nothing else changed. Judgement J1: separate SILENT VARIANT row.
- Live page fetched 2026-09-02: HTTP 200, 93579 bytes, SHA-256 7f7d0f45d2338bb5c82c77199c505250053c9a6a78a5816c2b85ac6735cda011. Extracted text identical to the 20240720163019 capture. The live page therefore matches the later text, as the brief expected.
- Digest anomaly: local SHA-1 base32 ZYPCCL6RUUSNSVPD7YXQ6ZLDDY6DEQTI does not equal the CDX digest NGMJGTAD6AJGPE3YTO7LOQTUSBI6QHYV for this capture. A second fetch returned byte-identical content (SHA-256 e7996304e700cb5613092c34414501bedd17521a720ad7fe0dafeb51fdc8383b). The mismatch is attributed to the content-encoding of the archived record; the capture timestamp and text are as reported.
- Revision account: NONE. Checked the live page's 'How We Will Update This Policy' section, three Wayback captures, magic.dev, and web search on 2026-09-02.

## Failures and not-found

- g42.ai: HTTP 403 for the PDF (HEAD). Wayback used. Current hosting unknown.
- Microsoft CSR-path v1 URL: HTTP 404 live. Wayback used.
- NVIDIA CDX: one ReadTimeout (60 s); retry succeeded.
- No Microsoft announcement post for either edition (web search 2026-09-02; reconnaissance page checks).
- No Magic account of the July 2024 text change.
- No Wayback captures for any navercorp.com URL used (story, ASF 2.0 page, both PDF downloads, press releases).
- Amazon and Cohere pages render body text client-side; dates were read from raw HTML rather than html_to_text() output.

## Deviations

- The clova.ai English 2024 ASF was saved from the live page rather than the 20241103220646 capture (text identical; bytes differ only in boilerplate). The capture was fetched and its hash is recorded above.
- Reconnaissance's finding that only one Wayback capture of the G42 PDF existed is superseded: three later same-digest captures exist.
- The parent brief's 'Desired Final Outputs' list names manifest.csv and collection_log.md; this group's files follow the task rules as manifest_signatories.csv and log_signatories.md.


## 10. Phase B: candidate commitment extraction

Run on 2 September 2026 after Phase A was complete and logged, with extract_candidates.py (saved alongside the corpus) over every non-companion row's .txt file. Output candidates.csv: 2426 rows, columns provider, document, version, section_heading, sentence_index, sentence_verbatim, modal_verbs_found.

Method, as implemented:
- Text preparation: Unicode format characters (bidi marks, soft hyphens, zero-width characters) stripped; '[[page N]]' markers removed; lines rejoined into paragraphs; line-break hyphenation repaired when the next line starts in lower case; heading lines ('## ' prefix, set by the extraction toolkit from font size for PDFs and from h1-h6 for HTML) that recur on three or more pages are treated as running headers and dropped.
- Sentence splitting: regex split after . ! ? (optionally followed by a closing quote or bracket) when the next token starts with a capital, digit or opening quote; abbreviations (e.g., i.e., etc., U.S., No., Fig., month abbreviations), decimals and version numbers (2.1) and initials are protected. sentence_index counts every sentence in the document, not only candidates, so a candidate can be located.
- Operational test, applied literally per the brief: the sentence contains a provider-as-actor term (we, our, us, ourselves, the company, the Board, CEO, or the provider's name and named internal roles: Responsible Scaling Officer, LTBT, Safety Advisory Group, Frontier Safety team, etc.) AND a listed modal or commitment verb (will, must, commit*, shall, intend*, aim*, expect*, may, could, consider*, plan*). Conditional forms are included by construction. Sentences under 15 characters are dropped. modal_verbs_found lists the distinct matched forms.
- No classification, judgement or paraphrase. The brief's exclusion of sentences that describe the risk landscape, define terms or state other parties' obligations was NOT applied mechanically, because doing so needs judgement; such sentences remain in the list when they satisfy the operational test (over-inclusion accepted by the brief).
- section_heading is the nearest preceding detected heading. Heading detection is a font-size heuristic for PDFs and failed for the NVIDIA document (every candidate reads 'Abstract') and partly for others (a few candidates fall under 'Contents' or a changelog date heading). Treat section_heading as a locator, not a classifier.
- Excluded: the 7 companion rows (is_companion = yes) and the 3 Korean-language Naver renderings (English-only modal list). Silent-variant rows are included, so near-duplicate candidate sets exist for the nine variant pairs; downstream work may collapse them by version.

Candidates per document (candidates / sentences):
- Anthropic v1.0: 93 candidates / 459 sentences
- Anthropic v2.0: 123 candidates / 499 sentences
- Anthropic v2.0-reupload-20241101: 122 candidates / 500 sentences
- Anthropic v2.1: 126 candidates / 516 sentences
- Anthropic v2.1-reupload-20250402: 126 candidates / 515 sentences
- Anthropic v2.2: 117 candidates / 502 sentences
- Anthropic v3.0: 128 candidates / 401 sentences
- Anthropic v3.1: 130 candidates / 418 sentences
- Anthropic v3.2: 133 candidates / 439 sentences
- Anthropic v3.3: 131 candidates / 436 sentences
- Anthropic v3.4: 136 candidates / 457 sentences
- OpenAI beta: 47 candidates / 542 sentences
- OpenAI v2: 71 candidates / 474 sentences
- OpenAI v2-reupload-20250611: 71 candidates / 473 sentences
- Google DeepMind v1.0: 22 candidates / 143 sentences
- Google DeepMind v2.0: 36 candidates / 173 sentences
- Google DeepMind v2.0-reupload-20250213: 36 candidates / 173 sentences
- Google DeepMind v2.0-reupload-20250328: 36 candidates / 179 sentences
- Google DeepMind v3.0: 50 candidates / 258 sentences
- Google DeepMind v3.1: 65 candidates / 340 sentences
- xAI draft-2025-02-10: 30 candidates / 144 sentences
- xAI draft-2025-02-20: 30 candidates / 161 sentences
- xAI 2025-08-20: 31 candidates / 147 sentences
- xAI 2025-08-20-reupload-20250822: 31 candidates / 147 sentences
- xAI 2025-12-30: 34 candidates / 157 sentences
- xAI 2026-06-30: 33 candidates / 124 sentences
- Meta v1.1: 44 candidates / 367 sentences
- Meta v1.1-reupload-20250328: 44 candidates / 373 sentences
- Meta v2: 107 candidates / 600 sentences
- Amazon 2025-02: 22 candidates / 202 sentences
- Microsoft v1: 22 candidates / 240 sentences
- Microsoft v1-reupload-20250226: 21 candidates / 239 sentences
- Microsoft feb-2026: 21 candidates / 270 sentences
- NVIDIA 2025-02: 9 candidates / 313 sentences
- Cohere v1.0: 17 candidates / 259 sentences
- G42 2025-02: 38 candidates / 197 sentences
- Naver 2024: 5 candidates / 50 sentences
- Naver 2024-ko-navercorp: skipped: Korean-language rendering
- Naver 2024-ko-clova: skipped: Korean-language rendering
- Naver v2.0: 18 candidates / 299 sentences
- Naver v2.0-ko: skipped: Korean-language rendering
- Magic v1.0: 35 candidates / 72 sentences
- Magic v1.0-reupload-20240720: 35 candidates / 72 sentences

Known noise: table-of-contents lines and table cells that happen to contain 'we ... will'; footnote text merged into the sentence it interrupts; occasional missing space where a line break fell after a colon ('Long Term Benefit Trust:We will'). Recall was checked on the xAI drafts (the SaferAI red-team sentence is captured) and by sampling Anthropic v3.4, Meta v2 and NVIDIA; no systematic omission found, but no exhaustive recall audit was done.
