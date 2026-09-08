# Tracing log

First-pass coding of commitments across twelve framework version pairs, 2 September 2026. Codebook v0.1; brief 'first-pass tracing of commitments across framework version pairs'. Coder: first-pass (automated), for human adjudication. British spelling in the log's own prose; quotations are verbatim.

## 0. Order of work and method

1. restatement2.md was written and saved (artifact versions 01ed0dfc..., then 3df29e5a... after a word-count trim) before any tracing began.
2. For each pair an input bundle was built from the corpus: the two version text files (Unicode format characters stripped, otherwise the corpus .txt), the candidates.csv rows for both versions, and the revision-account file for v_next. Bundles are artifacts named '{pair}_v_i.txt', '{pair}_v_next.txt', '{pair}_candidates_v_i.csv', '{pair}_candidates_v_next.csv', '{pair}_revision_account.md'.
3. The twelve pairs were coded in eight parallel tracks (ANT-1; ANT-2; OAI-1; GDM-1 and GDM-2 in chain; META-1; MSFT-1; NAV-1; XAI-1 to XAI-4 in chain), each with the codebook, the brief, its bundle and the same written procedure. Each track wrote its own pair log as it coded; those logs are reproduced verbatim in section 2 in the brief's pair order. Per-pair conventions therefore differ in places; section 1.3 lists the differences an adjudicator should harmonise.
4. Every quoted field (v_i_text, v_next_text, changelog_pointer) was checked mechanically against the bundle text files with verify_rows.py (whitespace-, quote- and dash-insensitive substring match; a shingle fallback for sentences interrupted by a page break or footnote in the text file). Each track ran it before saving; I re-ran it independently on the merged file (section 1.1).
5. Silent variants (section 3) and disclosure regimes (section 4) were coded by me from word-level diffs and the changelogs/ files.

## 1. Assembly

### 1.1 Verification of quotations
Merged file tracing.csv: 710 rows, 18 columns as specified. Independent re-run of the verifier on all 710 rows x 3 fields (2,130 checks; locator prefixes such as '[changelog item 4]' or '[post]' stripped before matching): v_i_text 527 ok, 9 ok-fuzzy, 174 literal (NONE); v_next_text 639 ok, 13 ok-fuzzy, 58 literal (NONE); changelog_pointer 133 ok, 1 ok-fuzzy, 576 literal (NONE FOUND or NA). Zero NOT FOUND. All 22 ok-fuzzy quotations are sentences that a page break, running header or footnote interrupts in the text file, and each row's flags say so; the one fuzzy pointer (OAI-1-014) is two verbatim changelog segments joined with an ellipsis. Field validation: every row has an outcome in R/S/W/X/L/A, material yes/no consistent with the outcome, announcement in ANN/SIL/NCL/NA (NA only on R rows, NCL only on xAI rows), a pointer or NONE FOUND on every SIL/ANN row, NONE in v_i_text on A rows and in v_next_text on X rows, a category, a confidence grade and a rationale.

### 1.2 Counts
| Pair | Rows | v_i commitments | Material | ANN | SIL | NCL | Low confidence |
|---|---|---|---|---|---|---|---|
| ANT-1 | 95 | 73 | 75 | 33 | 42 | 0 | 8 |
| ANT-2 | 95 | 69 | 86 | 29 | 57 | 0 | 21 |
| OAI-1 | 51 | 41 | 41 | 16 | 25 | 0 | 10 |
| GDM-1 | 42 | 33 | 30 | 8 | 22 | 0 | 7 |
| GDM-2 | 50 | 39 | 27 | 12 | 15 | 0 | 5 |
| META-1 | 106 | 49 | 80 | 25 | 55 | 0 | 20 |
| MSFT-1 | 48 | 40 | 21 | 5 | 16 | 0 | 8 |
| NAV-1 | 26 | 17 | 22 | 6 | 16 | 0 | 10 |
| XAI-1 | 42 | 42 | 1 | 0 | 0 | 1 | 6 |
| XAI-2 | 49 | 42 | 35 | 0 | 0 | 35 | 13 |
| XAI-3 | 48 | 43 | 8 | 0 | 0 | 8 | 2 |
| XAI-4 | 58 | 48 | 45 | 0 | 0 | 45 | 10 |

Outcomes by pair:
| Pair | R | S | W | X | L | A |
|---|---|---|---|---|---|---|
| ANT-1 | 20 | 11 | 36 | 6 | 0 | 22 |
| ANT-2 | 9 | 3 | 30 | 24 | 3 | 26 |
| OAI-1 | 10 | 2 | 26 | 3 | 0 | 10 |
| GDM-1 | 12 | 6 | 12 | 3 | 0 | 9 |
| GDM-2 | 23 | 9 | 6 | 1 | 0 | 11 |
| META-1 | 26 | 12 | 9 | 2 | 0 | 57 |
| MSFT-1 | 27 | 4 | 8 | 1 | 0 | 8 |
| NAV-1 | 4 | 3 | 7 | 3 | 0 | 9 |
| XAI-1 | 41 | 0 | 1 | 0 | 0 | 0 |
| XAI-2 | 14 | 9 | 16 | 3 | 0 | 7 |
| XAI-3 | 40 | 2 | 1 | 0 | 0 | 5 |
| XAI-4 | 13 | 8 | 15 | 12 | 0 | 10 |

Pooled outcomes: R 239, A 174, W 167, S 69, X 58, L 3. Categories: G 148, M 124, EC3 99, EC2 92, EC6 71, EC5 68, S 47, EC1 31, EC4 30. Low-confidence rows: 120.

Silent revision rate by stratum (material rows with an ANN or SIL code; xAI pairs excluded because SRR is undefined without an account). These are first-pass figures for orientation only; they will move under adjudication.
| Pair | Evidentiary material | Evidentiary SIL | Evidentiary SRR | Non-evidentiary material | Non-evidentiary SIL | Non-evidentiary SRR |
|---|---|---|---|---|---|---|
| ANT-1 | 35 | 19 | 0.54 | 40 | 23 | 0.57 |
| ANT-2 | 59 | 33 | 0.56 | 27 | 24 | 0.89 |
| OAI-1 | 32 | 18 | 0.56 | 9 | 7 | 0.78 |
| GDM-1 | 20 | 14 | 0.7 | 10 | 8 | 0.8 |
| GDM-2 | 19 | 10 | 0.53 | 8 | 5 | 0.62 |
| META-1 | 62 | 42 | 0.68 | 18 | 13 | 0.72 |
| MSFT-1 | 13 | 9 | 0.69 | 8 | 7 | 0.88 |
| NAV-1 | 17 | 13 | 0.76 | 5 | 3 | 0.6 |
Pooled: evidentiary 158/257 = 0.61; non-evidentiary 90/125 = 0.72.

### 1.3 Cross-pair conventions the adjudicator should harmonise
- **Present-tense practice statements** ('we conduct', 'xAI utilizes', 'is run'). The codebook's include rule lists modal forms only. Every track met this and every track included such statements when they name a specific procedure or object, dropping bare descriptions. The xAI track adopted the convention that present indicative is not below 'will' on the modal scale (so 'we will allow' to 'we allow' is R); the Microsoft and Naver logs record the same reading as unsettled. A codebook rule is needed; the choice affects a large share of rows (Microsoft: 24 of 40 v_i rows; xAI: many rows).
- **Loss of specificity** (calibration example G versus 'changes to examples that do not alter the rule'). Tracks ANT-1, GDM, xAI and NAV-1 each record this tension; most coded W on dim 1 or 2 where a named method, benchmark or quantity disappears, with R as the alternative. Rows citing example F or G in flags are the set to review together.
- **Both-directions rows** are coded W per codebook section 4 in every track, with the strengthening side in the rationale. Several logs (ANT-2, OAI-1, MSFT-1, xAI) note S as the alternative and that reviewers may see W as harsh where strengthening dominates.
- **Class-level changelog lines** ('content requirements', 'clarified which actors are in scope', 'more outcome-focused safeguard requirements'). Tracks ANT-1, META-1 and MSFT-1 coded ANN only where the line points at the specific commitment and direction; where it points at the commitment without a direction they coded SIL with the alternative flagged.
- **Calibration example I** is attached to an existing consequence row in OAI-1 (027) and GDM-1 (015, EC3 rather than EC6) and to a new A row in MSFT-1 (048), with alternatives flagged in each.
- **Companion documents.** 6 rows carry a 'companion' flag (Anthropic FCF, OpenAI FGF or Model Spec). They are coded X or W with low confidence pending the author's check; the FCF is not in the corpus.
- **LessWrong post (ANT-2).** 7 rows carry an 'LW-only' flag: the Karnofsky post alone would identify the change. They are coded SIL because the post is not a provider account; the author may decide otherwise.
- **v3.0 Introduction (ANT-2).** The v3.0 text itself contains change language ('we have removed', 'we now ...') outside the designated revision account. The ANT-2 track did not count it as an account; if counted, several SIL threshold-structure rows become ANN (see the ANT-2 log).
- **xAI chains.** XAI-2's example D was verified with a correction: the replacement sentence SaferAI quotes is a separate disclosure row (XAI-2-025); the safeguard-testing commitment itself traces to 'we continually evaluate and improve robustness to adversarial attacks' (XAI-2-014, W dim 3). The external red-team commitment is retained in XAI-3 and removed in XAI-4 (XAI-4-029, X).

### 1.4 Deviations declared by tracks
- GDM: n_merged for GDM-2 counts candidate rows folded into another candidate's row; example I coded on the safety-case row (EC3) rather than a separate EC6 row, alternative flagged.
- NAV-1: verifier run with the '[press release]' prefix stripped (the prefix was my instruction).
- All other tracks declared none.


---

# 2. Pair logs (verbatim, in the brief's order)


## 2.1 ANT-1

# ANT-1 tracing log: Anthropic Responsible Scaling Policy v1.0 (19 Sep 2023) to v2.0 (15 Oct 2024)

First-pass coder output. Every row is a proposal for adjudication. Codebook v0.1 sections 2 to 6 applied; British spelling in coder prose; quotations verbatim from the text files.

## 1. Inputs

- v_i text: ANT-1_v_i.txt (RSP v1.0, 22 PDF pages, 10,600 words).
- v_next text: anthropic_rsp_v2.0_2024-10-15.txt (27 PDF pages, 9,587 words).
- Candidates: 93 rows for v1.0, 123 rows for v2.0 (recall-oriented extractor).
- Revision account: in-document changelog (v2.0 pages 17-18) plus the saved revision-account file (RSP-page entry of 15 Oct 2024, changelog copy, announcement post). Prefixes [changelog], [post], [page entry] mark the source in changelog_pointer.

## 2. Candidate screening (v1.0 side)

| quantity | count |
|---|---|
| candidates for v1.0 | 93 |
| kept (used in a row, alone or merged) | 67 |
| dropped | 26 |
| merged into another candidate's row | 29 |
| splits (one v1.0 passage giving two or more rows) | 3 |
| v1.0 commitments added from the full text (no candidate) | 35 |
| v1.0-side rows (traced commitments) | 73 |
| v2.0-side addition rows (A) | 22 (7 with no v2.0 candidate) |
| total rows | 95 |

Dropped candidates by reason class:

- description / preamble: 12 (candidate indices 0, 1, 2, 3, 5, 8, 11, 18, 19, 43, 44, 68)
- description of scheme, duplicated by detailed rows: 3 (candidate indices 12, 13, 20)
- aspirational (ASL-4 'early guess', investment framing): 3 (candidate indices 24, 69, 70)
- definition: 1 (candidate indices 26)
- cross-reference to external commitments (unsettled, see U1): 1 (candidate indices 28)
- task text, not a commitment: 5 (candidate indices 78, 79, 80, 81, 82)
- report / status statement, not a commitment: 1 (candidate indices 88)

Splits: (a) v1.0 'T&S tooling' bullet gives ANT-1-020 (detection tooling) and ANT-1-021 (fine-tuning protections); (b) v1.0 'Automated detection' bullet gives ANT-1-042 (classifiers), 043 (law enforcement) and 044 (30-day retention); (c) v1.0 procedural commitment 7 gives ANT-1-055 (RSO position) and 056 (quarterly report).

Main merges: 002 (candidates 6, 7, 14, 15, 36 and response step 2b); 003 (9, 10, 17, procedural 1); 005 (16, 55, 64, 65, response step 2); 006 (21, 25, 83); 007 (22, 23, 90); 025 (ASL-3 definition sentence, Evaluation Protocol 'best capabilities elicitation' clause, appendix Elicitation bullet); 026 (ARA threshold, 50% rule, 1-in-10 rule, 2-8 hour calibration); 027 (31, 32, 84); 058 (53, 54, 55, 'conservative warning signs'); 069 (73, 74, 75, 76); 072 (85, 86, 87).

Added from the full text (35 v1.0 rows): six ASL-2 security bullets (008 to 013); six ASL-2 deployment bullets under the lead-in candidate 27 (016 to 021, with 016 credited to the lead-in); ASL-3 threshold, cyber, elicitation and harmlessness rows (023, 024, 025, 028); internal compartmentalisation (030); eight ASL-3 security bullets (031 to 038); ASL-3 deployment bullets whose subject is a measure rather than 'we' (039, 041, 042, 043, 046, 047); procedural items 3, 5, 6 (051, 053, 054); appendix evaluation-detail bullets (068, 071). The extractor missed most bullet-list items whose grammatical subject is the measure ('Model cards: Publish ...') and most 'should/must' security bullets.

v2.0 side: 22 A rows. Fifteen draw on v2.0 candidates (32, 34-37, 49, 50, 54, 57, 58, 65, 81, 90, 92-95, 101, 102, 109, 110); seven were added from the full text (077, 081, 082, 083, 085, 086, 092). v2.0 candidates from the Executive Summary and Introduction were treated as duplicates of the section text; v2.0 candidates 114 to 122 are changelog text, not commitments.

## 3. Cases the codebook did not settle

- U1. Candidate 28 ('White House voluntary commitments ... which we also continue to maintain'): the codebook does not say whether a statement that the developer maintains commitments made in another document is a framework commitment. Dropped as a cross-reference; alternative is an M row traced to v2.0 'This policy also helps satisfy our Voluntary White House Commitments (2023)' with outcome R or W (dim 4).
- U2. Class-level changelog lines. The v2.0 changelog line 'More outcome-focused safeguard requirements ... Rather than detailing specific operational and technical safeguards, we now specify the overall security or deployment standards' identifies the whole class of ASL-3 safeguard specifics and the direction (less prescriptive) but names no single measure. Codebook section 6 requires that the account 'point at the commitment'. Rule applied here: W rows whose v1.0 measure was generalised into a 4.1 or 4.2 criterion are ANN on this line (ANT-1-031 to 035, 037, 038, 040 to 044) with the flag 'class-level'; X rows with no surviving analogue (030, 036, 047) are SIL; A rows that are new 4.1/4.2 criteria (082 to 086) are SIL with alternative ANN. If the adjudicator rules the class-level line insufficient, 12 rows move from ANN to SIL.
- U3. ANT-1-029 (ASL-3 security threat actors). The changelog line 'We have clarified which actors are in and out of scope for the ASL-3 Security Standard' points at the commitment but gives no direction; the v2.0 text removes the requirement that 'advanced threat actors (e.g. states) cannot steal them without significant expense'. Coded SIL, low confidence; alternative ANN.
- U4. ANT-1-001, 005, 062, 064, 065 (pause / interim measures). Whether v2.0 section 6.2 interim measures 'that provide the same level of assurance' change the consequence of an unmet standard (W) or restate the same commitment with an implementation route (R) is not settled by codebook section 5. Coded W on dim 6 with alternatives stated. The changelog asserts the commitment is maintained, which supports SIL either way.
- U5. ANT-1-022 (tooling exception footnote). The exception moves from the T&S classifier (v1.0 footnote 6) to fine-tuning protections (v2.0 Appendix B item 3). Neither the trace nor the direction is settled; coded R, low confidence.
- U6. Specificity as materiality. Codebook example G treats reduced specificity as W on dim 1, but section 5 lists 'changes to examples that do not alter the rule' as not material. Rows 048, 051, 068, 071 were coded R with the example-G alternative flagged; rows 031 to 035, 042 were coded W following example G. The boundary between 'example' and 'specification' is the adjudicator's call.
- U7. Threshold definitions as commitments. Codebook section 2 excludes statements that 'define terms', while EC2 covers 'what result constitutes crossing a threshold' and example F codes threshold definitions. Threshold definitions (023, 026, 074) are coded as EC2 commitments; Effective Compute definitions (v1.0 and v2.0 footnote 4) are dropped as definitions.
- U8. ANT-1-063 (2a overly conservative evaluation route). Removal deletes both a procedural safeguard (policy update before resuming training) and an escape route (resume training after re-evaluation). The codebook does not say which reading governs direction; coded X with the ambiguity flagged.
- U9. Companion material. The RSP-page entry of 15 October 2024 ('Planned ASL-3 Safeguards') describes non-binding plans that overlap v1.0 measures (compartmentalisation of training techniques, threat-intelligence sharing with partners). It is part of the revision account, not the framework, so it was not used as a counterpart; rows 030 and 047 flag this. The author may wish to decide whether it is a companion document for L coding.
- U10. Dropped soft statements present in both versions: 'We also welcome input on this document from other groups' (v1.0) / 'We actively welcome feedback ... rsp@anthropic.com' (v2.0); 'we will continue to share our findings with policymakers' (v2.0 Introduction); 'We expect to continue refining our framework' (v2.0). Treated as aspirational rather than standing commitments; the codebook's 'aim to / intend to' inclusion could be read to cover them.

## 4. Low-confidence rows and the alternative reading

- ANT-1-001 (EC6, W, SIL): Alternative reading R: the changelog opens with 'maintaining our commitment not to train or deploy models unless we have implemented adequate safeguards' and interim measures must 'provide the same level of assurance'; adjudicator to decide whether the interim-measure route is a new consequence. Footnote 13 ('minimize changes to customer experience') sits inside this counterpart. Related rows 005, 064, 065. Candidate 4.
- ANT-1-014 (S, W, SIL): Alternative X: 7.2.1 may not be a counterpart because it concerns plans and report summaries rather than the implemented ASL-2 measure list. v_next sentence is interrupted by footnotes and a page break in the text file (internal ellipsis). Candidate 91.
- ANT-1-015 (S, W, SIL): Alternative X; alternative R because v2.0 section 4.2 states the ASL-3 Security Standard criteria within the policy itself. Same page-break note as ANT-1-014. Candidate 92.
- ANT-1-022 (M, R, NA): Unsettled: the referent of 'this tooling' moves from T&S detection to fine-tuning protections; alternative W (exception stated as standing practice rather than consideration) or S (exception scope narrowed to fine-tuning). v_i is footnote 6, listed by the extractor under the ASL-3 heading. Candidates 29, 30.
- ANT-1-029 (S, W, SIL): Unsettled: [changelog] 'Clarified ASL-3 and ASL-2 security threat models: We have clarified which actors are in and out of scope for the ASL-3 Security Standard' points at this commitment but does not state the direction (removal of the state-actor expense requirement); alternative ANN. Merged candidates 33, 34, 35. v1.0 footnote 7 already excluded ~10 state-backed non-state actors, which v2.0 retains.
- ANT-1-061 (EC2, W, SIL): Alternative R: 3.1 preliminary assessments 'on both new and existing models, as needed' at 4x Effective Compute could be read as covering mid-training checkpoints. Alternative X. Merged candidates 58, 59, 60 ('may transition to doing full fine-tuning even for mid-training evals').
- ANT-1-064 (EC6, W, SIL): Both directions present; coded W per codebook section 4. Alternative R. v_next first segment ends at a page break ('ASL-3 ... Standard'). Candidate 62 (first sentence).
- ANT-1-073 (EC5, R, NA): Trace uncertain: alternative X for v1.0 plus A for footnote 21; alternative S dim 3 (recipients specified). A page footer interrupts the v1.0 sentence in the text file (internal ellipsis). v_next is footnote 21. Candidate 89.

