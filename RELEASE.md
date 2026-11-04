# Release process

Two versioned surfaces live in this repo (see `docs/versioning.md`): the
**scoring ruleset** (`RULESET_VERSION`, currently 1.0.0) and the **ledger
format** (`schema`, currently 1). The **package version** (`pyproject.toml`)
tracks the toolkit itself and moves independently — bump it for any
user-visible tooling change.

## Checklist — cutting vX.Y.Z

1. CI green on `main` (all three jobs).
2. `CHANGELOG.md`: fold "Unreleased" into a `## vX.Y.Z — YYYY-MM-DD`
   heading. The release workflow publishes that section verbatim as the
   release notes, so write it for users.
3. Set `version = "X.Y.Z"` in `pyproject.toml` to match.
4. Parity still green (a release blocker per `docs/versioning.md`):
   - `python3 tools/autonomy_score.py --self-test`
   - `node tools/site_selftest.js`
5. Commit via PR, merge, then tag and push the tag:
   ```bash
   git tag vX.Y.Z && git push origin vX.Y.Z
   ```
6. The Release workflow (`release.yml`) then:
   - builds the sdist + wheel and smoke-tests both console commands in a
     fresh venv (`--self-test`, CLI smoke, reference-ledger validation);
   - builds one-file binaries (PyInstaller) for macOS arm64, Linux x86_64,
     Windows x86_64 and gate-tests each one's `--self-test`;
   - publishes the GitHub Release with the changelog notes and all artifacts.
7. Verify: download the macOS binary from the release and run
   `./autonomy-score-macos-arm64 --self-test`.
8. PyPI (optional, manual): configure a **trusted publisher** once on
   pypi.org — project `measuring-autonomy`, owner `emmanuel-a-otchere`,
   repository `measuring-and-managing-autonomy`, workflow `publish-pypi.yml`,
   environment `pypi` — then run the "Publish to PyPI" workflow from the
   Actions tab. (Confirm the package name is free first; fallback name:
   `mama-toolkit`.)
9. Kanban: move the release item to Done on the project board.

## Bump classes

From `docs/versioning.md`: any change to items, level definitions, dimension
set, weights, or the weakest-link rule is a **MAJOR** `RULESET_VERSION` bump
in *both* engines (Python and `site/scoring.js`) plus green parity. Scoring
semantics are frozen at v1.x — treat such changes accordingly.
