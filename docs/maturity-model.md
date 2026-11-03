# The Maturity Model

> **Status:** v0.1 draft. The measurement half of the framework:
> [framework.md](framework.md) defines *what* autonomy is; this document
> defines *how much* of it exists and how well it is used.

## 1. Purpose

The maturity model serves two distinct measurement jobs:

1. **Calibrate grants** — before granting a level, verify the unit's *capability*
   maturity supports it.
2. **Score performance** — after granting, measure whether autonomy is being
   used well enough to keep or expand.

## 2. The six dimensions

Each dimension is scored 0–5: the definitive autonomy levels **L1–L5** from
the [framework](framework.md#4-the-five-levels-of-autonomy), with **L0 — the
Submarine Line — reserved for no autonomy at all** (the unit holds nothing in
this domain: no decision rights, not even analysis standing). A unit's
maturity profile is the vector of its six scores.

| # | Dimension | Question it answers |
|---|---|---|
| D1 | **Decision clarity** | Does the unit know exactly which decisions it owns, at what level, with what limits? |
| D2 | **Capability** | Does the unit have the skills and tools to make this class of decisions well? |
| D3 | **Guardrails** | Are the limits, budgets, automated checks, and rollback paths that justify the level in place and *tested*? |
| D4 | **Telemetry** | Can the unit and its grantor observe the consequences of decisions quickly and accurately? |
| D5 | **Transparency** | Are decisions, reasoning, and outcomes visible to affected parties and auditable later? |
| D6 | **Accountability** | Does the unit own outcomes — including failure — and does an escalation path actually work? |

## 3. The grid

| Dimension | L0 (Submarine Line) | L1 Ask | L2 Inform-after | L3 Guardrailed | L4 Supervised | L5 Accountable |
|---|---|---|---|---|---|---|
| **D1 Decision clarity** | No standing in this domain: the unit holds no decision rights and is not part of the decision process | No inventory of decisions; everything runs through the grantor ad hoc | Unit can list its decisions but boundaries are informal | Written decision inventory with explicit limits per class | Limits, thresholds, and exceptions are codified and versioned | Unit redesigns its own decision inventory; boundaries are negotiated, not discovered |
| **D2 Capability** | No decisions made — nothing to assess | Decisions routinely need rework or reversal | Decisions are sound but slow; heavy reliance on one person | Repeatable decision quality across the team, standard playbooks | Predictable quality under pressure; exceptions handled without drama | Unit teaches decision-making to others; sets org-wide standards |
| **D3 Guardrails** | No grant, so no unit guardrails — the Submarine Line itself (total pre-approval or no engagement) is the protection | None beyond the approval gate; safety comes from pre-approval | Verbal norms ("don't spend more than…") | Written limits enforced by checklists and reviews | Automated enforcement (budgets, rate limits, CI gates, auto-rollback) exercised regularly | Guardrails are self-designed, monitored, and stress-tested by the unit |
| **D4 Telemetry** | No decisions to observe | Outcomes discovered weeks later, by others | Post-hoc reporting; manual, inconsistent | Standard dashboards for key decisions, reviewed at set cadence | Near-real-time signals; anomaly alerts reach the grantor automatically | Predictive signals; the unit detects and corrects drift before the grantor sees it |
| **D5 Transparency** | No decisions to disclose | Decisions invisible outside the room | Summary reports on request | Decision log accessible to stakeholders | Every consequential decision has a written, linkable rationale | Externally auditable trail; transparency duties designed into the workflow itself |
| **D6 Accountability** | No owned outcomes | Blame shifts to the grantor or the process | Outcomes reviewed only after failures | Unit reviews its own outcomes at fixed cadence; escalation path defined | Escalation path exercised and improved; post-incident learning is routine | Unit accounts for outcomes to the org; failure analysis is published and reused |

### Scoring rules

- Score each dimension **independently** at the highest level *fully* achieved
  (all row cells for that level true). Partial achievement of a level scores
  as the level below. A dimension where not even the L1 cell is true scores
  **0** — the Submarine Line for that dimension.
- **The weakest Link rule:** the safe autonomy level for a *grant* is
  `min(D3, D4, D6)` — guardrails, telemetry, and accountability bound the level,
  because a breach in any of them turns autonomy into unmanaged risk. A safe
  level of 0 means nothing is grantable yet: stay on the Submarine Line and
  build the safety dimensions first.
- Capability (D2) and clarity (D1) gaps are *coaching* signals, not
  *revocation* signals. They cap the pace of expansion, not the current grant.

## 4. From scores to decisions

| Profile pattern | Management move |
|---|---|
| All dimensions ≥ current grant level, stable for 2+ review cycles | **Expand** — raise level or widen scope for the strongest dimensions |
| D3/D4/D6 below grant level | **Contract or re-shape** — fix guardrails/telemetry first; step down only if a breach occurred |
| D1/D2 lag the rest | **Hold and coach** — keep the grant, invest in clarity and capability |
| Used autonomy consistently below granted (unused headroom) | **Clarify or shrink** — the contract is either confusing or wrong-sized |
| Exercised autonomy above granted (shadow autonomy) | **Legitimate or stop** — either formalize the practice into the contract or enforce the boundary immediately |

## 5. The Autonomy Ledger

The ledger is the registry of all autonomy contracts — the measurement of
**granted autonomy (supply)**:

| Unit | Domain | Level | Guardrails | Horizon | Telemetry | Last review | Revocation triggers |
|---|---|---|---|---|---|---|---|
| Payments team | Production deploys | L2 | CI gates, canary, auto-rollback, 2 deploys/day cap | 2025-12-31 | Deploy dashboard, error-rate alerts | 2025-06-30 | Error budget burn > 50% in a week |
| *…add rows per grant* | | | | | | | |

Ledger hygiene is itself a maturity signal: an organization whose ledger is
incomplete has *shadow autonomy* — real decision rights that exist nowhere on
paper. The first assessment in most organizations should start by inventorying
granted autonomy, including the informal kind.

The ledger has a machine-readable format — see
[ledger-format.md](ledger-format.md) — with a reference file at
[`examples/ledger.yaml`](../examples/ledger.yaml) and a validation/health tool
at [`tools/ledger_health.py`](../tools/ledger_health.py).

## Next steps

- Run the [Assessment](assessment.md) to produce scores in practice
- See the [Worked Example](../examples/README.md)
- Automate the arithmetic with [`tools/autonomy_score.py`](../tools/autonomy_score.py)