## 5. Revision account: what made announcement status hard to judge

Three sources were searched for every material row: the in-document changelog (v2.0 pages 17-18), the announcement post, and the RSP-page entry dated 15 October 2024. Difficulties: (1) the changelog mixes item-specific lines (ARA checkpoint, AI R&D threshold, cadence, 1% and 6x specifics, distillation removal) with class-level lines ('More outcome-focused safeguard requirements', 'new procedures related to internal governance', 'Internal and external accountability'); the class-level lines drove the U2 rule. (2) 'Clarified' is used for two changes whose direction the text does not state (ASL-3 security actors; trusted users), so pointing at the commitment and stating the direction come apart (U3). (3) The page entry is mostly a description of planned safeguards and a list of v1.0 compliance shortfalls; only its 'extends the interval to 6 months' and 'proactively clarify policy ambiguities' sentences bear on specific commitments. (4) The post repeats the changelog's opening paragraph and lists the two thresholds; it adds no item the changelog lacks except the RSO personnel change, which is not a commitment change. (5) Announcement counts: of 75 material rows, 33 ANN (12 of them resting on class-level lines under U2) and 42 SIL; no row needed [post] or [page entry] as its sole pointer.

## 6. Verifier

95 rows x 3 fields = 285 checks: ok=195, literal=90, ok-fuzzy=0, NOT FOUND=0; account prefixes [changelog]/[post]/[page entry] stripped before matching. All v_i_text, v_next_text and changelog_pointer values matched the source files exactly after whitespace, quote and dash normalisation. Internal ellipses were used where a footnote, page footer or bullet marker interrupts a sentence in the text file (rows 001, 002, 004, 007, 014, 015, 023, 024, 025, 026, 029, 041, 050, 053, 056, 064, 065, 068, 069, 072, 073, 074, 075, 076, 078); these are flagged in the rows.

## 7. Counts

Outcome by category:

| category | A | R | S | W | X | total |
|---|---|---|---|---|---|---|
| EC1 | 1 | 0 | 0 | 1 | 0 | 2 |
| EC2 | 2 | 1 | 0 | 6 | 0 | 9 |
| EC3 | 0 | 2 | 4 | 4 | 2 | 12 |
| EC4 | 0 | 0 | 1 | 1 | 0 | 2 |
| EC5 | 2 | 2 | 1 | 0 | 1 | 6 |
| EC6 | 2 | 0 | 1 | 5 | 1 | 9 |
| G | 10 | 2 | 3 | 3 | 0 | 18 |
| M | 2 | 7 | 1 | 5 | 0 | 15 |
| S | 3 | 6 | 0 | 11 | 2 | 22 |
| total | 22 | 20 | 11 | 36 | 6 | 95 |

Announcement by outcome (NA = retained rows):

| outcome | ANN | NA | SIL | total |
|---|---|---|---|---|
| A | 5 | 0 | 17 | 22 |
| R | 0 | 20 | 0 | 20 |
| S | 5 | 0 | 6 | 11 |
| W | 20 | 0 | 16 | 36 |
| X | 3 | 0 | 3 | 6 |
| total | 33 | 20 | 42 | 95 |

Provisional silent revision rate (first-pass codes, before adjudication): evidentiary stratum EC1-EC6 19/35 material changes silent (0.54); non-evidentiary stratum G/S/M 23/40 (0.57); pooled 42/75 (0.56). Under the U2 alternative (class-level lines not accepted) pooled silent count rises to 54/75.

Confidence: high 21, medium 66, low 8.

## 8. Self-check

Every row has an outcome and a non-blank material value; every material row has ANN or SIL and a verbatim pointer or NONE FOUND; every R row has announcement NA and pointer NA; A rows have v_i_text NONE and X rows have v_next_text NONE; all quotations are 80 words or fewer (ellipsis marks truncation); commitment_ids ANT-1-001 to ANT-1-095 are unique.


## 2.2 ANT-2

# ANT-2 tracing log: Anthropic RSP v2.2 (14 May 2025) to v3.0 (24 Feb 2026)

First-pass coder output. Every row is a proposal for adjudication. Files: `ANT-2_tracing.csv` (95 rows), this log.

## 1. Inputs

- v_i text: `ANT-2_v_i.txt` (RSP v2.2, 23 PDF pages). v_next text: `ANT-2_v_next.txt` (RSP v3.0, 19 PDF pages).
- Candidates: 117 rows for v2.2, 128 rows for v3.0. Both texts were read in full in addition to the candidate lists.
- Revision account: `anthropic_rsp_v3.0_2026-02-24_revision-account.md`. Provider account = RSP page version-history entry, the v3.0 in-document changelog entry, and the news post "Anthropic's Responsible Scaling Policy: Version 3.0". The LessWrong post by Holden Karnofsky (personal capacity) is in the file but was not used to ground ANN; where it alone identifies a change the flag carries `LW-only: <quote>`.
- Frontier Compliance Framework is not in the corpus. Commitments that may have moved there are coded X, confidence low, flag `companion? FCF`.

## 2. Candidate accounting (v2.2, 117 rows)

| class | n | notes |
|---|---|---|
| kept (primary basis of a row) | 44 | |
| merged (fragment folded into another row) | 26 | cand 20,22,30,44,47,50,52,55,58,63,64,66,67,70,71,73,78,84,89,92,95,35,37,42,75,81 |
| dropped | 47 | see reason classes below |
| **total** | **117** | |

Drop reason classes: duplicate (Executive Summary restates body text) 15 (cand 0-14); duplicate/description (Introduction) 2 (17,18); description 12 (15,16,19,27,29,32,33,38,46,56,61,104); aspirational 4 (23,24,25,28); TOC/lead-in 3 (62,79,97); report-not-commitment (historical changelog entries) 11 (106-116).

Splits: 3. (i) The AI R&D-4 table row was split into the ASL-3 Security requirement (ANT-2-009) and the affirmative-case requirement (ANT-2-010). (ii) Candidate 99 (7.2 Public disclosures) holds three commitments: report summaries on deployment (063), forward-looking plans (064, with footnote 19), and periodic release of noncompliance information (066). (iii) Footnote 14 (cand 93) holds a channel for raising any policy issue (057) and a regular compliance review (058).

Added from full text (v_i commitments the extractor missed): 23 rows. ANT-2-004, 005, 006 (Appendix B ASL-2 Standard), 007, 008, 009 (Section 2 table cells), 018 (notably-more-capable trigger), 020, 021, 023 (3.2 criteria), 024 (Capability Report), 026 (7.2 Expert input), 027 (Board/LTBT sharing), 032, 033, 034, 035 (4.1 criteria), 037, 038, 041 (4.2 criteria, 4.3 re-approval), 062 (publish before effect), 064 (footnote 19), 068 (U.S. Government notice). Most are list items whose lead-in carried the modal verb, or table cells.

v2.2 commitment rows: 69. Addition rows (A): 26. Total rows: 95.

## 3. Counterpart conventions used for this pair

- v3.0 Section 1 is a three-column table. The middle column ("Mitigations, our plan as a company") is treated as company commitment text; the right column ("ambitious industry-wide recommendations") is treated as the non-binding recommendations section for L purposes (codebook section 4, calibration example A). Footnote 3 says the middle column "summarizes commitments drawn from other sections of this policy and associated artifacts"; the Introduction says Roadmap goals "are not hard commitments". Rows that quote middle-column "We will" bullets carry this caveat in flags.
- v2.2 pause/restrict/upgrade consequences (ANT-2-028, 042, 046) are traced to v3.0 Appendix A "Anthropic in the lead" (delay development and deployment as needed, conditional on a significant lead). Three v_i rows therefore share one v_next passage. Alternative readings (X, or L via the recommendation column) are in flags.
- AI R&D-4 is traced to the "High-stakes sabotage opportunities" row, following the v2.2 changelog statement that AI R&D-4 threat models "entail AI systems engaging in autonomous internal sabotage". AI R&D-5 is traced to "Automated R&D in key domains", whose operationalisation (two years of 2018-2024 progress in one year) matches the v2.2 definition.
- Method criteria in 3.2, 4.1 and 4.2 are coded EC3 (evaluation or safeguards-assessment method) where they define what a showing must demonstrate, and M or S where they name a control to be implemented.

## 4. Announcement rules applied

The provider account contains no itemised changelog. The in-document entry is one sentence ("This update is a comprehensive rewrite of our RSP... see here"); the page entry adds that v3.0 "involves the publication of Frontier Safety Roadmaps... and Risk Reports that quantify risk across all our deployed models". The news post is narrative.

- ANN-1: commitments forming the v2.2 unilateral structure (Capability Threshold -> Required Safeguards; unable to show -> upgrade/restrict/pause/de-deploy/delete) are coded ANN against the post passage "Instead, we are choosing to acknowledge these challenges transparently and restructure the RSP... The revised RSP aims to adopt more realistic unilateral commitments...", the "two sets of mitigations" passage, or the "higher ASLs... might prove outright impossible to implement without collective action" passage. This follows calibration example A. Rows: 008-012, 028, 029, 040, 042, 044-046, 048.
- ANN-2: procedural, methodological and governance commitments not named in the post are SIL. The "comprehensive rewrite" language is generic under codebook section 6.
- Additions announced in the post (Roadmap, Risk Reports content and cadence, redaction policy, external review, three named Roadmap goals) are ANN; other additions are SIL.

## 5. Cases the codebook does not settle

1. **Direction framed differently by the account (ANT-2-030, 063).** The post identifies the Safeguards Report -> Risk Report change and the new disclosure regime but frames them as extensions. The rows are coded W on codebook dimensions (gate removed; per-deployment summaries dropped). The codebook standard requires that a reader know the commitment changed "in this direction". Coded ANN with the alternative SIL flagged. Adjudicator to decide whether direction-mismatch defeats ANN.
2. **Granularity of the example A reading (029, 043, 044, 045, 047).** The post identifies the removal of unilateral threshold-contingent commitments as a class. Whether that identifies each specific consequence (de-deploy, delete weights, interim measures, footnote 8 training limit, follow-up assessment) is not settled. De-deploy/delete/footnote 8 are coded ANN low; interim measures and follow-up assessment are coded SIL with the alternative flagged. A consistent adjudication either way will move 3-5 rows.
3. **Appendix A as counterpart versus new commitment (028, 042, 046).** If Appendix A is treated as a new commitment, these three rows become X (or L via the recommendation column) and an A row is needed for "Anthropic in the lead". Example K says the choice depends on whether an equivalent survives in the recommendations section; an equivalent standard ("strong argument that catastrophic risk is contained") survives in the right column, and a conditional version survives as a company commitment.
4. **Both-directions rows (007, 008, 021, 024, 026, 030, 056, 063).** Coded W per codebook section 4. The S side is documented in each rationale so the direction breakdown can be recomputed.
5. **v3.0 Introduction as account.** The v3.0 Introduction contains more explicit change language than the account ("This approach represents a change from our previous RSP... Our previous RSP committed to implementing mitigations that would reduce our models' absolute risk levels to acceptable levels, without regard to whether other frontier AI developers would do the same... But we cannot commit to following them unilaterally"). It is not part of the designated revision account and was not used for ANN. If the author counts it, several SIL rows in the threshold structure become ANN.
6. **ASL-2 baseline (003-006).** No all-model baseline exists in v3.0. Appendix B items are coded L where a recommendation-column equivalent exists (005, 006) and X otherwise (003, 004). Alternative W via "maintain or improve on our ASL-3 protections" is flagged.
7. **Middle-column "We will" bullets (011, 090-093).** Quoted as commitments because the RSP text says "We will", but footnote 3 and the Introduction describe them as Roadmap goals that are not hard commitments. Obligation strength is ambiguous; flagged on each row.
8. **RSO remit (049).** Rewording versus narrowing of scope; coded W low.

## 6. Low-confidence rows (21)

- **ANT-2-002** (W, EC5): alternative readings: R (general policymaker engagement continues via policy advocacy language in Section 1) or X (v3.0 sentence is a different object). Counterpart sits in the company-plan column of the Section 1 table.
- **ANT-2-003** (X, M): alternative: W with counterpart Section 1 row 1 company column (maintain or improve on our ASL-3 protections), which applies to ASL-3 models rather than all models; merged cand 1 (Exec Summary duplicate)
- **ANT-2-004** (X, EC5): added from full text; alternative: R implied by 3.1 wording (in our System Card or elsewhere) which presupposes continued system cards
- **ANT-2-005** (L, M): example A (moved to recommendations); alternatives: X, or W with counterpart row 1 company column which lists bug bounties and classifier guards; added from full text
- **ANT-2-006** (L, S): example A; alternatives: X, or W via company column phrase (a number of noteworthy security controls) inside ASL-3 protections; added from full text
- **ANT-2-009** (W, EC6): split: AI R&D-4 row split into safeguard requirement (this row) and affirmative case (next row); example A; alternative SIL (post names neither AI R&D-4 nor sabotage; only the structural change) and alternative L (recommendation column carries the strong-argument requirement); counterpart identified via v2.2 changelog note that AI R&D-4 threat models entail autonomous internal sabotage
- **ANT-2-010** (W, EC6): split (see previous row); example A; alternative L: the affirmative-case requirement survives as the recommendation that a frontier developer should make a strong argument that AI systems will not carry out sabotage; alternative SIL
- **ANT-2-029** (X, EC6): footnote 8; coded ANN under the example A reading (a unilateral training restriction tied to a threshold); alternative SIL (a discretionary footnote provision not named in the post)
- **ANT-2-033** (X, M): added from full text; items 4 and 5 merged; alternative W with counterpart phrase in Section 1 row 1 company column (threat intelligence for continually assessing the threat of jailbreaks)
- **ANT-2-037** (X, S): added from full text; sub-items a-e merged; alternative: merge into ANT-2-036 as part of the same standard (W)
- **ANT-2-039** (L, S): example A; alternatives: W with counterpart Section 1 row 4 company column (eyes on everything logging to detect concerning behavior by insiders, coded as A row), or X; cand 64 (committed to further enhancing these protections) merged
- **ANT-2-041** (W, G): added from full text; alternative X (no re-approval procedure exists)
- **ANT-2-044** (X, EC6): example A; alternative SIL (the post does not name de-deployment)
- **ANT-2-045** (X, EC6): example A; alternative SIL (the post does not name weight deletion)
- **ANT-2-049** (W, G): alternative R (rewording at the same modal force; duties otherwise identical); duty (1) loses the words to the Board of Directors; cand 13 (Exec Summary) merged
- **ANT-2-056** (W, G): both directions present, W coded per codebook rule; alternative S; footnote 15 (quarterly summary reports for minimal-risk cases) and RSO duty (6) merged
- **ANT-2-057** (X, G): companion? FCF; footnote 14; alternative W with counterpart 4. Governance item 3 (narrower object)
- **ANT-2-059** (W, G): footnote 16; alternative R (the dropped clause is an aim, not a will)
- **ANT-2-063** (W, EC5): both directions present, W coded per rule; alternative S; the account identifies the new instrument and cadence but not the loss of per-deployment summaries; cand 14 (Exec Summary) merged
- **ANT-2-067** (X, EC5): companion? FCF; footnote 18; alternative: superseded by public Risk Report coverage of in-scope internal models (different recipient)
- **ANT-2-068** (X, EC5): companion? FCF; added from full text

## 7. Revision account: difficulties

- No itemised changelog and no redline. The in-document changelog entry defers to the news post. SRR for this pair therefore rests on a narrative account.
- The post explains the rationale for restructuring at length but names few specific v2.2 commitments (Safeguards Report, ASL-3 deployment standard as history, ASL-4/5 definitions). Most procedural removals (assessment triggers, elicitation, forecasting, audits, readiness, U.S. Government notice, cyber assessment) are not identifiable.
- The LessWrong post is more specific (unilateral pause as "the biggest change", internal-only models in scope, competitor commitments, late external-review trigger, Roadmap no-backsliding). It is flagged `LW-only` on 7 rows and never grounds ANN.
- The post's Roadmap example goals are worded differently from the RSP middle-column bullets (e.g. "measures to ensure Claude behaves according to its constitution" versus "systematic alignment assessments"); ANT-2-092 is SIL with the near-miss quoted.
- Pointer prefixes `[post]` / `[page entry]` were required by the brief. The generic verifier returns `ok-fuzzy` on prefixed pointers (the bracketed prefix is not in the account) and `ok` when the prefix is stripped. Both runs are reported below.

## 8. Verifier summary

Raw CSV (pointers with prefixes): v_i_text ok 69, literal 26; v_next_text ok 71, literal 24; changelog_pointer ok-fuzzy 29 (prefix only), literal 66.
Prefix-stripped pointers: v_i_text ok 69, literal 26; v_next_text ok 71, literal 24; changelog_pointer ok 29, literal 66. No NOT FOUND. Internal ellipses are used in 036, 042, 048, 011, 013, 023, 092 to skip footnotes, page breaks or interleaved table-column text; the verifier matches segments in order.

## 9. Count tables

Category by outcome:

| category | A | L | R | S | W | X | total |
|---|---|---|---|---|---|---|---|
| EC1 | 1 | 0 | 0 | 0 | 0 | 2 | 3 |
| EC2 | 0 | 0 | 0 | 0 | 2 | 3 | 5 |
| EC3 | 2 | 0 | 0 | 0 | 5 | 2 | 9 |
| EC4 | 6 | 0 | 1 | 0 | 1 | 1 | 9 |
| EC5 | 7 | 0 | 0 | 1 | 4 | 5 | 17 |
| EC6 | 2 | 0 | 0 | 0 | 10 | 5 | 17 |
| G | 4 | 0 | 8 | 2 | 6 | 2 | 22 |
| S | 2 | 2 | 0 | 0 | 1 | 1 | 6 |
| M | 2 | 1 | 0 | 0 | 1 | 3 | 7 |
| total | 26 | 3 | 9 | 3 | 30 | 24 | 95 |

