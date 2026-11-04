# Security policy

## Reporting a vulnerability

Please use **GitHub's private vulnerability reporting** for this repository
(**Security → Report a vulnerability**) — do not open a public issue for
something exploitable.

Include: the affected component (CLI tools, `src/measuring_autonomy/`, the
static `site/`, workflows), a minimal reproduction, and the impact you see.
You will get an acknowledgment within 7 days and a follow-up as fixes are
prepared. Reporters who wish to be credited in the release notes should say
so; otherwise reports are handled confidentially.

## Scope

- **In scope:** the Python package and CLI tools, the standalone binaries'
  build configuration, the static assessment site, the ledger YAML
  handling, and the CI/release workflows (anything that would let a
  crafted ledger/document/binary mislead a user or execute code).
- **Considerations specific to `mama`:** the tools process organizational
  governance documents. A security issue here includes any way a crafted
  ledger or scorecard file could misrepresent data (e.g., bypass
  validation) or leak local files when run.
- **Out of scope:** the scoring method's semantics and validity (use
  [framework feedback](https://github.com/emmanuel-a-otchere/measuring-and-managing-autonomy/issues/new?template=framework-feedback.md));
  vulnerabilities in GitHub Pages, PyPI, or third-party actions should also
  be reported to those platforms.

## Handling

Fixes land via PR with regression tests, are disclosed in the
[changelog](CHANGELOG.md) with the release that carries them, and binaries
are rebuilt for affected releases.
