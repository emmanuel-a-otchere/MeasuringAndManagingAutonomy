#!/usr/bin/env python3
"""Autonomy score calculator — zero-install shim over measuring_autonomy.score.

The implementation lives in src/measuring_autonomy/score.py and ships as the
`autonomy-score` console command (pip install measuring-autonomy). This shim
keeps the documented `python3 tools/autonomy_score.py` workflow working from
a repository checkout without installing anything.

License: MIT (see LICENSE).
"""
from __future__ import annotations

import os
import sys

try:
    from measuring_autonomy import score as _impl
except ImportError:  # repository checkout without pip install
    sys.path.insert(
        0,
        os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "src"),
    )
    from measuring_autonomy import score as _impl

# Re-exported for direct imports and parity checks (tools/site_selftest.js).
DIMENSIONS = _impl.DIMENSIONS
WEAKEST_LINK = _impl.WEAKEST_LINK
CLEAN_CYCLES_TO_EXPAND = _impl.CLEAN_CYCLES_TO_EXPAND
RULESET_VERSION = _impl.RULESET_VERSION
parse_scores = _impl.parse_scores
safe_level = _impl.safe_level
gap_analysis = _impl.gap_analysis
recommended_move = _impl.recommended_move
assess = _impl.assess
render = _impl.render
_self_test = _impl._self_test
main = _impl.main

if __name__ == "__main__":
    sys.exit(main())