Outcome by announcement:

| outcome | ANN | NA | SIL | total |
|---|---|---|---|---|
| A | 13 | 0 | 13 | 26 |
| L | 0 | 0 | 3 | 3 |
| R | 0 | 9 | 0 | 9 |
| S | 1 | 0 | 2 | 3 |
| W | 11 | 0 | 19 | 30 |
| X | 4 | 0 | 20 | 24 |
| total | 29 | 9 | 57 | 95 |

Material changes: 86 (evidentiary stratum EC1-EC6: 59, of which SIL 33, ANN 26; non-evidentiary G/S/M: 27, of which SIL 24, ANN 3). Provisional first-pass SRR (all material): 57/86 = 0.66; evidentiary 33/59 = 0.56; non-evidentiary 24/27 = 0.89. These depend on the unsettled cases in section 5, in particular items 1, 2 and 5.

## 10. Self-check

Every row has an outcome and non-blank `material`; every material row has ANN or SIL and a pointer or NONE FOUND; every R row has NA/NA; A rows have v_i_text NONE; X rows have v_next_text NONE. Columns match the brief's section 7 layout. CSV written with QUOTE_ALL.


## 2.3 OAI-1

# OAI-1 tracing log: OpenAI Preparedness Framework, Beta (18 December 2023) to v2 (15 April 2025)

Coder: first-pass (automated). Codebook v0.1, brief section 4. Revision account: Appendix A 'Change log' (12 items) inside v2 and the announcement post of 15 April 2025, both in the saved revision-account file. Pointers are prefixed '[changelog item N]' or '[post]'. The original 15 April v2 file was used; the June re-upload was not.

## 1. Candidate disposition (v_i = Beta, 47 candidates)

| disposition | n | definition |
|---|---|---|
| kept as primary | 16 | the candidate sentence is the v_i_text (or its first segment) of a row |
| merged | 16 | the candidate is a fragment or restatement of a commitment whose row draws its v_i_text from another sentence |
| dropped | 15 | excluded under codebook section 2 |
| total | 47 | |

Candidates contributing to rows (primary or merged): 32. Splits: 2. Commitments added from the full text with no candidate contribution: 19. Traced rows (Beta commitments): 41. Addition rows (A): 10. Total rows: 51.

Kept as primary (candidate index in brackets, row): [7] to 006; [13] to 017; [18] to 003; [21] to 022; [24] to 019; [25] to 023; [27] to 002; [28] to 024; [31] to 026; [32] to 027; [33] to 028; [36] to 030; [37] to 032; [38] to 034; [39] to 035; [44] to 041.

Merged: [1] into 002; [2] into 026; [5] into 005; [6] into 004; [12] into 003 and 007; [14] into 019; [19] into 024; [22] into 022; [23] into 022; [26] into 027; [30] into 020; [35] into 004, 006 and 033 (split); [40] into 035; [41] into 033; [42] into 034; [43] into 041.

Dropped, with reason class:

- [0] description (aspirational statement about the effect of the Framework)
- [3] description (cross-reference to Governance)
- [4] definition (catastrophic risk)
- [8] aspirational (research required to make AGI safe)
- [9] TOC (How to read this document)
- [10] TOC
- [11] TOC
- [15] description (deferral of evaluation details to Scorecard)
- [16] description (footnote on intelligence explosion)
- [17] description (expected expansion of the list)
- [20] description (origin of the initial category set)
- [29] description (lead-in to Governance)
- [34] description (lead-in to Operations; substance is candidate [35])
- [45] TOC/duplicate (restates the standard decision process)
- [46] report-not-commitment (example scenario fragment)

Splits (2): candidate [35] (the three-party operational structure) is split into 004 (Preparedness team), 006 (SAG) and 033 (Leadership as final decision-maker); the Beta sentence pair "We will be running these evaluations continually ... >2x effective compute increase or major algorithmic breakthrough" is split into 020 (cadence and trigger) and 021 (coverage of models, codebook example B).

Added from the full text (no candidate row; 19 commitments): 001, 008, 009, 010, 011, 012, 013, 014, 015, 016, 018, 021, 025, 029, 031, 036, 038, 039, 040. The extractor missed all threshold definitions in the four risk tables (008 to 016), the category definitions (010, 013, 014), the any-category rule (018; the gradation-scale row 017 draws on candidate [13]), the alignment-evidence sentence (029), the SAG appointment sentence (031), the Framework-update process (036), internal visibility (038), the audit and external-access commitments (039, 040) and the introductory evaluation-suite sentence (001).

v_next candidates (71): used as the starting list for additions. Candidates [0] to [4], [8], [11], [12], [14], [16], [17], [21], [32] to [34], [60], [65] to [67], [69], [70] are descriptions or illustrative material and were not coded. [55] to [59] are the changelog text itself, not body commitments. [15] ("we will by then need to have made significant progress on those investments") is a rationale statement in the AI Self-improvement threat model and was not coded; an adjudicator may treat it as a commitment to invest ahead of Critical. The remaining candidates map to traced rows or to A rows as noted in flags. Added from the v2 full text with no candidate: 5.1 Noncompliance (049), the annual review sentence in Appendix B (036), the Table 1 safeguard guideline cells (047) and C.3 "We will require the following practices for High capability models" (026).

## 2. Cases the codebook does not settle

1. Definition of severity (dropped candidate [4]). Beta: "hundreds of billions of dollars in economic damage or lead to the severe harm or death of many individuals". v2 footnote 1: "the death or grave injury of thousands of people or hundreds of billions of dollars of economic damage". Section 2 excludes definitions, so no row was created, but the definition scopes every commitment in the Framework. Alternatives: leave uncoded (done), or add an EC1 row (W if "thousands" is read as a higher bar than "many").
2. Low and Medium levels (017). Coded as one W row on the gradation-scale commitment with ANN (item 2). Alternatives: R (the action trigger, High, is unchanged and the removed levels triggered nothing) or four X rows (one per category). The choice affects the outcome count by up to three rows and the announcement count not at all (all would be ANN via item 2).
3. Persuasion (013). X with ANN. Alternative: L, since v2 says persuasion risks are handled via the Model Spec and usage policies. The codebook defines L for companion documents and non-binding sections; the Model Spec is neither a safety-framework companion nor a recommendation section. Flagged 'companion?'.
4. Marginal risk, section 4.3 (027). Folded into the deployment-gate row as a change to consequence per examples C and I, so it is not an A row. Alternative: a separate W row, which would add one ANN material change.
5. Post-mitigation evaluation to Safeguards Report (023). The change substitutes one evidentiary method for another. The materiality dimensions do not name evidentiary method, and item 9 frames the change as more thorough. Coded W (mixed directions, per the codebook rule) with ANN. Alternative: S.
6. Threshold redefinitions with unclear direction (008, 015, 016). The cyber High and AI Self-improvement High and Critical thresholds are re-specified in different terms. W was chosen where at least one reading raises the bar, per the codebook's conservative rule, with confidence low. Alternatives are recorded in flags. Example F (de-commensuration) does not apply directly because both versions are qualitative for these thresholds; the 2x compute trigger removal in 020 is the closest analogue.
7. Rows with mixed announcement: 016 (ARA prong removal announced, AI research prong re-specification not) and 022 (renaming announced, cadence change not). Resolved by attributing the announced element to another row (014, 023) and coding the residual change SIL. An adjudicator who treats each row as one change would code ANN for both.
8. Table 2 'Potential response' column (044). Entries such as "Adopt elicitation approach that overcomes sandbagging" and "Convert Autonomous Replication and Adaptation to a Tracked Category" are conditional and headed 'Potential response'. Not coded as separate commitments; the include rule admits "may"-strength statements, so an adjudicator may add rows.
9. Footnote 5 (045): coded A rather than as a second weakening dimension on 010. Either reading yields one SIL material change.
10. Whether governance information flows to the Board count once (034) or in each row where a Board-sharing clause disappears (005, 035). Coded once, in 034; 005 carries its own W on cadence and recipients.
11. Update process (036): the annual review is added and the evidence-case requirement is dropped; W under the mixed-direction rule. Alternative: S, or an R row plus an A row.
12. Public disclosures (050): ANN on the post's "clearer operational guidance on how we evaluate, govern, and disclose" and "We'll continue to publish our Preparedness findings"; the post frames publication as continuing practice and the changelog has no disclosure item, so SIL is a defensible alternative.

## 3. Low-confidence rows (10) and their alternative readings

- OAI-1-002 (EC3, W, SIL): Merged candidates [1] ("we will also be forecasting the future development of risks") and [27]; Preparedness team duty iv "forecasting potential changes to catastrophic risk levels" also merged. Alternative reading: X (no counterpart; v2 only refers to "our forecasts" as existing inputs in 3.2 and 4.4). Second alternative: R (forecast trigger survives in "reached or are forecasted to reach Critical capability", 4.4).
- OAI-1-003 (EC1, W, SIL): Merged candidates [12], [18] and Preparedness team duties ii and iii (monitoring for unknown unknowns; ensuring risk level distinctions are appropriate). Alternative reading: R (both are standing review processes and "periodically" is not a weaker obligation), or ANN via [changelog item 1] "we use a holistic process to decide which areas of frontier AI capability to track" and item 5 (Research Categories as the maturation route). Neither item identifies a change in review cadence.
- OAI-1-008 (EC2, W, SIL): Added from full text. Direction is genuinely unclear; alternative readings: S (automation without a supplied strategy is not required, "reasonably hardened" is a lower target class) or R (re-specification of the same threshold). [changelog item 2] defines High generically and [changelog item 4] says categories were updated "accordingly"; neither identifies a change to the cyber threshold. Source hyphenation line-breaks retained verbatim from the text file (hyphen followed by space, e.g. "opera- tions").
- OAI-1-015 (EC2, W, SIL): Added from full text. Direction uncertain; alternative readings: S (a "research engineer assistant" for every researcher may be reached before a production-codebase PR capability) or R (re-specification of the same milestone). [changelog item 4] identifies the category change, not the threshold direction; alternative announcement reading: ANN via item 4. Source hyphenation line-breaks retained verbatim from the text file (hyphen followed by space, e.g. "opera- tions").
- OAI-1-016 (EC2, W, SIL): Added from full text. The prong removals are announced ([changelog item 4], [changelog item 5]) and counted in 014; the re-specification of the autonomous AI research prong is not identified in the account, so this row is SIL on its own change. Alternative readings: ANN via item 4 if the row is treated as one change; S if the "leading indicator" is read as a lower bar than fully autonomous research. Source hyphenation line-breaks retained verbatim from the text file (hyphen followed by space, e.g. "opera- tions").
- OAI-1-017 (EC2, W, ANN): Added from full text. Per-category Low and Medium definitions (cyber, CBRN, persuasion, model autonomy) are folded into this row rather than coded as four X rows. Alternative reading: R (the action trigger, High, is unchanged; the removed levels triggered nothing, as the changelog states). Candidate [13] merged here.
- OAI-1-022 (EC3, W, SIL): Merged candidates [21], [22], [23] and Preparedness team duty i. Category alternative: EC5 (internal reporting instrument) or G. Alternative outcome: R (same artefact renamed; the post says "Capabilities Reports (formerly known as the “Preparedness Scorecard”)"). Alternative announcement: ANN via [changelog item 8] and that post sentence; neither identifies the change from continuous to per-deployment.
- OAI-1-029 (EC6, W, SIL): Added from full text. Alternative readings: R or S (the report is "require[d]" and applies from High; Appendix C.2 sets out misalignment safeguards); the codebook does not settle how to weigh a "Potential response" table heading against an imperative "require" in the cell.
- OAI-1-040 (EC4, X, SIL): Added from full text. Alternative reading: W, tracing to 5.2 "when available and feasible, OpenAI will work with third-parties to independently evaluate models" (conditional third-party access) or to 2.1 "incorporates feedback from ... the U.S. government and its partners".
- OAI-1-050 (EC5, A, ANN): Candidates v_next [47], [48], [49]. Alternative announcement: SIL, because the post frames publication as continuing existing practice ("We’ll continue to publish") rather than as a new commitment, and the changelog has no disclosure item; the codebook standard (a reader would know this commitment was added) is not clearly met.

## 4. Revision account: difficulties in judging announcement status

- The account has two parts: twelve numbered changelog items and a prose post. Items 1, 7 and 12 are broad ('Clarify the relationship among capabilities, risks and safeguards'; 'Provide risk-specific safeguard guidelines'; 'Clarify the governance process'). They point at areas rather than at specific commitments. Under the codebook standard they were accepted as ANN only where the item names the new element that the row codes (threat models in item 1 for 043; safeguard guidelines in item 7 for 026 and 047). They were not accepted for governance changes in Appendix B (004, 005, 031, 034, 038), none of which item 12 identifies.
- Item 8 and the post identify the Capabilities Report as the renamed Scorecard but do not state that the instrument moved from continuous to per-deployment or that the monthly report to Leadership and the Board was dropped (022, 005 coded SIL).
- Item 6 presents the elicitation changes as added detail; it does not identify that fine-tuned evaluation became conditional on access (019 coded SIL).
- The v2 body contains two explanatory boxes ('Changes to Tracked Categories in version 2', 'Persuasion') that read like changelog material. They are part of the document, not the account, and were not used for announcement status; every change they describe is also in item 4 or 5.
- The post's 'Responding to shifts in the frontier landscape' paragraph and item 11 both identify the 4.3 adjustment (027, example C confirmed).
- Example B confirmed: footnote 6 is not among the twelve items and is not in the post (021 SIL).
- No item or post sentence mentions third-party audits (039), external or government access (040), Board committee oversight (034), SAG appointment consultation (031), internal visibility (038), noncompliance (049) or the 2x compute trigger (020).

## 5. Verifier summary

Run 1 (pointers as written, with the mandated '[changelog item N]' / '[post]' prefixes): {('v_i_text', 'ok'): 41, ('v_next_text', 'ok'): 47, ('changelog_pointer', 'literal'): 35, ('changelog_pointer', 'ok-fuzzy'): 16, ('v_next_text', 'literal'): 3, ('v_i_text', 'literal'): 10, ('v_next_text', 'ok-fuzzy'): 1}. Run 2 (identical rows, prefixes stripped from changelog_pointer before verification): {('v_i_text', 'ok'): 41, ('v_next_text', 'ok'): 47, ('changelog_pointer', 'literal'): 35, ('changelog_pointer', 'ok'): 16, ('v_next_text', 'literal'): 3, ('v_i_text', 'literal'): 10, ('v_next_text', 'ok-fuzzy'): 1}. All 153 field checks return ok, ok-fuzzy or literal in both runs. The only non-pointer ok-fuzzy is 048 v_next_text, where a page break interrupts the sentence (flagged). Pointer ok-fuzzy results in run 1 are caused solely by the prefixes; every pointer is 'ok' once the prefix is removed.

Text handling: the v2 text file breaks words across lines with hyphens inside tables (for example "opera-\ntions"). Where a quote spans such a break the file text is copied verbatim with the hyphen retained and the line break rendered as a space ("opera- tions"); affected rows are flagged. Candidate [13]'s paragraph and other Beta passages contain PDF extraction noise (stray control characters, "0" and "D" line endings); quotes stop before such characters.

## 6. Counts

Per category and outcome:

| category | R | S | W | X | L | A | total |
|---|---|---|---|---|---|---|---|
| EC1 | 1 | 0 | 4 | 1 | 0 | 2 | 8 |
| EC2 | 1 | 1 | 7 | 0 | 0 | 0 | 9 |
| EC3 | 1 | 0 | 5 | 0 | 0 | 3 | 9 |
| EC4 | 0 | 0 | 1 | 1 | 0 | 1 | 3 |
| EC5 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| EC6 | 0 | 1 | 3 | 0 | 0 | 1 | 5 |
| G | 6 | 0 | 6 | 1 | 0 | 1 | 14 |
| S | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| M | 1 | 0 | 0 | 0 | 0 | 1 | 2 |
| total | 10 | 2 | 26 | 3 | 0 | 10 | 51 |

Announcement status per outcome (material rows only; R rows are NA):

| outcome | ANN | SIL | total material |
|---|---|---|---|
| S | 1 | 1 | 2 |
| W | 6 | 20 | 26 |
| X | 2 | 1 | 3 |
| L | 0 | 0 | 0 |
| A | 7 | 3 | 10 |
| all material | 16 | 25 | 41 |
| evidentiary stratum (EC1 to EC6) | 14 | 18 | 32 |
| non-evidentiary stratum (G, S, M) | 2 | 7 | 9 |

Confidence: {'medium': 25, 'low': 10, 'high': 16}.

## 7. Self-check

Every row has an outcome and a non-blank material field; every material row has an announcement status (ANN or SIL) and a verbatim pointer or NONE FOUND; every R row has NA in both fields; every A row has v_i_text NONE and every X row has v_next_text NONE; all quotes are at most 80 words; the CSV was written with csv.QUOTE_ALL and re-read with 51 rows and the 18 mandated columns in order.


## 2.4 GDM-1

# GDM-1 log: Google DeepMind Frontier Safety Framework v2.0 to v3.0

Coder: first-pass (automated). Inputs: v2.0 text file, v3.0 text file, v2.0 candidates (36 rows), v3.0 candidates (50 rows), revision account file for v3.0 (announcement post 'Strengthening our Frontier Safety Framework', 22 September 2025, plus section 5.3, which lists version dates only). Output: GDM-1_tracing.csv, 42 rows.

## 1. Candidate handling (v2.0, 36 candidates)

- Kept: 21 candidates (rows 5, 7, 9, 10, 11, 12, 13, 14, 15, 19, 20, 21, 22, 24, 26, 27, 28, 29, 30, 31, 32 of the candidates file).
- Dropped: 15 candidates. Reason classes: description (0, 1, 2, 3, 4, 6, 8, 16, 17, 25); definition (18); belief statement about the field, coded as description (23); aspirational future-work agenda (33, 34, 35). Candidate 8 is also a duplicate of 4.
- Merged: 3 candidate rows folded into another candidate's row (21 with 22 in GDM-1-024; 30 with 29 in GDM-1-031; 24 with 20 in GDM-1-023). Candidate 32's first clause duplicates candidate 7; its second clause is GDM-1-030. Several kept candidates were also merged with adjacent full-text sentences the extractor missed (GDM-1-001 bullets, GDM-1-002 second sentence, GDM-1-008 second sentence, GDM-1-032 first sentence, GDM-1-026 bullets).
- Split: 0.
- Added from full text (v2.0 commitments with no candidate row): 15 rows, GDM-1-007, 009, 010, 011, 012, 013, 014, 015, 016, 018, 019, 020, 021, 022, 025. These are the external-evaluator sentence, the hold provision, the distant-from-CCL provision, the automated-monitoring mitigation, the mitigation-review sentence (example G), the deployment-mitigation process steps, and the five CCL definitions in Tables 1 and 2. The extractor missed them because they carry no first-person modal verb or sit in table cells.
- v2.0 commitment list: 33 rows. Additions found in v3.0: 9 rows (GDM-1-034 to 042). Total 42.

