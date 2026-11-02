# Autonomy Ledger format (v1)

> **Status:** v0.1 draft. The machine-readable form of the
> [Autonomy Ledger](maturity-model.md#5-the-autonomy-ledger): the registry of
> all autonomy contracts, i.e. the measurement of **granted autonomy
> (supply)**.

## Purpose

The ledger answers: *who holds which decision rights, at what level, under
which guardrails, until when — and is any of that stale or broken?*

Ledger health (coverage and staleness) is an org-level metric; the tool
[`tools/ledger_health.py`](../tools/ledger_health.py) computes it.

## File

`examples/ledger.yaml` is the reference ledger, seeded from the
[worked example](../examples/README.md). Copy it as your starting point.

## Schema

One YAML file, top-level key `contracts`, a list of autonomy contracts:

```yaml
contracts:
  - id: payments-deploys-v2          # required, unique, stable across versions
    unit: payments-team              # required
    domain: production-deploys       # required, machine-friendly slug
    level: 2                         # required, 0-4 (L0-L4)
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
| `level` | Integer 0–4 |
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
- [Autonomy contract template](contract-template.md)
- [Maturity model: the Autonomy Ledger](maturity-model.md#5-the-autonomy-ledger)
