# Changelog

All notable changes to the framework, its instruments, and tooling.
Versioning policy: [docs/versioning.md](docs/versioning.md) — the framework
follows semantic versioning with two versioned surfaces: the **scoring
ruleset** (`RULESET_VERSION`, e.g. `1.0.0`) and the **ledger format**
(`schema`, integer).

## Unreleased

- Archived the original 2022 concept diagram ("Measuring Autonomy Based on
  3-Axis of Freedom") in `docs/img/` with provenance and a mapping of its
  2022 axes (self-governance, adaptability, automation) to the current
  scope/level/horizon axes. Closes the last v0.2 lineage item. Documentation
  only — no scoring or schema change.

## v1.1.0 — 2026-11-03

Toolkit release: the framework tools are now installable and distributable.

### Tooling

- Packaging: `measuring-autonomy` installs with `autonomy-score` and
  `ledger-health` console commands (`src/` layout; the `tools/` scripts
  remain as zero-install shims over the package)
- Release pipeline: pushing a `v*` tag builds the wheel + sdist and
  standalone one-file binaries (macOS arm64, Linux x86_64, Windows x86_64),
  gates every artifact on its `--self-test` and a CLI smoke, then publishes
  a GitHub Release with notes taken from this changelog (`RELEASE.md`)
- Optional PyPI publishing workflow (`publish-pypi.yml`, manual dispatch,
  requires one-time trusted-publisher setup)
- CI: install PyYAML for the ledger tooling — the runner's toolcache Python
  does not bundle it, which had left every CI run red (PR #6)
- Pages: the deploy workflow enables GitHub Pages itself; the assessment
  site is live at https://emmanuel-a-otchere.github.io/MeasuringAndManagingAutonomy/

### Scoring semantics

None — `RULESET_VERSION` stays 1.0.0; no scored output changed.

## v1.0.0 — 2025-10-29

First versioned release. Scoring semantics frozen; comparability policy in
effect.

### Framework (previously unreleased work, folded into v1.0.0)

- Written framework: definitions, three axes (scope/level/horizon), five
  autonomy levels L0–L4, autonomy contracts (`docs/framework.md`)
- Maturity model: six dimensions × five levels, weakest-link rule
  `min(guardrails, telemetry, accountability)`, decision table,
  Autonomy Ledger (`docs/maturity-model.md`)
- Assessment questionnaire and scoring procedure (`docs/assessment.md`)
- Governance loop with cadence and anti-patterns (`docs/governance-loop.md`)
- Positioning, related work, open questions, BibTeX (`docs/positioning.md`)
- Worked end-to-end example (`examples/README.md`)

### Instrumentation

- `tools/autonomy_score.py` — scoring CLI (weakest-link, coaching vs
  revocation signals, over-grant detection) with `--self-test`
- `tools/ledger_health.py` — ledger validation + health report (coverage,
  stale reviews, expired horizons) with `--self-test`
- `site/` — dependency-free web self-assessment (questionnaire, live
  scoring, printable scorecard); `site/scoring.js` engine with
  `tools/site_selftest.js` parity tests
- Ledger format v1 (`docs/ledger-format.md`, `examples/ledger.yaml`) with
  contract + review agenda template (`docs/contract-template.md`)
- CI: tool self-tests, CLI smoke tests, ledger validation, doc-link and
  hotlinked-image checks; GitHub Pages deploy for `site/`

### Versioning & compatibility (this release)

- `RULESET_VERSION = "1.0.0"` stamped in `tools/autonomy_score.py` and
  `site/scoring.js`; emitted in every CLI and web scorecard output
- Cross-implementation parity tests: each self-test verifies the other
  engine carries the same version (drift is a release blocker)
- Ledger schema versioning: `schema:` field (`1`); missing field is
  backward-compatibly treated as `1`; newer schemas warn but still validate
  (forward compatibility)
- Comparability policy: scores comparable across PATCH/MINOR; MAJOR =
  re-scoring and requires a re-baseline plan (`docs/versioning.md`)
- CHANGELOG introduced at v1.0.0

### Frozen semantics (comparability guarantees)

- Five level definitions L0–L4
- Six dimensions D1–D6 and the weakest-link rule `min(D3, D4, D6)`
- Two-clean-cycles expansion rule

Changes to any of the above require a MAJOR bump and a migration note here.
