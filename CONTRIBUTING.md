# Contributing to Measuring and Managing Autonomy

Thanks for helping make autonomy legible.

## Ways to contribute

### 1. Case studies (highest value right now)

Run the [assessment](docs/assessment.md) on a real team or system you know and
submit the anonymized results. The framework is at the validation stage —
evidence of where it works and where it breaks is the most useful gift.

### 2. Framework feedback

A definition unclear? A level definition wrong for your context? The weakest-link
rule contradicted by your experience? Open an issue using the *Framework feedback*
template and tell us what happened.

### 3. Improvements to the instrument

The questionnaire, scoring rules, and CLI are all open to refinement. Small,
well-argued changes preferred — the scoring rules must stay stable enough for
assessments to be comparable over time.

### 4. Research

See [Positioning → Open questions](docs/positioning.md#open-questions-research-friendly-gaps)
for the research-friendly gaps.

## How to submit

1. Fork / branch, commit with a clear message, open a PR against `main`.
2. For doc-only changes, no CI is required; verify the Mermaid diagrams render
   on GitHub in your PR preview.
3. For tool changes: run `python3 tools/autonomy_score.py --self-test` and make
   sure it passes before submitting.
4. PRs that change level definitions or scoring rules should present evidence
   (case study or data), not just opinion.

## Conventions

- Plain Markdown, Mermaid for diagrams (no binary-only images — the original
  2022 diagram was a hotlinked PNG that cannot be versioned or diffed; that
  is the mistake this fixes).
- British/neutral English where the framework text is normative.
- Evidence or it didn't happen: any maturity score asserted at L2+ needs a
  link, log, or artifact.

## Original diagram

The original 2022 concept diagram is archived at
[`docs/img/`](docs/img/README.md) with its mapping to the current framework
axes. If you have higher-resolution or earlier variants, a PR adding them
alongside is welcome.
