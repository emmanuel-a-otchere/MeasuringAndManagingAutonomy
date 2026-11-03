# Versioning and backward compatibility

> **Status:** v2.0 policy (current ruleset `RULESET_VERSION = 2.0.0`). The framework freezes its scoring rules and manages
> changes so that **assessments stay comparable over time**.

## Why versioning matters

The framework's whole claim is that autonomy becomes a *measured* quantity.
A measurement is only useful longitudinally if the instrument is stable: a
score of "L2, D3=3" must mean the same thing in this quarter's review as it
did last quarter's. Two failure modes destroy that:

1. **Silent drift** — questionnaire items or scoring rules are edited over
   time and old scorecards quietly become incomparable.
2. **Version ambiguity** — a scorecard doesn't say which rules produced it,
   so nobody can tell whether a change is real or a rule change.

Both are prevented the same way: every instrument carries a **ruleset
version**, every scorecard records it, and changes follow a written
compatibility policy.

## The two versioned things

| What | Constant | Where it lives |
|---|---|---|
| **Scoring ruleset** | `RULESET_VERSION` | `tools/autonomy_score.py`, `site/scoring.js` (kept identical, parity-tested) |
| **Ledger format** | `SCHEMA_VERSION` (integer, currently `2`) | top-level `schema:` field in `ledger.yaml`, handled by `tools/ledger_health.py` |

## Ruleset versioning: MAJOR.MINOR.PATCH

Scores are **comparable across versions** as follows:

| Change | Version bump | Score comparability |
|---|---|---|
| Bug fix that doesn't change any scored output; wording typos; docs | **PATCH** | Fully comparable |
| **Additive**: new *optional* metadata (e.g. a new non-scoring field); new tool output that doesn't alter existing values; new non-scoring notes | **MINOR** | Fully comparable — existing scores unchanged |
| **Re-wording of questionnaire items** that changes what evidence counts (same meaning, clearer bar) | **MINOR** + changelog entry marked *clarification* | Comparable with a footnote; re-run on next review cadence anyway |
| **Re-scoring**: changed items, changed level definitions, changed dimension set, changed weights, changed the weakest-link rule | **MAJOR** | **Not comparable.** Requires a re-baseline: re-score the domain before comparing to any earlier scorecard |

Rules of the road:

- **No MAJOR without a re-baseline plan.** A MAJOR bump ships with a
  migration note in the changelog and (where feasible) a mapping table
  from old to new levels for coarse trend continuity.
- **Comparability zone:** scorecards may be compared within the same MAJOR
  version, and with the immediately preceding MAJOR *only* if a mapping table
  exists in the changelog.
- **Frozen semantics at v2.x:** the definitive level definitions (L1–L5, with
  L0 as the Submarine Line), the six dimensions (D1–D6), the weakest-link
  rule `min(D3,D4,D6)`, and the two-clean-cycles expansion rule are frozen.
  Changes to them are MAJOR by definition.
- **Mapping from v1.x (the re-baseline that produced 2.0.0):** the v1 scale's
  L0–L4 map to v2's L1–L5 (old level *n* → new level *n+1*); v1's implicit
  floor becomes the named Submarine Line (L0). A coarse trend comparison
  across the re-baseline may use this mapping; formal comparability starts
  with re-scored v2 baselines.

## Ledger schema versioning

- `ledger.yaml` SHOULD declare `schema: 2` (top-level, integer) — the v2.0.0
  ruleset's level scale (definitive L1–L5, L0 Submarine Line).
- **Backward compatibility:** `ledger_health.py` treats a *missing* `schema:`
  field as the current supported schema — pre-versioning ledgers keep
  validating unchanged.
- **Schema 1 (retired):** files declaring `schema: 1` (the pre-2.0.0 0–4
  scale) still validate, with a **warning** that their levels are not
  comparable with the current scale and should be re-baselined to `schema: 2`
  using the mapping above.
- **Forward compatibility:** a ledger declaring a *newer* schema than the tool
  supports is a **readable but flagged** condition (warning, not a schema
  error): the tool reports on the fields it understands rather than refusing
  the file.
- Schema changes follow the same MAJOR/MINOR logic: new optional fields are a
  MINOR bump; removing/renaming/re-typing existing fields is MAJOR and
  requires a documented migration.

## Where versions are recorded

| Artifact | Records |
|---|---|
| CLI / web scorecard output | `ruleset_version` field (and printed line) — e.g. `"2.0.0"` |
| Web scorecard print view | ruleset version in the scorecard header |
| Autonomy contract (`docs/contract-template.md`) | ruleset version + date of the assessment baseline |
| Ledger file | `schema:` integer |
| Changelog | every bump, with change class and migration note |

## Governance

- Bumps are proposed in PRs that must: (a) update `RULESET_VERSION` /
  `SCHEMA_VERSION` in **both** tools, (b) update `CHANGELOG.md` under a
  "Unreleased" heading, and (c) keep the Python/JavaScript parity test green.
- The parity test (`tools/site_selftest.js` cross-checked against
  `autonomy_score.py --self-test`) guarantees the two implementations of the
  same ruleset version produce the same results — drift between them is a
  release blocker.
- Release process: roll the "Unreleased" changelog section into a versioned
  heading, tag `v<version>`, and publish a GitHub release referencing the
  changelog entry.
