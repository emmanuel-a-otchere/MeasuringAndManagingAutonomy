# `mama` machine-readable export format (scorecard export v1)

> The interface by which consumers — primarily the broader **MAMA**
> framework — ingest `mama` outputs. See the
> [integration guide](mama-integration.md) for the ownership boundary and
> data-handling rules; this document specifies the payload.

## Principles

1. **Versions travel with the data.** Every record carries
   `ruleset_version` and (where a ledger is referenced) the ledger `schema`.
   Consumers MUST NOT compare records across different MAJOR
   `ruleset_version`s
   ([versioning policy](versioning.md), [migration](migration-v1-to-v2.md)).
2. **Evidence minimization.** Export references (ids, URLs), not raw
   evidence. A conforming export contains no personal data beyond the
   linkage fields the exporter chooses to include.
3. **No derived composites.** The payload contains `mama` measures only.
   Consumers may join it to automation/value measures by `use_case_id` but
   must keep the measures separately interpretable
   ([integration guide](mama-integration.md#keep-the-measures-separate)).

## Envelope

A **scorecard export** is a JSON object:

```json
{
  "export_format": "mama-scorecard-export",
  "export_version": "1.0.0",
  "generated_at": "2026-11-04T09:00:00Z",
  "ruleset_version": "2.0.0",
  "linkage": {
    "use_case_id": "acme-2026-041",
    "unit": "support-refund-agent",
    "unit_type": "ai-agent",
    "domain": "customer-refunds",
    "contract_id": "refund-agent-v2",
    "grantor": "support-director",
    "assessors": ["assessor-a", "assessor-b"],
    "review_date": "2026-11-04"
  },
  "scorecard": {
    "ruleset_version": "2.0.0",
    "scores": { "D1": 4, "D2": 4, "D3": 3, "D4": 4, "D5": 3, "D6": 3 },
    "safe_grant_level": 3,
    "granted_level": 2,
    "notes": ["headroom: safe level exceeds granted level by 1; expand after 2 clean review cycles"],
    "recommended_move": "expand (after 2 clean cycles): raise one level or widen scope in the strongest dimension"
  },
  "evidence": [
    { "dimension": "D3", "ref": "https://wiki.example/guardrails/refund-caps-v3" }
  ],
  "ledger_ref": { "file": "ledgers/support.yaml", "schema": 2, "contract_id": "refund-agent-v2" }
}
```

## Field rules

| Field | Rule |
|---|---|
| `export_format` | Literal `"mama-scorecard-export"` |
| `export_version` | This spec's version (`"1.0.0"`); additive changes bump MINOR, breaking changes MAJOR + changelog |
| `ruleset_version` | Required; MUST equal `scorecard.ruleset_version` |
| `linkage.unit`, `linkage.domain` | Required, non-empty |
| `linkage.unit_type` | Optional; free string (e.g. `team`, `service`, `ai-agent`, `robot`) |
| `linkage.use_case_id` | Optional; the consumer-side MAMA record this scorecard belongs to |
| `scorecard` | Required; exactly the `autonomy-score --json` output: `scores` D1–D6 each an integer **0–5**, `safe_grant_level` integer **0–5** (0 = Submarine Line), `granted_level` integer 0–5 or `null`, `notes` list of strings, `recommended_move` string |
| `evidence[]` | Optional; `ref` is a pointer (URL/id), never embedded content |
| `ledger_ref` | Optional; points at the ledger entry backing the assessment |

A machine-checkable schema lives at
[`schema/mama-scorecard-export.schema.json`](../schema/mama-scorecard-export.schema.json)
(JSON Schema draft 2020-12).

## Producing and consuming

- **Producing:** run `autonomy-score <6 scores> --current <L> --json` and
  place its object verbatim in `scorecard` (do not recompute or round);
  add linkage, evidence references, and versions. Assessments per
  [assessment.md](assessment.md); grants per the
  [contract template](contract-template.md).
- **Consuming:** validate against the schema; reject records whose
  `ruleset_version` is outside your comparability zone; store `use_case_id`
  as the join key to automation/value measures; render autonomy measures
  **beside** — never blended with — those measures.
- **Multiple domains:** export one scorecard per unit × domain
  ([assessment rule](assessment.md#2-how-to-run-it): never average across
  domains).

## Roadmap

- CLI flag(s) to emit the full envelope directly (linkage + scorecard in
  one command) — tracked on the
  [roadmap](roadmap.md).
- Ledger-export (contract-level) payload spec — the ledger YAML is already
  machine-readable; a JSON binding will follow the same principles.
