# The Autonomy Assessment

> **Status:** v0.1 draft. The practical instrument: a questionnaire and
> scoring procedure that turns the [Maturity Model](maturity-model.md) into
> numbers you can act on.

## 1. When to run an assessment

- **Pre-grant:** before raising a unit's autonomy level in any domain.
- **Standing review:** at the horizon date of each
  [autonomy contract](framework.md#5-autonomy-contracts) (typically quarterly).
- **Post-incident:** after any breach of a guardrail or escalation failure.
- **Org-wide census:** annually, to build the Autonomy Ledger.

## 2. How to run it

1. One assessor from the unit, one from the grantor side. Independent scoring,
   then reconcile — the disagreements are the most valuable output.
2. Score **per domain**, not per unit. A team may be L3 on deploys and L0 on
   hiring; averaging across domains destroys the signal.
3. For each of the six dimensions, answer the questionnaire items below.
   Each item maps to a level; the dimension score is the **lowest** level at
   which all items are true — and **0 (the Submarine Line)** when not even
   the L1 item is true.
4. Record evidence (links, logs, dashboards) for any score ≥ L3. Scores
   without evidence drop one level.
5. Use [`tools/autonomy_score.py`](../tools/autonomy_score.py) to aggregate
   and apply the scoring rules — or the dependency-free web version in
   [`site/`](../site/) (published on GitHub Pages), which walks the same
   questionnaire and prints a scorecard.

## 3. The questionnaire

Levels L2–L5 describe increasing maturity of the unit's own practice; the
**L1 items describe the Ask arrangement** (the unit analyzes and recommends,
everything approved). A dimension where not even the L1 item is true scores
**0 — the Submarine Line**: no autonomy at all in this dimension.

### D1 — Decision clarity

- **L1:** Does the unit know which decisions it may analyze and recommend in
  this domain, and that every decision requires approval?
- **L2:** Can the unit produce a list of decisions it currently makes?
- **L3:** Is there a written inventory naming the decision classes, their
  level, and their limits? Is it current (updated in the last quarter)?
- **L4:** Are thresholds, exceptions, and edge cases codified and versioned
  (not just "the lead knows")?
- **L5:** Has the unit redesigned its own decision inventory in the last two
  cycles, with the changes negotiated rather than discovered?

### D2 — Capability

- **L1:** Can the unit produce a sound analysis or recommendation in this
  domain, even if slowly or with rework?
- **L2:** Are decisions sound but slow, with heavy reliance on one person?
- **L3:** Do playbooks/standard procedures exist, and can *any* member make a
  routine decision to the same standard?
- **L4:** Has the unit handled at least one genuine exception (pressure,
  ambiguity, missing rule) without escalation and without harm?
- **L5:** Has the unit taught this decision domain to another unit, or set a
  standard adopted org-wide?

### D3 — Guardrails

- **L1:** Is every decision gated — nothing acts without the grantor's
  explicit approval?
- **L2:** Are there any stated limits at all — even verbal?
- **L3:** Are limits written and checked (checklist, reviewer, manual gate)?
- **L4:** Are limits **automated** (budget caps, rate limits, CI gates,
  auto-rollback)? Has the automation been exercised (drill or real event)
  in the last two quarters?
- **L5:** Did the unit design its own guardrails, with monitoring, and
  stress-test them (game day, chaos, penetration of limits)?

### D4 — Telemetry

- **L1:** Does the grantor see each decision as part of approving it?
- **L2:** Would a bad decision in this domain be noticed by someone within a
  quarter?
- **L3:** Are there standard dashboards for this domain, reviewed at a fixed
  cadence by the unit?
- **L4:** Are signals near-real-time, with alerts that reach the grantor
  automatically on breach?
- **L5:** Can the unit demonstrate catching and correcting drift *before* any
  external party noticed?

### D5 — Transparency

- **L1:** Is each decision visible to the grantor at approval time?
- **L2:** Can the grantor get a summary of recent decisions on request?
- **L3:** Is there a decision log that stakeholders can find without asking
  anyone?
- **L4:** Does every consequential decision have a written, linkable
  rationale (ADR, note, ticket)?
- **L5:** Could an external auditor reconstruct the decision history and
  reasoning end-to-end?

### D6 — Accountability

- **L1:** Is ownership explicit at approval — the grantor owns what they
  approve?
- **L2:** After the last failure in this domain, was ownership assigned to the
  unit (vs. deflected to the process or grantor)?
- **L3:** Does the unit review its own outcomes on a fixed cadence? Is the
  escalation path written down?
- **L4:** Has the escalation path actually been exercised at least once? Is
  there routine post-incident learning (not blame)?
- **L5:** Has the unit published a failure analysis that another unit has
  reused?

## 4. Scoring procedure

For each dimension `d`, score `S(d) ∈ {0..5}` = the lowest level whose items
are all true, with evidence — or **0 (Submarine Line)** when not even the L1
item is true.

Then, for the **domain under assessment**:

```
Safe grant level  = min(S(D3), S(D4), S(D6))      # weakest-link rule
Expansion headroom = safe level − current granted level
```

Interpretation:

| Safe level | Meaning |
|---|---|
| 0 | **Submarine Line** — nothing is grantable; build guardrails, telemetry, and accountability before any contract |
| 1 | At most an Ask arrangement — analyze and recommend only; invest in guardrails and telemetry before granting more |
| 2 | Grant L2 (inform-after) with basic reporting |
| 3 | Grant L3 with written limits — usually the highest ROI move |
| 4 | Grant L4 with automated guardrails and alerting |
| 5 | Move to outcome accountability; step back to transparency duties only |

## 5. Outputs

Every assessment produces four artifacts, filed with the autonomy contract:

1. **Scorecard** — six dimension scores (0–5) per domain, with evidence links and
   the **ruleset version** that produced them (emitted automatically by the
   CLI and the web tool; see [versioning](versioning.md)).
2. **Gap list** — specific items that failed, ranked by (impact × effort to fix).
3. **Recommended move** — expand / contract / re-shape / hold-and-coach,
   per the [decision table](maturity-model.md#4-from-scores-to-decisions).
4. **Next horizon** — the review date and the specific items to re-check.

A worked end-to-end example lives in
[`examples/README.md`](../examples/README.md).
