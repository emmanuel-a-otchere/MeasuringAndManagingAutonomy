# Roadmap

## v0.1 — Written framework (shipped)

- [x] Core definitions, three axes, five autonomy levels (docs/framework.md)
- [x] Autonomy contracts as the management artifact
- [x] Maturity model: 6 dimensions × 5 levels, scoring rules (docs/maturity-model.md)
- [x] Assessment questionnaire and scoring procedure (docs/assessment.md)
- [x] Governance loop with cadence and anti-patterns (docs/governance-loop.md)
- [x] Worked end-to-end example (examples/README.md)
- [x] Scoring CLI with self-test (tools/autonomy_score.py)
- [x] Positioning and related work (docs/positioning.md)
- [x] Mermaid framework diagram (renders natively on GitHub)
- [x] CI workflow: tool self-test, CLI smoke test, docs consistency (pulled forward from v0.3)
- [x] Machine-readable Autonomy Ledger (YAML v1) + `ledger_health.py` validation & health tool (pulled forward from v0.3)
- [x] Reference ledger seeded from the worked example (`examples/ledger.yaml`)
- [x] Autonomy contract + review agenda template (`docs/contract-template.md`)

## v0.2 — Validation

- [ ] Apply the assessment to 3+ real teams; record whether the weakest-link
      rule predicted outcomes (breaches, over/under-grants)
- [ ] Revise dimension definitions and questionnaire items based on findings
- [ ] Preserve the original 2022 concept diagram in docs/img/ for lineage
- [x] AI agents as units: first-pass extension of the framework
      (`docs/agents-as-units.md`, `examples/agents-ledger.yaml`; engines
      unchanged at the time — since re-based by v2.0.0 below)

## v0.3 — Tooling & reach

- [x] Autonomy Ledger as a machine-readable format (YAML) + ledger
      health report (coverage, staleness) — pulled forward into v0.1
- [x] Web-based self-assessment — `site/` (static, dependency-free; questionnaire,
      weakest-link scoring, printable scorecard; scoring engine tested in
      `tools/site_selftest.js` and checked in CI)
- [x] CI: run the tool's self-test on every push — pulled forward into v0.1
- [ ] Case studies from 2+ different industries

## v1.0 — Stability (shipped)

- [x] Frozen level definitions and scoring rules; semantic versioning of the
      maturity model so assessments stay comparable over time
      (`docs/versioning.md`; `RULESET_VERSION = 1.0.0` at the time, in both
      engines, parity-tested; `CHANGELOG.md` tracks every bump — superseded
      by the v2.0 scale revision below)
- [ ] Cross-cultural validation of level norms
- [x] Autonomy contract + review agenda template (`docs/contract-template.md`)
- [x] Printable assessment pack (one-pager + rubric) — the site's print
      output plus the rubric in `docs/contract-template.md`

## v2.0 — Scale revision (current)

- [x] Level scale re-based: definitive levels **L1–L5**, with **L0 as the
      Submarine Line** (no autonomy at all) as the grounding floor —
      `RULESET_VERSION` 2.0.0, ledger `schema: 2`, one new L1 (Ask
      arrangement) item per dimension, submarine move in both engines;
      v1→v2 mapping table in `CHANGELOG.md` (`PR #15`)
- [ ] Validation items above (v0.2/v0.3) now apply to the v2 scale; v1.x
      assessments are not comparable — re-baseline with the mapping

## How to help

Each unchecked item is a good first contribution. See
[CONTRIBUTING.md](../CONTRIBUTING.md) — case-study submissions are the
highest-value feedback right now.
