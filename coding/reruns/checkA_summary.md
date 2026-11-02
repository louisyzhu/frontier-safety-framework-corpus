# Check A: independent re-runs of the first pass (Brief 5) — version 3, all 710 rows

These figures measure **run-to-run stability** of one coding procedure. They are not reliability or inter-coder agreement.

Version history: v1 and v2 (3 October) covered 615 rows, with ANT-2 held for the FCF v2 PDF. v3 (11 October) adds the three ANT-2 runs, so every table below covers all 12 pairs and 710 rows. Where a v2 figure is quoted elsewhere, it is the 615-row figure.

## Scope and procedure
- **Runs:** 24 (8 tracks × 3). Model `claude-fable-5-1`, effort high, codebook v0.2. Seed and temperature: not settable. ANT-2's three runs started 11 October, eight days after the other 21, after the FCF v2 PDF (SHA-256 8e4d91e1…5e23f, matching the manifest) arrived.
- **Inputs:** each run received the original commitment list without codes (author decision 4). Every change to the original task text is an exact replacement, listed in `task_diff.md` and `task_edits.csv`. ANT-2's old instruction "FCF not in corpus, code X" was replaced by codebook v0.2 §11.5, with the FCF v2 and both Noncompliance Policy versions supplied.
- **Comparisons:** `alpha_nominal` and `bootstrap` are taken verbatim from `compute_agreement.py` (SHA-256 `ab2ca52a4bfbc070c86bd23662a39b6055e5d18d0a46001e163259254ebdec7d`), loaded without running its main block. **Adjudicated** = the `ADJ_*` value where filled, otherwise the first-pass value. Codes are compared after trimming whitespace and upper-casing.

## Integrity
- **Coverage:** every run returned exactly its supplied rows (710 per run after merging; none missing, duplicated or added).
- **Blindness:** a scan of every tool call in all 24 runs found no lookup of codes, tracings, adjudication, memory, frames or the web, and no run opened an artifact outside its task (one run re-read its own saved file; one re-saved its own log).
- **Memory declarations:** 9 of 24 runs declared "yes"; in each case what surfaced was the same two project-convention rows (coding role split, corpus conventions). No run reported seeing any code, count or result for its pairs. The three ANT-2 runs declared "no".
- **Declared deviations** concern only how quotes were checked: the required pointer prefixes, page-break hyphenation, three lengthened pointers in META-1 r1, and, in ANT-2, that the supplied verifier cannot match companion-document quotes (7 L rows per run were checked against the FCF and Noncompliance Policy texts instead). ANT-2 r3 also notes it did not use v3.0's Introduction or Appendix B prose as part of the account. None touches `material`, `outcome` or `announcement`.
- **Correction in flight (ANT-2):** the dispatched text said the "companion post-dates pair" flag applies to both companions; it applies only to versions post-dating v3.0 (the FCF v2 and the March 2026 policy, not the December 2025 policy). A correction was sent to all three runs about three minutes after dispatch, before any had written rows.

## Agreement, all 710 rows

| comparison                   | variable     |   n |   raw |   alpha |   95% lo |   95% hi |
|:-----------------------------|:-------------|----:|------:|--------:|---------:|---------:|
| run 1 vs run 2               | material     | 710 | 0.97  |   0.933 |    0.902 |    0.96  |
| run 1 vs run 3               | material     | 710 | 0.973 |   0.94  |    0.911 |    0.965 |
| run 2 vs run 3               | material     | 710 | 0.963 |   0.918 |    0.885 |    0.947 |
| run 1 vs original first pass | material     | 710 | 0.963 |   0.918 |    0.885 |    0.948 |
| run 2 vs original first pass | material     | 710 | 0.956 |   0.902 |    0.868 |    0.935 |
| run 3 vs original first pass | material     | 710 | 0.962 |   0.915 |    0.881 |    0.945 |
| run 1 vs adjudicated         | material     | 710 | 0.961 |   0.911 |    0.879 |    0.942 |
| run 2 vs adjudicated         | material     | 710 | 0.956 |   0.902 |    0.865 |    0.935 |
| run 3 vs adjudicated         | material     | 710 | 0.959 |   0.908 |    0.873 |    0.939 |
| run 1 vs run 2               | outcome      | 710 | 0.923 |   0.897 |    0.869 |    0.923 |
| run 1 vs run 3               | outcome      | 710 | 0.934 |   0.912 |    0.887 |    0.936 |
| run 2 vs run 3               | outcome      | 710 | 0.931 |   0.908 |    0.883 |    0.934 |
| run 1 vs original first pass | outcome      | 710 | 0.9   |   0.868 |    0.836 |    0.895 |
| run 2 vs original first pass | outcome      | 710 | 0.906 |   0.875 |    0.847 |    0.905 |
| run 3 vs original first pass | outcome      | 710 | 0.904 |   0.873 |    0.843 |    0.9   |
| run 1 vs adjudicated         | outcome      | 710 | 0.899 |   0.866 |    0.836 |    0.894 |
| run 2 vs adjudicated         | outcome      | 710 | 0.903 |   0.871 |    0.842 |    0.9   |
| run 3 vs adjudicated         | outcome      | 710 | 0.901 |   0.869 |    0.839 |    0.898 |
| run 1 vs run 2               | announcement | 710 | 0.892 |   0.859 |    0.828 |    0.887 |
| run 1 vs run 3               | announcement | 710 | 0.889 |   0.856 |    0.826 |    0.885 |
| run 2 vs run 3               | announcement | 710 | 0.894 |   0.863 |    0.833 |    0.893 |
| run 1 vs original first pass | announcement | 710 | 0.718 |   0.632 |    0.589 |    0.675 |
| run 2 vs original first pass | announcement | 710 | 0.73  |   0.645 |    0.604 |    0.688 |
| run 3 vs original first pass | announcement | 710 | 0.746 |   0.667 |    0.626 |    0.707 |
| run 1 vs adjudicated         | announcement | 710 | 0.765 |   0.696 |    0.657 |    0.735 |
| run 2 vs adjudicated         | announcement | 710 | 0.762 |   0.691 |    0.653 |    0.731 |
| run 3 vs adjudicated         | announcement | 710 | 0.777 |   0.711 |    0.671 |    0.75  |

