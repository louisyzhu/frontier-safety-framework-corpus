# Codebook v0.2 — Commitments in Frontier Safety Frameworks

Status: **FROZEN for coding on 3 September 2026.** Both coders use this version. v0.2 resolves six questions raised by the first pass (section 11); no further changes before the agreement study.
Unit of analysis: a commitment traced across one consecutive version pair of one provider's framework.

v0.1: all commitments coded; strata G, S, M added; SaferAI Table 10 calibration cases; framing note.
v0.2: present-tense rule; enumeration rule; MIX flag; partial-announcement code ANN-P; provider-account definition; example D corrected.

---

## 1. What we are measuring

**Framing.** Frontier safety frameworks are treated as knowledge infrastructure: standards that commensurate catastrophic risk into thresholds and commit developers to procedures for evidencing it. The question is infrastructural: when the standard is revised, is the revision visible?

**Research question.** When frontier AI developers revise their published safety frameworks, how do their commitments change, and how much of that change is disclosed in the developer's own account of the revision? The analytical focus is on evidentiary commitments (EC1–EC6); non-evidentiary commitments are coded so the corpus is complete and reported as a separate stratum.

**Headline metric: silent revision rate (SRR).** Computed over all material changes, and reported separately for the evidentiary stratum (EC1–EC6) and the non-evidentiary stratum (G, S, M).
For a version pair (v_i → v_{i+1}) with a provider-published changelog:

    SRR = (material evaluation-commitment changes NOT mentioned in the changelog) / (all material evaluation-commitment changes)

Reported per version pair, per provider, and pooled. For version pairs with no changelog, SRR is undefined and the pair is reported under "no changelog," which is itself a finding.

**Secondary descriptives.** Direction of change (strengthened / weakened / removed / added) as shares of material changes, overall and by commitment category.

---

## 2. Scope: what counts as an evaluation commitment

A statement in the framework that commits the developer to something about **how the risk or capability of its models will be evidenced**. Six categories. Code every commitment into exactly one primary category.

| Code | Category | Covers |
|---|---|---|
| **EC1** | Scope of evaluation | Which capabilities or risk domains will be evaluated (CBRN, cyber, autonomy / AI R&D, persuasion, manipulation, self-replication, etc.) |
| **EC2** | Trigger and threshold | When evaluations must occur (compute thresholds, capability thresholds, pre-deployment, pre-training milestones, cadence) and what result constitutes crossing a threshold |
| **EC3** | Method | How evaluations are conducted (elicitation standards, red-teaming, named benchmarks, uplift studies, expert panels, forecasting) |
| **EC4** | Third-party involvement | External evaluation, government or AISI access, independent red teams, audits, replication by outside parties |
| **EC5** | Disclosure | What evaluation methods and results will be published, to whom, and when (system cards, risk reports, model cards, regulator briefings) |
| **EC6** | Consequence linkage | What action a specified evaluation result obligates (pause, mitigations before deployment, deployment restriction, escalation to a board or officer) |

Non-evidentiary strata, coded for completeness and reported separately:

| Code | Category | Covers |
|---|---|---|
| **G** | Governance and oversight | Named decision bodies, officers, review cadences, board involvement, whistleblowing, audit commitments not tied to a specific evaluation result |
| **S** | Security and containment | Weight security, access controls, infosec standards, and their tiering by capability level |
| **M** | Mitigation and deployment measures | Safeguards against misuse, monitoring, staged deployment, when not expressed as a consequence of an evaluation result |

**Include** a statement if it is phrased as a commitment by the developer about its own practice, at any strength ("will," "must," "commit to," "aim to," "may," "intend to").
**Exclude** statements that describe the general risk landscape, define terms, describe other actors' obligations, or are purely aspirational about the field.

Stratum rule: a security, governance or mitigation commitment goes to EC6 if it is expressed as a *consequence of an evaluation result*, otherwise to S, G or M. "We will implement ASL-3 security once evaluations show X" is EC6. "We will implement ASL-3 security" is S.

