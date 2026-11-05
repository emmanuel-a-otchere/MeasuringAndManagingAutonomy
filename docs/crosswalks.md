# Crosswalks: `mama` and external frameworks

> **Rules of this document.** Crosswalks explain **coverage and gaps**. They
> make **no equivalence, certification, or endorsement** claims in either
> direction; external frameworks are authoritative for themselves; the
> [TM Forum reference policy](#tm-forum-mama--same-name-independent-work)
> limits which TM Forum assets may be cited; and each mapping is dated
> (this version: 2026-11-04, ruleset `RULESET_VERSION` 2.0.0). Reviewed on
> every MAJOR ruleset change and when a mapped framework updates.

`mama` (lowercase — *measuring and managing autonomy*) is the autonomy
method in this repository; **MAMA** (uppercase, *Measuring Automation &
Measuring Autonomy*) is the umbrella framework that consumes it — the
boundary is in the [integration guide](mama-integration.md).

## TM Forum MAMA — same name, independent work

> **TM Forum reference policy (steward decision, 2026-11-04, retroactive).**
> References to TM Forum assets in this repository are limited to
> **GB1040** (MAMA Framework Guidebook), **GB1042A** (Autonomous Operations
> Maturity Model), and **IG1301** (MAMA Whitepaper). Other TM Forum assets —
> including IG1403 and anything building on the Autonomous Networks (AN) /
> ANLET evaluations — are deliberately **not** referenced. This policy
> applies to all documentation, crosswalks, and communications, past and
> future.

**TM Forum operates a framework with the identical name and expansion:**
*Measuring and Managing Autonomy*, published as the
[MAMA Whitepaper (IG1301, v1.0.0 August 2022, latest v1.2.0)](https://www.tmforum.org/resources/introductory-guide/ig1301-measuring-and-managing-autonomy-whitepaper-v1-2-0),
the [MAMA Framework Guidebook (GB1040, v1.0.0, December 2022)](https://www.tmforum.org/resources/guidebook/gb1040-mama-framework-guidebook-v1-0-0),
and the [Autonomous Operations Maturity Model (AOMM, GB1042A)](https://www.tmforum.org/resources/guidebook/gb1042a-autonomous-operations-maturity-model-aomm-v1-8-0) —
an industry programme for realizing business value from automation and
autonomy.

**There is no affiliation, endorsement, or derivation between this
repository and TM Forum's MAMA programme** in either direction. This
method's own lineage is the 2022 concept diagram preserved in the
repository's history; the identical name and expansion reflect the same
natural naming of the same problem, arrived at independently (the
publications are contemporaries: IG1301 v1.0.0 dates to August 2022).

| Aspect | TM Forum MAMA (GB1040 / GB1042A / IG1301, as published) | `mama` (this repository) |
|---|---|---|
| Primary domain | Enterprise automation/autonomy programmes in digital transformation | Any sociotechnical unit × decision domain: teams, services, functions, **AI agents** |
| Focus | Business-value cadence for automation/autonomy investments (IG1301); organization-wide operations maturity assessment (AOMM, GB1042A) | **Contract-level** governance per unit × domain, with a machine-readable ledger |
| Level model | AOMM's operations-maturity assessment | L0 Submarine Line (no autonomy at all) + definitive L1–L5, bounded by the weakest-link rule `min(D3, D4, D6)` |
| Value measurement | Central (the MAMA value cadence) | Out of scope — consumed by MAMA via the [integration interface](mama-integration.md) |

**No mapping is claimed** between AOMM constructs and `mama`'s scale —
they are separate instruments; organizations using both should say so in
any analysis.

## NIST AI RMF 1.0 (2023)

| RMF function | Where `mama` aligns | Gaps in `mama` |
|---|---|---|
| **GOVERN** | Autonomy contracts, named grantors, revocation triggers, and the [governance loop](governance-loop.md) are accountability and risk-management mechanisms; [GOVERNANCE.md](../GOVERNANCE.md) names stewardship roles | No policy/culture program, no third-party supply-chain governance, no legal/regulatory scanning |
| **MAP** | Unit × decision-domain selection, blast radius and reversibility as context-setting ([framework §3–4](framework.md)) | No stakeholder-harm taxonomy, no AI-system inventory schema of its own (such inventories are a documented integration capability, not built here) |
| **MEASURE** | Six-dimension scoring with evidence, telemetry requirements, ledger health metrics | No model evaluation, no benchmark/TEVV methodology, no quantitative safety measurement |
| **MANAGE** | Expand/contract/re-shape/revoke moves, incremental raises, drills ([governance loop](governance-loop.md)) | No incident-response runbooks, no continuous-control-monitoring tooling beyond the ledger |

`mama` positions itself as a **GOVERN/MEASURE/MANAGE support instrument for
decision-rights**, not an AI risk management framework.

## ISO/IEC 42001:2023 (AI management systems)

- **Aligns:** documented operational controls (contracts = specified,
  evidence-backed control instruments); roles and accountabilities
  ([GOVERNANCE.md](../GOVERNANCE.md)); performance evaluation signals (D4
  telemetry, ledger health); continual improvement shape (the review loop).
- **Gaps:** `mama` is **not an AIMS** and does not implement
  management-system requirements (policy documents, internal audit,
  management review, certification). Nothing here claims conformance.

## ISO/IEC 23894:2023 (AI risk management guidance)

- **Aligns:** grants-as-risk-treatment (a guardrailed grant is a documented
  treatment for decision-rights risk); blast radius/reversibility as
  assessment inputs; review cadence as monitoring.
- **Gaps:** no full risk-management process (no risk register, risk
  criteria, or treatment optioneering); `mama` covers the autonomy-control
  slice only.

## OECD AI Principles (2019, updated 2024)

| Principle | `mama` coverage |
|---|---|
| Inclusive growth, sustainable development | **Not covered** |
| Human-centred values (human rights, diversity, fairness) | **Partial** — [accountability stays human](agents-as-units.md#6-accountability-stays-human); no fairness measurement |
| Transparency and explainability | **Strong** — D5 transparency dimension; agent decision-log requirements |
| Robustness, security, safety | **Partial** — D3 guardrails (tested, automated limits); no security methodology of its own |
| Accountability | **Strong** — D6 accountability; named grantors; revocation triggers |

## OWASP GenAI (Top 10 for LLM Applications)

`mama` does **not** test for LLM vulnerabilities (prompt injection, insecure
output handling, sensitive-information disclosure, and peers). What it does
require of higher autonomy levels — enforced tool allow-lists, output gates,
rate/spend caps, scoped credentials, structured decision logging, human
gates for consequential actions ([agents-as-units §5](agents-as-units.md#5-starter-menus-for-contracts-and-ledgers)) — are the **control classes**
such mitigations implement. Vulnerability discovery belongs to the
evaluation/security-testing capability, documented in the CR's
vendor-neutral capability map, not built here.

## MITRE ATLAS

`mama` includes **no adversary model** and no ATLAS-style TTP coverage. The
complementarity: D3's drill/stress-test requirements (L4–L5) and revocation
triggers give ATLAS-informed red-teaming something to target and a
governance consequence to feed. Threat modeling is out of scope.

## Using these crosswalks

- Say which version you mapped and when; re-check when either side changes.
- Report **gaps**, not just alignments — the tables above are the claim.
- Never present a crosswalk as conformance, certification, or endorsement.
- Mappings are **positional aids for governance design**, not
  instrument-score transformations; do not aggregate across frameworks
  ([why measures stay separate](mama-integration.md#keep-the-measures-separate)).
