# `mama` training module (self-guided)

> A ~60-minute walkthrough that takes you from zero to a defensible
> autonomy assessment on a domain you actually operate. Read alongside the
> [method handbook](handbook.md); this module adds exercises and the
> judgment calls the reference docs assume. Method status:
> [pilot / under validation](limitations.md).

## Lesson 1 — What `mama` is (and refuses to be) · ~10 min

**Read:** the [README naming box](../README.md) and
[limitations](limitations.md).

`mama` (lowercase — *measuring and managing autonomy*) makes delegated
decision rights explicit: a unit × decision domain gets a written
[contract](framework.md#5-autonomy-contracts) at a level bounded by tested
guardrails. It is the autonomy component of the broader **MAMA** umbrella
framework. Three refusals to internalize now:

1. **No org-wide score.** Autonomy is assessed per unit × domain.
2. **No automatic authority.** A score is evidence for a human decision,
   never the decision.
3. **No comparability across MAJOR rulesets.** Every scorecard carries its
   `ruleset_version`.

✏️ *Exercise:* name one decision domain you personally delegate (or hold).
Write it as a decision class with stakes — "production deploys of X", not
"engineering". That's your practice domain for the rest of this module.

## Lesson 2 — Units, domains, and the Submarine Line · ~10 min

**Read:** [framework §3–4](framework.md#3-the-three-axes-of-autonomy).

Every assessment positions a **unit** (person, team, service, AI agent) on
a **domain** along three axes: scope, level, horizon. The scale: **L0
Submarine Line** (no autonomy at all — nothing granted, nothing to review)
below definitive **L1 Ask → L5 Accountable**. Two rules bound the level:
the **guardrail rule** (level *n* requires tested level-*n* guardrails) and
the **reversibility rule** (high blast radius + low reversibility ⇒ L1–L2
at most).

✏️ *Exercise:* for your practice domain, write down (a) who the unit is,
(b) who the grantor is, (c) blast radius, (d) reversibility. If (b) is
"nobody" — that's shadow autonomy, the thing the
[first inventory](governance-loop.md#8-starting-from-zero) exists to find.

## Lesson 3 — Run an assessment · ~20 min

**Read:** [assessment](assessment.md) and the
[facilitator guide](facilitator-guide.md). Best done with a second person
(one from the unit, one from the grantor side), scoring independently.

For each of the six dimensions (D1 clarity, D2 capability, D3 guardrails,
D4 telemetry, D5 transparency, D6 accountability), mark the highest level
whose items are **all** true **with evidence** — unevidenced scores drop a
level, and a dimension with not even the L1 item true scores **0**
(Submarine Line for that dimension). Then compute:

```bash
python3 tools/autonomy_score.py <D1> <D2> <D3> <D4> <D5> <D6> --current <granted L>
```

✏️ *Exercise:* score your practice domain. Note which dimension is the
**weakest link** — `min(D3, D4, D6)` is the safe grant level, and it is
rarely the dimension the unit is proudest of.

## Lesson 4 — From score to decision · ~5 min

**Read:** [maturity model §4](maturity-model.md#4-from-scores-to-decisions).

The output is a **move**: formalize / expand (after 2 clean cycles) /
contract or re-shape / hold and coach / hold. Coaching dimensions (D1/D2)
lag → invest, don't revoke. Safety dimensions (D3/D4/D6) lag → fix or step
down. And the move is a **recommendation to the grantor**, who weighs blast
radius and context — [limitations](limitations.md) apply.

✏️ *Exercise:* write your domain's recommended move and one sentence of
grantor rationale (or objection) for it.

## Lesson 5 — Make it governable · ~15 min

**Read:** [contract template](contract-template.md) and
[ledger format](ledger-format.md).

Turn the assessment into a contract (scope + exclusions, level, horizon,
grantor, guardrails, telemetry, escalation, revocation triggers) and record
it in the [ledger](../examples/ledger.yaml) (`schema: 2`). Check health:

```bash
python3 tools/ledger_health.py your-ledger.yaml
```

✏️ *Exercise:* draft the contract for your practice domain. If you can't
fill the revocation-triggers row, the domain isn't ready to be granted
above the Submarine Line.

## Lesson 6 — Keep it alive · ~5 min

**Read:** [governance loop](governance-loop.md).

The loop — grant → instrument → observe → review → move — runs on the
contract's horizon (typically quarterly). Reviews re-assess, compare
granted vs. exercised autonomy, and decide. Where the broader MAMA
framework consumes your outputs, link by stable use-case ids and keep the
measures separate ([integration](mama-integration.md)).

## Check yourself

1. Why is an org-wide average autonomy score forbidden? *(It hides the
   per-domain signal; a team can be L4 on deploys and L1 on hiring.)*
2. A domain scores D3=2, D4=4, D6=4, currently granted L3. Move? *(Safe
   level 2 < 3 → contract or re-shape: fix guardrails or step down.)*
3. What does L0 mean, and how does it differ from "not assessed"? *(No
   autonomy at all — nothing granted. Not-assessed is an unknown, not a
   zero; assess before grounding.)*
4. Your agent's prompt changed materially. Same unit? *(No — new version,
   re-assess before it keeps its level; [agents-as-units §5](agents-as-units.md#5-starter-menus-for-contracts-and-ledgers).)*

## Where to go next

- Score for real and file the scorecard with the contract
  ([outputs](assessment.md#5-outputs))
- Bring disagreements back as [feedback](../CONTRIBUTING.md) — the rubric
  improves only through use
- Deep dives: [agents as units](agents-as-units.md) ·
  [crosswalks](crosswalks.md) · [export format](export-format.md) ·
  [governance](../GOVERNANCE.md)