---

## 3. Tracing commitments across versions

For each version pair, start from the commitment list of v_i and locate each commitment's counterpart in v_{i+1}. Then check v_{i+1} for commitments with no counterpart in v_i.

A counterpart is the passage in v_{i+1} that governs the same category and the same object (same risk domain, same threshold, same third-party relationship). Renumbering, relocation to a different section, and rewording do not break correspondence.

**Relocation to a different document** (e.g. a commitment moved from the main framework into a companion document such as a compliance framework or a separate "industry recommendations" annex) is coded as its own outcome, see below, because it is a recurring pattern with its own meaning.

---

## 4. Outcome codes (one per traced commitment)

| Code | Outcome | Definition |
|---|---|---|
| **R** | Retained | Counterpart exists; no material change (rewording, reformatting, renumbering only) |
| **S** | Strengthened | Counterpart exists; at least one materiality dimension moves toward greater obligation, broader scope, lower threshold, more third-party involvement, or more disclosure |
| **W** | Weakened | Counterpart exists; at least one materiality dimension moves the other way |
| **X** | Removed | No counterpart in v_{i+1} and the commitment is not relocated |
| **L** | Relocated | Counterpart exists only in a separate companion document, or is moved from "company commitment" to "industry recommendation" or equivalent non-binding section |
| **A** | Added | Present in v_{i+1} with no counterpart in v_i |

If both strengthening and weakening dimensions are present in one commitment, code **W** and note both in the free-text field. Weakening on any dimension is the conservative call and the one reviewers will expect.

**L counts as a material change** and is analysed alongside W in the direction breakdown, but is reported separately so a reader can see how much "weakening" is relocation rather than deletion.

---

## 5. Materiality rule

A change is **material** if it alters at least one of:

1. **Scope** — the set of capabilities, risk domains, or model classes the commitment covers
2. **Threshold or trigger** — the level, timing, or condition at which evaluation or action is required
3. **Actor** — who conducts, verifies, or must be given access (including the addition or removal of a third party)
4. **Obligation strength** — the modal force of the commitment. Ordered scale for reference: *must / will / commit to* > *intend to / aim to / expect to* > *may / could / consider* > *recommend / encourage* (the last is not a self-commitment)
5. **Disclosure scope** — what is published, to whom, when, or with what redaction
6. **Consequence** — what action a result obligates, or the conditions under which that action can be deferred or overridden

Not material: rewording with the same modal force, reorganisation, typographical changes, updated cross-references, changes to examples that do not alter the rule.

**Conditional commitments.** Broadening the condition under which a commitment can be suspended or adjusted (e.g. adding "if a competitor deploys without comparable safeguards") is a change to *consequence* and is coded W even if the core commitment is untouched.

**Modal drift.** "We will" → "we aim to" is material (obligation strength). "We will" → "we commit to" is not.

---

## 6. Announcement status (one per material change)

Compare the change against the provider's own account of the revision: a changelog, "summary of changes," version-history table, or the accompanying announcement post for that version.

| Code | Status | Definition |
|---|---|---|
| **ANN** | Announced | The specific change is identifiable in the provider's account of the revision: a reader of the account alone would know that *this* commitment changed in *this* direction |
| **ANN-P** | Partially announced | The account identifies the commitment (or the class of commitments it belongs to) as having changed, but not the direction or substance. E.g. "updated our threshold definitions" when a threshold was weakened |
| **SIL** | Silent | The provider published an account of the revision and this change is not identifiable in it, even at class level. Generic lines ("clarified language throughout", "comprehensive rewrite") do not count as identification |
| **NCL** | No changelog | The provider published no account of what changed for this version pair |

**Two silent revision rates are reported.** SRR-strict counts ANN-P as silent (the reader could not learn what happened). SRR-lenient counts ANN-P as announced (the reader was pointed at the commitment). Both are reported; the paper leads with strict and shows lenient alongside.

