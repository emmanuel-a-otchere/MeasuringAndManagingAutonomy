# Autonomy Contract Template

> Copy this template per contract. A worked instance lives in
> [`examples/ledger.yaml`](../examples/ledger.yaml) and
> [`examples/README.md`](../examples/README.md). Field rules:
> [ledger-format.md](ledger-format.md). See
> [framework.md §5](framework.md#5-autonomy-contracts) for the reasoning.

```markdown
# Autonomy Contract — <unit> / <domain>

| Field | Value |
|---|---|
| **ID** | <unit>-<domain>-v<n> |
| **Unit** | <who holds the autonomy> |
| **Grantor** | <named person/role — no grantor, no autonomy> |
| **Domain** | <decision class, e.g. production deploys> |
| **Level** | <L0 Ask / L1 Inform-after / L2 Guardrailed / L3 Supervised / L4 Accountable> |
| **Horizon** | <ISO date — "ongoing" is not a horizon> |
| **Review cadence** | <default quarterly; monthly after a level raise> |
| **Status** | <active / draft / expired / revoked> |

## Scope
What this contract covers — the decision classes granted, and the
explicit exclusions (what still requires approval).

## Guardrails (justify the level)
- <written limit / automated cap / checklist / rollback path — each one
  tested, with the date of its last exercise>

## Telemetry obligations
- <usage signal>, <outcome signal>, <breach signal routed to grantor>

## Revocation triggers
- <observable, pre-agreed conditions that step the level down immediately>

## Escalation path
<route + SLA for decisions that exceed this contract's scope>

## Assessment baseline
D1 clarity / D2 capability / D3 guardrails / D4 telemetry / D5 transparency /
D6 accountability — scores with evidence, per docs/assessment.md.
Safe level (min D3, D4, D6): <L*>
Ruleset version used for this baseline: <e.g. 1.0.0> (see docs/versioning.md —
scores are comparable only within the same MAJOR ruleset version)

## Notes
<why this level, what changed vs the previous version, incident history>
```

## Review agenda template (per horizon)

Use at each [contract review](governance-loop.md#4-review):

1. **Scores** — re-score the six dimensions (dual assessor, evidence-based)
2. **Gap analysis** — granted vs exercised autonomy: unused headroom or shadow autonomy?
3. **Incident walk** — breaches, alerts, escalations since last review
4. **Move decision** — expand / contract / re-shape / hold-and-coach, with the next horizon date
5. **Ledger update** — version the contract (`-v<n+1>`), record the review date