Category assignment notes. Security levels tiered by CCL are coded S, not EC6, following the codebook's S definition ('tiering by capability level'); the automated-monitoring mitigation tied to the first deceptive alignment CCL is coded M by the same analogy; the deployment-mitigation process 'applied to models reaching a CCL' is coded EC6 because it is the action a CCL determination obligates. Alternatives are noted in the flags.

## 2. Calibration examples F to J (verified against both texts)

| Example | Row(s) | Verified | Outcome coded | Announcement |
|---|---|---|---|---|
| F (ML R&D 2x anchor; cyber collapse) | GDM-1-021; GDM-1-019, GDM-1-020 | Yes: '(e.g. 2x) from 2020-2024 rates' becomes 'from historical rates'; two cyber CCLs with quantitative anchors become one qualitative CCL | W (021, 020); X (019) | SIL for all three |
| G (monitoring sources) | GDM-1-012 | Yes: four named information sources become 'post-market monitoring' | W (dims 1;2;4) | SIL |
| H (safety case update modal) | GDM-1-017 | Yes: 'will be updated through red-teaming' becomes 'may be updated if deemed necessary' | W (dim 4) | SIL |
| I (marginal risk provision) | GDM-1-015 (also visible in 1.6, noted on GDM-1-036) | Yes: 2.1.2 factor iv and 1.6 allow other models' capabilities and mitigations to justify deployment; no v2.0 provision | W (dims 4;6) on the safety-case assessment row | SIL |
| J (governance de-naming) | GDM-1-027, GDM-1-028 | Yes: three named councils absent from v3.0; 'appropriate governance function' and 'appropriate corporate governance bodies' | W (dim 3) | SIL |

The announcement post identifies none of F to J. Its section 'Sharpening our risk assessment process' says 'We’ve sharpened our CCL definitions', which points at CCL definitions as a class and claims a direction (sharpening) opposite to the de-commensuration coded under F; see section 4 below.

## 3. Cases the codebook did not settle

1. Whether a framework-wide caveat is a commitment. GDM-1-033 ('our adoption of the protocols ... may depend on whether such organizations across the field adopt similar protocols') is coded G, S on dim 6 because the clause is removed; it could equally be excluded as description, or treated as relocated into the marginal-risk considerations of 1.6 and 2.2.
2. Whether a restated operationalisation of a threshold is material. GDM-1-022 (ML R&D autonomy: 'the AI R&D pipeline at a competitive cost' to 'the work of any team of researchers at Google ... approximately comparable all-inclusive costs') is coded R with alternatives S and W.
3. Where example I attaches. The codebook says I is a change to an existing consequence commitment, not A. The v2.0 candidates are the safety-case assessment step (1b, method) and the pre-deployment gate (item 2). Coded on 1b (GDM-1-015, EC3) because the v3.0 marginal-risk text sits in the factor list of 1b; the codebook labels I as EC6. The adjudicator may move it to GDM-1-016 or create a separate EC6 row anchored to 1.6.
4. Whether an implied publication counts as a disclosure commitment. GDM-1-030 ('we will publish substantive revisions as appropriate') has no v3.0 sentence about publishing; coded W on dim 5, alternatives R and X.
5. Whether 'illustrative only' is material for unchanged threshold definitions. GDM-1-025 (instrumental reasoning CCLs) coded R with alternative W on dim 6.
6. Whether an 'expect' statement addressed to 'AI developers' is a self-commitment. GDM-1-026 (control evaluations) coded X with alternatives: exclude, or W with 3.1.2 as counterpart.
7. Whether the removal of the response-plan approval sentence is X or the de-naming W of example J. GDM-1-027 follows J (W) with alternative X.
8. Direction of the evaluation-trigger rewrite. GDM-1-002 coded S (lower bar 'meaningful new capabilities', firmer modal) with alternatives W (loss of 'regularly') and R.
9. Whether a new exemption within a new section is A or a change. GDM-1-036 (risk acceptance criteria) is A; its embedded override for security levels is coded as W on GDM-1-024 rather than duplicated.
10. Whether GA-to-external deployment is a scope change. GDM-1-016 coded S on dim 1, alternative R.

## 4. Revision account: difficulties for announcement status

- The account is a narrative post with four 'Key updates' subsections and no itemised changelog; section 5.3 of v3.0 lists version numbers and dates only.
- Clearly identifying lines: harmful manipulation CCL (GDM-1-001, 041); internal deployments for ML R&D (GDM-1-013); mitigations before CCLs (GDM-1-038, though framed as continuing practice).
- Borderline: 'we describe how we conduct holistic assessments that include systematic risk identification, comprehensive analyses of model capabilities and explicit determinations of risk acceptability' is used as ANN for three additions (GDM-1-034, 035, 036) because it names the three added elements; an adjudicator may treat it as generic. 'we now provide further protocols for our machine learning research and development CCLs' is used as ANN for the ML R&D safeguard list (GDM-1-042) but not for the ML R&D alert-threshold rule (GDM-1-037); the line names the section, so both calls are contestable.
- 'We’ve sharpened our CCL definitions' is not treated as identifying any CCL change (GDM-1-018 to 021): it points at the class, not the commitment, and claims a direction (narrowing to critical threats) that does not match the removal of quantitative anchors. If the adjudicator treats it as ANN, four W rows and one X row change from SIL to ANN.
- No line in the post addresses examples F to J, the removal of the development-hold provision, the removal of control evaluations, the change to the pre-deployment gate, the annual update cadence, or the security-level adjustment conditions.

## 5. Low-confidence rows and alternative readings

- GDM-1-007 (EC4, W): Added from full text (not in candidates). Both directions present so W per codebook section 4. Alternative reading R: 'external evaluations as appropriate' is the same discretionary commitment reworded. Alternative reading S: governments newly named as parties engaged. v_next_text joins two sentences from the same section with an ellipsis.
- GDM-1-018 (EC2, W): Added from full text. 'additional10' in v_next_text is a footnote marker. Both directions present so W per section 4; alternative reading S (broader actor set) or R (rewording of an equivalent severity criterion). closest account line is 'We’ve sharpened our CCL definitions specifically to identify the critical threats that warrant the most rigorous governance and mitigation strategies', which points at CCL definitions collectively but claims sharpening, not the direction coded here; adjudicator may read it as ANN.
- GDM-1-022 (EC2, R): Added from full text. Alternative reading S (dim 2): automating 'any team' is a lower bar than automating 'the AI R&D pipeline'. Alternative reading W: 'approximately comparable all-inclusive costs' may be a higher cost bar than 'competitive cost'. Codebook does not settle whether a restated operationalisation is material.
- GDM-1-025 (EC2, R): Added from full text; row covers both Level 1 and Level 2 (Level 2 identical in both versions). Alternative reading W (dim 6): v3.0 states 'we do not associate them with explicit risk acceptance criteria' and 'we do not indicate security mitigations for models at these CCLs' and labels the CCLs 'intended for illustration only', which may be read as detaching the thresholds from any consequence; v2.0 also attached no security level to them. Mitigation change coded in GDM-1-011.
- GDM-1-026 (EC3, X): Merged candidate 26 with the two bullets and the two-safety-case paragraph. '14' is a footnote marker. Alternative reading: exclude as other-party or aspirational ('AI developers should', 'we expect'). Alternative reading W: treat v3.0 3.1.2 (ML R&D deployment mitigations with safety case, testing and 'alignment training') as the counterpart, since the account says misalignment is now addressed through ML R&D CCLs; the account does not identify the removal of control evaluations.
- GDM-1-030 (EC5, W): Candidate 32. Alternative reading R: an updated public framework implies publication, so the commitment survives in 5.1. Alternative reading X: no counterpart governs publication. Codebook does not settle whether an implied publication counts.
- GDM-1-033 (G, S): Candidate 5. Alternative reading: exclude as description rather than commitment. Alternative reading: the industry-conditionality reappears in narrower form as marginal-risk considerations in 1.6 and 2.2 (see GDM-1-015 and GDM-1-024), so the condition is relocated rather than removed. Codebook does not settle whether a framework-wide caveat is a commitment.

## 6. Verifier summary

GDM-1 verifier: 77 ok, 3 ok-fuzzy, 46 literal, 0 NOT FOUND over 42 rows x 3 fields. ok-fuzzy: GDM-1-002 v_next_text (page break in 1.3), GDM-1-023 v_i_text (footnote block and page break between pages 4 and 5), GDM-1-037 v_next_text (footnote 4 and page break between pages 5 and 6); each is flagged in the row.

## 7. Count tables

Per category and outcome:

| category | R | S | W | X | L | A | total |
|---|---|---|---|---|---|---|---|
| EC1 | 0 | 1 | 0 | 0 | 0 | 1 | 2 |
| EC2 | 5 | 1 | 3 | 1 | 0 | 2 | 12 |
| EC3 | 2 | 0 | 2 | 1 | 0 | 1 | 6 |
| EC4 | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
| EC5 | 2 | 0 | 1 | 0 | 0 | 0 | 3 |
| EC6 | 1 | 2 | 1 | 1 | 0 | 1 | 6 |
| G | 0 | 2 | 2 | 0 | 0 | 1 | 5 |
| M | 1 | 0 | 1 | 0 | 0 | 2 | 4 |
| S | 1 | 0 | 1 | 0 | 0 | 1 | 3 |
| total | 12 | 6 | 12 | 3 | 0 | 9 | 42 |

Outcomes: {'R': 12, 'W': 12, 'A': 9, 'S': 6, 'X': 3}. Announcement: {'SIL': 22, 'NA': 12, 'ANN': 8}. Material rows: 30; of these ANN 8, SIL 22.


## 2.5 GDM-2

# GDM-2 log: Google DeepMind Frontier Safety Framework v3.0 to v3.1

Coder: first-pass (automated). Inputs: v3.0 text file (identical to the GDM-1 v_next file), v3.1 text file, v3.0 candidates (50 rows), v3.1 candidates (65 rows), revision account file for v3.1 (in-document changelog in section 5.3 with six bullets, and the section 'FSF 3.1: Introducing tracked capability levels' inserted into the 22 September 2025 post by in-place edit on 17 April 2026). Output: GDM-2_tracing.csv, 50 rows.

## 1. Commitment list for v3.0

Per the pair instructions the v3.0 list is the GDM-1 v3.0 side: the 39 GDM-1 rows with a v3.0 counterpart (all rows except the three X rows GDM-1-009, 019, 026). Each GDM-2 row names the GDM-1 row it continues in flags. Adjustments:

- Merged (list level): GDM-1-012 and GDM-1-017 both traced to the same v3.0 sentence (post-deployment processes), so they are one v_i row here (GDM-2-011); GDM-1-029 and GDM-1-030 both traced to the 5.1 annual-update sentence, so they are one row (GDM-2-026). 2 merges.
- Split: GDM-1-025 covered Instrumental Reasoning Levels 1 and 2 as one row; in v3.1 they diverge (Level 1 becomes a TCL, Level 2 disappears), so it is split into GDM-2-022 and GDM-2-023. 1 split.
- Added from full text for v3.0: GDM-2-039 (security-adequacy override in 1.6), which GDM-1 recorded only in the flags of GDM-1-024. Of the 39 v_i rows, 20 quote v3.0 text that has no row in the v3.0 candidates file (CCL definitions, process steps, table cells, the 1.4 and 1.6 passages); these were already identified from full text in GDM-1.
- v_i rows: 39. Additions found in v3.1: 11 (GDM-2-040 to 050). Total 50.

Candidate accounting against the v3.0 candidates file (50 rows), for the schema: kept 31 (rows 3, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 27, 28, 30, 31, 32, 36, 37, 41, 44, 45, 46, 47, 48, 49); dropped 19 (description: 0, 1, 2, 4, 5, 24, 25, 29, 34, 38, 39, 40, 42, 43; definition: 6, 26, 35; statement of non-commitment about misalignment CCLs: 9; belief statement: 33). Of the kept, 10 were folded into another candidate's row (8 into 7; 17, 18, 19 into 16; 41 into 30; 32 into 31; 37 into 28; 46 into 44; 48 into 47; 36 into the gate row with 27).

v3.1 candidates (65 rows) were used as the starting list for additions; most are retained sentences (traced) or glossary definitions (excluded). Glossary entries were treated as definitions, not commitments, including 'will conduct additional testing on new versions as specified in Section 1.3', which restates 1.3.2.

## 2. Cases the codebook did not settle

1. Direction of the CCL-to-TCL move for Instrumental Reasoning Level 1 (GDM-2-022). The threshold gains a process (S on dims 6 and 4) but is re-tiered from 'critical' to 'tracked', that is from severe to significant harm. Coded S; the re-tiering is noted.
2. Whether Instrumental Reasoning Level 2 is removed or absorbed (GDM-2-023). Coded X, low confidence; the 3.2 tiered approach assigns higher misalignment risk to the ML R&D CCLs, which supports W or L.
3. Whether 'large scale internal deployments' to 'high-risk internal deployments' is a narrowing (GDM-2-012). Both directions present with the TCL extension; coded W per section 4, low confidence.
4. Whether alert thresholds drawing on 'expert assessments, and other sources of information' weakens the trigger (GDM-2-003). Coded W with alternative R.
5. Whether 'updated at least once a year' to 'reviewed at least once a year' is material (GDM-2-026). Coded W on dim 4; alternative R because v3.0 already said the update 'may' follow the assessment.
6. Whether the deferral clause 'the specific mitigations we implement may be determined when a T/CCL is reached' is an A row or a W on existing mitigation rows under the conditional-commitment rule (GDM-2-050). Coded A with the alternative stated.
7. Whether the footnote 4 exemption for low-risk external deployments is a change to the assessment trigger (coded on GDM-2-002 as W) or an A row.
8. Whether the 4.1 governance description and the insider-misuse determination are commitments (GDM-2-049, 048). Coded A, low confidence, alternatives exclude.
9. Whether mitigations contingent on a residual risk assessment (GDM-2-010) are stronger or weaker than an illustrative 'may be applied' monitor. Coded S on dim 4, with the contingency noted as a possible dim 6 weakening.
10. Announcement standard for structural additions under 'Included more detail on our risk management process' (see section 3).

## 3. Revision account: difficulties for announcement status

- The account is itemised (six bullets) but three bullets are generic ('Included more detail on our risk management process', 'Included description of our internal governance structure', 'Introduced a glossary'). The 'more detail' bullet was not treated as identifying any specific commitment or direction, following codebook section 6 (section mention is not enough). This decides SIL for GDM-2-002, 003, 006, 009, 011, 030, 045, 046, 050. If the adjudicator accepts the bullet as identifying additions to the risk management process, GDM-2-045, 046 and 050 (A rows) would become ANN; the W rows would remain SIL because the bullet gives no direction.
- Bullets 1 and 2 identify the TCL introduction and the misalignment restructuring, and were used as ANN for rows whose change is the TCL extension or the misalignment re-tiering (GDM-2-001, 010, 015, 022, 032, 040 to 044). Where a row combines an announced TCL extension with an unannounced change in the other direction (GDM-2-012), the announcement is coded for the W direction.
- Bullet 3 identifies the Security Level 2+ change (GDM-2-020) but not the SAIF paragraph (GDM-2-047) or the insider-misuse determination (GDM-2-048).
- The edited post section adds nothing beyond the TCL introduction and the generic 'more detail' statement.
- Not identified anywhere: the added condition (2) and footnote 4 exemption on the assessment trigger (GDM-2-002), 'updated' to 'reviewed' in 5.1 (GDM-2-026), the alert-threshold response (GDM-2-009), the security-adequacy override addition (GDM-2-039), the removal of Instrumental Reasoning Level 2 (GDM-2-023).

## 4. Low-confidence rows and alternative readings

- GDM-2-003 (EC2, W): continues GDM-1-003. Both directions present so W per section 4. Alternative reading R: added detail on the same alert-threshold mechanism. Alternative reading S (dim 1) for the TCL extension alone. Changelog line 'Included more detail on our risk management process' points at the section without identifying this commitment or its direction (codebook section 6: section mention is not enough); adjudicator may disagree.
- GDM-2-012 (EC6, W): continues GDM-1-013. Alternative reading S: the TCL extension is the dominant change and the large-scale to high-risk redefinition is a clarification. The TCL extension is identified by changelog bullet 1 ('outlined mitigation and risk acceptance process') but the redefinition of internal deployments is not; announcement coded for the W direction. Same redefinition appears in 1.3.5 and 3.1.2 item 2.
- GDM-2-023 (EC2, X): continues GDM-1-025. split (see GDM-2-022). Alternative reading W or L: the tiered approach in 3.2 assigns the higher misalignment tier to the ML R&D CCLs, so the object may be treated as merged into GDM-2-018 and GDM-2-019. Changelog bullet 2 identifies the incorporation of the misalignment domain but not the removal of this threshold; adjudicator may read it as ANN.
- GDM-2-048 (S, A): Alternative: exclude as a point-in-time assessment ('our current assessment ... indicates') rather than a commitment; only 'we monitor' is a standing practice. Changelog bullet 3 mentions insider threats in the context of Security Level 2+, not this determination.
- GDM-2-049 (G, A): Phrased as description ('We have in place') and names no body, officer or cadence; alternative: exclude as description. Confidence low on inclusion, not on announcement.

## 5. Verifier summary

GDM-2 verifier: 97 ok, 3 ok-fuzzy, 50 literal, 0 NOT FOUND over 50 rows x 3 fields. ok-fuzzy: GDM-2-002 v_i_text and GDM-2-033 v_i_text (inherited page-break quotes from GDM-1-002 and GDM-1-037), GDM-2-005 v_next_text (footnote 4 and page break between pages 5 and 6 of v3.1); each is flagged in the row.

## 6. Count tables

Per category and outcome:

| category | R | S | W | X | L | A | total |
|---|---|---|---|---|---|---|---|
| EC1 | 1 | 1 | 0 | 0 | 0 | 1 | 3 |
| EC2 | 6 | 2 | 3 | 1 | 0 | 3 | 15 |
| EC3 | 3 | 2 | 0 | 0 | 0 | 1 | 6 |
| EC4 | 1 | 0 | 0 | 0 | 0 | 0 | 1 |
| EC5 | 2 | 0 | 0 | 0 | 0 | 0 | 2 |
| EC6 | 1 | 2 | 1 | 0 | 0 | 2 | 6 |
| G | 4 | 0 | 1 | 0 | 0 | 1 | 6 |
| M | 3 | 1 | 0 | 0 | 0 | 1 | 5 |
| S | 2 | 1 | 1 | 0 | 0 | 2 | 6 |
| total | 23 | 9 | 6 | 1 | 0 | 11 | 50 |

