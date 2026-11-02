#!/usr/bin/env python3
"""Autonomy score calculator for the Measuring & Managing Autonomy framework.

Implements the scoring rules from docs/maturity-model.md and
docs/assessment.md:

  - Each dimension (D1..D6) is scored 0..4 (autonomy levels L0..L4).
  - Safe grant level per domain = min(D3, D4, D6)  ("weakest-link rule").
  - D1/D2 are coaching signals; they cap expansion pace, not current grants.
  - Recommended move comes from the decision table in the maturity model.

Usage:
    python3 tools/autonomy_score.py 3 3 2 2 1 1        # scores for D1..D6
    python3 tools/autonomy_score.py --current 1 3 3 2 2 1
    python3 tools/autonomy_score.py --self-test       # run the built-in tests

Scores are given in order: D1_clarity D2_capability D3_guardrails
D4_telemetry D5_transparency D6_accountability.

License: MIT (see LICENSE).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

DIMENSIONS = [
    ("D1", "decision_clarity"),
    ("D2", "capability"),
    ("D3", "guardrails"),
    ("D4", "telemetry"),
    ("D5", "transparency"),
    ("D6", "accountability"),
]

WEAKEST_LINK = ("D3", "D4", "D6")  # guardrails, telemetry, accountability
CLEAN_CYCLES_TO_EXPAND = 2  # consecutive clean reviews required to expand

# Semantic version of the scoring ruleset. See docs/versioning.md.
# MAJOR = re-scoring (scores not comparable); MINOR = additive/clarification;
# PATCH = no change to scored outputs. Kept identical to site/scoring.js;
# parity is asserted by tools/site_selftest.js.
RULESET_VERSION = "1.0.0"


def parse_scores(values: list[str]) -> dict[str, int]:
    """Parse and validate six dimension scores (ints 0..4)."""
    if len(values) != 6:
        raise SystemExit(
            f"error: expected exactly 6 scores (D1..D6), got {len(values)}\n"
            "usage: autonomy_score.py D1 D2 D3 D4 D5 D6"
        )
    scores: dict[str, int] = {}
    for (code, _name), raw in zip(DIMENSIONS, values):
        try:
            score = int(raw)
        except ValueError:
            raise SystemExit(f"error: score for {code} must be an integer, got {raw!r}")
        if not 0 <= score <= 4:
            raise SystemExit(f"error: score for {code} must be in 0..4, got {score}")
        scores[code] = score
    return scores


def safe_level(scores: dict[str, int]) -> int:
    """Weakest-link rule: min over D3, D4, D6."""
    return min(scores[d] for d in WEAKEST_LINK)


def gap_analysis(scores: dict[str, int], current: int | None) -> list[str]:
    """Notes on granted-vs-exercised and coaching signals."""
    notes: list[str] = []
    weakest = min(scores[d] for d in WEAKEST_LINK)
    coaching = [d for d in ("D1", "D2") if scores[d] < weakest]
    if coaching:
        notes.append(
            f"coaching signal: {', '.join(coaching)} below the safety floor — "
            "invest in clarity/capability; do not revoke for this"
        )
    if current is not None:
        headroom = safe_level(scores) - current
        if headroom > 0:
            notes.append(
                f"headroom: safe level exceeds granted level by {headroom}; "
                f"expand after {CLEAN_CYCLES_TO_EXPAND} clean review cycles"
            )
        elif headroom < 0:
            notes.append(
                f"over-grant: granted level exceeds safe level by {-headroom}; "
                "fix guardrails/telemetry/accountability or step down"
            )
        else:
            notes.append("granted level matches safe level: hold and review")
    return notes


def recommended_move(scores: dict[str, int], current: int | None) -> str:
    """Map a score vector to the management move (maturity model §4)."""
    weakest = safe_level(scores)
    if current is None:
        return "formalize: write a contract at the safe level before any change"
    if weakest < current:
        return "contract or re-shape: safety dimensions lag the grant"
    if weakest > current:
        return (
            f"expand (after {CLEAN_CYCLES_TO_EXPAND} clean cycles): "
            "raise one level or widen scope in the strongest dimension"
        )
    if min(scores["D1"], scores["D2"]) < weakest:
        return "hold and coach: capability/clarity lag; keep the grant"
    return "hold: stable at the current level; re-review next horizon"


def assess(scores: dict[str, int], current: int | None) -> dict:
    return {
        "ruleset_version": RULESET_VERSION,
        "scores": {code: scores[code] for code, _ in DIMENSIONS},
        "safe_grant_level": safe_level(scores),
        "granted_level": current,
        "notes": gap_analysis(scores, current),
        "recommended_move": recommended_move(scores, current),
    }


def render(result: dict) -> str:
    lines = ["Autonomy assessment", "=" * 40]
    lines.append(f"Ruleset version: {RULESET_VERSION}")
    for (code, name) in DIMENSIONS:
        lines.append(f"{code} ({name}): {result['scores'][code]}")
    lines += ["", f"Safe grant level (min D3,D4,D6): L{result['safe_grant_level']}"]
    if result["granted_level"] is not None:
        lines.append(f"Currently granted level:       L{result['granted_level']}")
    lines.append(f"Recommended move: {result['recommended_move']}")
    for note in result["notes"]:
        lines.append(f"note: {note}")
    return "\n".join(lines)


def _self_test() -> None:
    # Version stamp present in outputs, and identical to the JS engine
    # (parity: docs/versioning.md makes cross-implementation drift a blocker)
    assert RULESET_VERSION == "1.0.0"
    assert assess({d: 1 for d, _ in DIMENSIONS}, None)["ruleset_version"] == RULESET_VERSION
    with open(
        os.path.join(os.path.dirname(__file__), "..", "site", "scoring.js"), encoding="utf-8"
    ) as _fh:
        _js = _fh.read()
    _m = re.search(r'RULESET_VERSION\s*=\s*"([^"]+)"', _js)
    assert _m and _m.group(1) == RULESET_VERSION, f"version drift: py={RULESET_VERSION} js={_m and _m.group(1)}"
    # Weakest-link rule
    assert safe_level({d: 4 for d, _ in DIMENSIONS}) == 4
    assert safe_level({"D3": 2, "D4": 3, "D6": 1, "D1": 4, "D2": 4, "D5": 4}) == 1
    # Weakest link ignores D1/D2/D5
    assert safe_level({"D3": 3, "D4": 3, "D6": 3, "D1": 0, "D2": 0, "D5": 0}) == 3
    # Worked example from examples/README.md: scores 1 3 2 2 1 1, no formal grant
    ex = assess({"D1": 1, "D2": 3, "D3": 2, "D4": 2, "D5": 1, "D6": 1}, current=None)
    assert ex["safe_grant_level"] == 1
    assert ex["recommended_move"].startswith("formalize")
    # Coaching signal fires when D1/D2 lag the safety floor
    coach = assess({"D1": 0, "D2": 1, "D3": 3, "D4": 3, "D6": 3, "D5": 3}, current=3)
    assert any("coaching" in n for n in coach["notes"])
    assert coach["recommended_move"].startswith("hold and coach")
    # Over-grant detection
    over = assess({"D1": 4, "D2": 4, "D3": 1, "D4": 4, "D5": 4, "D6": 4}, current=3)
    assert any("over-grant" in n for n in over["notes"])
    assert over["recommended_move"].startswith("contract")
    # Validation errors
    for bad in (["1", "2", "3", "4", "5"], ["1", "2", "3", "4", "5", "x"], ["9"] * 6):
        try:
            parse_scores(bad)
        except SystemExit:
            pass
        else:
            raise AssertionError(f"expected validation failure for {bad}")
    print("self-test: OK")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Compute safe autonomy level and recommended move from six dimension scores."
    )
    parser.add_argument("scores", nargs="*", help="six scores 0..4 for D1..D6")
    parser.add_argument("--current", type=int, metavar="L", help="currently granted level 0..4")
    parser.add_argument("--json", action="store_true", help="emit JSON")
    parser.add_argument("--self-test", action="store_true", help="run built-in tests and exit")
    args = parser.parse_args(argv)

    if args.self_test:
        _self_test()
        return 0

    if args.current is not None and not 0 <= args.current <= 4:
        raise SystemExit("error: --current must be in 0..4")

    scores = parse_scores(args.scores)
    result = assess(scores, args.current)
    print(json.dumps(result, indent=2) if args.json else render(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
