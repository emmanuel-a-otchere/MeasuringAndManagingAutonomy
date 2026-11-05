# Governance of the `mama` method

How the `mama` method and toolkit are stewarded. The structure is
deliberately small and can begin as a project governance group — no legal
incorporation required.

## Roles

| Role | Holder | Decision rights |
|---|---|---|
| **Method steward** | *vacant* (interim: Emmanuel A. Otchere) | Approves terminology, construct definitions, scoring changes, versioning, crosswalks, and this handbook |
| **Repository maintainer / tool owner** | Emmanuel A. Otchere (interim) | Code, schemas, CI, packaging, site, security, accessibility, releases |
| **Validation lead** | *vacant* | Owns the [validation protocol](docs/validation-plan.md), evidence quality, inter-rater analysis, validation reporting |
| **Adoption lead** | *vacant* | Facilitator guidance, training, examples, community feedback |
| **Independent reviewers / advisors** | *open — sought across operations, people/workforce, risk & security, AI/automation, research, and impacted-stakeholder perspectives* | Review proposals and findings; flag risks; no operational authority |

Vacancies are real: if you want a role, introduce yourself in an issue.
Until a role is filled, the interim steward holds its decision rights and
says so when exercising them.

## Decision rights and process

- **Scoring semantics** (dimensions, level definitions, weakest-link rule)
  change only via the [versioning policy](docs/versioning.md): PRs that
  update both engines, the changelog, and keep parity green. MAJOR changes
  require a re-baseline plan and mapping table.
- **Naming and terminology** (`mama` vs. MAMA, Submarine Line, dimension
  names) are steward-approved; propose via issue.
- **TM Forum reference policy** (steward decision, 2026-11-04, applied
  retroactively): references to TM Forum assets are limited to **GB1040**,
  **GB1042A**, and **IG1301**. Other TM Forum assets — including IG1403 and
  anything building on the Autonomous Networks (AN) / ANLET evaluations —
  are not referenced in documentation, crosswalks, or communications.
- **Releases** follow [RELEASE.md](RELEASE.md); every release states shipped
  ruleset/schema versions, breaking changes, migration, and known
  limitations.
- **Contributions** follow [CONTRIBUTING.md](CONTRIBUTING.md): PRs pass CI
  (self-tests, parity, ledger validation, docs checks); substantive doc
  changes need steward review.

## Issue triage, appeals, and conflict of interest

- **Triage:** framework-feedback and case-study issues are triaged weekly by
  the maintainer; scoring-semantics proposals are escalated to the method
  steward.
- **Appeals:** a closed decision may be appealed by reopening the issue with
  the `governance-appeal` label; the steward must respond with a written
  rationale in the issue.
- **Conflicts of interest:** reviewers and assessors do not review or score
  units they own, fund, or build; material interests are disclosed in the
  relevant issue/PR. Validation pilot sites disclose their relationship to
  the method.
- **No certification claims:** governance artifacts and the
  [positioning](docs/positioning.md) crosswalks make no equivalence,
  certification, or endorsement claims about external frameworks.
- **Change rationale:** every substantive decision lands in the
  [changelog](CHANGELOG.md) or the deciding issue — public by default.

## Related policies

Security reporting: [SECURITY.md](SECURITY.md) · License:
[LICENSE](LICENSE) (MIT) · Data expectations for assessments and ledgers:
[integration guide, data handling](docs/mama-integration.md) · Method
limits: [limitations](docs/limitations.md)
