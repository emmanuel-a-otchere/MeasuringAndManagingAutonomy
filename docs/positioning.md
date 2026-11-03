# Positioning and Related Work

> **Status:** v0.1 draft. Where this framework sits relative to existing
> ideas, and what it borrows.

This framework is a synthesis, not an invention. Its claim to novelty is
narrow: treating autonomy as a **ledgered, time-boxed, contract-based property
that is granted only with tested guardrails and measured on both supply and
demand** — and packaging that into an assessable maturity model for
organizational use.

## Lineage

| Source | What this framework takes from it |
|---|---|
| **Deere & Kramer (1995), *Levels of Autonomy* (NRL formal report)* | The explicit ladder of autonomy levels for supervised systems; the idea that levels are a design choice, not a mood |
| **Levels of driving automation (SAE J3016)** | The discipline of level definitions tied to responsibility; the popularity proof that ladders make autonomy negotiable |
| **Sheridan & Verplanck; Parasuraman, Sheridan & Wickens (2000), *A Model for Types and Levels of Human Interaction with Automation*** | Separation of *decision scope* from *monitoring intensity* — the ancestor of the scope/level axis split |
| **Delegation theory & management practice** (incl. Tannenbaum & Schmidt's leadership continuum) | Inform-after → pre-approval → full ownership progression for people, and the insight that delegation is a contract, not an event |
| **Sociotechnical systems & responsibility models** (e.g., STPA, Leveson) | Blast radius and reversibility as first-class design constraints; guardrails as tested mechanisms rather than intentions |
| **HRM / job-design literature (job characteristics model, empowerment research)** | The measurement of autonomy as experienced practice, and the gap between designed and lived empowerment |
| **Cloud spend governance (budgets, allow-lists, rate limits)** | Working examples of L3/L4 guardrails in production business settings |
| **AWS Well-Architected / Google SRE error budgets** | Telemetry-driven accountability; quantitative revocation triggers |

## What differs from the nearest neighbors

- **Vs. SAE-style ladders:** those describe *state of the art of a system*;
  this framework describes *a managed organizational grant* with contract,
  telemetry, horizon, and revocation triggers.
- **Vs. empowerment literature:** empowerment research mostly *measures
  perception*; this framework measures both the granted (supply) and
  exercised (demand) sides and treats the gap as the primary signal.
- **Vs. RACI/decision-rights charts:** RACI answers *who*; this framework
  answers *who, at what level, under which guardrails, until when, and with
  what evidence it changes*.

## Open questions (research-friendly gaps)

1. Construct validity: does the six-dimension model measure what matters, or
   can it be reduced without losing predictive power?
2. Does the weakest-link rule (`min(D3,D4,D6)`) empirically predict breach
   rates better than mean maturity?
3. How should the framework extend to **AI agents as units** — where
   "capability" is opaque and "intent" is unmeasurable — without collapsing
   back to pure output monitoring?
4. Cross-cultural validity of level definitions (inform-after norms differ
   sharply across corporate cultures).

## Citation

If you use or adapt the framework, cite this repository:

```bibtex
@misc{otchere2022autonomy,
  author = {Emmanuel A. Otchere},
  title  = {Measuring and Managing Autonomy},
  year   = {2022},
  howpublished = {\url{https://github.com/emmanuel-a-otchere/MeasuringAndManagingAutonomy}},
  note   = {Framework, maturity model, and assessment instrument}
}
```

*Contributions of corrections, additional lineage, or empirical applications
are welcome — see [CONTRIBUTING.md](../CONTRIBUTING.md).*
