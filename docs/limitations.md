# Method limitations

> What `mama` does and does not claim. Read this before acting on a score.

**Status: pilot / under validation.** Until the
[validation program](validation-plan.md) reports, the method's claims are
design rationales, not demonstrated predictions.

## Limits of the instrument

1. **No demonstrated predictive validity (yet).** The weakest-link rule
   `min(D3, D4, D6)` is a reasoned design (breach in any safety dimension
   turns autonomy into unmanaged risk), not an empirically validated
   predictor. Whether assessment signals correspond to observed breaches,
   over/under-grants, or incidents is a
   [hypothesis under test](validation-plan.md), not an established result.
2. **Evidence-backed scores are still self-reported.** Scores are produced
   by assessors with access and incentives. Dual assessment and evidence
   requirements reduce — not remove — gaming and optimism bias.
3. **Rubric boundaries involve judgment.** "Highest level fully achieved"
   requires interpreters to agree on what a row cell means; inter-rater
   agreement is unmeasured until the pilot reports.
4. **Cultural transferability is untested.** L-level norms and what counts
   as "inform-after" differ across cultures; the level definitions have not
   been validated outside their original context.
5. **Domain comparability is structural, not psychometric.** A "3" in
   deploys and a "3" in hiring mean the same rubric position, not the same
   difficulty or risk. Never pool unlike domains without rationale.
6. **Binary scores hide profiles.** The six-value profile is the signal;
   the safe level is a floor derived from it. Acting on the safe level
   alone conceals the strengths the profile shows
   ([why no composite score](mama-integration.md#keep-the-measures-separate)).
7. **The AI-agent extension is a first pass.**
   [agents-as-units](agents-as-units.md) reuses the human instrument for
   agent units; agent-specific dimensions may prove necessary — that would
   be a versioned ruleset change.
8. **Cross-framework mappings are positional, not certified.** Where docs
   relate `mama` to external frameworks (AI RMF, ISO/IEC 42001, and peers —
   see [positioning](positioning.md)), they explain coverage and gaps and
   claim **no equivalence, certification, or endorsement**.

## Rules of use that follow

- A score is an **evidence input to a human governance decision**; it never
  authorizes a deployment or grant by itself.
- Record `ruleset_version` with every scorecard; compare only within the
  same MAJOR version ([versioning](versioning.md)).
- Preserve historical records; re-baseline after MAJOR changes
  ([migration](migration-v1-to-v2.md)).
- Publish, don't hide: if you use `mama` in earnest, your disagreement with
  a rubric row is [feedback the method needs](../CONTRIBUTING.md).
