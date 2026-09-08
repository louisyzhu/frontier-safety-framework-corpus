# Frontier Safety Framework Corpus

A versioned, hash-pinned corpus of the safety frameworks published by frontier AI developers, together with each provider's own account of each revision, and the coding that supports the paper *Silent Revision: Measuring Undisclosed Change in the Safety Frameworks of Frontier AI Developers*.

**Paper:** [arXiv link to be added]
**Contact:** yiven.zhu@oii.ox.ac.uk

## What this is for

Existing assessments of frontier safety frameworks score their content at a moment in time. This corpus lets a reader ask a different question: when a developer revises its framework, how much of that revision can anyone identify from the developer's own account of it? The paper defines the *silent revision rate* as the share of material changes to a framework's commitments that the provider's published account does not identify, and reports it across twelve consecutive version pairs.

## Contents

```
corpus/
  manifest.csv          52 rows, one per document: provider, version, date, source,
                        retrieval provenance, SHA-256 hash
  documents/            every retrieved framework and companion document as published,
                        with a plain-text extraction of each
  changelogs/           the provider's revision account for each labelled pair
  pairs.csv             19 consecutive labelled pairs with disclosure regime
  candidates.csv        2,426 commitment-candidate sentences
  silent_variants.csv   9 same-label re-uploads and the materiality of each difference
  collection_log.md     what was searched, found and not found, per provider
coding/
  tracing_FINAL.csv     710 rows: first-pass codes, adjudicated codes, adjudication
                        notes, verbatim passages from both versions, changelog pointers
  METHODS_NOTE.md       the coding procedure as executed
  results.md            every statistic reported in the paper
  second_coder_package/ the 50-unit sample, its instructions and a standalone codebook
analysis/
  compute_agreement.py  Krippendorff's alpha for the second coding
  corpus_tools.py       hashing, extraction and manifest verification
  extract_candidates.py commitment-candidate extraction
codebook_v0.2_FROZEN.md  frozen 3 September 2026; the rules all coding followed
```

## Reproducing the paper's numbers

Every statistic in the paper is computed from `coding/tracing_FINAL.csv`. Python 3.10+ with `scipy` and `matplotlib`; no other dependency.

To verify the corpus against the originals:

```bash
python analysis/corpus_tools.py --verify corpus/manifest.csv
```

This recomputes the SHA-256 of every file on disk and compares it with the manifest. Provider-hosted documents can be re-retrieved from the URLs in the manifest and hashed the same way.

## Reproducibility tiers

Read this before citing any number.

- **Corpus and manifest** are reproducible in the strongest sense. Every file is hash-pinned, and its retrieval source and date are recorded.
- **Statistics** are recomputed from the coding sheet by the released scripts. A reader who runs them gets the numbers in the paper exactly.
- **The coding sheet itself is an archived output.** The first pass was produced by a language-model system whose sampling parameters were not fixed, and the adjudication was performed by the author. It is reproducible only by re-running the procedure in the paper's Section 4, and a re-run would agree with this sheet to a degree that the planned seed re-runs and second coding will measure. Inter-coder agreement is not yet reported; the sample and script are here so that any reader can complete it.

## Versioning and errata

The corpus is versioned by release tag. Any correction to a code, a hash or a manifest row is recorded in `ERRATA.md` with the date, the affected row and the reason, and the paper's figures are regenerated from the corrected sheet. Provider documents are never altered. A document replaced by its provider is added as a new row, and the earlier row is retained.

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
  eprint = {TO BE ADDED},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CY}
}
```
