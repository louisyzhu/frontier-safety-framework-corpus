# Frontier Safety Framework Corpus

[![DOI](https://zenodo.org/badge/1354518995.svg)](https://doi.org/10.5281/zenodo.22670700)

A versioned, hash-pinned corpus of the safety frameworks published by frontier AI developers, together with each provider's own account of each revision, and the coding that supports the paper *Silent Revision: Measuring Undisclosed Change in the Safety Frameworks of Frontier AI Developers*.

**Paper:** [arXiv:2609.08789](https://arxiv.org/abs/2609.08789) (version 2 is computed from this release; version 1 from release v1.0)
**Contact:** louis.zhu@oii.ox.ac.uk

## What this is for

Existing assessments of frontier safety frameworks score their content at a moment in time. This corpus lets a reader ask a different question: when a developer revises its framework, how much of that revision can anyone identify from the developer's own account of it? The paper defines the *silent revision rate* as the share of material changes to a framework's commitments that the provider's published account does not identify, and reports it across twelve consecutive version pairs.

## What changed in v2.0

Release v2.0 accompanies version 2 of the paper. The coding was checked three further ways, and every number was recomputed from the resulting sheet.

- The first pass was re-run three times on all 710 rows, and the 249 rows on which any run disagreed with an adjudicated code were re-examined against the texts.
- Fresh coders re-coded those 249 rows blind, and each of the 92 disagreements was adjudicated against the texts. 37 rows changed.
- Two model coders of a different model family coded the 50-unit sample from the coder package alone.

The strict silent revision rate moved from 0.67 to 0.64 and the lenient rate from 0.53 to 0.30, because many changes the first analysis coded silent are accounts that name the class of change without identifying it. The difference between narrative and itemised accounts that version 1 reported is no longer distinguishable from chance. The direction findings hold. `ERRATA.md` records each correction, and the v1.0 sheet is kept unchanged in `coding/archive/`.

## Contents

```
corpus/
  manifest.csv            52 rows, one per document: provider, version, date, source,
                          retrieval provenance, SHA-256 hash
  documents/              every retrieved framework and companion document as published,
                          with a plain-text extraction of each
  changelogs/             the provider's revision account for each labelled pair
  pairs.csv               19 consecutive labelled pairs with disclosure regime and, for the
                          twelve traced pairs, the counts under the final codes
  candidates.csv          2,426 commitment-candidate sentences
  silent_variants.csv     9 same-label re-uploads and the materiality of each difference
  collection_log.md       what was searched, found and not found, per provider
coding/
  tracing_FINAL_v3.csv    710 rows: first-pass codes, adjudicated codes, the codes of the three
                          independent re-runs, the re-examined codes as reviewed, the blind
                          re-coding of the 249 disputed rows, every note, the verbatim passages
                          from both versions and the changelog pointers
  METHODS_NOTE.md         the coding procedure as executed, stage by stage
  results.md              every statistic reported in the paper, as written by the script
  reruns/                 the three re-run sheets, their run log and the stability-check summary
  redlined_pair/          the from-scratch trace of the redlined pair RSP 3.0 to 3.1 and the
                          hunk map of its redline
  blind_recoding/         the rules given to the blind re-coders, their twelve output sheets and
                          the review decision on each of the 92 disagreements
  second_coder_package/   the 50-unit sample, its instructions and a standalone codebook, exactly
                          as given to the second coders
  second_coder_returns/   the two returned sheets and the key from unit to commitment
  archive/                tracing_FINAL_v1.csv, the sheet of release v1.0, kept for the record
analysis/
  compute_results.py      every table, figure input and statistic in the paper, from the sheet
  compute_agreement.py    Krippendorff's alpha for the second coding, the blind re-coding and
                          the re-runs
  make_figures.py         Figures 2 and 3 of the paper, from the two figure-input CSVs
  make_examples.py        the verbatim-text appendix, from the sheet
  corpus_tools.py         hashing, extraction and manifest verification
  extract_candidates.py   commitment-candidate extraction
codebook_v0.2_FROZEN.md   frozen 3 September 2026; the rules all coding followed
ERRATA.md                 every correction to a code or a quoted text, with date and reason
```

## Reproducing the paper's numbers

Every statistic in the paper is computed from `coding/tracing_FINAL_v3.csv`. The scripts need Python 3.10 or later with `scipy` and `matplotlib`, and nothing else.

```bash
python analysis/compute_results.py coding/tracing_FINAL_v3.csv out/            # every table and statistic
python analysis/compute_results.py coding/tracing_FINAL_v3.csv out_adj/ --codes adj   # the codes that preceded the re-examination
mkdir -p out/figures
python analysis/make_figures.py out/fig1_srr_by_pair.csv out/fig2_direction_by_pair.csv out/figures
python analysis/compute_agreement.py second coding/second_coder_returns/SECOND_CODER_returned_A.csv
python analysis/compute_agreement.py pair coding/second_coder_returns/SECOND_CODER_returned_A.csv coding/second_coder_returns/SECOND_CODER_returned_B.csv
python analysis/compute_agreement.py blind
python analysis/compute_agreement.py reruns
python analysis/corpus_tools.py --verify corpus/manifest.csv                 # recompute every hash
```

The figure files keep the names they had while the paper was drafted. `fig1_srr_by_pair` is the paper's Figure 2 (silent revision rate by pair) and `fig2_direction_by_pair` is its Figure 3 (direction of material change by pair). Figure 1, the diagram of the measurement construct, is drawn separately and takes no data beyond the pooled rates in `coding/results.md`.

The final code of each row is the re-examined code where `READJ_mode` begins with `re-examined`, otherwise the adjudicated code where filled, otherwise the first-pass code. The review that followed the blind re-coding wrote its changes into the `READJ_*` columns and logged each one in `READJ_notes` and `REVIEW_notes`, so the pre-review code of every changed row can be read back from the sheet.

## How the coding was produced

The pipeline had six stages. `coding/METHODS_NOTE.md` states each as executed.

1. **Reconnaissance and collection.** A written protocol fixed the search order before anything was retrieved: provider framework pages and version histories first, then announcement posts, then Internet Archive capture histories. Retrieval, hashing and text extraction were scripted (`analysis/corpus_tools.py`). Every judgement call, every source checked that yielded nothing and every deviation from the protocol is recorded in `corpus/collection_log.md`.
2. **Candidate extraction.** A recall-oriented rule-based pass (`analysis/extract_candidates.py`) produced 2,426 candidate sentences.
3. **First-pass coding.** Tracing and coding of outcome, materiality and announcement status was performed with language-model assistance under codebook version 0.1, producing 710 rows with verbatim text from both versions, a rationale and a confidence grade. Every quoted field was verified mechanically against the corpus text (2,130 checks). Version 0.2, frozen the next day, settled six questions the first pass raised.
4. **Adjudication.** 244 rows were adjudicated individually from the passages, the account and the codebook; the remaining 466 were accepted after a spot-check of 45 produced one change.
5. **Re-runs and re-examination.** The first pass was re-run three times on all 710 rows under version 0.2 (`coding/reruns/`). Every row on which any run disagreed with an adjudicated code, 249 rows, was re-examined against the texts under four readings fixed in advance (stated in the paper's codebook appendix), with a decision and a reason recorded per row.
6. **Blind re-coding and review.** Fresh model instances re-coded the 249 rows with the documents, the account and the fixed readings but no code (`coding/blind_recoding/`). Each of the 92 disagreements was adjudicated against the texts; 37 rows changed. Two further model coders of a different model family then coded the 50-unit sample from the coder package alone (`coding/second_coder_returns/`).

No human coded independently of the author. The coder package is released so that a reader can supply that check.

## Reproducibility tiers

Read this before citing any number.

- **Corpus and manifest** are reproducible in the strongest sense. Every file is hash-pinned, and its retrieval source and date are recorded.
- **Statistics** are recomputed from the coding sheet by the released scripts. A reader who runs them gets the numbers in the paper exactly.
- **The coding sheet itself is an archived output.** A language-model system whose sampling parameters were not fixed assisted with the first pass, and the author performed the adjudication and the reviews. The sheet is reproducible only by re-running the procedure in the paper's method section, and the re-runs and second coding report how closely such a re-run agrees.

## Versioning and errata

The corpus is versioned by release tag. Any correction to a code, a quoted text, a hash or a manifest row is recorded in `ERRATA.md` with the date, the affected row and the reason, and the paper's figures are regenerated from the corrected sheet. Provider documents are never altered. A document replaced by its provider is added as a new row, and the earlier row is retained.

If you find an error, open an issue. Corrections about a specific coded row are especially welcome; each row carries the verbatim passages it was coded from, so disagreements can be checked directly.

## Licensing

Three different things live here and they are licensed differently. See `NOTICE.md` for the detail.

- **Code** (`analysis/`): MIT, see `LICENSE-CODE`.
- **Author-created data and documentation** (manifest, codebook, coding sheets, logs, this README): CC BY 4.0, see `LICENSE-DATA`.
- **Provider documents** (`corpus/documents/`, `corpus/changelogs/`): the property of their publishers, included unmodified for verification. Not covered by the CC BY licence above.

## Citation

```bibtex
@misc{zhu2026silentrevision,
  title  = {Silent Revision: Measuring Undisclosed Change in the Safety Frameworks of Frontier AI Developers},
  author = {Zhu, Louis Yiven},
  year   = {2026},
  eprint = {2609.08789},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CY}
}
```

```bibtex
@dataset{zhu2026corpus,
  title     = {Silent Revision: a versioned corpus of frontier AI safety frameworks and their revision accounts},
  author    = {Zhu, Louis Yiven},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.22670700}
}
```
