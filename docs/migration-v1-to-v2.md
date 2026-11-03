# Migrating from v1.x to v2 (level scale re-baseline)

> Ruleset v2.0.0 re-based the autonomy level scale. **v1.x assessments are
> not formally comparable with v2** — this guide is the re-scoring path, and
> the policy for interpreting historical records.

## What changed

| Surface | v1.x (retired) | v2.x (current) |
|---|---|---|
| Definitive levels | L0–L4 | **L1–L5** |
| No autonomy | implicit floor | **L0 — Submarine Line** (named level of the scale) |
| Dimension scores | 0–4 | **0–5** (0 = Submarine Line for that dimension) |
| Questionnaire items | L1–L4 per dimension | **L1–L5** per dimension (new L1 = the Ask arrangement; former items shift up one label) |
| Ledger schema | `schema: 1` | **`schema: 2`** |
| Ruleset version | `RULESET_VERSION` 1.0.0 | **2.0.0** |

**Mapping:** v1 level *n* → v2 level *n+1*.

| v1 (retired) | v2 |
|---|---|
| — | L0 Submarine Line |
| L0 Ask | L1 Ask |
| L1 Inform-after | L2 Inform-after |
| L2 Guardrailed | L3 Guardrailed |
| L3 Supervised | L4 Supervised |
| L4 Accountable | L5 Accountable |

The weakest-link rule `min(D3, D4, D6)` is unchanged in form; on the new
scale a result of 0 means nothing is grantable yet.

## Re-scoring path (per unit × domain)

1. **Do not rewrite v1 records.** Preserve the original scorecards and
   ledger history — comparability policy depends on originals surviving.
2. Re-run the assessment with the v2
   [questionnaire](assessment.md#3-the-questionnaire) and the current tool
   (`autonomy-score` prints `ruleset_version: 2.0.0`).
3. Write the result as a **new contract version** in the ledger: bump the
   contract id (`-v<n+1>`), record the new scores, and set the ledger's
   top-level `schema: 2`. The old contract version stays in the file as
   history (`status` per its real state).
4. Note in the contract's `notes` that this is a scale re-baseline, and
   carry over any v1 evidence that still stands.

`ledger_health.py` still reads `schema: 1` files but warns that their levels
use the retired scale — that warning is your to-do list.

## Historical score interpretation policy

- **No direct comparison** of v1 scores to v2 scores is presented as
  formally valid — the level semantics moved.
- **Coarse trend continuity** may use the mapping table (e.g., a v1 "L2
  Guardrailed" grant corresponds to a v2 "L3 Guardrailed" grant), clearly
  labeled as a crosswalk, not a measurement.
- Scorecards record the `ruleset_version` that produced them; any analysis
  across the re-baseline must state which versions it mixes and that the
  mapping is semantic, not psychometric.
- A MAJOR ruleset change always ships with a mapping table
  ([versioning policy](versioning.md)); this document is the v1→v2 instance.

## Worked mini-migration

The payments-team worked example was re-baselined with the v1→v2 mapping:
v1 scores `1 3 2 2 1 1` (safe L1) became v2 scores `2 4 3 3 2 2` (safe L2),
the grant moved from v1 L2 to v2 L3, and the ledger was re-baselined to
`schema: 2` — see [examples/README.md](../examples/README.md) and
[examples/ledger.yaml](../examples/ledger.yaml).