Outcomes: {'R': 23, 'A': 11, 'S': 9, 'W': 6, 'X': 1}. Announcement: {'NA': 23, 'SIL': 15, 'ANN': 12}. Material rows: 27; of these ANN 12, SIL 15.


## 2.6 META-1

# META-1 tracing log: Meta Frontier AI Framework v1.1 (3 February 2025, original file) to Advanced AI Scaling Framework v2 (7 April 2026)

First-pass coder output. Every row is a proposal for adjudication. Codebook v0.1 applied (sections 2 to 6). Revision account: Appendix II change log inside v2 ('[changelog]') and the 8 April 2026 announcement post ('[post]'), both in the saved revision-account file. Per the pair instructions, the retitle (Frontier AI Framework to Advanced AI Scaling Framework) and the March 2025 silent edit of the v1.1 PDF are not part of this pair.

## 1. Candidate disposition (v1.1, 44 extractor rows)

| disposition | n | detail |
|---|---|---|
| kept (contributed to a row) | 26 | idx 42, 52, 60, 78, 80, 81, 83, 93, 105, 117, 118, 171, 176, 197, 268, 275, 280, 282, 284, 287, 289, 290, 313, 316, 318, 320 |
| dropped | 18 | see reason classes below |
| merge events | 7 | 52+171+197 (stop development, stated three times, plus Table 1 pause text) = 2 merges; 60+313+316+318 (framework updates) = 3; 78+80 (reference class) = 1; 105+287 (evaluations account for deployment context) = 1 |
| split events | 1 | idx 289 held two sentences: 'We may take into account monetary costs ...' (EC3, row 045) and 'we will not release the frontier AI externally' (EC6, merged into the High-threshold row 032) |
| rows from candidates | 20 | 26 kept minus 7 merges plus 1 split |
| rows added from full text | 29 | 002, 005, 008, 010, 011, 012, 014, 015, 016, 017, 019, 020, 021, 024, 026, 027, 028, 030, 033, 034, 035, 036, 037, 038, 039, 041, 047, 048, 050 |
| v1.1 commitment rows | 49 | |
| addition rows (A) from v2 | 57 | starting list: 107 v2 candidate rows, then the full v2 text |
| total rows | 106 | |

Drop reasons for the 18 dropped candidates:
- description of approach or benefit (10): idx 22, 26, 120, 127, 130, 131, 140, 164, 178, 179
- table of contents (2): idx 39, 266
- aspirational (2): idx 133, 145
- definition (2): idx 168, 354
- report of past action, not a standing commitment (1): idx 103 (CyberSecEval open-sourced)
- belief statement (1): idx 308 ('we believe that it is important to consider the benefits')

The extractor missed commitments whose subject is a table cell (Table 1 security and measures cells), a footnote (footnote 7 on senior-level approval of uplift assessments), an outcomes table (Cyber 1 to 3, CB 1 to 3) and present-tense process statements without a listed modal ('we conduct periodic threat modelling exercises', 'we conduct red teaming exercises once ...'). These account for the 29 rows added from full text.

## 2. Coding conventions applied in this pass (where the codebook did not settle the point)

U1. Present-tense practice statements. The codebook's include rule lists modal forms ('will', 'must', 'commit to', 'aim to', 'may', 'intend to'). Much of v1.1 and v2 states procedure in the present tense ('we conduct red teaming exercises once a model achieves certain levels of performance'). These were included where they specify a procedure the developer follows (who, what, when), and excluded where they describe an approach or a benefit. The alternative (modal-only inclusion) would remove roughly a third of the v1.1 rows and most of the section 4.2.1 to 4.2.3 A rows. Confidence for such rows is at most medium unless the text is identical across versions.

U2. Definitions that set scope. Row 001 (Frontier AI definition) is kept although the codebook excludes definitions, because the definition fixes which models every other commitment applies to and the change log announces its revision. Alternative: drop. Low confidence. The inclusion criteria for catastrophic outcomes (3.2/3.3 'Plausible, Catastrophic, Net new, Instantaneous or irremediable') were dropped as definitions; note that v2 changes 'Net new' to add 'but without access to general-purpose AI' and adds a sentence that harms not meeting all four criteria 'are addressed through other safety and integrity processes outside of the scope of this Framework'. If the adjudicator keeps definitions, these are candidate rows.

U3. Outcome tables as commitments. Rows 038 (Cyber 1 to 3) and 039 (CB 1 to 3) treat the catastrophic-outcome definitions as EC1 scope commitments, following example F's treatment of threshold definitions. Alternative: R or exclusion as descriptions.

U4. One announced vocabulary change, several rows. The change log announces one replacement ('uniquely enable' to 'substantially contribute to'). It is the material change in rows 009, 025, 027 and 028, each of which governs a different object (threat-modelling trigger, evaluation design, critical threshold, high/moderate boundary). All four are coded ANN with pointer P_STD. The adjudicator may prefer to count the change once. Direction: coded S for 009, 025 and 027 (a lower bar for triggering threat modelling, further evaluation and the critical threshold) and W for 028 (direction undetermined; conservative call). The threshold consequences (rows 003, 032) are coded W separately.

U5. Class-level change-log clause and preparedness-report content. The change log line 'Defined criteria for publishing preparedness reports, including content requirements, update triggers, and internal-use risk reporting' names classes. Rows were coded ANN where the account points at the commitment itself (the publication commitment 023; the content items the post lists by name, row 053; update obligation 064; internal-use assessment and report 065 and 066; expedited updates 067; model spec 068 and 069) and SIL for the remaining content items (050, 054, 058 to 061, 063), each flagged with the class-level alternative. Rows 064, 065 and 067 are medium confidence because 'update triggers' and 'internal-use risk reporting' are named but not restated.

U6. Loss of Control procedures. 'Added Loss of Control as a risk domain' announces the domain (row 036, ANN, high). The two-stage LoC evaluation procedure (row 096) is coded ANN medium on the reading that adding an outcomes-led domain entails its evaluation; the specific checkpoint tasks, propensity thresholds, safety-case step and mitigation focus areas (097 to 100) are SIL, each flagged with the alternative. The same logic was not extended to the cyber operational thresholds (082 to 089), which are new and unmentioned in either account.

U7. Both-directions rows. Rows 030 (critical security: access restriction removed, named oversight added), 032 (High: prohibition becomes conditional permission; validation requirement added), 035 (threshold assignment: officers named; third-party involvement clause not repeated, coded S with W as alternative) and 038 (cyber outcomes) carry both directions; 030, 032 and 038 are coded W per codebook section 4, with both directions in the rationale.

U8. Table 1 'Moderate or lower' relabel. 'Release' to 'Deploy' is announced in the change log but treated as a relabel, not a material change (row 034, R).

U9. Domain-specific restatements. v2 4.2.2 restates the High rule ('we will not deploy the model externally unless we have strong additional evidence that mitigations are sufficiently robust') and defines high and critical for CB. The first is used as part of the counterpart in row 032 rather than as an A row; the second is an A row (091) with the overlap flagged.

U10. Category for the model spec (068). Coded EC5 as a publication commitment; G or M are defensible.

## 3. Low-confidence rows (20) with alternative readings

- META-1-001 (S): Codebook section 2 excludes definitions; this row is kept because the definition fixes which models every other commitment applies to (dim 1). Alternative reading: drop as a definition, or W because the capability comparison is now restricted to catastrophic-risk domains. Merged candidate idx42 (1.1 Scope sentence) with the appendix definition.
- META-1-007 (W): Alternative readings: R (the practice is retained and 'models with new capabilities' is a rewording), or S (a wider set of models is covered). Coded W because a specific trigger becomes unspecified, following the logic of example F.
- META-1-022 (X): Alternative readings: W on dim 4 (intend -> 'we see this as a key benefit'), with the v2 2.2 sentence as counterpart; or drop as a release-strategy statement outside the safety commitments. Category M is a best fit; the statement is about release approach, not a safeguard.
- META-1-023 (S): Trace is contestable. Alternative: the same-place v2 sentence 'We also plan to continue sharing relevant information about how we develop and evaluate our models responsibly by providing guidance to model deployers through resources like our Developer Use Guide' is the counterpart, in which case 'model cards and research papers' are no longer named and the code would be W on dim 5. The content requirements of preparedness reports are coded as separate A rows.
- META-1-028 (W): Added from full text; High and Moderate definitions merged because they define one boundary. Direction is genuinely undetermined: 'substantially contribute' (Appendix I: 'a material factor in a given outcome') may be a higher bar than capability uplift (W) or 'could' may be a lower bar than 'provides' (S). W chosen as the conservative call per codebook section 4; alternative S or R. The section 1.1 sentence changes from 'high and moderate risk thresholds are defined in terms of the level of uplift' to 'thresholds for weaponization are defined in terms of the level of uplift'.
- META-1-029 (W): Alternative reading: X (the 3.3 commitment is removed and the 4.3 sentence is not a counterpart because it existed in v1.1 alongside it). The Table 1 note in v2 ('Final deployment decisions may also consider additional factors beyond those covered in this Framework') is a further candidate counterpart.
- META-1-030 (W): Added from full text. Both directions noted. Alternative reading on announcement: ANN via the change log clause 'with security processes commensurate with the threshold initiated', which describes the new wording but does not say the access restriction was loosened. Stratum rule: security expressed as a consequence of the threshold, so EC6 not S.
- META-1-031 (X): Merged Table 1 Critical process bullets with candidate idx284 (4.2). Source typo 'threshol' retained. Alternative reading: W with the v2 2.1.3 sentence 'This usually takes the form of a threat modeling exercise to determine the degree to which the model substantially contributes to a threat scenario' as a generalised counterpart. The 'do not further develop' clause is coded in the stop-development row.
- META-1-033 (W): Added from full text. Alternative readings: R (rewording of the same security measure) or ANN via the change log clause 'with security processes commensurate with the threshold initiated'. Stratum rule: EC6 not S.
- META-1-035 (S): Added from full text (footnote missed by the extractor). The v1.1 clause 'with the involvement of numerous experts – including third parties where appropriate' is not repeated in the v2 counterpart, which would be a weakening on dim 3 and, under the both-directions rule, W; external-expert involvement in the risk assessment survives elsewhere in v2 (2.1.2, 2.2). Alternative reading: W. 'Risk2' in the v2 quote is a footnote marker in the source.
- META-1-038 (W): Added from full text. Both directions present; W chosen per the both-directions rule. Alternative readings: S (Cyber 1 now covers any cyberattack that 'substantially lowers the barrier', not only end-to-end compromise of a protected corporate environment) or R (outcome descriptions rather than commitments). Threat scenarios and example enabling capabilities also changed; treated as examples. The hyphenated line breaks in the v1.1 text file are reproduced as in the file.
- META-1-041 (W): Added from full text. Alternative reading: R (the first-checkpoint wording was descriptive and 'We typically repeat evaluations as a Frontier AI model nears or completes training' is retained). v2 adds 'propensities' to what is measured, which could be read as S on dim 1.
- META-1-049 (S): Added from full text. Research-focus statement ('we’ll continue to work on'); alternative reading R, treating the change as wording in an aspirational statement, or exclusion as aspirational.
- META-1-075 (A): Alternative reading: not a distinct commitment but a restatement of preparedness-report content; or R against v1.1's 'plan to continue sharing relevant information'.
- META-1-079 (A): Weak modal ('may additionally explore'); alternative reading: exclude as aspirational.
- META-1-090 (A): Alternative reading: exclude as aspirational or outside the framework's scope (ecosystem defence rather than model safeguard).
- META-1-100 (A): Stated as focus areas rather than measures; alternative reading: exclude as aspirational.
- META-1-102 (A): Alternative reading: exclude as aspirational ('in the future we may'). The change log names physical autonomy as an emerging area.
- META-1-105 (A): Weak modal; alternative reading: exclude as aspirational.
- META-1-106 (A): Alternative readings: R against the v1.1 2.2 sentence 'open sourcing advanced models makes it possible for us to ... work with outside experts to improve our own evaluation of risk' (dropped in this pass as a description of a benefit), or exclude as description.

## 4. Revision account: what made announcement status hard to judge

- The change log is itemised at the level of themes ('Revised thresholds', 'Expanded governance and accountability', 'Added transparency requirements'). Sub-clauses name specific changes (Stop to Develop with Mitigations; Do not release to Deploy with mitigations; officers named; whistleblower protocols; incident response; model spec; Frontier AI definition) but most section 4.2 operational content (cyber CTF thresholds, BioTIER criteria, LoC checkpoint tasks, elicitation standards, held-out evaluations, weight-security baseline) is not mentioned at all.
- 'All thresholds now permit proceeding with sufficient mitigations validated to reduce risk to moderate or lower, with security processes commensurate with the threshold initiated.' The clause on security processes describes the new Table 1 wording but does not say that the access restrictions ('strictly limited to a small number of experts'; 'limited to a core research team') were replaced. Rows 030 and 033 are SIL with ANN as the alternative.
- The post is narrative and mostly about the Muse Spark report. Two sentences identify report content ('These reports will detail our risk assessments, evaluation results, the rationale behind our deployment decisions, and any limitations') and limitations disclosure ('where our evaluations fell short'); these support ANN for rows 053 and 062. 'These standards apply across our frontier deployments, whether they’re open, controlled API access, or closed models' does not identify the new controlled-deployment assessments (051, 052).
- Nothing in either account mentions: the annual review cadence (004), the removal of the barrier-investigation procedure (031), the removal of the intention to continue open release (022), the removal of the 'take into account both potential risks and benefits' sentence (029), the widening of mitigation-robustness evaluation to all models (046), or the cyber and CB outcome redefinitions (038, 039).
- The newsroom post of 3 February 2025 was re-dated 20 April 2026 with a link to v2 but its body is unchanged; it was not used.

## 5. Verifier summary

Verifier run on all 106 rows against META-1_v_i.txt, META-1_v_next.txt and META-1_revision_account.md, with the '[changelog]' / '[post]' prefixes stripped from changelog_pointer before matching (the prefixes are not in the source file).

changelog_pointer literal: 81, changelog_pointer ok: 25, v_i_text literal: 57, v_i_text ok: 49, v_next_text literal: 2, v_next_text ok: 101, v_next_text ok-fuzzy: 3

ok-fuzzy (3), all page-break or footnote interruptions in the v2 text file, stated in flags: 009 (page 4 to 5), 015 (footnote 1 and page 5 to 6), 025 (page 25 to 26). No NOT FOUND remains. Two v2 quotes contain source footnote markers ('Risk2' in 035; '(CTF)6' and 'mode,7' in 082) and one v1.1 quote retains the source typo 'threshol' (031); none were cleaned up.

## 6. Count tables

Outcome: {'S': 12, 'R': 26, 'W': 9, 'X': 2, 'A': 57}
Announcement: {'ANN': 25, 'NA': 26, 'SIL': 55}
Confidence: {'low': 20, 'high': 45, 'medium': 41}

Material rows: 80; SIL share among material rows (provisional first-pass SRR, not a result): all 55/80; evidentiary EC1 to EC6 42/62; non-evidentiary G/S/M 13/18.

Category by outcome:

| category | R | S | W | X | L | A | total |
|---|---|---|---|---|---|---|---|
| EC1 | 0 | 2 | 1 | 0 | 0 | 2 | 5 |
| EC2 | 2 | 2 | 2 | 0 | 0 | 9 | 15 |
| EC3 | 11 | 3 | 1 | 0 | 0 | 12 | 27 |
| EC4 | 4 | 0 | 0 | 0 | 0 | 2 | 6 |
| EC5 | 1 | 1 | 0 | 0 | 0 | 14 | 16 |
| EC6 | 2 | 1 | 4 | 1 | 0 | 5 | 13 |
| G | 4 | 3 | 1 | 0 | 0 | 7 | 15 |
| S | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| M | 2 | 0 | 0 | 1 | 0 | 5 | 8 |
| total | 26 | 12 | 9 | 2 | 0 | 57 | 106 |

## 7. Self-check

- Every row has an outcome, a non-blank material value, and (for S/W/X/A) an announcement status with a verbatim pointer or NONE FOUND; R rows carry NA.
- No L rows: Meta has no companion document for this pair; 'companion?' was not needed.
- No paraphrase in v_i_text, v_next_text or changelog_pointer; internal ellipses mark elided source text only.
- Splits: 1 in v1.1 (idx 289) and 2 in v2 (controlled-deployment sentence pair 051/052; internal-use sentence 065/066), each flagged 'split'.
- Calibration examples cited after checking against the texts: A (003), B (076, direction differs), F (007, 082), J (021, reverse direction).


## 2.7 MSFT-1

# MSFT-1 coding log: Microsoft Frontier Governance Framework, v1 (February 2025) to feb-2026

Pair: MSFT-1. Provider: Microsoft. v_i = 'v1' (original February 2025 rendering, not the reupload). v_next = 'feb-2026'. Revision account: Appendix II change log inside the February 2026 edition. No announcement post exists. Pointers are prefixed '[changelog]'.

Output: `MSFT-1_tracing.csv`, 48 rows (40 traced from v1, 8 additions).

## 1. Candidate accounting (v_i candidates file, 22 rows)

| Disposition | n | Sentence indices | Reason class |
|---|---|---|---|
| Kept as a commitment row | 16 | 26, 39, 51, 63, 64, 82, 90, 117, 125, 127, 133, 134, 136, 137, 141, 146 | |
| Merged into another candidate | 1 | 95 (into 90) | verbatim duplicate paragraph in the v1 source |
| Dropped | 5 | 2, 3, 21, 34, 45 | 2, 3, 45: description of the framework or of the broader governance programme; 21: description/aspirational ('we expect will be revised'); 34: description duplicating the section 3 rules coded in rows 003 to 008 |
| Split | 1 | (full-text passage) | the 'Capability evaluation' bullet was split into method/documentation (011) and third-party involvement (012); its new disclosure sentence is the A row 042 |
| Added from full text | 24 | rows 003, 005, 006, 007, 008, 011, 012, 013, 014, 016, 017, 019, 020, 021, 022, 023, 024, 025, 027, 028, 031, 032, 033, 034 | present-tense rule statements ('is run', 'are subject to', 'we apply') and named-role sentences the modal-verb extractor missed |

Candidate s39 ('We will revisit our list of tracked capabilities frequently') was merged with the two preceding sentences of the same paragraph (not candidates) to form row 002, because the v_next counterpart rewrites the whole paragraph.

v_next candidates file (21 rows): 19 are counterparts of traced v1 rows; s156 and s159 are additions (rows 044, 046); s126 is part of the rewritten monitoring bullet (row 026). Six further additions were found from the full text (041, 042, 043, 045, 047, 048).

## 2. Cases the codebook does not settle

