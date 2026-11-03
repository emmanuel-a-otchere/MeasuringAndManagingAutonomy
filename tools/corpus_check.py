#!/usr/bin/env python3
"""Shared scoring corpus checker (Python implementation).

Runs every case in tests/corpus.json through measuring_autonomy.score and
fails on any drift from the expected values. The corpus is the single test
fixture shared by all scoring implementations (see tools/corpus_check.js for
the JavaScript engine); CI runs both and blocks release on drift.

Usage:
    python3 tools/corpus_check.py            # from a repository checkout
    (no flags — the corpus path is resolved relative to this file)

License: MIT (see LICENSE).
"""
from __future__ import annotations

import json
import os
import sys

try:
    from measuring_autonomy import score as impl
except ImportError:  # repository checkout without pip install
    sys.path.insert(
        0,
        os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "src"),
    )
    from measuring_autonomy import score as impl


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    corpus_path = os.path.join(here, os.pardir, "tests", "corpus.json")
    with open(corpus_path, encoding="utf-8") as fh:
        corpus = json.load(fh)

    if corpus["ruleset_version"] != impl.RULESET_VERSION:
        print(
            f"error: corpus targets ruleset {corpus['ruleset_version']} "
            f"but the engine is {impl.RULESET_VERSION} — update "
            f"tests/corpus.json with the scoring change",
            file=sys.stderr,
        )
        return 2

    failures: list[str] = []
    for case in corpus["cases"]:
        name = case["name"]
        result = impl.assess(dict(case["scores"]), case["current"])
        expect = case["expect"]
        if result["safe_grant_level"] != expect["safe_grant_level"]:
            failures.append(
                f"{name}: safe_grant_level {result['safe_grant_level']} "
                f"!= {expect['safe_grant_level']}"
            )
        if result["recommended_move"] != expect["recommended_move"]:
            failures.append(
                f"{name}: recommended_move {result['recommended_move']!r} "
                f"!= {expect['recommended_move']!r}"
            )
        for needle in expect.get("notes_contain", []):
            if not any(needle in n for n in result["notes"]):
                failures.append(f"{name}: no note containing {needle!r} in {result['notes']}")

    for bad in corpus["invalid_inputs"]["score_vectors"]:
        try:
            impl.parse_scores([str(v) for v in bad["scores"]])
        except SystemExit:
            pass
        else:
            failures.append(f"invalid input {bad['name']} was accepted")

    for current in corpus["invalid_inputs"]["current_values"]:
        try:
            impl.main([str(1)] * 6 + ["--current", str(current)])
        except SystemExit as exc:
            code = exc.code
            if code in (0, None):
                failures.append(f"--current {current} exited 0, expected rejection")
        else:
            failures.append(f"--current {current} was accepted")

    if failures:
        for f in failures:
            print(f"FAIL - {f}", file=sys.stderr)
        print(f"corpus (python): {len(failures)} failure(s)", file=sys.stderr)
        return 1

    n = len(corpus["cases"])
    print(f"corpus (python): {n} cases OK against ruleset {impl.RULESET_VERSION}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
