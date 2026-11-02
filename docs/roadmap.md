# Roadmap

## v0.1 — Written framework (current)

- [x] Core definitions, three axes, five autonomy levels (docs/framework.md)
- [x] Autonomy contracts as the management artifact
- [x] Maturity model: 6 dimensions × 5 levels, scoring rules (docs/maturity-model.md)
- [x] Assessment questionnaire and scoring procedure (docs/assessment.md)
- [x] Governance loop with cadence and anti-patterns (docs/governance-loop.md)
- [x] Worked end-to-end example (examples/README.md)
- [x] Scoring CLI with self-test (tools/autonomy_score.py)
- [x] Positioning and related work (docs/positioning.md)
- [x] Mermaid framework diagram (renders natively on GitHub)

## v0.2 — Validation

- [ ] Apply the assessment to 3+ real teams; record whether the weakest-link
      rule predicted outcomes (breaches, over/under-grants)
- [ ] Revise dimension definitions and questionnaire items based on findings
- [ ] Preserve the original 2022 concept diagram in docs/img/ for lineage
- [ ] AI agents as units: first-pass extension of the framework

## v0.3 — Tooling & reach

- [ ] Autonomy Ledger as a machine-readable format (YAML/CSV) + ledger
      health report (coverage, staleness)
- [ ] Web-based self-assessment (static site) replacing the CLI for
      non-technical audiences
- [ ] CI: run the tool's self-test on every push
- [ ] Case studies from 2+ different industries

## v1.0 — Stability

- [ ] Frozen level definitions and scoring rules; semantic versioning of the
      maturity model so assessments stay comparable over time
- [ ] Cross-cultural validation of level norms
- [ ] Printable assessment pack (one-pager + rubric)

## How to help

Each unchecked item is a good first contribution. See
[CONTRIBUTING.md](../CONTRIBUTING.md) — case-study submissions are the
highest-value feedback right now.
