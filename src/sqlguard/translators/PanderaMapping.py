from pandera import Check
from typing import Dict, Any
import numpy as np

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
    "regex_contains": lambda params: {"value": params["pattern"]},
    "between": lambda params: {"min": params["min_value"], "max": params["max_value"]},
    "is_in": lambda params: {"value": params["allowed_values"]},
    "is_not_in": lambda params: {"value": params["forbidden_values"]}
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
    },

    # Range Checks
    "between": {
        "check_name": "between",
        "param_mapper": PANDERA_PARAM_MAPPER_FUNC["between"]
    },
    "in_range": {
        "check_name": "between",
        "param_mapper": PANDERA_PARAM_MAPPER_FUNC["between"]
    },
    "isin": {
        "check_name": "is_in",
        "param_mapper": PANDERA_PARAM_MAPPER_FUNC["is_in"]
    },
    "notin": {
        "check_name": "is_not_in",
        "param_mapper": PANDERA_PARAM_MAPPER_FUNC["is_not_in"]
    },
}


# consult numpy doc: https://github.com/numpy/numpy/blob/main/numpy/dtypes.pyi
# Pandera dtypes use numpy dtype in the background

NUMPY_DTYPES = [np.dtypes.__dict__[key] for key in np.dtypes.__all__]

PANDERA_NUMPY_DTYPES_MAPPING = {
    np.dtypes.BoolDType: {
        "check_name": "is_boolean"
    },
    np.dtypes.Int8DType: {
        "check_name": "is_integer"
    },
    np.dtypes.UInt8DType: {
        "check_name": None
    },
    np.dtypes.Int16DType: {
        "check_name": "is_integer"
    },
    np.dtypes.UInt16DType: {
        "check_name": None
    },
    np.dtypes.Int32DType: {
        "check_name": "is_integer"
    },
    np.dtypes.UInt32DType: {
        "check_name": None
    },
    np.dtypes.Int64DType: {
        "check_name": "is_integer"
    },
    np.dtypes.UInt64DType: {
        "check_name": None
    },
    np.dtypes.LongLongDType: {
        "check_name": None
    },
    np.dtypes.ULongLongDType: {
        "check_name": None
    },
    np.dtypes.Float16DType: {
        "check_name": "is_float"
    },
    np.dtypes.Float32DType: {
        "check_name": "is_float"
    },
    np.dtypes.Float64DType: {
        "check_name": "is_float"
    },
    np.dtypes.LongDoubleDType: {
        "check_name": None
    },
    np.dtypes.Complex64DType: {
        "check_name": None
    },
    np.dtypes.Complex128DType: {
        "check_name": None
    },
    np.dtypes.CLongDoubleDType: {
        "check_name": None
    },
    np.dtypes.ObjectDType: {
        "check_name": None
    },
    np.dtypes.BytesDType: {
        "check_name": None
    },
    np.dtypes.StrDType: {
        "check_name": "is_string"
    },
    np.dtypes.VoidDType: {
        "check_name": None
    },
    np.dtypes.DateTime64DType: {
        "check_name": "is_date"
    },
    np.dtypes.TimeDelta64DType: {
        "check_name": None
    },
    np.dtypes.StringDType: {
        "check_name": "is_string"
    }
}