## Announcement, rows coded material by both sides

| comparison           |   n |   raw |   alpha |   95% lo |   95% hi |
|:---------------------|----:|------:|--------:|---------:|---------:|
| run 1 vs run 2       | 463 | 0.879 |   0.835 |    0.793 |    0.874 |
| run 1 vs run 3       | 464 | 0.871 |   0.824 |    0.782 |    0.863 |
| run 2 vs run 3       | 459 | 0.893 |   0.856 |    0.817 |    0.892 |
| run 1 vs adjudicated | 460 | 0.698 |   0.591 |    0.531 |    0.65  |
| run 2 vs adjudicated | 457 | 0.698 |   0.59  |    0.533 |    0.647 |
| run 3 vs adjudicated | 458 | 0.718 |   0.616 |    0.558 |    0.673 |

## ANT-2 alone (95 rows)

| comparison                   | variable     |   n |   raw |   alpha |   95% lo |   95% hi |
|:-----------------------------|:-------------|----:|------:|--------:|---------:|---------:|
| run 1 vs run 2               | material     |  95 | 1     |   1     |    1     |    1     |
| run 1 vs run 3               | material     |  95 | 1     |   1     |    1     |    1     |
| run 2 vs run 3               | material     |  95 | 1     |   1     |    1     |    1     |
| run 1 vs original first pass | material     |  95 | 0.979 |   0.878 |    0.646 |    1     |
| run 2 vs original first pass | material     |  95 | 0.979 |   0.878 |    0.646 |    1     |
| run 3 vs original first pass | material     |  95 | 0.979 |   0.878 |    0.646 |    1     |
| run 1 vs adjudicated         | material     |  95 | 0.979 |   0.878 |    0.646 |    1     |
| run 2 vs adjudicated         | material     |  95 | 0.979 |   0.878 |    0.646 |    1     |
| run 3 vs adjudicated         | material     |  95 | 0.979 |   0.878 |    0.646 |    1     |
| run 1 vs run 2               | outcome      |  95 | 0.895 |   0.863 |    0.779 |    0.942 |
| run 1 vs run 3               | outcome      |  95 | 0.926 |   0.904 |    0.827 |    0.971 |
| run 2 vs run 3               | outcome      |  95 | 0.937 |   0.917 |    0.848 |    0.972 |
| run 1 vs original first pass | outcome      |  95 | 0.832 |   0.781 |    0.68  |    0.873 |
| run 2 vs original first pass | outcome      |  95 | 0.832 |   0.779 |    0.678 |    0.864 |
| run 3 vs original first pass | outcome      |  95 | 0.842 |   0.793 |    0.687 |    0.876 |
| run 1 vs adjudicated         | outcome      |  95 | 0.832 |   0.782 |    0.68  |    0.873 |
| run 2 vs adjudicated         | outcome      |  95 | 0.821 |   0.766 |    0.66  |    0.856 |
| run 3 vs adjudicated         | outcome      |  95 | 0.853 |   0.807 |    0.705 |    0.89  |
| run 1 vs run 2               | announcement |  95 | 0.737 |   0.633 |    0.495 |    0.76  |
| run 1 vs run 3               | announcement |  95 | 0.716 |   0.603 |    0.464 |    0.733 |
| run 2 vs run 3               | announcement |  95 | 0.811 |   0.733 |    0.612 |    0.844 |
| run 1 vs original first pass | announcement |  95 | 0.526 |   0.313 |    0.151 |    0.452 |
| run 2 vs original first pass | announcement |  95 | 0.695 |   0.536 |    0.393 |    0.659 |
| run 3 vs original first pass | announcement |  95 | 0.737 |   0.589 |    0.443 |    0.719 |
| run 1 vs adjudicated         | announcement |  95 | 0.589 |   0.412 |    0.241 |    0.554 |
| run 2 vs adjudicated         | announcement |  95 | 0.611 |   0.434 |    0.287 |    0.564 |
| run 3 vs adjudicated         | announcement |  95 | 0.653 |   0.485 |    0.337 |    0.616 |

