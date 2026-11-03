# Changelog

All notable changes to the framework, its instruments, and tooling.
Versioning policy: [docs/versioning.md](docs/versioning.md) — the framework
follows semantic versioning with two versioned surfaces: the **scoring
ruleset** (`RULESET_VERSION`, e.g. `1.0.0`) and the **ledger format**
(`schema`, integer).

## Unreleased

## v2.0.1 — 2026-11-04

Establishment release (CR MAMA-AUT-CR-001, Phase 0). No scoring changes —
`RULESET_VERSION` stays 2.0.0.

### License (corrective)

- The LICENSE **file** was BSD-3-Clause (© 2022) while every doc and the
  package metadata said MIT — a contradiction present since the original
  import. The intended license is **MIT**: the LICENSE file now carries the
  MIT text, and repository metadata, README, package, and distribution
  artifacts are reconciled. Prior distributions (v1.x–v2.0.0) shipped the
  BSD-3 file with MIT-claiming metadata; treat MIT as intended and
  re-download current artifacts where the distinction matters.

### Identity

- Naming established: **`mama`** (lowercase) = measuring and managing
  autonomy, this method and toolkit (canonical home: this repository);
  **MAMA** (uppercase) = Measuring Automation & Measuring Autonomy, the
  umbrella framework that uses `mama`. Naming box added to README and the
  assessment site; integration guide published
  (`docs/mama-integration.md`).

### Method governance & documentation

- `GOVERNANCE.md` (stewardship roles, decision rights, appeals, COI) and
  `SECURITY.md` (private vulnerability reporting)
- `docs/handbook.md` — the end-to-end operating guide
- `docs/migration-v1-to-v2.md` — re-baselining guide + historical-score
  policy (supersedes reading migration only from the changelog)
- `docs/limitations.md` + `docs/validation-plan.md` — the method is
  labeled **pilot / under validation** until the validation program
  reports
- README: current status (was stale "v0.1 draft"), intended users, offline
  use, links to all governance artifacts; roadmap reconciled with a v2.1
  establishment section

## v2.0.0 — 2026-11-03

**MAJOR — re-baseline required.** The level scale changed; assessments and
ledgers on the retired scale are **not comparable** with v2 scores.

### Level scale (scoring change, `RULESET_VERSION` 1.0.0 → 2.0.0)

- Definitive autonomy levels are now **L1–L5**; **L0 is the Submarine Line**
  — no autonomy at all, nothing granted, nothing to review or revoke — kept
  as the grounding floor beneath the scale.
- **Mapping from v1.x** (old level *n* → new level *n+1*): v1 L0 Ask → v2 L1;
  v1 L1 Inform-after → v2 L2; v1 L2 Guardrailed → v2 L3; v1 L3 Supervised →
  v2 L4; v1 L4 Accountable → v2 L5. Coarse trend comparisons across the
  re-baseline may use this mapping; formal comparability starts with
  re-scored v2 baselines.
- Dimension scores are now 0–5 (was 0–4): a dimension with not even the L1
  (Ask-arrangement) item true scores 0 — Submarine Line for that dimension.
- The questionnaire gains an L1 item per dimension describing the Ask
  arrangement; former items shift up one level label.
- Weakest-link rule unchanged: `min(D3, D4, D6)`. A safe level of 0 means
  nothing is grantable yet; the tools now say so explicitly (submarine move).

### Ledger format (`schema` 1 → 2)

- `schema: 2` = the v2 level scale. `ledger_health.py` validates levels 0–5.
- Schema-1 files still validate but warn: "retired 0–4 scale — re-baseline
  and set schema: 2". Missing `schema:` field = current supported schema.
- Reference ledgers (`examples/ledger.yaml`, `examples/agents-ledger.yaml`)
  re-baselined to schema 2 with levels shifted accordingly.

### Docs & tooling

- All framework docs re-based: levels tables, maturity grid (now six
  columns), questionnaire, governance-loop thresholds, contract template,
  worked examples re-scored (payments team: safe L3, hold at L3; refund
  agent: safe L3, expand from L2).
- Site (`site/`) and CLI engines updated in lockstep; parity-tested at 2.0.0.

### Migration (v1.x → v2.0.0)

1. Re-score each domain with the v2 questionnaire (`autonomy-score` prints
   `ruleset_version: 2.0.0`).
2. Rewrite ledger contracts onto the new scale (mapping above) and set
   `schema: 2`; version the contract id (`-v<n+1>`) rather than mutating
   history in place.
3. Do not compare v1.x scorecards to v2 scorecards directly — use the
   mapping for coarse trends only.

## v1.1.1 — 2026-11-03

Metadata only — no code or scoring changes (`RULESET_VERSION` stays 1.0.0).

### Packaging

- PyPI project description: the README's repo-relative links rendered as
  broken `pypi.org/project/...` paths there; all links now use absolute
  GitHub URLs (identical behavior on GitHub and PyPI)
- Wheel classifiers corrected for PyPI's server-side validation —
  `Intended Audience :: Management` is not a valid trove classifier; replaced
  with `Developers` + `Information Technology` (the PyPI 1.1.0 artifacts
  already carried this fix; the GitHub Release artifacts rebuild with it here)

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
