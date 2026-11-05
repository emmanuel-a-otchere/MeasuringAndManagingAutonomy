# Facilitator guide — running a `mama` assessment session

> For the person convening and facilitating an assessment. The method is in
> the [handbook](handbook.md) and [assessment](assessment.md); this guide is
> the session craft: how to run it so the numbers mean something. Session
> length: 60–90 minutes per unit × domain.

## Before the session

1. **Fix the unit and the domain** — one unit × one decision domain per
   session ([why](assessment.md#2-how-to-run-it): averaging across domains
   destroys the signal). Write the domain as a decision class with real
   stakes ("production deploys of the payments service", not "engineering").
2. **Recruit two assessors** — one from the unit, one from the grantor
   side. Neither should be the [grantor](governance-loop.md#6-roles) them-
   self, and both should have actually seen the domain operate.
3. **Collect evidence pointers** — dashboards, logs, inventories, drill
   records, incident reviews. The session debates evidence, not opinions;
   scores of L3+ without evidence drop a level
   ([assessment rule](assessment.md#2-how-to-run-it)).
4. **Send both assessors the [questionnaire](assessment.md#3-the-questionnaire)**
   and have them score **independently first**.

## During the session

1. **Walk dimensions one at a time, L1 → L5.** For each item: what evidence
   exists? Mark the item only if both assessors accept the evidence. The
   dimension score is the *lowest* level whose items are all true —
   partial achievement scores as the level below.
2. **Expect disagreement to be productive.** Where the two assessors score
   differently, that gap is the session's best output: it usually means the
   unit and the grantor see different realities (or one of them knows
   something the other doesn't). Record the disagreement, don't average it
   away — then reconcile explicitly.
3. **Watch the L1 items.** On the v2 scale, a dimension where not even the
   L1 (Ask-arrangement) item is true scores **0 — the Submarine Line**. If
   the room hesitates on an L1 item, the honest score is 0 and the finding
   is "this unit has no standing here at all" — often the most valuable
   sentence of the session.
4. **Safety dimensions are not coaching dimensions.** D3/D4/D6 bound the
   grant (weakest link); D1/D2 cap the pace. Keep the distinction audible —
   teams hear "D2 low" as "we might lose the grant" when it means "we'll
   invest, not revoke".
5. **Compute in the room.** Run `autonomy-score` (or the [web version](../site/))
   with the reconciled scores and the currently granted level; the printed
   `ruleset_version` and safe level go straight into the record.

## After the session

1. **File the scorecard** with evidence links and the ruleset version
   ([outputs](assessment.md#5-outputs)): scorecard, gap list, recommended
   move, next horizon.
2. **The grantor decides.** The safe level is an evidence input, not an
   automatic authorization — the grantor weighs blast radius, reversibility,
   and context ([handbook step 4](handbook.md#step-4--apply-the-weakest-link-rule-and-decide)).
3. **Update the ledger** if the contract changes; version the contract id
   rather than rewriting history.
4. **Publish disagreements upward** — recurring rubric disputes are
   [framework feedback](../CONTRIBUTING.md) the method needs.

## Common pitfalls

| Pitfall | Why it breaks the method | Do instead |
|---|---|---|
| Assessing the whole team/agent across domains at once | Averages hide the exact per-domain signal the method exists to produce | One session per unit × domain |
| "We're basically an L4" narrative scoring | Optimism bias inflates exactly the safety dimensions that bound risk | Evidence per item; unevidenced = drop a level |
| Skipping the drill question at L4 (automated limits) | Untested guardrails are documentation, not protection ([governance loop §1](governance-loop.md)) | Ask "when was it last exercised?" — a date or a 0 |
| Reading the safe level as an order to grant | The score informs a human decision; it never authorizes one ([limitations](limitations.md)) | Grantor decision recorded with rationale |
| Averaging a 0 (Submarine Line) into a profile | A zero means *no autonomy at all* in that dimension — it grounds the grant at L0 via the weakest link | Surface the zero loudly; build that dimension first |
| Treating disagreement as failure | The dual-assessor gap is the method's debugging output | Record, reconcile explicitly, feed back |