ANT-2 is the least stable pair on `outcome` and `announcement`. Its outcome disagreements are concentrated in the X / L / W triangle created by §11.5: run 1 against the adjudicated codes (rows adjudicated, columns run 1):

| row_0   |   A |   L |   R |   S |   W |   X |
|:--------|----:|----:|----:|----:|----:|----:|
| A       |  26 |   0 |   0 |   0 |   0 |   0 |
| L       |   0 |   3 |   0 |   0 |   1 |   0 |
| R       |   0 |   0 |   8 |   0 |   1 |   0 |
| S       |   0 |   0 |   0 |   3 |   0 |   0 |
| W       |   0 |   1 |   1 |   1 |  26 |   1 |
| X       |   0 |   7 |   0 |   0 |   3 |  13 |

The adjudication, made under v0.1's "FCF not in corpus, code X" rule, has 23 X rows; each run moves 5 to 7 of them to L (found in a companion) and 3 to 7 to W.

## Counterpart location
Measured on the 536 non-addition rows. Rule: two v_next passages count as the same if the first 40 normalised characters of one occur in the other; NONE matches only NONE.

| Comparison | Share agreeing |
|---|---|
| run 1 vs run 2 | 0.929 |
| run 1 vs run 3 | 0.935 |
| run 2 vs run 3 | 0.937 |
| run 1 vs original | 0.907 |
| run 2 vs original | 0.916 |
| run 3 vs original | 0.910 |

## Flagged count: the 132 rows
- **Definition:** `ADJ_mode` = "accepted" and first-pass `announcement` = SIL, excluding the single "accepted+ANN-P rule" row: 132 rows, all now in scope (96 in the first 11 pairs, 36 in ANT-2).
- **Coded ANN-P by each re-run:** run 1 64, run 2 53, run 3 58, out of 132.
  - By all three runs: 43. By at least one run: 71.
  - Of the 36 ANT-2 rows: 20, 14 and 15 per run; 10 by all three, 20 by at least one.
  - The rest are SIL, apart from 2 to 6 per run coded NA (the run judged the row not material) and 2 coded ANN in runs 2 and 3.

## Announcement: re-run 1 against the adjudicated code, 710 rows

| row_0   |   ANN |   ANN-P |   NA |   NCL |   SIL |
|:--------|------:|--------:|-----:|------:|------:|
| ANN     |    80 |      42 |    3 |     0 |     1 |
| ANN-P   |     4 |      43 |    0 |     0 |     7 |
| NA      |     2 |       8 |  222 |     1 |     4 |
| NCL     |     0 |       0 |    3 |    87 |     0 |
| SIL     |     2 |      83 |    7 |     0 |   111 |

The two largest off-diagonal cells: 83 adjudicated SIL rows coded ANN-P, and 42 adjudicated ANN rows coded ANN-P. The second shift does not come from the 132 rows; it is the re-runs applying v0.2's ANN-P to rows the adjudication left as ANN.

## Context only: pooled SRR on the same 710 rows
Not requested by the brief and not a re-estimate. Material changes with an account (ANN, ANN-P or SIL); strict = SIL + ANN-P, lenient = SIL. The adjudicated row reproduces the paper's 67% and 53%.

| source                 |   n_material_with_account |   srr_strict |   srr_lenient |
|:-----------------------|--------------------------:|-------------:|--------------:|
| adjudicated (710 rows) |                       383 |        0.671 |         0.53  |
| run 1                  |                       387 |        0.773 |         0.318 |
| run 2                  |                       387 |        0.742 |         0.333 |
| run 3                  |                       385 |        0.738 |         0.351 |

## Rows that differ across the three re-runs
`unstable_rows.csv` has 220 row-variable cases on 138 commitments (45 of the cases in ANT-2):

| Variable | Cases |
|---|---|
| material | 33 |
| outcome | 73 |
| announcement | 114 |

Each case gives the three re-run codes, the original first-pass code, the adjudicated code, and whether the row is one of the 132.

## Files
- `rerun_1.csv` to `rerun_3.csv`: 710 rows each, the brief's columns, ANT-2 rows appended. `rerun_k_full.csv` adds category, rationale and flags.
- `checkA_agreement.csv`: every agreement figure above, with a `subset` column (all 710 / ANT-2 only).
- `unstable_rows.csv`; `run_log.csv` (24 runs: model, effort, seed and temperature, start, wall time, tool calls, forbidden lookups = 0 for all, memory declaration); `srr_context.csv`.
