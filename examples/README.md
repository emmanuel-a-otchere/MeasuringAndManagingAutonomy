# Worked Example: The Payments Team and Deployment Autonomy

> A single team, scored end to end with the
> [Assessment](../docs/assessment.md), producing a governance move.

## Context

- **Unit:** Payments team (6 engineers, 1 PM)
- **Domain:** Production deployment of the payments service
- **Current grant (informal, discovered during inventory):** "The team
  deploys whenever they feel ready; the engineering director approves
  anything risky." — i.e., *shadow autonomy*: exercised somewhere between L1
  and L2, granted nowhere on paper. Blast radius: customer payments — high.
  Reversibility: good (deploys are rollback-able) — so L2+ is plausible *if*
  guardrails exist.

## Step 1 — Score the six dimensions

| Dim | Score | Evidence / what's missing |
|---|---|---|
| D1 Decision clarity | **1** | No written inventory; "risky" is undefined; the director cannot name the actual limits |
| D2 Capability | **3** | 40+ deploys/quarter, consistent quality, one real exception (failed migration) handled well |
| D3 Guardrails | **2** | CI gates + manual review exist; no cap, no canary, auto-rollback never exercised |
| D4 Telemetry | **2** | Error dashboard exists; alerts go to the team chat but not the grantor; usage not tracked |
| D5 Transparency | **1** | Deploy log exists only in the CI tool; no written rationale for consequential deploys |
| D6 Accountability | **1** | No escalation path written down; last incident review was ad hoc and blame-tinged |

## Step 2 — Apply the scoring rules

```
Safe grant level = min(D3, D4, D6) = min(2, 2, 1) = 1
Current *formal* grant = none (shadow autonomy at ~L2)
```

The team is *operating above* its legitimate level — not because it is
untrustworthy (D2 = 3 shows strong capability), but because D6
(accountability) and the surrounding contract are missing. The gap analysis
says: **formalize or stop.** The right answer is *formalize at L2* with
guardrails that D3 already nearly meets, plus a hard fix on D6.

## Step 3 — The grant (autonomy contract, first version)

| Field | Value |
|---|---|
| Domain | Production deploys, payments service (excl. schema migrations) |
| Level | **L2** — inform-after within contract limits |
| Guardrails | CI gates mandatory; canary on every deploy; ≤ 10 deploys/day; spending on infra changes capped; auto-rollback exercised before go-live |
| Horizon | 3 months (shortened — new level for this team) |
| Telemetry | Deploy log + error budget dashboard shared with grantor; breach alert routed to grantor automatically |
| Revocation triggers | Error budget burn > 50% in a week; any un-reviewed migration; missed review cadence |
| Escalation path | On-call lead → engineering director, 30-min SLA during business hours |

## Step 4 — The review, one horizon later

- D3 rose to **3** (canary + exercised auto-rollback, drill completed).
- D4 rose to **3** (grantor-visible alerts live).
- D6 rose to **2** (written escalation path, first self-run review done).
- D1 rose to **2** (deploy inventory written).
- Usage: 26 deploys/month, zero breaches, one alert (handled within SLA).

```
Safe level = min(3, 3, 2) = 2  → hold at L2, one more cycle before expansion
```

Per the [decision table](../docs/maturity-model.md#4-from-scores-to-decisions):
all dimensions trending up and stable, but only one clean review cycle —
the loop requires **two consecutive clean cycles before expansion**, so the
move is **hold**, with D6 named as the dimension to watch.

## What this example demonstrates

1. **Shadow autonomy is found, not punished** — the inventory converted an
   informal practice into a legitimate, guardrailed grant.
2. **Capability did not decide the level** — D2 was already 3, but the
   weakest-link rule (`min(D3,D4,D6)`) correctly held the grant to what the
   safety net could support.
3. **Small, dated contracts beat permanent vague trust** — three months,
   explicit triggers, and a re-raise path made expansion a routine decision
   rather than a political one.

Try scoring your own team with
[`tools/autonomy_score.py`](../tools/autonomy_score.py).