**What counts as the provider's account.** Publications by the provider itself, released with or for the version: an in-document changelog or version table; prose in the document describing what changed (e.g. an introduction that says "this revision replaces X with Y"); the provider's announcement post; a provider-published redline. Commentary by individuals, including employees writing in a personal capacity on external platforms, is not a provider account. It may be cited in the paper as context but does not confer ANN.

Note SaferAI's observation that some changes are explained at length (Anthropic's removal of unilateral pause commitments in RSP v3 was accompanied by a rationale). Such changes are **ANN**. The metric is about disclosure, not about whether we agree with the rationale.

---

## 7. Coding form

One row per traced commitment. Fields:

```
provider | pair (v_i → v_{i+1}) | commitment_id | category (EC1–6) |
v_i_text (verbatim, ≤80 words) | v_{i+1}_text (verbatim or NONE) |
outcome (R/S/W/X/L/A) | materiality_dims (1–6, multi) |
announcement (ANN/SIL/NCL) | changelog_pointer (quote or NONE) |
coder | notes
```

Verbatim text is required. Paraphrase is not accepted in the form; it is what lets the second coder and reviewers check the call.

---

## 8. Pilot procedure

1. Louis codes all version pairs in full.
2. A stratified sample of ~50 traced commitments (at least 8 per provider, oversampling W/X/L) is given to the second coder with **this codebook and the two document versions only**, not Louis's codes.
3. Agreement is reported as Krippendorff's α on three decisions separately: materiality (binary), outcome (nominal, 6 levels), announcement (nominal, 3 levels). Report α with bootstrap CI.
4. Disagreements are adjudicated by discussion against the codebook text. Where the codebook was the cause, revise the rule and note it in the paper. One revision round only.
5. Frozen codebook is released with the corpus.

---

## 9. Worked calibration examples

Use these to align before coding. Verify each against the primary documents before relying on it.

**Example A — announced weakening (ANN, W, dims 4 & 6).**
Anthropic RSP v2.2 → v3.0: removal of unilateral pause commitments, replaced by a structure separating company commitments from industry recommendations. Announced and explained by the provider. Code W (and L for any commitment that moved into the recommendations section), ANN.

**Example B — silent weakening (SIL, W, dims 1 & 3).**
OpenAI Preparedness Framework Beta → v2: models distilled, fine-tuned or quantised from a model below a High threshold "will ordinarily not require additional safety measures" (footnote 6). Not among the twelve items in the v2 changelog. Code W on scope, SIL. (Confirm against the Beta text before using.)

**Example C — announced consequence change (ANN, W, dim 6).**
OpenAI Preparedness Framework v2, §4.3: safeguards may be adjusted if another developer releases a High or Critical system without comparable safeguards. Changelog item 11. Code W on consequence (broadened suspension condition), ANN.

**Example D — silent third-party weakening, no changelog (NCL, W, dim 3).**
xAI Risk Management Framework, Feb 2025 → Aug 2025: commitment to external red-team testing of safeguards replaced by "may provide" unredacted publications to vetted external parties. xAI published no changelog. Code W on actor and obligation strength, NCL. (Source: SaferAI §7.2, Table 9. Verify against both xAI documents.)

**Example E — not material (R).**
A framework renumbers its capability levels and rewrites a paragraph with identical modal force and identical scope. Code R.

**Examples F–J, from SaferAI Table 10 (DeepMind FSF 2.0 → 3.0). No changelog table exists; check the v3.0 announcement post to determine ANN vs SIL for each.**

