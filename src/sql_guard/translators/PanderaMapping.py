from pandera import Check
from typing import Dict, Any


# Params returned should be equivalent to ValidationCheck params
# See github for list of classmethods checks
# https://github.com/unionai-oss/pandera/blob/main/pandera/api/checks.py
PANDERA_PARAM_MAPPER_FUNC = {
    "greater_than": lambda params: {"value": params["min_value"]},
    "greater_or_equal_than": lambda params: {"value": params["min_value"]},
    "equal": lambda params: {"value": params["value"]},
    "not_equal": lambda params: {"value": params["value"]},
    "less_than": lambda params: {"value": params["max_value"]},
    "less_or_equal_than": lambda params: {"value": params["max_value"]},
    "starts_with": lambda params: {"value": params["string"]},
    "ends_with": lambda params: {"value": params["string"]},
    "str_contains": lambda params: {"value": params["pattern"]},
    "regex_contains": lambda params: {"value": params["pattern"]}
}

PANDERA_CHECK_MAPPING = {

    # Comparison Checks
    "greater_than": {
        "check_name": "greater_than",
        "param_mapper": PANDERA_PARAM_MAPPER_FUNC["greater_than"]
    },
    "greater_than_or_equal_to": {
        "check_name": "greater_or_equal_than",
        "param_mapper": PANDERA_PARAM_MAPPER_FUNC["greater_or_equal_than"]
    },
    "equal_to": {
        "check_name": "equal",
        "param_mapper": PANDERA_PARAM_MAPPER_FUNC["equal"]
    },
    "not_equal_to": {
        "check_name": "not_equal",
        "param_mapper": PANDERA_PARAM_MAPPER_FUNC["not_equal"]
    },
    "less_than": {
        "check_name": "less_than",
        "param_mapper": PANDERA_PARAM_MAPPER_FUNC["less_than"]
    },
    "less_than_or_equal_to": {
        "check_name": "less_or_equal_than",
        "param_mapper": PANDERA_PARAM_MAPPER_FUNC["less_or_equal_than"]
    },

    # String Manipulation Checks
    "str_startswith": {
        "check_name": "starts_with",
        "param_mapper": PANDERA_PARAM_MAPPER_FUNC["starts_with"]
    },
    "str_endswith": {
        "check_name": "ends_with",
        "param_mapper": PANDERA_PARAM_MAPPER_FUNC["ends_with"]
    },
    "str_contains": {
        "check_name": "str_contains",
        "param_mapper": PANDERA_PARAM_MAPPER_FUNC["str_contains"]
    },
    "str_matches": {
        "check_name": "regex_contains",
        "param_mapper": PANDERA_PARAM_MAPPER_FUNC["regex_contains"]
    }
}