# Second-coder instructions

Thank you for doing this. It should take two to three hours. You are coding 50 units independently; I will not see your codes until you send them back, and you have not seen mine. Agreement between us is what the paper reports, so please do not look anything up beyond what is in this package, and do not consult me on individual units. If the codebook genuinely does not settle a case, pick the reading you find best and say why in `E_notes`.

## What is in the package

- `SECOND_CODER_SAMPLE.csv` — the 50 units. Each row is one commitment in an earlier framework version (`v_i_text`, with its section) and the passage in the later version that the first pass located as its counterpart (`v_next_text`), or NONE if none was found. Rows where `v_i_text` is NONE are candidate additions in the later version.
- `codebook.md` — the frozen codebook. Sections 2 to 6 define the codes; section 9 has worked calibration examples; section 11 has clarifications. Please read sections 2 to 6 and 11 before starting, and use section 9 when you hit a case that resembles one.
- `revision_accounts/` — the provider's own account of each revision (changelog, version table, or announcement post), one file per pair. You need these for the announcement code. The four xAI pairs have no account; that is why those rows are coded NCL by rule.

## The four things to code, per row

1. **`E_material`** — `yes` or `no`. Is the difference between `v_i_text` and `v_next_text` material under codebook section 5 (scope, threshold, actor, obligation strength, disclosure, consequence)? Rewording with the same force is `no`. An addition (v_i NONE) or a removal (v_next NONE) is always `yes`.
2. **`E_outcome`** — one of `R` retained, `S` strengthened, `W` weakened, `X` removed, `L` relocated, `A` added. Codebook section 4. If both strengthening and weakening are present, code `W` and write MIX in notes (11.3).
3. **`E_materiality_dims`** — which of dimensions 1 to 6 changed (section 5), e.g. `2;4`. Leave blank for `R`.
4. **`E_announcement`** — for material rows only. Open the revision account for that row's pair and decide: `ANN` if a reader of the account alone would know this commitment changed in this direction; `ANN-P` if the account names the commitment or its class but not the direction; `SIL` if the account exists and does not identify it, even at class level; `NCL` for the four xAI pairs. Leave blank for `R`.

`E_notes` is free text. Use it for the alternative reading whenever you were close to a different code.

## Three rules that matter most

- **Present-tense practice statements** ("we conduct", "evaluations are run") count as commitments at the strongest rung, equal to "will". Present ↔ will is not a change in obligation strength (11.1).
- **Enumerations** are scope-defining if introduced by "including" or if the list is the substance of the commitment; illustrative if introduced by "e.g." or "such as". Only scope-defining lists make a change material (11.2).
- **Provider account** means the provider's own publications only. Commentary by individuals, including employees writing personally, does not make a change announced.

## Returning it

Fill the five `E_` columns in the CSV and send the file back. No need to reformat or explain the ones you found easy. If you can, return by Saturday 5 September so we have Sunday to compute agreement and finish the draft.