- **F — de-commensuration of a threshold (W, EC2, dim 2).** FSF 2.0 defined ML R&D acceleration as "substantially accelerating (e.g. 2x) from 2020–2024 rates"; FSF 3.0 says "substantially accelerating from historical rates." A quantitative anchor becomes qualitative. Also: cyber collapsed from two thresholds with quantitative benchmarks to one shared definition.
- **G — reduced specificity of monitoring (W, EC3, dim 1).** FSF 2.0 listed what post-market monitoring draws on (incidents, post-mitigation testing, escalation statistics, updated threat models); FSF 3.0 says "post-market monitoring."
- **H — modal drift on safety-case updates (W, EC6, dim 4).** "the safety case will be updated through red-teaming" became safety cases "may be updated if deemed necessary."
- **I — marginal-risk provision added (W, EC6, dim 6).** FSF 3.0 allows marginal risk increases relative to competitors to justify deployment decisions; FSF 2.0 had no such provision. Note this is coded as a *change to an existing consequence commitment* (a new suspension condition), not as A.
- **J — governance de-naming (W, G, dim 3).** Three named councils became "appropriate governance function." Non-evidentiary stratum.

**Example K — announced removal with rationale (X or L, EC6, ANN).**
Anthropic RSP v2.2 → v3.0 removed unilateral pause commitments, with extended public reasoning (Shlegeris, 2026). Whether this is X or L depends on whether an equivalent commitment survives in the industry-recommendations section; check before coding.

---

## 10. Known hard cases to decide before coding

- **Companion documents.** Anthropic's Frontier Compliance Framework (Dec 2025) sits alongside the RSP. Decide whether the "framework" for tracing purposes is the RSP alone or RSP + FCF. Recommendation: RSP alone as the unit, FCF checked only to distinguish X from L.
- **Replacement documents.** OpenAI's Frontier Governance Framework (May 2026) may replace or supplement the Preparedness Framework. Establish which before tracing PF v2 → FGF.
- **Framework vs. system card.** Only frameworks are in the corpus, following SaferAI's scope rationale (frameworks are standing commitments; cards document point-in-time implementation). Commitments that appear only in system cards are out of scope and noted as a limitation.
- **Point-in-time vs. standing commitments.** "We evaluated model X for Y" is a report, not a commitment. Only standing commitments about future practice are coded.

---

## 11. Decisions made after the first pass (v0.2)

**11.1 Present-tense practice statements.** "We conduct X before deployment", "xAI utilizes Y", "evaluations are run" are commitments: in a policy document the descriptive present is the standing-commitment register. They sit at the **top rung** of the obligation scale, equal to *will / must / commit to*. A change between present tense and *will* is not material on dimension 4. A change from present tense or *will* to *may / aim to / consider* is material on dimension 4.

**11.2 Enumerations.** An enumeration is **scope-defining** when it is introduced by "including", "comprising", "consists of", or when it is the operative content of the commitment (the list *is* what is committed to). Removing or shortening a scope-defining enumeration is material on dimension 1 (Example G). An enumeration is **illustrative** when introduced by "e.g.", "for example", "such as", and the rule stands independently of it; changes to an illustrative enumeration are not material unless the rule text itself changes (section 5, "changes to examples").

**11.3 Both directions in one commitment.** Code the outcome **W** (section 4 rule) and add `MIX` to flags. The paper reports the MIX count so readers can see how much weakening is mixed.

**11.4 Class-level changelog lines.** Use **ANN-P** (section 6). Do not code SIL when the account names the commitment's class; do not code ANN when it omits direction.

**11.5 Companion documents.** Anthropic's Frontier Compliance Framework v2 (24 July 2026) and its RSP Noncompliance Reporting and Anti-Retaliation Policy are in the corpus. A commitment that leaves the RSP at v3.0 and appears in either companion is coded **L**, with the temporal caveat noted in flags when the companion version post-dates the pair. OpenAI's Frontier Governance Framework post-dates PF v2 by thirteen months and is not consulted for OAI-1.

**11.6 Example D, corrected.** In xAI Feb→Aug 2025 the "may also provide … unredacted versions" sentence is a *disclosure* commitment (EC5) and is its own row. The external red-team *testing* commitment traces to a different sentence and is coded W on dimension 3 (actor). The red-team commitment is removed outright (X) in the June 2026 document.
