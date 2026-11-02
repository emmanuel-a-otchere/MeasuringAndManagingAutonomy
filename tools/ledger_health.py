#!/usr/bin/env python3
"""Autonomy Ledger health checker for the Measuring & Managing Autonomy framework.

Validates a ledger (YAML, format described in docs/ledger-format.md) against
the framework's rules and prints an org-level health report:

  - validity:   schema errors (bad level, missing fields, date inconsistencies)
  - coverage:   fraction of contracts with all required fields
  - staleness:  contracts whose last_review is older than their cadence
  - expiry:     active contracts past their horizon (autonomy with no live review)
  - guardrails: contracts with empty guardrail/telemetry/trigger lists

Exit code 0 = healthy ledger; 1 = findings; 2 = unreadable/invalid file.

Usage:
    python3 tools/ledger_health.py examples/ledger.yaml
    python3 tools/ledger_health.py ledger.yaml --today 2025-12-31
    python3 tools/ledger_health.py --self-test

Requires PyYAML (standard on GitHub runners; pip install pyyaml otherwise).
License: MIT (see LICENSE).
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

REQUIRED_LISTS = ("guardrails", "telemetry", "revocation_triggers")
REQUIRED_FIELDS = (
    "id",
    "unit",
    "domain",
    "level",
    "scope",
    "guardrails",
    "telemetry",
    "revocation_triggers",
    "grantor",
    "horizon",
    "last_review",
)
STATUSES = ("active", "expired", "revoked", "draft")
DEFAULT_CADENCE_DAYS = 90


def parse_date(value) -> dt.date | None:
    if isinstance(value, dt.date):
        return value
    try:
        return dt.date.fromisoformat(str(value))
    except ValueError:
        return None


def check_contract(c: dict, today: dt.date, idx: int) -> tuple[list[str], dict]:
    """Return (errors, metrics) for one contract. Errors are fatal findings;
    metrics feed the health report."""
    errors: list[str] = []
    label = c.get("id") or f"contract[{idx}]"
    status = c.get("status", "active")

    # required fields
    for field in REQUIRED_FIELDS:
        if field not in c or c[field] in (None, ""):
            errors.append(f"{label}: missing required field '{field}'")
    # non-empty lists
    for field in REQUIRED_LISTS:
        value = c.get(field)
        if value is not None and not (isinstance(value, list) and len(value) > 0):
            errors.append(f"{label}: '{field}' must be a non-empty list")
    # level
    if "level" in c and (not isinstance(c["level"], int) or not 0 <= c["level"] <= 4):
        errors.append(f"{label}: level must be an integer 0..4")
    # status
    if status not in STATUSES:
        errors.append(f"{label}: status must be one of {STATUSES}")
    # dates
    horizon = parse_date(c.get("horizon")) if "horizon" in c else None
    last_review = parse_date(c.get("last_review")) if "last_review" in c else None
    if "horizon" in c and horizon is None:
        errors.append(f"{label}: horizon is not an ISO date")
    if "last_review" in c and last_review is None:
        errors.append(f"{label}: last_review is not an ISO date")
    if horizon and last_review and last_review > horizon:
        errors.append(f"{label}: last_review is after horizon")

    # health metrics (only meaningful for live contracts)
    cadence = c.get("review_cadence_days", DEFAULT_CADENCE_DAYS)
    stale = expired = False
    if status == "active":
        if last_review and (today - last_review).days > cadence:
            stale = True
        if horizon and today > horizon:
            expired = True
    metrics = {
        "id": c.get("id"),
        "unit": c.get("unit"),
        "domain": c.get("domain"),
        "level": c.get("level"),
        "status": status,
        "stale": stale,
        "expired": expired,
    }
    return errors, metrics


def health_report(ledger: dict, today: dt.date) -> dict:
    contracts = ledger.get("contracts")
    if not isinstance(contracts, list):
        raise ValueError("ledger must contain a 'contracts' list")

    errors: list[str] = []
    metrics: list[dict] = []
    ids: set[str] = set()
    for idx, c in enumerate(contracts):
        if not isinstance(c, dict):
            errors.append(f"contract[{idx}]: must be a mapping")
            continue
        c_errors, c_metrics = check_contract(c, today, idx)
        errors += c_errors
        if c_metrics["id"]:
            if c_metrics["id"] in ids:
                errors.append(f"{c_metrics['id']}: duplicate id")
            ids.add(c_metrics["id"])
        metrics.append(c_metrics)

    active = [m for m in metrics if m["status"] == "active"]
    valid = [m for m in metrics if m["id"] and m["status"] in ("active", "draft")]
    report = {
        "total_contracts": len(metrics),
        "active": len(active),
        "valid": len(valid),
        "validity_errors": errors,
        "coverage": round(len(valid) / len(metrics), 2) if metrics else 1.0,
        "stale_reviews": [m["id"] for m in active if m["stale"]],
        "expired_horizons": [m["id"] for m in active if m["expired"]],
        "unhygienic": len(errors),
        "today": today.isoformat(),
    }
    return report


def render(report: dict) -> str:
    lines = ["Autonomy Ledger health", "=" * 40]
    lines.append(
        f"Contracts: {report['total_contracts']} total, {report['active']} active"
    )
    lines.append(f"Coverage: {int(report['coverage'] * 100)}% valid contracts")
    if report["stale_reviews"]:
        lines.append(f"STALE reviews (past cadence): {', '.join(report['stale_reviews'])}")
    else:
        lines.append("Stale reviews: none")
    if report["expired_horizons"]:
        lines.append(
            f"EXPIRED horizons (active past horizon): {', '.join(report['expired_horizons'])}"
        )
    else:
        lines.append("Expired horizons: none")
    for err in report["validity_errors"]:
        lines.append(f"error: {err}")
    verdict = "HEALTHY" if not (report["validity_errors"] or report["stale_reviews"] or report["expired_horizons"]) else "NEEDS ATTENTION"
    lines.append(f"Verdict: {verdict}")
    return "\n".join(lines)


def _self_test() -> None:
    good = {
        "contracts": [
            {
                "id": "c1", "unit": "u", "domain": "d", "level": 2, "scope": "s",
                "guardrails": ["g"], "telemetry": ["t"],
                "revocation_triggers": ["r"], "grantor": "G",
                "horizon": "2025-12-31", "last_review": "2025-09-30",
                "status": "active",
            }
        ]
    }
    today = dt.date(2025, 10, 1)
    r = health_report(good, today)
    assert not r["validity_errors"] and not r["stale_reviews"], r
    assert r["coverage"] == 1.0

    # staleness: review 200 days ago, cadence 90
    stale = {"contracts": [dict(good["contracts"][0], last_review="2025-01-01")]}
    r = health_report(stale, today)
    assert r["stale_reviews"] == ["c1"], r

    # expiry: active contract past horizon
    expired = {"contracts": [dict(good["contracts"][0], horizon="2025-09-30", last_review="2025-09-01")]}
    r = health_report(expired, dt.date(2025, 10, 2))
    assert r["expired_horizons"] == ["c1"], r

    # schema violations
    bad = {"contracts": [{"id": "c", "level": 7, "guardrails": [], "status": "weird"}]}
    r = health_report(bad, today)
    errs = " ".join(r["validity_errors"])
    assert "level" in errs and "status" in errs and "guardrails" in errs, r["validity_errors"]

    # duplicate ids
    dup = {"contracts": [good["contracts"][0], dict(good["contracts"][0])]}
    r = health_report(dup, today)
    assert any("duplicate" in e for e in r["validity_errors"]), r["validity_errors"]

    # last_review after horizon
    inv = {"contracts": [dict(good["contracts"][0], horizon="2025-06-30", last_review="2025-09-30")]}
    r = health_report(inv, today)
    assert any("after horizon" in e for e in r["validity_errors"]), r["validity_errors"]

    # not a contracts list
    for bad_ledger in ({}, {"contracts": "nope"}):
        try:
            health_report(bad_ledger, today)
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError for malformed ledger")

    print("self-test: OK")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check Autonomy Ledger health (v1 format).")
    parser.add_argument("ledger", nargs="?", help="path to ledger.yaml")
    parser.add_argument("--today", help="override today's date (ISO) for testing")
    parser.add_argument("--json", action="store_true", help="emit JSON")
    parser.add_argument("--self-test", action="store_true", help="run built-in tests and exit")
    args = parser.parse_args(argv)

    if args.self_test:
        _self_test()
        return 0

    if not args.ledger:
        parser.error("a ledger file is required (or --self-test)")

    if yaml is None:
        print("error: PyYAML is required (pip install pyyaml)", file=sys.stderr)
        return 2

    try:
        with open(args.ledger, encoding="utf-8") as fh:
            ledger = yaml.safe_load(fh)
    except (OSError, yaml.YAMLError) as exc:
        print(f"error: cannot read ledger: {exc}", file=sys.stderr)
        return 2

    today = parse_date(args.today) if args.today else dt.date.today()
    if today is None:
        print("error: --today must be an ISO date", file=sys.stderr)
        return 2

    try:
        report = health_report(ledger or {}, today)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    print(json.dumps(report, indent=2) if args.json else render(report))
    bad = report["validity_errors"] or report["stale_reviews"] or report["expired_horizons"]
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
