"""Measuring & Managing Autonomy toolkit.

Scoring engine and Autonomy Ledger health checker for the framework
(https://github.com/emmanuel-a-otchere/MeasuringAndManagingAutonomy).

The ledger module is imported lazily by its console command only, so
`import measuring_autonomy` stays dependency-free; PyYAML is required
solely by `ledger-health`.
"""
from .score import (
    DIMENSIONS,
    WEAKEST_LINK,
    RULESET_VERSION,
    assess,
    gap_analysis,
    parse_scores,
    recommended_move,
    safe_level,
)

__version__ = "2.1.0"

__all__ = [
    "__version__",
    "DIMENSIONS",
    "RULESET_VERSION",
    "WEAKEST_LINK",
    "assess",
    "gap_analysis",
    "parse_scores",
    "recommended_move",
    "safe_level",
]
