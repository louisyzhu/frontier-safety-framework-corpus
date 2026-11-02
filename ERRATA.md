# Errata

Released versions:

| Version | Date | DOI |
|---|---|---|
| v1.0 | 2026-09-09 | 10.5281/zenodo.22670701 |
| v2.0 | 2026-11 | assigned by Zenodo on release; the concept DOI 10.5281/zenodo.22670700 always resolves to the latest version |

Corrections to the corpus, codebook or coding are recorded here with the date, the affected row or file, and the reason. Version 2.0 moves the v1.0 coding sheet to `coding/archive/tracing_FINAL_v1.csv` unchanged; every statistic in the v2 paper is computed from `coding/tracing_FINAL_v3.csv`.

| Date | Affected | Change | Reason |
|---|---|---|---|
| 2026-10-11 | coding/tracing_FINAL_v3.csv (whole sheet) | Three independent re-runs added (`RERUN*` columns); 249 rows on which any run disagreed with an adjudicated code re-examined (`READJ_*` columns). The first analysis had run the first pass under codebook v0.1 and had never checked its 132 accepted silent rows for the partial-announcement code introduced in v0.2. | Stability check (`coding/reruns/checkA_summary.md`) showed the re-runs applying ANN-P far more widely than the adjudication. |
| 2026-10-11 | Section-granularity analysis | Additions are grouped by their section in the later version instead of one unit per pair. | The earlier rule lumped every addition in a pair into one unit (99 units; now 170). |
| 2026-10-13 | coding/tracing_FINAL_v3.csv, 37 rows | Codes changed after a blind re-coding of the 249 re-examined rows and a row-by-row review of the 92 disagreements (`coding/blind_recoding/review_decisions.csv`); each change is logged in `READJ_notes` and `REVIEW_notes` with the code it replaced. | Second check of the re-examination. |
| 2026-10-13 | MSFT-1-001 (sheet and second-coder sample unit U50) | `v_i_text` and `v_next_text` replaced by the tracked-capabilities list of each version. | The row carried a duplicate of the security sentence quoted at MSFT-1-017; its code (S, two capabilities added, ANN) always referred to the list. |
| 2026-10-13 | corpus/pairs.csv | Count columns for the twelve traced pairs recomputed from the final codes. | They carried the counts of the first analysis. |
| 2026-10-13 | coding/second_coder_package/INSTRUCTIONS.md | Return date and time estimate removed from the released copy. | Not meaningful outside the original request. |
