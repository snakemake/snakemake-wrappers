"""
Constraint dictionaries for validating TRF numeric parameters and options.

TRF_NUMERIC_CONSTRAINTS:
    Defines rules for numeric TRF parameters. Each key corresponds to a parameter
    (e.g., 'match', 'mismatch') and contains allowed values or bounds:
        - 'min'/'max': Enforce minimum/maximum numeric limits.
        - 'allowed': Accept only specific integer values.
        - 'recommended': Suggest a preferred value (used for warnings).

TRF_OPTION_VALUE_CONSTRAINTS:
    Defines rules for TRF options that accept values (e.g., '-l').
    Includes allowed ranges and thresholds that trigger warnings when exceeded.
"""

TRF_NUMERIC_CONSTRAINTS = {
    "match": {
        "min": 1,
        "recommended": 2,
    },
    "mismatch": {
        "allowed": {3, 5, 7},
    },
    "delta": {
        "allowed": {3, 5, 7},
    },
    "pm": {
        "allowed": {75, 80},
    },
    "pi": {
        "allowed": {10, 20},
    },
    "minscore": {
        "min": 1,
    },
    "maxperiod": {
        "min": 1,
        "max": 2000,
    },
}

TRF_OPTION_VALUE_CONSTRAINTS = {
    "-l": {
        "min": 1,
        "max": 29,  # Above 29 is allowed but warned
    }
}
