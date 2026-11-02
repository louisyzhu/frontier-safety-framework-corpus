# Blind re-coding task: rules and output format

## What this is
A content-analysis study traces every commitment in one version of a frontier AI developer's safety framework (v_i) to its counterpart in the next version (v_next), classifies each change, and asks whether the developer's own published account of the revision identifies the change. You are an independent coder. You receive the row texts and the primary documents and nothing else. Code every row from the documents and the rules below. Do not guess what another coder decided; there is no "expected" answer available to you.

## Files
- Codebook (authoritative; read sections 3, 4, 5, 6, 9, 10 and 11 in full before coding): `/mnt/user-data/outputs/aiscik-drift/codebook_v0.2_FROZEN.md`
- Your rows: the CSV named in your brief. Columns: commitment_id, pair_id, category, v_i_section, v_i_text (verbatim from v_i, or NONE for an added commitment), v_next_section, v_next_text (verbatim from v_next, or NONE where no counterpart was found).
- The two framework texts and the revision account: paths in your brief. The account file may contain several sections (version-history entry, in-document changelog, announcement post, sometimes third-party commentary). Only provider-published material counts as the account; a section headed as a non-official or personal post is not the provider's account and must be ignored for announcement status.

## Variables to code (per row)
1. `material`: yes or no. A change is material if it alters at least one of six dimensions: scope; threshold or trigger; actor; obligation strength; disclosure scope; consequence (codebook section 5). An added commitment (v_i_text NONE) is material by convention. A row whose counterpart differs only by rewording with the same modal force, reorganisation, renumbering or updated cross-references is not material.
2. `outcome`: R, S, W, X, L or A (codebook section 4). R only when material is no. X when there is no counterpart in v_next and the commitment is not relocated. L when the commitment leaves the framework and survives in a companion document that is in the corpus (paths in your brief) or in a non-binding recommendations section of the framework itself. If v_next_text says NONE, check the v_next document and any companion yourself before choosing X or L; the extraction may have missed a counterpart, in which case say so in the reason and code against what you find.
3. `mix`: yes if the commitment moves in both directions at once (then outcome is W by rule 11.3), else no.
4. `announcement`: ANN, ANN-P, SIL or NCL for material changes; NA for non-material rows. NCL only when the brief says the pair has no provider account at all.
5. `account_passage`: the verbatim sentence or clause of the account that supports ANN or ANN-P, or `none` for SIL.
6. `reason`: one or two sentences naming the dimension(s) that move and, for announcement status, why the passage does or does not identify this change.

## Announcement rules (apply exactly)
- ANN: a reader of the account alone would know that this commitment changed in this direction. A class-level mention counts as ANN when the class is specific enough to locate the affected commitments in the document and the account states a direction that applies to this change (for example "removed the unilateral pause commitments", "safeguard requirements for ASL-3 were made less prescriptive").
- ANN-P: the account identifies the commitment or a locatable class it belongs to as having changed, without stating the direction or substance, or stating a direction that does not apply to this change. A class is locatable when a reader could find the affected commitments from the account's wording (a named section, a named safeguard level, a named provision such as Risk Reports, the actors in scope of a named standard).
- SIL: the account does not identify the change even at class level. Overview sentences ("key improvements include refined processes", "comprehensive rewrite", "clarified language throughout", "updated throughout") and generic lines do not count as identification.
- A relocation (L) takes its announcement status from how the account treats the move: ANN if the account says the content moved to the companion or recommendations section, ANN-P if it names the class without saying it moved, SIL if neither.

## Materiality rules that decided many earlier disputes (apply exactly)
- Present-tense practice statements ("we conduct X", "evaluations are run") are commitments at the top rung of the obligation ladder, equal to will/must/commit. Present tense to "will" is not material on obligation strength; present tense or "will" to "may", "aim to", "consider" is material.
- Enumerations: a list introduced by "including", "comprising" or "consists of", or a list that is the operative content of the commitment, is scope-defining, so shortening or removing it is material on scope. A list introduced by "e.g.", "for example", "such as" is illustrative, so changing it is not material unless the rule text itself changes.
- Broadening the condition under which a commitment can be suspended or adjusted is a change to consequence and is W.
- Modal drift: "we will" to "we aim to" is material; "we will" to "we commit to" is not.
- Three named bodies replaced by "appropriate governance function" is W on actor.

## Output
Write a CSV to the path named in your brief with exactly these columns, one row per input row, same commitment_id values, no rows added or dropped:
`commitment_id,material,outcome,mix,announcement,account_passage,reason`
Values: material in {yes,no}; outcome in {R,S,W,X,L,A}; mix in {yes,no}; announcement in {ANN,ANN-P,SIL,NCL,NA}. Quote fields that contain commas. Keep `account_passage` to the shortest clause that carries the identification (at most 40 words) and `reason` to at most 50 words. Write the file in instalments of at most 10 rows (write the header with the first ten rows, then append the next ten with a shell append or a further Write of the whole file) so that no single tool call carries more than ten rows; a single very long output will be cut off and lost. Read documents in parts (Read with offset and limit, or Grep) and never print a whole document in one call. Then reply with a short note (under 150 words) stating how many rows you coded, anything in the documents you could not resolve, and nothing else.
