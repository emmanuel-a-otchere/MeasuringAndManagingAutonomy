# Validation plan

> `mama`'s core claim — that assessment signals bound safe autonomy — is a
> **hypothesis**, not a finding. This program tests it. Until it reports,
> the method is labeled **pilot / under validation** everywhere it is
> presented.

## Design principles

- Evidence before claims; publish methods, context, and limitations with
  any findings.
- A successful pilot is **not** certification or proof of universal
  validity — it establishes the method is decision-useful where tested.
- Any MAJOR scoring change re-triggers validation for the changed surface
  ([versioning policy](versioning.md)).

## 1. Independent desk review

Before field work: an independent review of construct validity, rubric
clarity, usability, risk proportionality, privacy, and accessibility.
Findings and resulting changes are published.

## 2. Pilot program

- **Scale:** at least **6 decision domains** across **3+ organizations** and
  **2+ sectors**; different unit types (human team, service, AI agent)
  included where feasible.
- **Protocol:** the [handbook](handbook.md) steps run as written; each pilot
  site records contracts, scorecards (with `ruleset_version`), evidence
  links, and review outcomes.
- **No pooling** of unlike domains without stated rationale.

## 3. Inter-rater analysis

Dual independent assessors on a representative sample of domains. Report
agreement and disagreement patterns per dimension, and document how
reconciliations were handled — disagreements are data about rubric clarity.

## 4. Decision-usefulness and outcome correspondence

Pre-state the outcomes to look for (breaches, incidents, over-grants,
under-grants, unused headroom, shadow-autonomy discoveries) **before**
collecting data. Then test whether weakest-link results and dimension
signals correspond to those outcomes. Report descriptive vs. causal
readings honestly — the design supports the former.

## 5. MAMA interface test

Where a consumer connects outputs to the broader **MAMA** framework, test
the [interface](mama-integration.md): stable use-case identifiers, versioned
exports, and linked automation/value measures — confirming the measures
stay separate and interpretable.

## 6. Publication

For each pilot wave, publish: methods, sample and context, consent and
anonymization approach, findings, limitations, changes made as a result, and
unresolved questions — in this repository, linked from the
[changelog](../CHANGELOG.md).

## Status

| Step | State |
|---|---|
| Desk review | not started |
| Pilot (6+ domains / 3+ orgs / 2+ sectors) | not started |
| Inter-rater analysis | not started |
| Outcome correspondence | not started |
| Interface test | not started |
| Publication | — |

Until all rows report, keep the **pilot / under validation** label in the
[README](../README.md) and scorecard-facing materials. Want to help? Pilot
sites and case studies are the highest-value contributions — see
[CONTRIBUTING.md](../CONTRIBUTING.md).
