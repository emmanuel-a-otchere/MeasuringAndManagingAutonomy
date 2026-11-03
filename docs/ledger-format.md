# Autonomy Ledger format (schema v2)

> **Status:** v2 draft (schema 2, since ruleset v2.0.0). The machine-readable
> form of the [Autonomy Ledger](maturity-model.md#5-the-autonomy-ledger): the
> registry of all autonomy contracts, i.e. the measurement of **granted
> autonomy (supply)**. Schema 1 files (retired 0–4 level scale) are still
> readable but warned about — see [versioning](versioning.md).

## Purpose

The ledger answers: *who holds which decision rights, at what level, under
which guardrails, until when — and is any of that stale or broken?*

Ledger health (coverage and staleness) is an org-level metric; the tool
[`tools/ledger_health.py`](../tools/ledger_health.py) computes it.

## File

`examples/ledger.yaml` is the reference ledger, seeded from the
[worked example](../examples/README.md). Copy it as your starting point.

The file declares its format version with a top-level `schema: 2`. A missing
`schema:` field is treated as the current supported schema (backward
compatibility with pre-versioning files); a `schema: 1` file is still
validated but warned about (retired 0–4 level scale — re-baseline), and
newer schemas are flagged but still validated — see
[versioning](versioning.md).

## Schema

One YAML file, top-level key `contracts`, a list of autonomy contracts:

```yaml
contracts:
  - id: payments-deploys-v2          # required, unique, stable across versions
    unit: payments-team              # required
    domain: production-deploys       # required, machine-friendly slug
    level: 3                         # required, 0-5 (L0 Submarine Line .. L5 Accountable)
    scope: >                         # required, human sentence
      Production deploys of the payments service (excl. schema migrations).
    guardrails:                      # required, non-empty list
      - CI gates mandatory on every deploy
      - Canary on every deploy
      - Auto-rollback exercised before go-live
    telemetry:                       # required, non-empty list
      - Deploy log shared with grantor
      - Error budget dashboard, grantor-visible
    revocation_triggers:             # required, non-empty list
      - Error budget burn > 50% in a week
    escalation: oncall-lead -> eng-director, 30-min SLA business hours
    grantor: eng-director-payments   # required
    horizon: 2025-12-31              # required, ISO date
    last_review: 2025-09-30          # required, ISO date, <= horizon
    review_cadence_days: 90          # optional, default 90
    status: active                   # active | expired | revoked | draft
    notes: >
      Formalized 2025-07 after inventory found shadow autonomy at ~L2.
```

### Field rules

| Field | Rule |
|---|---|
| `id` | Unique; version the contract (`-v2`) rather than mutating history in place |
| `level` | Integer 0–5 (definitive levels 1–5; 0 = Submarine Line — no autonomy at all) |
| `horizon`, `last_review` | ISO-8601 dates; `last_review` ≤ `horizon` |
| `status` | `active` contracts must have all required fields; `draft` is exempt from health penalties but listed |
| `guardrails`, `telemetry`, `revocation_triggers` | Non-empty lists — a contract without them is not a contract (see framework §5) |

## Health report

`tools/ledger_health.py <ledger.yaml> [--today YYYY-MM-DD]` validates the
schema and reports org-level health:

- **Validity** — schema errors (bad level, missing fields, `last_review > horizon`)
- **Coverage** — fraction of contracts with all required fields
- **Staleness** — contracts whose `last_review` is older than their cadence
- **Expiry** — `active` contracts past `horizon` (autonomy with no live review)
- **Guardrail hygiene** — contracts with empty guardrail/telemetry/trigger lists

Exit code is non-zero if any check fails, so it can run in CI.

Run the tool's self-test with `python3 tools/ledger_health.py --self-test`.

## Next steps

- [Worked example ledger](../examples/ledger.yaml)
- [Autonomy contract & review agenda template](contract-template.md)
- [Maturity model: the Autonomy Ledger](maturity-model.md#5-the-autonomy-ledger)
