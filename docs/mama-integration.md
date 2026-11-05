# `mama` ↔ MAMA integration guide

> The interface between **`mama`** (*measuring and managing autonomy* — this
> method and toolkit, whose canonical home is this repository) and **MAMA**
> (*Measuring Automation & Measuring Autonomy* — the broader framework that
> uses `mama` alongside automation measurement and value tracking).

## The boundary in one table

| | **`mama`** (this repository) | **MAMA** (umbrella framework) |
|---|---|---|
| Owns | Autonomy vocabulary; the L0–L5 scale; autonomy contracts; the ledger; assessment rules and scoring; autonomy evidence; grant-review recommendations | Portfolio/project framing; automation measurement; value hypotheses and baselines; cross-project and organizational synthesis |
| Answers | What authority does this unit hold, how well is it held, and what should the grant do next? | Are our automation and autonomy investments producing intended outcomes? |
| Core artifacts | Contracts, ledgers, scorecards, CLI/site tools | Use-case records, automation/value dashboards, synthesis |

**Names are not interchangeable.** `mama` is a component used within MAMA;
this repository is not the MAMA umbrella home, and MAMA is not an autonomy
scoring framework.

## How the systems link

1. **Stable identifiers.** Every MAMA use-case/project record carries
   identifiers that link to the `mama` side: unit id, decision domains,
   contract id and version, and scorecard (ruleset version + date).
2. **Versioned, machine-readable exports.** `mama` outputs are already
   structured: `autonomy-score --json` emits the scorecard
   (`ruleset_version`, per-dimension scores, `safe_grant_level`,
   `granted_level`, notes, `recommended_move`); the
   [ledger](ledger-format.md) is YAML (`schema: 2`) with contracts carrying
   scope, level, guardrails, telemetry, escalation, revocation triggers,
   grantor, horizon, review history, and status. Consumers should persist
   the `ruleset_version` and `schema` alongside every record.
3. **Reviews stay in `mama`.** Expand/contract/re-shape/revoke decisions
   come from the [governance loop](governance-loop.md) using contract,
   profile, telemetry, and incidents. MAMA context (automation outcomes,
   value signals) is an **input** a grantor may consider, not an override
   of the method.

## Keep the measures separate

Autonomy scores and automation/value metrics answer different questions and
must remain **separately interpretable**. Do **not** invent a composite
"MAMA score" that blends autonomy levels with automation performance or
value measures unless its purpose, weights, validity, and limitations are
established and tested — and published. Correlation is the interface:
e.g., does an expanded autonomy grant coincide with improved
successful-completion or exception rates for the linked use case? Report
such relationships as descriptive unless a causal design justifies more.

## Data handling

Assessment and ledger data can name people, teams, and sensitive internal
controls. Exchange must support:

- **Evidence minimization** — export scores, levels, versions, and dates;
  keep raw evidence references as links, not copies.
- **Access control and redaction** — a scorecard should not expose
  sensitive organizational or personal information by default; redact unit
  names where the audience doesn't need them.
- **Local/offline use** — the CLI and web assessment run entirely locally;
  nothing leaves the environment unless the user sends it.
- **Retention and traceability** — preserve historical records; every
  exported record carries `ruleset_version` and ledger `schema`, and
  re-baselines follow the [migration policy](migration-v1-to-v2.md).

## What MAMA does with `mama` outputs

Typical connections (all consumer-side): linking grants to eligible-work
coverage, successful-completion and exception/rework rates, latency,
availability, recovery, costs, and customer/worker impacts; comparing
pre/post a grant change within a use case; portfolio views of where
autonomy concentrates vs. where outcomes lag. See also
[vendor-neutral capability mapping](positioning.md) for the tooling
categories that can supply such measures.
