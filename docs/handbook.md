# The `mama` Method Handbook

> **Status:** v2 (tracks `RULESET_VERSION` 2.0.0). The end-to-end operating
> guide: how to run `mama` on a real unit and domain, in order, with the
> canonical documents linked at each step. This handbook moves with the
> ruleset — a MAJOR ruleset bump revises it.

`mama` (lowercase — *measuring and managing autonomy*) is the autonomy
method and toolkit whose home is this repository. It is the
autonomy-governance component used within the broader **MAMA** (*Measuring
Automation & Measuring Autonomy*) framework; see the
[integration guide](mama-integration.md) for the boundary. The two names are
not interchangeable.

## Step 0 — Read the ground rules

- **Units and domains, not vibes.** Autonomy is assessed per **unit ×
  decision domain** — never per brand, model, or organization-wide average
  ([framework §2–3](framework.md)). Averaging across domains destroys the
  signal.
- **Grants, never assumptions.** Autonomy exists only where a
  [contract](framework.md#5-autonomy-contracts) grants it: scope, level,
  horizon, grantor, guardrails, telemetry, escalation, revocation triggers.
- **The Submarine Line is the floor.** L0 means *no autonomy at all* —
  nothing granted, nothing to review. Definitive grants are
  [L1–L5](framework.md#4-the-five-levels-of-autonomy-and-the-submarine-line).

## Step 1 — Inventory units and decision domains

List the units whose autonomy you will govern, and for each, the decision
classes they hold or reach for. Include informal and shadow autonomy — the
first inventory usually finds decisions being made nowhere on paper. Record
blast radius and reversibility per domain; they bound the grantable level
([framework §4 rules](framework.md#4-the-five-levels-of-autonomy-and-the-submarine-line)).

## Step 2 — Draft the contract

For each unit × domain, write an
[autonomy contract](contract-template.md): scope with explicit exclusions,
level per decision class with the guardrails that justify it, horizon, named
grantor, telemetry obligations, escalation route, and revocation triggers.
**Test guardrails before the grant goes live** — untested guardrails are
documentation, not protection ([governance loop §1](governance-loop.md)).

## Step 3 — Assess the unit (per domain)

Run the [assessment](assessment.md): one assessor from the unit, one from
the grantor side; score independently, then reconcile — the disagreements
are the most valuable output. Score the six dimensions
([questionnaire](assessment.md#3-the-questionnaire)) with **evidence** for
any score ≥ L3; unevidenced scores drop a level. Use the
[`autonomy-score` CLI](../README.md#quick-start-score-a-team) or the
[web version](../site/) and record the `ruleset_version` printed with the
scorecard.

## Step 4 — Apply the weakest-link rule and decide

The safe grant level is `min(D3, D4, D6)` — guardrails, telemetry, and
accountability bound the grant. D1/D2 gaps are coaching signals, not
revocation signals. The score is an **evidence input to a human decision**,
never an automatic authorization: the grantor weighs domain risk, blast
radius, and context before granting
([maturity model §4](maturity-model.md#4-from-scores-to-decisions)).

## Step 5 — Record the grant in the ledger

Enter the contract in the [Autonomy Ledger](ledger-format.md) (`schema: 2`),
including evidence references and the ruleset version used for the baseline.
Check ledger health (`ledger-health`) — coverage and staleness are
org-level metrics. For AI agents and other technology units, read
[agents as units](agents-as-units.md) first: enforced tool limits, decision
logging, and the material-change rule (new agent version ⇒ re-assess).

## Step 6 — Instrument and observe

Stand up the three signal sets before the grant goes live — usage, outcome,
and breach signals — with breach alerts routed to both unit and grantor.
Between reviews, nobody intervenes inside a live contract; intervention
itself is a logged breach ([governance loop §2–3](governance-loop.md)).

## Step 7 — Review at the horizon

At each contract horizon, re-assess, compare granted vs. exercised autonomy,
walk the incident log, and decide the move: **expand, contract, re-shape, or
revoke** (revocation triggers fire immediately). Level raises are
incremental — at most one level per cycle absent a documented capability
review. Use the [review agenda](contract-template.md#review-agenda-template-per-horizon).

## Step 8 — Feed the loop (and MAMA, where used)

Every review produces a dated, versioned record. Where the broader **MAMA**
framework consumes your outputs, link them by stable use-case identifiers
and keep autonomy measures separate from automation/value measures —
[integration guide](mama-integration.md).

## Escalation and revocation

Escalation routes and revocation triggers are agreed **up front** in the
contract. A fired trigger steps the level down immediately, then an early
review follows within five working days. Anti-patterns — panic revocation,
ratchet-only-up, vague horizons — are named so you can enforce against them
([governance loop §5](governance-loop.md)).

## Known limits

Read [limitations](limitations.md) before claiming anything from a score:
the method is **pilot / under validation** until the
[validation program](validation-plan.md) reports.
