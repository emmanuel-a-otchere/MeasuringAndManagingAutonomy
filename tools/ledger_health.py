#!/usr/bin/env python3
"""Autonomy Ledger health checker — zero-install shim over measuring_autonomy.ledger.

The implementation lives in src/measuring_autonomy/ledger.py and ships as the
`ledger-health` console command (pip install measuring-autonomy). This shim
keeps the documented `python3 tools/ledger_health.py` workflow working from
a repository checkout without installing anything.

License: MIT (see LICENSE).
"""
from __future__ import annotations

import os
import sys

try:
    from measuring_autonomy import ledger as _impl
except ImportError:  # repository checkout without pip install
    sys.path.insert(
        0,
        os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "src"),
    )
    from measuring_autonomy import ledger as _impl

# Re-exported for direct imports and tests.
REQUIRED_LISTS = _impl.REQUIRED_LISTS
REQUIRED_FIELDS = _impl.REQUIRED_FIELDS
STATUSES = _impl.STATUSES
DEFAULT_CADENCE_DAYS = _impl.DEFAULT_CADENCE_DAYS
SUPPORTED_SCHEMA_VERSION = _impl.SUPPORTED_SCHEMA_VERSION
parse_date = _impl.parse_date
check_contract = _impl.check_contract
health_report = _impl.health_report
render = _impl.render
_self_test = _impl._self_test
main = _impl.main

if __name__ == "__main__":
    sys.exit(main())
