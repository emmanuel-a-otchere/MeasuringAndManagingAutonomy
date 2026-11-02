# The Governance Loop

> **Status:** v0.1 draft. The operating procedure that makes autonomy a
> managed quantity rather than a vibe. Builds on
> [framework.md](framework.md#7-the-management-loop).

## The loop

```
GRANT → INSTRUMENT → OBSERVE → REVIEW → (Expand | Contract | Re-shape) → …
```

Each stage is defined below. The loop runs **per autonomy contract**, on the
contract's horizon — typically quarterly, shorter (monthly) for newly raised
levels, longer (biannual) for mature L4 domains.

## 1. GRANT

Autonomy is granted, never assumed. A grant has five mandatory components
(the [autonomy contract](framework.md#5-autonomy-contracts)):

1. Named domain and decision classes
2. Level (L0–L4) per domain, **with the guardrails that justify it**
3. Horizon / review date
4. Telemetry obligations
5. Revocation triggers — observable conditions, agreed *up front*

**Grant hygiene rules:**

- Every grant has a named grantor. No grantor, no autonomy — not "the org".
- Guardrails must be *tested* before a grant goes live. Untested guardrails
  are documentation, not protection.
- The grant is recorded in the [Autonomy Ledger](maturity-model.md#5-the-autonomy-ledger).
- Level raises are incremental: skip at most one level per cycle, except
  after a formal capability review (this slows ladder-skipping, which is
  the classic cause of autonomy blowups).

## 2. INSTRUMENT

At grant time, the telemetry that the review will rely on must already exist
or be built as part of the grant. Minimum set per domain:

- **Usage signals** — how often the unit exercises the right (unused autonomy
  is a contract-quality bug).
- **Outcome signals** — error rate, budget burn, incident count, cycle time,
  whatever "good" means for the domain.
- **Breach signals** — automated alerts on guardrail violation, routed to
  both the unit and the grantor.

If you cannot instrument it, you cannot safely grant above L2.

## 3. OBSERVE

Between reviews, nobody intervenes on decisions inside the contract —
**intervention inside a live contract is itself a contract breach** by the
grantor, and must be logged as such. Exceptions:

- A revocation trigger fired (grantor steps the level down immediately,
  then initiates an early review).
- Safety-critical emergency (then the contract is re-negotiated after).

## 4. REVIEW

The review compares reality to the contract using the
[Assessment](assessment.md):

1. Re-score the six dimensions for the domain (dual assessor, evidence-based).
2. Compare granted vs. exercised autonomy — the gap analysis:
   - *Granted > exercised:* clarify the contract or shrink it.
   - *Exercised > granted:* formalize the shadow autonomy or enforce the
     boundary — never ignore it.
3. Walk the incident/breach log since the last review.
4. Decide the move.

## 5. The three moves

| Move | Trigger | Typical action |
|---|---|---|
| **Expand** | Safe level > granted level for 2 consecutive reviews, no breaches | Raise one level or widen scope in the strongest dimension; set a shorter first horizon |
| **Contract** | Revocation trigger fired, or D3/D4/D6 below granted level *with a breach* | Step down one level; shorten horizon; keep coaching signals intact |
| **Re-shape** | Performance mixed: strong capability, weak guardrails (or the reverse) | Same level, new guardrail set — usually cheaper and more effective than level changes |

**Anti-patterns to enforce against:**

- *Panic revocation:* a single incident permanently dropping a mature unit to
  L0. Contracts exist precisely to prevent emotional resets. One breach ⇒
  one step down, with a defined re-raise path.
- *Ratchet only up:* expansions that are never reviewed and never come down
  quietly turn the ledger into fiction.
- *Vague horizons:* "ongoing" autonomy is unmanaged autonomy. Every contract
  has a date.

## 6. Roles

| Role | Responsibility |
|---|---|
| **Grantor** | Owns the contract, the ledger entry, and revocation decisions. Provides the escalation path. |
| **Unit** | Owns decisions within the contract, the telemetry, and transparency duties. |
| **Reviewer / assessor** | Runs assessments; must be neither the unit nor its grantor for org-wide censuses. |
| **Ledger keeper** | Maintains the [Autonomy Ledger](maturity-model.md#5-the-autonomy-ledger); reports ledger health (coverage, staleness) as an org-level metric. |

## 7. Cadence

| Event | Frequency |
|---|---|
| Standing contract review | Quarterly (monthly after a level raise; biannual for mature L4) |
| Incident-triggered early review | Within 5 working days of a revocation trigger |
| Org-wide ledger census | Annually |
| Guardrail drills (for L3+) | At least every two quarters per domain |

## 8. Starting from zero

For an organization adopting this loop:

1. **Inventory** (2–4 weeks): build the first Autonomy Ledger, including
   informal/shadow autonomy. Expect uncomfortable findings.
2. **Instrument** (per domain): stand up the three signal sets. Do not raise
   any level before this.
3. **Formalize** (per domain): convert each informal arrangement into a
   written contract at its *current* level — no instant raises.
4. **Operate the loop**: only now do reviews start proposing moves.
