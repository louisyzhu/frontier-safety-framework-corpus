# Check B: RSP 3.0 to 3.1, traced from scratch (Brief 5)

**Procedure.** One first-pass coder (claude-fable-5-1, effort high; seed and temperature not settable) ran the original first-pass procedure under codebook v0.2: it built its own commitment list from the v3.0 candidates (128 rows, the same list ANT-2 used for v3.0) and the full text, traced each into v3.1, and coded materiality and announcement. The account comprised all three provider publications (author decision 5): the RSP-page version-history entry, the in-document changelog entry, and the redline PDF. Blindness: no earlier coding of this pair exists; the coder's tool calls show no lookup of codes, memory, frames or the web, and it reported no code or count surfacing from memory. The task text is in `task_diff.md` (ANT-3 section).

**Commitments.** 61 rows: {'R': 56, 'W': 4, 'A': 1}. The coder kept 80 of 128 candidates, merged 31 into other rows, split 1, and added 11 commitments from the full text; counts and reasons are in `RSP-3.0-3.1_log.md`.

**Material changes: 5** (4 evidentiary, 1 non-evidentiary).

| id | category | outcome | dims | announcement (a) | announcement (b) | redline_shows | direction_stated | confidence |
|---|---|---|---|---|---|---|---|---|
| ANT-3-011 | EC2 | W | 2 | ANN | ANN | yes | yes | low |
| ANT-3-022 | EC5 | W | 1 | ANN | SIL | yes | no | low |
| ANT-3-035 | G | W | 3 | ANN | ANN-P | yes | no | medium |
| ANT-3-042 | EC4 | W | 2 | ANN | ANN | yes | yes | low |
| ANT-3-061 | EC6 | A | 6;4 | ANN | ANN | yes | yes | low |

(a) = all three publications count; (b) = redline excluded, page entry and changelog only.

## Silent revision rate

| | strict (SIL + ANN-P) | lenient (SIL) |
|---|---|---|
| (a) all three publications | 0.00 (0 of 5) | 0.00 (0 of 5) |
| (b) redline excluded | 0.40 (2 of 5) | 0.20 (1 of 5) |

- Under (a) every material change is ANN, because the redline marks every one of them (`redline_shows` = yes on all 5). This is zero by construction, as expected.
- Under (b) the page entry and changelog carry the two threshold changes (ANT-3-011 and its cross-reference ANT-3-042) and the Appendix A addition (ANT-3-061) as ANN; the changelog's "(2) how we use internal feedback on Risk Reports" names the class of ANT-3-035 without its direction (ANN-P); and the Risk Report scope change (ANT-3-022) is in neither text (SIL).
- **Direction stated by no provider text: 2 of 5** (ANT-3-022 and ANT-3-035). The redline shows both edits but states nothing about them.

## Redline hunks (`ANT-3_redline_hunk_map.csv`)
- The mechanical list has 15 hunks. The coder checked each against the redline PDF.
- **Editorial (non-material): 6.** Version number (H001), effective date (H002), two single-word style insertions (H003 'with', H004 'standards'), the changelog entry itself (H015), and H012, the permissive sentence "We may also use this feedback to improve or refine the report itself" (coded not material on its own, with the alternative recorded).
- **Material: 9 hunks producing the 5 changes.** The mechanical list splits three edits across unchanged words or a page break: H005+H006 (+H007, its footnote) are the threshold redefinition; H008+H009 the Risk Report scope change; H010+H011 the review change. Counted as edits rather than hunks: 5 material edits (one per material change), and 6 non-material hunks (5 editorial plus the H012 sentence).

## Quote verification
Every `v_i_text`, `v_next_text` and pointer quote was re-checked here against the cleaned v3.0 and v3.1 texts and the revision-account file after dropping format characters and punctuation: 57 rows match verbatim in every field; 7 fields on the other 4 rows (ANT-3-014, -018, -019 texts; one pointer on ANT-3-011) are ellipsis-spliced quotes whose parts each match verbatim. `[redline]` pointers quote the inserted words from v3.1 and the deleted words from v3.0; they are not in the revision-account file, which does not transcribe the redline.

## Cases the codebook does not settle (coder's log, section 3; adjudicator to decide)
- Whether ANT-3-042 double-counts ANT-3-011: it is the external-review trigger's cross-reference to the redefined threshold. Alternative R.
- Whether ANT-3-061 (Appendix A preamble, "we would strongly consider pausing") is a commitment at all; the provider says "This was true of RSP v3". Alternatives: no row, or S on ANT-3-058 to -060.
- ANT-3-011 is coded W with MIX (alternative S: the substitution prong dominates; alternative R: the provider calls it a clarification).
- ANT-3-022's direction: W on scope, but S if prior Risk Reports covered less capable models than current public ones.
- Section 11.5 was applied by analogy to this pair, as instructed; it was never reached, because no v3.0 commitment lacks a v3.1 counterpart, so no L or X arose and the companion-document flag was not used.
- Category of the Section 1 table's middle column (mitigation plans without an "if we determine" clause): coded by content, EC6 as the alternative.

**Correction in flight.** The coder received two messages during its run about the 'companion post-dates pair' flag (the first used the ANT-2 pair's date, the second the correct 2 April 2026 threshold). Both arrived before any row was written, and the flag was never needed.
