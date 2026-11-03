# AI Agents as Units — a first-pass extension

> **Status:** v0.2 draft (first pass, per the
> [roadmap](roadmap.md)). This document applies the existing framework —
> the [three axes](framework.md#3-the-three-axes-of-autonomy), the
> [five levels](framework.md#4-the-five-levels-of-autonomy), the
> [six dimensions](maturity-model.md#2-the-six-dimensions), and the
> [weakest-link rule](maturity-model.md#scoring-rules) — to AI agent units.
> **The scoring engines and `RULESET_VERSION` are unchanged**: an agent is
> assessed with the same instrument as a team
> ([`autonomy-score`](../tools/autonomy_score.py)); only the *interpretation*
> of the dimensions is agent-specific. Validation against real agent
> deployments may later justify new dimensions — that would be a versioned
> ruleset change, not a silent one ([versioning](versioning.md)).

## 1. Why agents are the hard case

The framework's [core definition](framework.md#2-core-definitions) already
names the AI agent as a unit type — and agents are where implicit autonomy
management fails hardest:

- **No tenure ramp.** Human autonomy is granted gradually as trust accumulates.
  An agent arrives at full execution speed on day one; there is no natural
  probation period unless one is designed.
- **Machine scale.** A human's worst hour is bounded by being one person. An
  agent's worst hour is bounded only by its tool access — the blast radius of
  an unbounded loop is unbounded.
- **Memory is not an audit log.** Human organizations rely on people who
  "remember why" for transparency and accountability. Agents have neither
  memory nor shame; everything that is not logged at decision time is gone.
- **Shadow autonomy is the default.** An agent with a broad prompt and a
  broad tool grant is exercising decision rights that exist on no ledger —
  the framework's definition of [shadow autonomy](maturity-model.md#5-the-autonomy-ledger).

The remedy is the same as for teams: make the autonomy explicit, bounded,
instrumented, and time-boxed. What changes is what the six dimensions mean.

## 2. What transfers unchanged

Everything structural:

- The **three axes** (scope, level, horizon) — an agent's grant names decision
  domains, a level, and an expiry like any unit's.
- The **five levels** L0–L4 — see the concrete reading in [§4](#4-the-levels-for-an-agent-domain).
- **Autonomy contracts** — same six elements; for agents the "unit" field
  names the agent (and version), the `guardrails` are mostly *enforced by
  tooling* rather than by social norms, and the contract must name a **human
  grantor** (see [§6](#6-accountability-stays-human)).
- The **Autonomy Ledger** — same schema, same
  [health checks](ledger-format.md#health-report); agent contracts sit in the
  same ledger as human ones. Reference:
  [`examples/agents-ledger.yaml`](../examples/agents-ledger.yaml).
- The **weakest-link rule** — `min(D3, D4, D6)` binds agents for the same
  reason it binds teams, and for one more: an agent will exploit any missing
  guardrail *faster and more literally* than a team ever would.
- The **guardrail rule** and the **reversibility rule** — level *n* requires
  tested level-*n* guardrails; blast radius and reversibility bound the level.

## 3. The six dimensions, read for an agent

Score each dimension exactly as in the
[questionnaire](assessment.md#3-the-questionnaire) — the item text still
applies; the table below is the translation guide for agent units.

| # | Dimension | For an agent unit, the evidence is… |
|---|---|---|
| D1 | **Decision clarity** | A written decision inventory for the agent: task classes, tool allow-list, spend/action caps, refusal rules — versioned with the agent (prompt + policy in git counts; a chat paragraph does not). L3 = thresholds and exceptions codified and versioned. |
| D2 | **Capability** | Measured task performance: an eval suite covering the routine decision classes, run on every agent change, with pass rates per class. L3 = the agent handled a genuine out-of-distribution case without harm and without escalation. |
| D3 | **Guardrails** | Enforced tool-level limits: spend caps, rate limits, allow-lists, sandboxing, dry-run mode, auto-rollback. L3 requires the enforcement be **automated and exercised** (drill or real trip) in the last two quarters. |
| D4 | **Telemetry** | Structured logs of every decision (input, output, tools used, cost, confidence/rationale if present) plus near-real-time anomaly alerts — spend rate, refusal rate, escalation rate, loop detection — routed to the grantor automatically. |
| D5 | **Transparency** | Every consequential action linkable to prompt version + policy version + input + output. Agents have an advantage here: the full trail *can* exist; L4 is an external auditor reconstructing history end-to-end. |
| D6 | **Accountability** | The human–agent arrangement: a named owner per domain, an escalation path that has actually fired and been improved, post-incident eval updates shipped. An agent scores on the system around it — see [§6](#6-accountability-stays-human). |

## 4. The levels for an agent domain

| Level | Name | An agent at this level… |
|---|---|---|
| L0 | **Ask** | Proposes only — drafts the action (the email, the refund, the PR) for a human to execute. |
| L1 | **Inform-after** | Executes and reports; every action reviewable and reversible by the grantor (e.g. acts in a staging path, or with next-day review of the log). |
| L2 | **Guardrailed** | Acts freely inside enforced limits — tool allow-list, per-action and per-day caps, hard refusal classes. The usual right size for production agents. |
| L3 | **Supervised** | Acts with a monitoring function intervening on trigger (anomaly alert → human pause), not on pre-approval. Requires D4 at L3+. |
| L4 | **Accountable** | Owns the domain within outcome accountability — e.g. redesigns its own guardrail thresholds under audit duties. Rare; requires all six dimensions at L4 and an owner who accepts the accountability terms. |

The two framework rules bite hardest here:

- **Guardrail rule:** an agent at L2 with unenforced limits is not L2 — it is
  an L0 agent that has been *assumed* into L2. Prompt text saying "do not
  spend more than…" is a verbal norm (D3 ≤ L1), not a guardrail.
- **Reversibility rule:** irreversible actions (payments sent, emails to
  customers, production data deletes) stay L0–L1 regardless of eval scores —
  unless a guardrail makes them effectively reversible (escrow, hold-for-review,
  soft delete).

## 5. Starter menus for contracts and ledgers

`guardrails`, `telemetry`, and `revocation_triggers` are required non-empty
lists in the [ledger format](ledger-format.md#schema). For agent contracts,
good starter entries:

**Guardrails** — spend cap per action / per day (enforced by the tool, not the prompt) · tool allow-list · rate limit · dry-run/plan mode for writes · sandboxed execution · hold-for-review class for irreversible actions · auto-rollback where the domain allows it.

**Telemetry** — structured decision log (input, output, tools, cost) · grantor-visible dashboard · anomaly alerts on spend/refusal/escalation rate · loop/repetition detector · eval pass-rate trend per release.

**Revocation triggers** — any guardrail trip without a matching drill · spend > cap × in a day (automatic step-down to L0) · eval pass-rate drop > n points on a release · unexplained escalation-rate spike · missed review cadence · prompt/policy change without re-assessment.

That last one is the agent-specific rule of thumb: **a material change to the
agent (prompt, model, tools, policy) is a new unit-version and restarts the
clock** — re-assess before the new version keeps its predecessor's level.

## 6. Accountability stays human

A unit can hold decision rights; accountability for outcomes must land
somewhere a consequence can land. For agent units, D6 scores the *arrangement*:

- every agent contract names a human `grantor` who owns the domain's outcomes;
- the escalation path is human-reachable and has been exercised;
- post-incident learning updates the agent (evals, policy, limits) — the fix
  is shipped, not just discussed.

An agent whose owner cannot say, in one sentence, what they are accountable
for when the agent fails is at D6 ≤ L1 — and the weakest-link rule caps the
grant accordingly, no matter how good the evals are.

## 7. Worked mini-example

A support-desk **refund agent** (decides refunds on tickets; money leaves the
company). First contract: L1 inform-after, cap $50, quarterly review. At the
horizon, the assessment:

```
$ python3 tools/autonomy_score.py 3 3 2 3 2 2 --current 1
...
Safe grant level (min D3,D4,D6): L2
Currently granted level:       L1
Recommended move: expand (after 2 clean cycles): raise one level or widen
scope in the strongest dimension
```

Reading: D1 = 3 (inventory of refund classes versioned with the policy), D2 = 3
(eval suite with pass rates; handled one OOD case cleanly), D3 = 2 (caps
written and checked, but the $50 cap is a checkout setting — enforced, though
never drilled), D4 = 3 (every refund logged; spend-rate alerts reach the
grantor), D5 = 2 (decision log stakeholders can find), D6 = 2 (owner named,
escalation defined but not yet exercised). Weakest link 2 → **safe L2**:
expand the grant to guardrailed (cap $200, allow-list of refund reasons,
hold-for-review over $100), drill the auto-step-down, exercise the escalation
path, re-review next horizon. A fuller ledger for this example (plus a
draft-stage docs agent) lives at
[`examples/agents-ledger.yaml`](../examples/agents-ledger.yaml).

## 8. Open questions

- **The unit boundary for multi-agent systems** — score the swarm or each
  agent? First-pass answer: each agent is a unit; a shared policy/tool grant
  is a contract on the *system*, and the agents' grants reference it.
- **Agent-to-agent grants** — can an agent be a grantor? Not under this
  framework today: grantors hold accountability, and accountability is human
  ([§6](#6-accountability-stays-human)).
- **Eval-to-level validity** — does eval pass rate actually predict safe
  level? That is the same open question as the human side's
  [validation roadmap item](roadmap.md), and needs real deployments.
- **Drift and versioning** — how much prompt/model drift before the unit is
  "the same unit"? The working rule ([§5](#5-starter-menus-for-contracts-and-ledgers)):
  material change ⇒ new version ⇒ re-assess. Precision awaits case studies.

## Next steps

- Score an agent domain with the same tools:
  [`autonomy-score`](../tools/autonomy_score.py) · [assessment](assessment.md)
- Ledger an agent contract: [`agents-ledger.yaml`](../examples/agents-ledger.yaml)
  ([format](ledger-format.md), [health tool](../tools/ledger_health.py))
- [Governance loop](governance-loop.md) — cadence and anti-patterns apply as-is