1. Present-tense rule statements. Microsoft states most of its substantive rules in the present indicative ('A leading indicator assessment is run on any model that...', 'Models posing critical risk ... are subject to'). Codebook section 2 lists modal examples but the rule is 'phrased as a commitment by the developer about its own practice, at any strength'. I included present-tense rule statements as commitments. Excluding them would remove 24 of the 40 v1 rows, including the leading-indicator trigger (004), the third-party clause (012) and the holistic-assessment modal drift (014). The adjudicator should confirm this reading; it applies to every provider whose framework is written in this register.
2. Announcement direction for itemised but direction-free lines. Three account lines point clearly at a specific commitment but use 'Adjusting' or 'Aligning' with no direction: 'Adjusting the update cadence to align with regulatory obligations' (row 036, six to twelve months), 'Adjusting the cadence by which we repeat deeper capability assessment to align with emerging industry standards' (row 015, six-monthly to event-triggered), 'Aligning the scope our framework to that of regulations' (row 004, capability and compute triggers replaced by legal scope). Codebook section 6 requires that a reader 'would know that this commitment changed in this direction' but also says the account 'must point at the commitment'. I coded ANN (medium confidence) because the commitment is identified; SIL is the alternative if direction is required strictly. This decision moves three of the five ANN rows and therefore the pair's SRR (ANN 5 of 21 material rows as coded; 2 of 21 under the strict reading).
3. Which commitment 'update cadence' refers to. The line could refer to the review-frequency commitment (036) or to the publication-timing commitment (038, 'at the same time' to 'within 30 days'), since both changed and both match regulatory terms. I attached it to 036 (cadence = frequency) and coded 038 SIL with low confidence.
4. Internal documentation content as a materiality dimension. Row 011 adds 'assumptions regarding the model' and 'assumptions underlying the evaluation' to what evaluation documentation must contain. Dimension 5 (disclosure scope) is the nearest fit but the codebook's dimension 5 concerns publication. Coded S, dim 5, low confidence; R is the alternative.
5. Both-directions rule on conditional wording. Rows 026 and 038 combine clear strengthening (incident response and regulatory reporting; unconditional 30-day publication of material revisions) with a shift to 'may' or a later deadline. The codebook's rule (section 4) requires W. Both are coded W with low confidence and S stated as the alternative; the adjudicator may judge that the 'may' in 026 ('Customer documentation may also be adjusted ... as needed') is not a material drop from 'adjust customer documentation as needed'.
6. Additions versus changes to existing commitments. Example I says a new condition on an existing commitment is a change, not A. I applied this to the incident-response addition (026) but coded the fine-tuning trigger (048), regulatory reporting (041), third-party disclosure (042) and the RAND benchmark (045) as A rows because each introduces a new object (model class, audience, disclosure subject, benchmark). Each flag names the fold-in alternative.
7. Aspirational self-commitments. Rows 023 and 039 ('will continue to contribute to research', 'will prioritize ongoing contributions ... and expand its collaboration') are self-commitments but concern contributions to the field. Kept (both R) with the drop alternative flagged.
8. Definitions removed by footnote reuse. Row 008: footnote 2 in v1 defined 'frontier capabilities', the term that triggers deeper capability assessment; in v_next footnote 2 is about fine-tuning compute and no definition survives. Coded W dim 2 (example F) with medium confidence; the alternative is that this is an editorial casualty rather than a rule change.

## 3. Low-confidence rows and their alternative readings

- **MSFT-1-002** (W): Alternative readings: (a) X, if the counterpart paragraph is read as not governing the 'revisit the list' object; (b) S, if the named identification methods and external-expert input outweigh loss of the 'frequently' cadence; (c) R, if the process description is read as carrying the same force as 'will revisit'. Category alternative EC1 (object is the evaluation scope list). Merged candidate s39 with the two preceding sentences of the same paragraph. Only candidate account line is the generic 'Other edits and additions for clarity and transparency', which does not identify this commitment.
- **MSFT-1-005** (X): Alternative: merge into MSFT-1-004 as a fragment of the trigger commitment (the trigger was in fact revisited and replaced, so the revisit commitment is moot); under that reading the account line 'Aligning the scope our framework to that of regulations' would cover it (ANN). The account does not identify removal of a revisit commitment as such.
- **MSFT-1-011** (S): Added from full text. Alternative: R, if added documentation elements are read as elaboration that does not alter the rule; dim 5 is used for internal documentation content, which the codebook does not explicitly cover (unsettled). v_i quote spans a page break in the text file (header interrupts 'robustness of the evaluation / method used'); expect ok-fuzzy. The third-party sentences of this bullet are coded separately as MSFT-1-012 and MSFT-1-042. Only candidate account line is the generic 'Other edits and additions for clarity and transparency', which does not identify this commitment.
- **MSFT-1-026** (W): Added from full text. Alternative: S, if 'may also be adjusted ... as needed' is read as no weaker than 'adjust ... as needed' because both are already conditional; the adjudicator should decide whether the new 'may' is material. A further alternative is a separate A row (EC5) for regulatory incident reporting; per example I it is coded here as a change to the existing commitment. The account's header sentence names the RAISE Act and TFAIA, which impose incident reporting, but no line identifies this change. Only candidate account line is the generic 'Other edits and additions for clarity and transparency', which does not identify this commitment.
- **MSFT-1-038** (W): Alternative: S, if the removal of 'Where appropriate' as a condition on publication is judged to dominate the later deadline. Category alternative EC5 (disclosure of framework changes). Announcement alternative ANN via 'Adjusting the update cadence to align with regulatory obligations' if 'update cadence' is read to include publication timing (the 30-day term matches a regulatory publication deadline); coded SIL because 'cadence' most naturally refers to review frequency (MSFT-1-036) and a reader could not tell which commitment is meant.
- **MSFT-1-045** (A): Alternative: S on MSFT-1-019 (the same best-practice-sources commitment gains a named benchmark) or R (a reference, not a requirement). 'we also reference' is weak force. Only candidate account line is the generic 'Other edits and additions for clarity and transparency', which does not identify this commitment.
- **MSFT-1-046** (A): Alternative: merge into MSFT-1-035 as elaboration of 'We will update our framework to keep pace with new developments' (then R, not A). Only candidate account line is the generic 'Other edits and additions for clarity and transparency', which does not identify this commitment.
- **MSFT-1-047** (A): Alternative ANN: the account line 'Adding harmful manipulation and loss of control as tracked high-risk capabilities' announces the capability addition but does not identify a usage prohibition; a reader of the account would not know this mitigation was added. Alternative: description of existing product terms rather than a framework commitment (drop). The 'We are researching approaches to evaluating' sentences for the two new capabilities are treated as research descriptions, not commitments, and are noted in MSFT-1-001.

## 4. The revision account

The account is a six-bullet change log in Appendix II. Five bullets are specific; the sixth ('Other edits and additions for clarity and transparency') is generic and was not used for ANN. Difficulties: (a) the specific bullets use 'Adjusting' and 'Aligning' without stating direction (see section 2, items 2 and 3); (b) the header sentence names the EU Code of Practice, the NY RAISE Act and the CA TFAIA, which would lead an informed reader to expect the regulatory-reporting and incident-response additions (041, 026), but no bullet identifies them, so they are SIL; (c) 'Adding harmful manipulation and loss of control as tracked high-risk capabilities' announces the scope change (001) but not the usage prohibition added under harmful manipulation (047), coded SIL with ANN as the alternative. No announcement post exists, so the change log is the whole account.

Pointer verification: the pair instruction requires the '[changelog]' prefix on pointers; the verifier tests substring containment, so pointers were verified with the prefix stripped. All five returned 'ok'.

## 5. Verifier summary

`{('v_i_text', 'ok'): 39, ('v_next_text', 'ok'): 47, ('changelog_pointer', 'ok'): 5, ('changelog_pointer', 'literal'): 43, ('v_next_text', 'literal'): 1, ('v_i_text', 'ok-fuzzy'): 1, ('v_i_text', 'literal'): 8}`

The single 'ok-fuzzy' is row 011 v_i_text: the sentence 'a statement on the robustness of the evaluation method used' crosses a page break in the text file and the page header interrupts it. The quote is verbatim as the sentence reads; the flag says so. No 'NOT FOUND'.

## 6. Count tables

Category by outcome (all 48 rows):

| category | A | R | S | W | X | All |
|---|---|---|---|---|---|---|
| EC1 | 0 | 0 | 1 | 0 | 0 | 1 |
| EC2 | 1 | 2 | 1 | 3 | 1 | 8 |
| EC3 | 1 | 4 | 1 | 1 | 0 | 7 |
| EC4 | 0 | 0 | 1 | 0 | 0 | 1 |
| EC5 | 2 | 2 | 0 | 0 | 0 | 4 |
| EC6 | 0 | 6 | 0 | 0 | 0 | 6 |
| G | 2 | 8 | 0 | 3 | 0 | 13 |
| M | 1 | 3 | 0 | 1 | 0 | 5 |
| S | 1 | 2 | 0 | 0 | 0 | 3 |
| All | 8 | 27 | 4 | 8 | 1 | 48 |

Announcement by outcome (21 material rows):

| outcome | ANN | SIL | All |
|---|---|---|---|
| A | 1 | 7 | 8 |
| S | 1 | 3 | 4 |
| W | 3 | 5 | 8 |
| X | 0 | 1 | 1 |
| All | 5 | 16 | 21 |

Confidence: high 25, medium 15, low 8.

Evidentiary stratum (EC1 to EC6) material rows: 13, of which ANN 4. Non-evidentiary stratum (G, S, M) material rows: 8, of which ANN 1.

## 7. Self-check

Every row has an outcome and a non-blank `material`; every material row has ANN or SIL and a pointer or NONE FOUND; every R row has NA in both announcement fields; A rows have v_i_text NONE and the X row has v_next_text NONE; all quotes are at most 80 words (truncated with an ellipsis where longer). v_i is the original February 2025 rendering (the text file carries 'Version 1 (February 2025)' page footers and the change log reads 'February 2025 – First version'). No source outside the two texts and the change log was used.


## 2.8 NAV-1

# NAV-1 first-pass tracing log

Pair: Naver, v_i = 2024 (NAVER's AI Safety Framework, English web page), v_next = v2.0 (NAVER ASF 2.0, English PDF). Revision account: PDF section 2 ('The Direction of ASF 2.0') plus the English press release of 8 July 2026. The Korean press release was ignored as instructed. Codebook v0.1 applied. Output: `NAV-1_tracing.csv`, 26 rows.

## 1. Building the v_i commitment list

The candidates file for v_i has 5 rows. The 2024 page is short and mostly written in the present indicative, so the extractor's modal-verb filter missed most of the operative rules. The full text was read and the list rebuilt from it.

Candidate disposition (5 rows):

| candidate (sentence index) | disposition | reason class |
|---|---|---|
| 2 ('our aim is to help people benefit from AI') | dropped | aspirational |
| 7 ('will be continuously updated') | kept, NAV-1-001 | |
| 19 ('will continue to work toward achieving AI safety') | dropped | aspirational |
| 20 ('outlines specific actions for everyone at NAVER ... committed to our AI Principles') | dropped | description (the modal attaches to staff, not to a practice) |
| 35 (matrix cell block plus 'we must implement appropriate guardrails') | kept and split into NAV-1-009, -010, -011, and contributes to -013 | |

Counts: candidates 5; kept 2; dropped 3; merged 6 (rows 002, 003, 005, 008, 009 and 015 were each formed by merging two or more fragments of one commitment, adjacent or not); split 2 (the sentence 'We should only deploy AI systems if those safeguards have proven effective ... and keep an eye on the systems even after deployment' split into 009 and 013; candidate 35's matrix block split into per-cell consequence rows 010 and 011); added from full text 13 (002, 003, 004, 005, 006, 007, 008, 012, 013, 014, 015, 016, 017). Total v_i rows 17.

Full-text passages considered and dropped, with reason class:

- 'We identify, assess, and manage risks at all stages of AI systems operations, from development to deployment.' Description (framework overview). Unsettled, see section 3.
- 'At NAVER, we take this risk seriously as we continually apply our standards to look for signs of alarm.' Aspirational; folded into NAV-1-002's quote as context rather than coded alone.
- 'To mitigate such risks, we have to place appropriate safeguards around AI technology.' Aspirational, no object.
- Definitions of hyper-scale, frontier and future AI. Definition.
- 'the amount of computing can serve as an indicator when measuring capabilities.' Description ('can serve'); no commitment to use compute as a trigger.
- 'We draw from our AI Principles and research studies to implement guardrails around AI models.' Description of source.
- 'Our partnerships with academia ... have led to meaningful research in building local datasets'. Report.
- 'We apply *SQuARe , KosBi , *KoBBQ datasets built from our research to our HyperCLOVA X models.' Report of current practice on named models. Unsettled, see section 3; flagged on NAV-1-006.
- 'Building trust in AI is a collective effort'. Aspirational.
- 'In April this year, we held our first Generative AI Red Teaming Challenge ...'. Point-in-time report (codebook section 10). Noted: this is the only red-teaming passage in v_i and there is no standing red-teaming commitment in either version.
- Table-of-contents style fragments of the two matrices (axis labels, 'Low', 'High', 'Use cases'). TOC/duplicate.

## 2. Additions from v_next

The candidates file for v_next has 18 rows. Disposition: 4 became A rows (98 -> 019; 229 -> 021; 235 -> 022; 238 -> 023); 7 served as counterparts of v_i rows (35 -> 001; 88 -> 003; 223 -> 011; 240 -> 017; 276 -> 014; 295 duplicates 001's counterpart); 7 dropped (44 revision rationale not a commitment; 46 general framing; 84, 233, 281, 290, 297 aspirational; 192 process description used as counterpart for 008). Full-text scan added 5 further A rows (018, 020, 024, 025, 026). Total A rows 9.

Passages in v_next considered and not made into rows: the three-pillar overview in section 2 (description); 'NAVER designs services with safety in mind throughout the entire service lifecycle, conducts evaluations, and continues to oversee safety even after launch' (overlaps 013 and 020); 'We will work to ensure that the experience accumulated ... becomes a shared asset for all of society' (aspirational); the AI Safety Center's establishment (folded into 015 as the actor change rather than coded as a separate A); the NAVER AI Safety Progress Report (folded into 014).

## 3. Cases the codebook does not settle

1. Present-tense practice statements. Codebook section 2 lists modal strengths ('will', 'must', 'aim to', 'may') but not the present indicative ('we use', 'we conduct'). Both Naver documents state most rules this way. Decision taken: present-tense statements with a specific object and a specific action are coded as commitments; present-tense overview statements without a specific object are dropped as description. If the adjudicator rejects present-tense statements, rows 003, 006, 007, 008, 013, 014, 016, 017, 021, 023, 025, 026 fall away.
2. Direction of a lateral restructuring (NAV-1-007). The assessment criteria were replaced (use case x need for guardrails -> domain x scope x impact). Section 5 makes this material (dim 2) but sections 4 and 5 give no code for a change with no clear direction. Coded W under the 'both directions -> W' rule; S is the alternative; a 'lateral' code does not exist.
3. Scope changes with mixed direction (NAV-1-003, -004). The risk-domain scope loses a named catastrophic object (biochemical weapons; loss of control) and gains user-protection domains. Coded per row; see flags. Whether the taxonomy's protected values should be one A row or two (018, 019) is left to the adjudicator.
4. Removal plus addition versus single weakening (NAV-1-005 and NAV-1-020). Section 3 requires the same object for a counterpart; the quarterly / 6x trigger governs loss-of-control evaluation of frontier models and the pre/post-launch impact assessments govern services, so they were coded X and A. Example F supports the alternative single-W reading. If merged, material changes fall from 22 to 21 and the announced count is unchanged (both rows are ANN).
5. Report versus standing commitment for named datasets ('We apply SQuARe, KoSBi, KoBBQ datasets ... to our HyperCLOVA X models'). Dropped as report; alternative is to merge into NAV-1-006.
6. Category for user-facing transparency (022, 023): EC5 is defined around evaluation methods and results; these concern disclosure of AI use to users. Coded M with EC5 flagged.
7. Category for external collaboration (016, 025, 026): EC4 is defined around evaluation, access and audit. Only 025 names evaluations, so 025 is EC4 and 016 and 026 are G.
8. Announcement standard when the coded direction is W by the mixed-direction rule but the account describes the S side. Rule applied: ANN when the account identifies the specific commitment as replaced or changed and its description does not contradict the coded change (007); SIL when the account announces only a broadening and a reader could not infer the removal or narrowing coded (002, 003). Recorded so the adjudicator can apply a different rule uniformly.

## 4. Low-confidence rows and alternative readings

| row | code | alternative |
|---|---|---|
| NAV-1-003 | W, SIL | S (biochemical misuse subsumed under life and physical safety), then ANN via 'Safety management scope expanded to focus on users and services' |
| NAV-1-006 | X, SIL | W (reduced specificity, example G) tracing to section 2 'within their sociotechnical context' |
| NAV-1-007 | W, ANN | S (more detailed criteria) or a lateral change without direction |
| NAV-1-008 | W, SIL | R (similar generality) or S (emergent-risk capture added) |
| NAV-1-011 | W, SIL | X (cell not accepted as counterpart) |
| NAV-1-012 | W, SIL | X (special-use capability concept absent from v2.0) |
| NAV-1-015 | S, SIL | R (same three-tier shape, renamed) or W (example J, layer 1 de-specified) |
| NAV-1-018 | A, SIL | ANN via 'extending it to encompass user protection'; or merge with 019 as one taxonomy row |
| NAV-1-019 | A, SIL | as 018 |
| NAV-1-021 | A, SIL | counterpart of 008 or 005 rather than an addition; ANN via 'conduct ongoing safety assessments' |

Medium-confidence rows with a stated alternative: 002 (ANN via the 'performance and risk levels of AI models' sentence), 004 (W or X), 005 (W merged with 020; SIL because the cadence is not named), 009 (R), 010 (X), 013 (S; category M), 014 (R; category G), 016 (W, example J), 017 (S), 020 (merge with 005), 022 and 023 (EC5; merge), 025 (ANN via 'expanded external collaboration'), 026 (SIL because 'expanded external collaboration' is near-generic; category EC4).

## 5. The revision account

- The account is narrative (section 2 of the PDF plus the press release). No itemised changelog, no redline, no version-history table.
- Section 2 describes the drivers of the revision and the new structure; it does not state what was removed. Nothing in section 2 identifies any individual v_i commitment.
- The press release carries the only change statements: scope moved from models to services; 'a single performance-based criterion' replaced by context, use case and impact criteria; 'more detailed classification and impact assessment criteria'; CHEC 2.0 established; 'expanded external collaboration'; lifecycle-wide safety reviews. These support ANN on 004, 005, 007, 020, 024, 026.
- Change statements exist elsewhere in the PDF but outside the account as defined for this pair: section 3 ('Building on the misuse risks defined in "NAVER ASF Beta", we have refined and classified them'), section 6 ('In establishing ASF 2.0, we strengthened the safety of AI models and services as well as user communication regarding AI-generated content'), section 7 ('ASF 2.0 has advanced the existing AI Safety governance structure into a three-layer management and oversight system'). If the account boundary were the whole PDF, rows 003, 015, 022 and 023 would move toward ANN. Recorded here for the author's decision.
- None of the account text mentions the loss-of-control risk category, the quarterly cadence, the 6x trigger, the 'do not deploy' consequence, the authorised-user restriction, or the special-use capability restriction. The removals and consequence weakenings (002, 009, 010, 011, 012) are therefore SIL with no near-miss quote.
- Pointer prefixes '[press release]' were used as instructed. No '[section 2]' pointer was needed because section 2 identifies no specific change.

## 6. Verifier

`verify_rows.py` run on all 26 rows against `NAV-1_v_i.txt`, `NAV-1_v_next.txt` and `NAV-1_revision_account.md`.

With the locator prefix '[press release] ' stripped from `changelog_pointer` before matching (the prefix is a locator, not part of the quote): v_i_text ok 17, literal 9; v_next_text ok 23, literal 3; changelog_pointer ok 6, literal 20. No 'ok-fuzzy', no 'NOT FOUND'.

With the prefix retained: identical except changelog_pointer ok-fuzzy 6 (shingle coverage above 0.75 because the prefix words are not in the account). Both runs are within the accepted set.

Source typos preserved in quotes: 'High riskDo not deploy', 'Risk identifiedOpen AI systems', 'Low riskDeploy AI systems' (the 2024 page runs the cell label into the cell text). Merged non-adjacent fragments are joined with ' ... ' and occur in document order.

## 7. Counts

Per category and outcome:

| category | R | S | W | X | L | A | total |
|---|---|---|---|---|---|---|---|
| EC1 | 0 | 1 | 1 | 1 | 0 | 2 | 5 |
| EC2 | 0 | 0 | 1 | 1 | 0 | 1 | 3 |
| EC3 | 0 | 0 | 1 | 1 | 0 | 1 | 3 |
| EC4 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| EC5 | 0 | 1 | 0 | 0 | 0 | 0 | 1 |
| EC6 | 1 | 0 | 4 | 0 | 0 | 0 | 5 |
| G | 2 | 1 | 0 | 0 | 0 | 2 | 5 |
| S | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| M | 1 | 0 | 0 | 0 | 0 | 2 | 3 |
| total | 4 | 3 | 7 | 3 | 0 | 9 | 26 |

Announcement: ANN 6, SIL 16, NA 4 (R rows). Material changes 22; announced 6; silent 16. Evidentiary stratum (EC1 to EC6): 18 rows, 17 material, ANN 4, SIL 13. Non-evidentiary stratum (G, M): 8 rows, 5 material, ANN 2, SIL 3. Confidence: high 2, medium 14, low 10.

## 8. Self-check

Every row has an outcome and a non-blank `material`. Every material row has ANN or SIL and a verbatim pointer or NONE FOUND. Every R row has announcement NA and pointer NA. Every A row has v_i_text NONE; every X row has v_next_text NONE. Column order matches the brief section 7. CSV written with QUOTE_ALL.


## 2.9 XAI-1

# XAI-1 tracing log

v_i = 10 Feb 2025 draft, v_next = 20 Feb 2025 draft. A word-level diff of the two text files shows one substantive change (a clause added to the vetted-user exception), one heading renumbered ('1.Implementation' to '2.Implementation') and otherwise only lost inter-word spaces and footnote spacing in the 20 Feb extraction. The v_i commitment list was built from the 30 candidates plus a full read of the text.

## Candidate accounting (v_i)

- candidates in file: 30
- kept as row anchors: 24
- dropped: 3
- merged into another row: 3
- splits (one sentence or list item coded as two rows): 2
- v_i commitments added from the full text (no candidate row): 18
- v_i commitments traced: 42; additions in v_next: 0; rows in CSV: 42

Dropped candidates (sentence index: reason class):

- idx9: risk-landscape description. "Without any safeguards, we recognize that advanced AI models could lower the barrier to entry for developing chemical, b"
- idx17: description of what benchmarks could measure. "Such benchmarks could be used to measure Grok’s dual-use capability and resistance to facilitating large-scale violence,"
- idx79: description. "It is possible that some AIs could have emergent value systems that could be misaligned with humanity’s interests,10 and"

Merged candidates (sentence index: into row):

- idx104 -> XAI-1-023
- idx106 -> XAI-1-024
- idx138 -> XAI-1-041

Splits:

- Candidate idx110 and the preceding clause: '1. Risk Management Framework compliance: regularly review our compliance with the Framework.' (G, compliance review) and 'Internally, we will allow xAI employees to anonymously report concerns ...' (G, whistleblowing) coded as two rows (XAI-1-026, XAI-1-027).
- Incident-response list item 1: 'We would immediately notify and cooperate with relevant law enforcement agencies ...' (XAI-1-036) and 'xAI employees have whistleblower protections ...' (XAI-1-037) coded as two rows.

## Cases the codebook does not settle

- Whether a framework's own applicability statement ('we expect to apply to future models not currently in development') is a commitment. Coded as a G row (XAI-1-001, low) so that the Aug 2025 broadening to current models can be traced; alternative: exclude as description.
- Whether a one-off dated promise ('We plan to release an updated version of this policy within three months') is a standing commitment (XAI-1-002, low). Alternatives: exclude as non-standing; merge with the publish-updates row.
- Whether placeholder threshold tables ('X% (e.g. 15%)') are commitments. Coded as EC2 rows (XAI-1-011 merged with its lead sentence; XAI-1-022 alone, low). Alternative: not a commitment.
- Where to code the added exception clause ('or if such requests cover information that is already readily and easily available'). Coded W dim 1 on the exception row XAI-1-005; alternative: R (clarification), or W on the heightened-safeguards row XAI-1-004.
- Present-tense practice statements without a modal ('We train Grok to robustly refuse ...', 'xAI employees have whistleblower protections') included as commitments at medium confidence; alternative: exclude as description.
- Two 'We will explore ...' items (truth-seeking tools; AI ID system) fit none of the codebook categories; coded M at low confidence; alternative: exclude.
- The four incident-response steps are coded as separate rows under a lead-in row (five rows for one list). Alternative: one merged row. Separate rows were chosen because the steps diverge in later versions.

## Low-confidence rows and their alternative readings

- XAI-1-001 (G, R): candidate idx2. Framework applicability statement ('future models not currently in development') coded as a scope commitment so the Aug 2025 broadening to current models can be traced; alternative reading: description of the document, exclude. Alt category EC1 (model classes).
- XAI-1-002 (G, R): added from full text. One-off timed commitment to publish a revised framework; alternative: exclude as non-standing, or merge with the 'publish updates' commitment in 1.Public transparency. Alt category EC5.
- XAI-1-017 (G, R): candidate idx80. Status statement with an intention to improve plans; alternative: exclude as description. Alt category EC3.
- XAI-1-022 (EC2, R): added from full text. Placeholder threshold table for loss of control (MASK <X% e.g. <50%; Utility/Power Correlation coercive <W e.g. <0, non-coercive <X e.g. <0.5; Utility/Fitness <Y e.g. <0.5; Corrigibility >Z e.g. >0.2). No verb; alternative: not a commitment, or part of the preceding 'adequate safeguards' row. Quote stops at a page break; remainder of table is on page 6.
- XAI-1-031 (M, R): added from full text. Fits none of the codebook categories well (societal risk); alternative: exclude.
- XAI-1-032 (M, R): candidate idx119. Fits none of the codebook categories well (agent ecosystem); alternative: exclude.

## Revision account

No account exists. The revision-account file is a NONE record listing what was checked (document text, predecessor, x.ai/safety Wayback captures, x.ai/news, web search, PDF metadata). Announcement for the single material row is NCL with changelog_pointer NA. Nothing in the account made the status hard to judge.

## Verifier summary

verify(rows, v_i, v_next, revision_account): {'ok': 82, 'literal': 42, 'ok-fuzzy': 2}. No NOT FOUND. ok-fuzzy fields (page break, page number or footnote interrupting the passage in the text file; flagged on the row): [('XAI-1-005', 'v_i_text'), ('XAI-1-005', 'v_next_text')].

## Counts

Outcome | n
---|---
R | 41
W | 1

Category | n
---|---
EC2 | 3
EC3 | 4
EC4 | 2
EC5 | 5
EC6 | 1
G | 10
M | 16
S | 1

Announcement | n
---|---
NA | 41
NCL | 1

Low-confidence rows: 6. Material rows: 1.

## Self-check

Every row has an outcome and non-blank material; every material row is NCL with changelog_pointer NA; every R row is NA/NA; A rows have v_i_text NONE and X rows have v_next_text NONE; files: XAI-1_tracing.csv, XAI-1_log.md.

## 2.10 XAI-2

# XAI-2 tracing log

v_i = 20 Feb 2025 draft, v_next = 20 Aug 2025 RMF. The v_i list is the XAI-1 v_next list (42 commitments; prior id XAI-1-nnn equals this pair's nnn). Aug 2025 is a rewrite: draft 'we intend to' language becomes present-indicative practice statements, the incident-response 'would' steps become 'may', placeholder thresholds are replaced by one concrete criterion per risk area, and several transparency and adversarial-testing statements change actor or force. Seven additions were found in the Aug text (starting from the 31 v_next candidates).

## Candidate accounting (v_i)

- candidates in file: 30
- kept as row anchors: 24
- dropped: 3
- merged into another row: 3
- splits (one sentence or list item coded as two rows): 0
- v_i commitments added from the full text (no candidate row): 18
- v_i commitments traced: 42; additions in v_next: 7; rows in CSV: 49

Dropped candidates (sentence index: reason class):

- idx9: risk-landscape description. "Without any safeguards, we recognize that advanced AI models could lower the barrier to entry for developing chemical, b"
- idx17: description of what benchmarks could measure. "Such benchmarks could be used to measure Grok’s dual-use capability and resistance to facilitating large-scale violence,"
- idx86: description. "It is possible that some AIs could have emergent value systems that could be misaligned with humanity’s interests,10and "

Merged candidates (sentence index: into row):

- idx113 -> XAI-2-023
- idx115 -> XAI-2-024
- idx155 -> XAI-2-041

Splits:

- Carried from XAI-1 (compliance review / whistleblowing; law-enforcement notification / whistleblower protections). No new splits.

## Cases the codebook does not settle

- Present indicative versus the codebook modal scale. Many rows move from 'we intend to / aim to' to 'xAI does'. The scale (must/will > intend/aim > may > recommend) has no rung for a present-indicative statement of practice. Coded consistently as a move to the top rung (S dim 4: XAI-2-006, 007, 009, 010, 020, 033, 034, 041; contributes to W-with-both-directions in 019, 021). Alternative applied to every such row: R. The adjudicator can flip the set as a block; the affected rows carry the note in flags.
- Rows that converge on one Aug passage. XAI-2-010 and 011 both trace to the bio/chem 'Thresholds' paragraph; 021 and 022 to the MASK threshold paragraph; 006 and 012 to the 'xAI utilizes public benchmarks ... Such benchmarks are used to measure' passage. Each pair is coded separately here and merged when the Aug list is carried into XAI-3 (noted in flags).
- Calibration example D. Verified against both texts with a correction: the sentence SaferAI treats as the replacement ('may also provide vetted and qualified external red teams or appropriate government agencies unredacted versions') already exists in Feb 2025 (XAI-2-025). The passage that governs adversarial testing of safeguards in Aug is 'we continually evaluate and improve robustness to adversarial attacks that seek to remove xAI model safeguards', which drops the external actor. XAI-2-014 is coded W dim 3 on that trace; under example D's trace it is W dims 3;4. Both readings give W, NCL.
- Both-directions rows coded W under codebook section 4 where a reader might expect S: XAI-2-005 (exception widened to enterprise customers, but made discretionary), 011 and 022 (placeholders become one concrete threshold, other benchmarks lose their thresholds), 018 (utility-function evaluation dropped, sycophancy added), 019 and 021 (indicative force, but internal deployments no longer named).
- XAI-2-013 (publish material changes to benchmarks or thresholds) coded X because no EC5 counterpart exists; alternative W dim 5 with 'xAI may change its approach from that listed above' as counterpart (that sentence is coded as addition XAI-2-048).
- Changes of listed examples (LAB-Bench absent from the benchmark list; circuit breakers replaced by system prompts) treated as not material under section 5; alternative W dim 1 noted on XAI-2-006 and 009.
- Aug sentences reporting completed work ('These steps were identified in close collaboration with domain matter experts at SecureBio, NIST, AISI, RAND, and EBRC'; 'Independent third-party assessments of xAI’s current models ... indicate'; 'Assessments to date lead xAI to conclude') are point-in-time reports and are not coded; they are the only third-party evaluation language in Aug apart from the unredacted-versions sentence.
- The 'Overall Approach' description of the three behaviour buckets (abuse potential, concerning propensities, dual-use capabilities) is not coded; alternative: an EC1 addition.

## Low-confidence rows and their alternative readings

- XAI-2-001 (G, S): prior id XAI-1-001. Alternative: not a commitment (description of the document), exclude; or R because applicability is not a commitment dimension. no account published by xAI for this pair; announcement NCL by construction
- XAI-2-002 (G, W): prior id XAI-1-002. Alternative: X (one-off commitment discharged by the Aug release itself, no standing counterpart) or exclude as non-standing. no account published by xAI for this pair; announcement NCL by construction
- XAI-2-006 (EC3, S): prior id XAI-1-006. Systematic pattern in this pair: draft 'we intend to / we aim to' becomes present-indicative 'xAI does'. The codebook modal scale has no rung for present indicative; coded here as a move to the top rung (S dim 4). Alternative reading for every such row: R (a statement of practice carries the same standing force as 'intend to'). LAB-Bench is absent from the Aug list (VCT, WMDP, BioLP-bench, Cybench); not coded as material because the Feb list was introduced by 'we have examined utilizing', not a commitment. Alternative: W dim 1 on that basis. no account published by xAI for this pair; announcement NCL by construction
- XAI-2-010 (M, S): prior id XAI-1-010. Alternative: X (no standing pre-release safeguards commitment survives; 'prior to releasing it for general availability' has no counterpart) or R. Shares its counterpart with XAI-2-011; the two rows are merged when carried into XAI-3. no account published by xAI for this pair; announcement NCL by construction
- XAI-2-011 (EC2, W): prior id XAI-1-011. Alternative: S (placeholders are no thresholds; any concrete criterion strengthens). Merged with XAI-2-010 when carried forward. no account published by xAI for this pair; announcement NCL by construction
- XAI-2-012 (EC2, W): prior id XAI-1-012. Alternative: X (no passage governs the pre-deployment trigger) or R (the 'risk acceptance criteria for system deployment' implies pre-deployment evaluation). Merged with XAI-2-006 when carried forward (adjacent sentences of one passage). no account published by xAI for this pair; announcement NCL by construction
- XAI-2-016 (M, R): prior id XAI-1-016. Alternative: W dim 1 (object narrows from safeguards against loss of control to measuring and reducing named propensities) or X.
- XAI-2-017 (G, R): prior id XAI-1-017. Alternative: W dim 1 (mitigation plans no longer covered) or X.
- XAI-2-018 (EC3, W): prior id XAI-1-018. Both directions (one domain dropped, one added); W per codebook section 4. Alternative: R (the list is examples under 'may use' and does not alter the rule). no account published by xAI for this pair; announcement NCL by construction
- XAI-2-019 (EC3, W): prior id XAI-1-019. Systematic pattern in this pair: draft 'we intend to / we aim to' becomes present-indicative 'xAI does'. The codebook modal scale has no rung for present indicative; coded here as a move to the top rung (S dim 4). Alternative reading for every such row: R (a statement of practice carries the same standing force as 'intend to'). Alternative: S or R if the dropped phrase is read as rewording. no account published by xAI for this pair; announcement NCL by construction
- XAI-2-021 (M, W): prior id XAI-1-021. Alternative: X (no standing pre-deployment safeguards commitment for loss of control survives). Shares its counterpart with XAI-2-022; merged when carried forward. no account published by xAI for this pair; announcement NCL by construction
- XAI-2-022 (EC2, W): prior id XAI-1-022. Alternative: S (placeholders are no thresholds). Merged with XAI-2-021 when carried forward. no account published by xAI for this pair; announcement NCL by construction
- XAI-2-025 (EC4, W): prior id XAI-1-025. Alternative: R (both versions are 'may'; the added hedge does not change a discretionary commitment). Also dim 3 arguable ('vetted' narrows the recipient class). Sentence crosses a page break in the Aug file (verifier may report ok-fuzzy). example D: this is the sentence SaferAI treats as the replacement for external red-team testing. no account published by xAI for this pair; announcement NCL by construction Verifier ok-fuzzy on v_next_text: a page break, page number or footnote interrupts the passage in the text file; quote is verbatim with that interruption removed.

## Revision account

No account exists (NONE record; same checks as XAI-1 plus the two Wayback captures of the Aug PDF). All 35 material rows are NCL with changelog_pointer NA.

## Verifier summary

verify(rows, v_i, v_next, revision_account): {'ok': 84, 'literal': 59, 'ok-fuzzy': 4}. No NOT FOUND. ok-fuzzy fields (page break, page number or footnote interrupting the passage in the text file; flagged on the row): [('XAI-2-005', 'v_i_text'), ('XAI-2-009', 'v_next_text'), ('XAI-2-025', 'v_next_text'), ('XAI-2-043', 'v_next_text')].

## Counts

Outcome | n
---|---
A | 7
R | 14
S | 9
W | 16
X | 3

Category | n
---|---
EC2 | 4
EC3 | 4
EC4 | 2
EC5 | 5
EC6 | 1
G | 11
M | 21
S | 1

Announcement | n
---|---
NA | 14
NCL | 35

Low-confidence rows: 13. Material rows: 35.

## Self-check

Every row has an outcome and non-blank material; every material row is NCL with changelog_pointer NA; every R row is NA/NA; A rows have v_i_text NONE and X rows have v_next_text NONE; files: XAI-2_tracing.csv, XAI-2_log.md.

## 2.11 XAI-3

# XAI-3 tracing log

v_i = 22 Aug 2025 re-upload (differs from the 20 Aug file only by the deletion of 'AISI,' in a report sentence that is not coded), v_next = 30 Dec 2025 Frontier AI Framework. The v_i list is the Aug commitment list carried from XAI-2 (39 traced survivors, three merges of rows that converged on one passage, seven additions: 43 commitments in Aug document order; prior ids in flags). A word-level diff shows the Dec text is the Aug text with RMF renamed FAIF, TFAIA framing and definition added, the harm threshold redefined by reference to the TFAIA, one security sentence added, two risk-owner duties added, two pre-deployment-review sentences and two framework-update triggers added, 'we will allow' changed to 'we allow', '5 critical steps' changed to 'critical steps', and an AB-2013 data disclosure appended.

## Candidate accounting (v_i)

- candidates in file: 31
- kept as row anchors: 20
- dropped: 4
- merged into another row: 7
- splits (one sentence or list item coded as two rows): 0
- v_i commitments added from the full text (no candidate row): 23
- v_i commitments traced: 43; additions in v_next: 5; rows in CSV: 48

Dropped candidates (sentence index: reason class):

- idx3: aspirational. "xAI seriously considers safety and security while developing and advancing AI models to help us all to better understand"
- idx5: description of the document. "This RMF discusses two major categories of AI risk—malicious use and loss of control—and outlines the quantitative thres"
- idx26: risk-landscape description. "Without any safeguards, we recognize that advanced AI models could lower the barrier to entry for bad actors seeking to "
- idx104: aspirational. "xAI aims to mitigate and address significant operational and societal risks posed by our AI models."

Merged candidates (sentence index: into row):

- idx63 -> XAI-3-013
- idx79 -> XAI-3-018
- idx107 -> XAI-3-025
- idx109 -> XAI-3-026
- idx138 -> XAI-3-041
- idx140 -> XAI-3-042
- idx142 -> XAI-3-042

Splits:

- None new; carried splits retained.

## Cases the codebook does not settle

- Redefinition of the focus threshold (XAI-3-008). 'more than one hundred deaths or over $1 billion in damages from weapons of mass destruction or cyberterrorist attacks on critical infrastructure' becomes 'a Catastrophic Risk' as defined by the TFAIA ('more than 50 people or more than one billion dollars', single incident, expert-level CBRN assistance, autonomous cyberattack or crime, evading control). The casualty anchor falls (S dim 2) while the covered conduct is redrawn (dim 1). Coded W (both directions), low. Alternatives: S, or R.
- 'we will allow' to 'we allow' (XAI-3-029). Coded R for consistency with the convention that present indicative is not below 'will'; alternative: material on dim 4 in either direction.
- Where to code the added framework-update triggers ('before major new capabilities are launched, and in response to incidents'). Coded S dim 2 on the deployment-decisions row XAI-3-043 whose passage contains the sentence; alternatives: on XAI-3-002, or as an addition.
- New risk-owner duties (periodic audits; incident monitoring channels) and pre-deployment reviews coded as additions (XAI-3-046, 047, 048); alternatives: S on the adherence-review, incident lead-in and benchmark rows respectively.
- The TFAIA compliance sentence is an assertion of legal compliance; coded as a G addition at low confidence, alternative exclude.
- The AB-2013 'xAI Data Disclosure' section (training-data description, model training dates) is a report and is not coded.

## Low-confidence rows and their alternative readings

- XAI-3-008 (M, W): prior id XAI-2-004. Alt category EC2 (harm threshold). Alternative: S (lower casualty threshold, loss of control added) or R (an externally defined threshold replaces a home-made one with similar coverage). The heightened-safeguards trigger sentence itself is unchanged. no account published by xAI for this pair; announcement NCL by construction
- XAI-3-044 (G, A): added from full text. Assertion of legal compliance rather than a commitment to future practice; alternative: exclude as description. no account published by xAI for this pair; announcement NCL by construction

## Revision account

No account exists (NONE record; the Dec document does not mention the RMF by name or state that it replaces it; treated as the successor version per collection judgement J4). All 8 material rows are NCL with changelog_pointer NA.

## Verifier summary

verify(rows, v_i, v_next, revision_account): {'ok': 88, 'literal': 53, 'ok-fuzzy': 3}. No NOT FOUND. ok-fuzzy fields (page break, page number or footnote interrupting the passage in the text file; flagged on the row): [('XAI-3-003', 'v_i_text'), ('XAI-3-017', 'v_i_text'), ('XAI-3-027', 'v_i_text')].

## Counts

Outcome | n
---|---
A | 5
R | 40
S | 2
W | 1

Category | n
---|---
EC2 | 4
EC3 | 5
EC4 | 1
EC5 | 4
EC6 | 1
G | 14
M | 18
S | 1

Announcement | n
---|---
NA | 40
NCL | 8

Low-confidence rows: 2. Material rows: 8.

## Self-check

Every row has an outcome and non-blank material; every material row is NCL with changelog_pointer NA; every R row is NA/NA; A rows have v_i_text NONE and X rows have v_next_text NONE; files: XAI-3_tracing.csv, XAI-3_log.md.

## 2.12 XAI-4

# XAI-4 tracing log

v_i = 30 Dec 2025 FAIF, v_next = 30 Jun 2026 FAIF. The v_i list is the Dec list carried from XAI-3 (43 traced + 5 additions = 48, Dec document order; prior ids in flags). June 2026 is a complete rewrite in the structure of the EU General-Purpose AI Code of Practice safety chapter (risk identification, systemic risk analysis, acceptance determination, mitigations, incident reporting, governance). The transparency section, the vetted-user exception, the enumerated bio/chem critical steps, both quantitative thresholds, the internal-AI-usage and survey items, whistleblowing and all external red-team language are absent; annual full assessments, named risk domains including harmful manipulation, a Security Goal and a legal-reporting duty are new.

## Candidate accounting (v_i)

- candidates in file: 34
- kept as row anchors: 17
- dropped: 8
- merged into another row: 9
- splits (one sentence or list item coded as two rows): 0
- v_i commitments added from the full text (no candidate row): 31
- v_i commitments traced: 48; additions in v_next: 10; rows in CSV: 58

Dropped candidates (sentence index: reason class):

- idx1: aspirational / date line. "Last updated: December 30, 2025 xAI seriously considers safety and security while developing and advancing AI models to "
- idx5: definition (TFAIA Catastrophic Risk) and description. "This risk includes, but is not limited to, Catastrophic Risk as defined in the TFAIA.1 This FAIF also outlines the quant"
- idx14: description. "AI usage by end users limits the utility of third-party reporting mechanisms that may be more effective for more publicl"
- idx31: risk-landscape description. "Without any safeguards, we recognize that advanced AI models could lower the barrier to entry for bad actors seeking to "
- idx48: description of a benchmark. "It includes 40 professional-level Capture the Flag (CTF) challenges selected from six categories: cryptography, web secu"
- idx97: aspirational. "xAI aims to mitigate and address significant operational and societal risks posed by our AI models."
- idx145: aspirational (AB-2013 data disclosure). "xAI aims to build AI models that are maximally truth-seeking, understand the true nature of the universe, and accelerate"
- idx156: report (training dates). "Grok 1 began training on or about August 2023; Grok 1.5 began training on or about August 2023; Grok 2 began training on"

Merged candidates (sentence index: into row):

- idx61 -> XAI-4-015
- idx75 -> XAI-4-020
- idx85 -> XAI-4-022
- idx100 -> XAI-4-027
- idx102 -> XAI-4-028
- idx131 -> XAI-4-045
- idx134 -> XAI-4-046
- idx136 -> XAI-4-046
- idx143 -> XAI-4-047

Splits:

- None new.

## Cases the codebook does not settle

- Counterparts for removed disclosure commitments. XAI-4-027 (publish framework updates), 031 (anonymous nonadherence reporting) and 038 (risk-owner audits) are coded X; each has a weaker candidate counterpart noted in flags ('We will review this Framework periodically'; 'Employee escalation'; 'ongoing legal and compliance reviews'), under which the row would be W. XAI-4-032 (benchmark results shared upon major releases) is coded W dim 5 with 'Results ... will be documented' as counterpart; alternative X.
- Rows with both directions coded W per section 4: XAI-4-016 (cyber re-assessment: method specified, per-release trigger becomes 'may'), 022 (loss-of-control benchmarks: 'may use' becomes 'utilizes', named evaluations become generic), 032, 041 (law-enforcement notification: 'may' becomes 'will' but only 'when reportable under applicable laws'). Alternative S on each.
- Loss of specificity as materiality (example G) applied to XAI-4-013, 022, 024, 026 and to X rows 015; alternative R where the generic statement still covers the object.
- De-commensuration (example F) applied to XAI-4-017 and 025: quantitative deployment criteria (1 in 20 restricted queries; 1 in 2 on MASK) become 'systemic risk acceptance criteria ... incorporating a margin of security'. Both rows share that counterpart.
- Acceptance gate (XAI-4-047). 'may depend on how a model performs on relevant benchmarks' plus a benefit-outweighs-risk override becomes 'will only proceed ... if the systemic risks ... are determined to be acceptable'. Coded S dims 4;6; the 'overall judgment based on all the available evidence' clause preserves discretion, so R is a defensible alternative.
- Framework scope (XAI-4-001): 'AI models' to 'frontier AI models' coded W dim 1 at low confidence; alternative R. The new Harmful Manipulation risk domain is coded as an EC1 addition (XAI-4-049); alternative S dim 1 on the scope row.
- Generic June lead-ins ('xAI implements appropriate safety mitigations'; 'xAI maintains internal governance structures'; personal-data security paragraph) included as low-confidence additions; alternative exclude.

## Low-confidence rows and their alternative readings

- XAI-4-001 (G, W): prior id XAI-3-001. Alternative: R (rewording; 'frontier' names the same models the document always addressed). Also 'handling' -> 'mitigation of'. no account published by xAI for this pair; announcement NCL by construction
- XAI-4-003 (G, S): prior id XAI-3-002. Alternative: R, or W dim 2 if 'continuously' -> 'periodically' is read as a looser cadence. Preceding sentence 'We may change our approach over time' retained the Dec reservation. no account published by xAI for this pair; announcement NCL by construction
- XAI-4-016 (EC2, W): prior id XAI-3-014. Alt category EC1. Alternative: S (a firm annual full assessment plus specified cyber benchmarks replaces an open-ended promise). The Dec clause 'still working on identifying enforceable critical steps' has no counterpart. no account published by xAI for this pair; announcement NCL by construction
- XAI-4-021 (M, S): prior id XAI-3-019. Alternative: R ('aims to' and 'makes significant efforts' are the same rung; the named practices are examples). no account published by xAI for this pair; announcement NCL by construction
- XAI-4-024 (M, W): prior id XAI-3-022. Alt category EC3. Alternative: R ('Monitoring and alerting of public comments from the X platform' is retained as an incident channel in section 3). no account published by xAI for this pair; announcement NCL by construction
- XAI-4-032 (EC5, W): prior id XAI-3-030. Alternative: X (documentation is not disclosure, so no counterpart). no account published by xAI for this pair; announcement NCL by construction
- XAI-4-041 (G, W): prior id XAI-3-037. Alternative: S (a discretionary notification becomes a mandatory one). no account published by xAI for this pair; announcement NCL by construction
- XAI-4-054 (M, A): added from full text (2.3. Safety mitigations). Generic; alternative: description of the section, exclude. no account published by xAI for this pair; announcement NCL by construction
- XAI-4-057 (S, A): added from full text (2.4). Concerns personal data and user content rather than model weights; alternative: outside the codebook's security stratum, exclude. no account published by xAI for this pair; announcement NCL by construction
- XAI-4-058 (G, A): added from full text (4. Governance). The compliance-review clause is also used as the counterpart of XAI-4-030; alternative: fold into that row. no account published by xAI for this pair; announcement NCL by construction

## Revision account

No account exists (NONE record; PDF metadata title 'Privileged/Confidential DRAFT working FRAMEWORK DOC' carries no change note). All 45 material rows are NCL with changelog_pointer NA. The June document does not mention the December version.

## Verifier summary

verify(rows, v_i, v_next, revision_account): {'ok': 92, 'literal': 80, 'ok-fuzzy': 2}. No NOT FOUND. ok-fuzzy fields (page break, page number or footnote interrupting the passage in the text file; flagged on the row): [('XAI-4-013', 'v_next_text'), ('XAI-4-036', 'v_next_text')].

## Counts

Outcome | n
---|---
A | 10
R | 13
S | 8
W | 15
X | 12

Category | n
---|---
EC1 | 2
EC2 | 5
EC3 | 7
EC4 | 1
EC5 | 4
EC6 | 1
G | 15
M | 20
S | 3

Announcement | n
---|---
NA | 13
NCL | 45

Low-confidence rows: 10. Material rows: 45.

## Self-check

Every row has an outcome and non-blank material; every material row is NCL with changelog_pointer NA; every R row is NA/NA; A rows have v_i_text NONE and X rows have v_next_text NONE; files: XAI-4_tracing.csv, XAI-4_log.md.

---

# 3. Silent same-label variants (silent_variants.csv)

Method: word-level diff (difflib SequenceMatcher on whitespace tokens, format characters and page markers removed) of each variant's .txt against its base .txt; every non-numeric hunk read in context; typographic and font-glyph hunks aggregated into one row per variant; each substantive hunk coded as its own row with both passages verbatim. Where a hunk looked like a content deletion I searched both PDFs directly (PyMuPDF) before coding; two such hunks (OpenAI 'Value alignment' duplicate text run; Microsoft full-stack security paragraph) are extraction artefacts, present in both files.

| Provider | Base | Variant | Passages coded | Material |
|---|---|---|---|---|
| Anthropic | v2.0 | v2.0-reupload-20241101 | 1 | 0 |
| Anthropic | v2.1 | v2.1-reupload-20250402 | 1 | 0 |
| OpenAI | v2 | v2-reupload-20250611 | 2 | 0 |
| Google DeepMind | v2.0 | v2.0-reupload-20250213 | 1 | 0 |
| Google DeepMind | v2.0 | v2.0-reupload-20250328 | 1 | 0 |
| xAI | 2025-08-20 | 2025-08-20-reupload-20250822 | 1 | 0 |
| Meta | v1.1 | v1.1-reupload-20250328 | 7 | 2 |
| Microsoft | v1 | v1-reupload-20250226 | 1 | 0 |
| Magic | v1.0 | v1.0-reupload-20240720 | 1 | 0 |

Sixteen rows, two material: both in Meta's March 2025 re-upload of the Feb 2025 framework. (1) The framework's scope sentence loses 'most advanced' and 'match or', so models that match rather than exceed frontier capabilities are no longer stated to be covered (EC1, dim 1). (2) The non-release trigger's object changes from 'a catastrophic outcome' to 'a threat scenario' (EC6, dim 2; low confidence, may be an alignment of wording with the threshold table). Neither is mentioned in Meta's 2026 change log, which describes the 2025 document as the 'Initial version'.

Cases recorded as not material but flagged for adjudication with the alternative reading: xAI removal of 'AISI' from the list of organisations that helped identify filter topics (past-tense description versus removal of a third party, dim 3); Meta 'i.e.' to 'e.g.' in the 'Net new' criterion (illustrative versus exhaustive list, dim 2); Meta 'internal deployment' to 'closed deployment'; Magic replacement of the LiveCodeBench baseline scores (the 50% trigger is unchanged, but the gap between the best public score and the trigger shrinks from 6 to 1.2 points).

The codebook's materiality rule is written for traced commitment pairs; applying it to a variant treats the variant as v_next of its base. silent_variants.csv has no confidence column, so low-confidence judgements are stated in the rationale.

# 4. Disclosure regime per labelled pair (pairs.csv)

Classification from the changelogs/ files: redline = provider-published marked-up diff; itemised = a list of individual changes (in-document changelog, page version-history list, section 5.3 bullets, Appendix change logs); narrative = prose account only (announcement post, ASF 2.0 section 2); none = no account found. Where several forms exist the strongest is recorded and the others named in regime_source. Nineteen consecutive labelled framework pairs are listed (Anthropic 8, OpenAI 1, DeepMind 3, xAI 4, Meta 1, Microsoft 1, Naver 1). Excluded: silent same-label variants (section 3), the three Korean renderings, and companion documents (Anthropic FCF Dec 2025 to Feb 2026, Frontier Safety Roadmap Feb to Jul 2026, RSP Noncompliance Policy draft to final), which are not framework versions.

| Provider | v_i | v_next | Traced | Regime |
|---|---|---|---|---|
| Anthropic | v1.0 | v2.0 | yes | itemised |
| Anthropic | v2.0 | v2.1 | no | itemised |
| Anthropic | v2.1 | v2.2 | no | redline |
| Anthropic | v2.2 | v3.0 | yes | narrative |
| Anthropic | v3.0 | v3.1 | no | redline |
| Anthropic | v3.1 | v3.2 | no | redline |
| Anthropic | v3.2 | v3.3 | no | redline |
| Anthropic | v3.3 | v3.4 | no | redline |
| OpenAI | beta | v2 | yes | itemised |
| Google DeepMind | v1.0 | v2.0 | no | narrative |
| Google DeepMind | v2.0 | v3.0 | yes | narrative |
| Google DeepMind | v3.0 | v3.1 | yes | itemised |
| xAI | draft-2025-02-10 | draft-2025-02-20 | yes | none |
| xAI | draft-2025-02-20 | 2025-08-20 | yes | none |
| xAI | 2025-08-20 | 2025-12-30 | yes | none |
| xAI | 2025-12-30 | 2026-06-30 | yes | none |
| Meta | v1.1 | v2 | yes | itemised |
| Microsoft | v1 | feb-2026 | yes | itemised |
| Naver | 2024 | v2.0 | yes | narrative |

Judgement calls: Anthropic v2.2 to v3.0 is 'narrative' although a page entry and in-document changelog exist, because both say only 'comprehensive rewrite' and point to the post. Anthropic v2.0 to v2.1 is 'itemised' (numbered page entry) with no redline; the corpus's redline set starts at v2.2. DeepMind v3.0 to v3.1 is 'itemised' on the six section-5.3 bullets although the announcement was an in-place edit of the earlier post. Counts in pairs.csv come from tracing.csv: n_commitments_v_i = non-A rows; n_material_changes = rows with material yes (includes A rows); n_announced / n_silent / n_ncl from the announcement column. Untraced pairs have blank counts.

# 5. Self-check (brief section 9)

- Every Tier-1 pair has rows in tracing.csv: ANT-1 95, ANT-2 95, OAI-1 51, GDM-1 42, GDM-2 50, META-1 106, MSFT-1 48, NAV-1 26, XAI-1 42, XAI-2 49, XAI-3 48, XAI-4 58 (710).
- Every row has an outcome and a non-blank material field (710/710, checked mechanically).
- Every material row has an announcement status (ANN 134, SIL 248, NCL 89) and a pointer (ANN) or NONE FOUND (SIL) or NA (NCL) (471/471).
- All nine silent variants are in silent_variants.csv (16 rows).
- Every consecutive labelled framework pair in the corpus is in pairs.csv (19 rows; 12 traced).
- restatement2.md was written and saved before tracing began (section 0).
- Tier 2 (DeepMind 1.0 to 2.0) was not traced; time was spent on verification instead. Its regime row is in pairs.csv.
- Not done: no independent second read of the 710 codes by me beyond the calibration-example rows and the checks in section 1; the codes are the tracks' proposals.
