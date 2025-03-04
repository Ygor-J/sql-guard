from sqlguard.validator.CheckBase import BaseCheck, CheckRegistry
from sqlguard.utils import SQLHelpers
from typing import Dict

# Type Checks

# https://duckdb.org/docs/stable/clients/python/types

@CheckRegistry.register("is_integer")
class IsIntegerCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str, ignore_nulls: bool) -> str:
        ignore_nulls_condition = SQLHelpers.get_ignore_nulls_condition(column, ignore_nulls)

        casting_function = ""
        cast_type = ""
        if dialect == "GoogleSQL":
            casting_function = "SAFE_CAST"
            cast_type = "INT"
        elif dialect == "DuckDBSQL":
            casting_function = "TRY_CAST"
            cast_type = "BIGINT"
        else:
            raise ValueError(f"ERROR: {dialect} dialect is not supported! Only GoogleSQL and DuckDBSQL are available!")

        return f"{casting_function}({column} AS {cast_type}) IS NOT NULL" + ignore_nulls_condition

@CheckRegistry.register("is_string")
class IsStringCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str, ignore_nulls: bool) -> str:
        ignore_nulls_condition = SQLHelpers.get_ignore_nulls_condition(column, ignore_nulls)

        casting_function = ""
        cast_type = ""
        if dialect == "GoogleSQL":
            casting_function = "SAFE_CAST"
            cast_type = "STRING"
        elif dialect == "DuckDBSQL":
            casting_function = "TRY_CAST"
            cast_type = "VARCHAR"
        else:
            raise ValueError(f"ERROR: {dialect} dialect is not supported! Only GoogleSQL and DuckDBSQL are available!")

        return f"{casting_function}({column} AS {cast_type}) IS NOT NULL" + ignore_nulls_condition

@CheckRegistry.register("is_boolean")
class isBooleanCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str, ignore_nulls: bool) -> str:
        ignore_nulls_condition = SQLHelpers.get_ignore_nulls_condition(column, ignore_nulls)

        casting_function = ""
        cast_type = ""
        if dialect == "GoogleSQL":
            casting_function = "SAFE_CAST"
            cast_type = "BOOL"
        elif dialect == "DuckDBSQL":
            casting_function = "TRY_CAST"
            cast_type = "BOOLEAN"
        else:
            raise ValueError(f"ERROR: {dialect} dialect is not supported! Only GoogleSQL and DuckDBSQL are available!")

        return f"{casting_function}({column} AS {cast_type}) IS NOT NULL" + ignore_nulls_condition

@CheckRegistry.register("is_float")
class IsFloatCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str, ignore_nulls: bool) -> str:
        ignore_nulls_condition = SQLHelpers.get_ignore_nulls_condition(column, ignore_nulls)

        casting_function = ""
        cast_type = ""
        if dialect == "GoogleSQL":
            casting_function = "SAFE_CAST"
            cast_type = "FLOAT64"
        elif dialect == "DuckDBSQL":
            casting_function = "TRY_CAST"
            cast_type = "DOUBLE"
        else:
            raise ValueError(f"ERROR: {dialect} dialect is not supported! Only GoogleSQL and DuckDBSQL are available!")

        return f"{casting_function}({column} AS {cast_type}) IS NOT NULL" + ignore_nulls_condition

@CheckRegistry.register("is_date")
class IsDateCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str, ignore_nulls: bool) -> str:
        ignore_nulls_condition = SQLHelpers.get_ignore_nulls_condition(column, ignore_nulls)

        casting_function = ""
        cast_type = ""
        if dialect == "GoogleSQL":
            casting_function = "SAFE_CAST"
            cast_type = "DATE"
        elif dialect == "DuckDBSQL":
            casting_function = "TRY_CAST"
            cast_type = "DATE"
        else:
            raise ValueError(f"ERROR: {dialect} dialect is not supported! Only GoogleSQL and DuckDBSQL are available!")

        return f"{casting_function}({column} AS {cast_type}) IS NOT NULL" + ignore_nulls_condition

@CheckRegistry.register("is_timestamp")
class IsTimestampCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str, ignore_nulls: bool) -> str:
        ignore_nulls_condition = SQLHelpers.get_ignore_nulls_condition(column, ignore_nulls)

        casting_function = ""
        cast_type = ""
        if dialect == "GoogleSQL":
            casting_function = "SAFE_CAST"
            cast_type = "TIMESTAMP"
        elif dialect == "DuckDBSQL":
            casting_function = "TRY_CAST"
            cast_type = "TIMESTAMP"
        else:
            raise ValueError(f"ERROR: {dialect} dialect is not supported! Only GoogleSQL and DuckDBSQL are available!")

        return f"{casting_function}({column} AS {cast_type}) IS NOT NULL" + ignore_nulls_condition

# Comparison Checks

@CheckRegistry.register("greater_than")
class GreaterThanCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str, ignore_nulls: bool) -> str:
        value = params["value"]
        ignore_nulls_condition = SQLHelpers.get_ignore_nulls_condition(column, ignore_nulls)
        return f"{column} > {value}" + ignore_nulls_condition

@CheckRegistry.register("greater_or_equal_than")
class GreaterThanCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str, ignore_nulls: bool) -> str:
        value = params["value"]
        ignore_nulls_condition = SQLHelpers.get_ignore_nulls_condition(column, ignore_nulls)
        return f"{column} >= {value}" + ignore_nulls_condition

@CheckRegistry.register("equal")
class GreaterThanCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str, ignore_nulls: bool) -> str:
        value = params["value"]
        ignore_nulls_condition = SQLHelpers.get_ignore_nulls_condition(column, ignore_nulls)
        if type(value) in [int, float, bool]:
            return f"{column} = {value}" + ignore_nulls_condition
        return f"{column} = '{value}'" + ignore_nulls_condition

@CheckRegistry.register("not_equal")
class GreaterThanCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str, ignore_nulls: bool) -> str:
        value = params["value"]
        ignore_nulls_condition = SQLHelpers.get_ignore_nulls_condition(column, ignore_nulls)
        if type(value) in [int, float, bool]:
            return f"{column} = {value}" + ignore_nulls_condition
        return f"{column} != '{value}'" + ignore_nulls_condition

@CheckRegistry.register("less_than")
class GreaterThanCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str, ignore_nulls: bool) -> str:
        value = params["value"]
        ignore_nulls_condition = SQLHelpers.get_ignore_nulls_condition(column, ignore_nulls)
        return f"{column} < {value}" + ignore_nulls_condition

@CheckRegistry.register("less_or_equal_than")
class GreaterThanCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str, ignore_nulls: bool) -> str:
        value = params["value"]
        ignore_nulls_condition = SQLHelpers.get_ignore_nulls_condition(column, ignore_nulls)
        return f"{column} <= {value}" + ignore_nulls_condition

# String Manipulation Checks

@CheckRegistry.register("starts_with")
class StartsWithCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str, ignore_nulls: bool) -> str:
        value = params["value"]
        ignore_nulls_condition = SQLHelpers.get_ignore_nulls_condition(column, ignore_nulls)
        return f"{column} LIKE '{value}%'" + ignore_nulls_condition
    
@CheckRegistry.register("ends_with")
class EndsWithCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str, ignore_nulls: bool) -> str:
        value = params["value"]
        ignore_nulls_condition = SQLHelpers.get_ignore_nulls_condition(column, ignore_nulls)
        return f"{column} LIKE '%{value}'" + ignore_nulls_condition
    
@CheckRegistry.register("str_contains")
class EndsWithCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str, ignore_nulls: bool) -> str:
        value = params["value"]
        ignore_nulls_condition = SQLHelpers.get_ignore_nulls_condition(column, ignore_nulls)
        return f"{column} LIKE '%{value}%'" + ignore_nulls_condition
    
@CheckRegistry.register("regex_contains")
class EndsWithCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str, ignore_nulls: bool) -> str:
        value = params["value"]
        ignore_nulls_condition = SQLHelpers.get_ignore_nulls_condition(column, ignore_nulls)

        regex_function = ""
        expression_symbol = ""
        if dialect == "GoogleSQL":
            regex_function = "REGEXP_CONTAINS"
            expression_symbol = "r"
        elif dialect == "DuckDBSQL":
            regex_function = "REGEXP_MATCHES"
            expression_symbol = "E"
        else:
            raise ValueError(f"ERROR: {dialect} dialect is not supported! Only GoogleSQL and DuckDBSQL are available!")

        return f"{regex_function}({column}, {expression_symbol}'{value}')" + ignore_nulls_condition

# Range Checks
   
@CheckRegistry.register("between")
class BetweenCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str, ignore_nulls: bool)  -> str:
        min = params["min"]
        max = params["max"]

        ignore_nulls_condition = SQLHelpers.get_ignore_nulls_condition(column, ignore_nulls)

        return f"{column} BETWEEN {min} AND {max}" + ignore_nulls_condition
    
@CheckRegistry.register("is_in")
class BetweenCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str, ignore_nulls: bool) -> str:
        values = params["value"]
        values = str(values)
        values = values[1:-1]

        ignore_nulls_condition = SQLHelpers.get_ignore_nulls_condition(column, ignore_nulls)

        return f"{column} IN ({values})" + ignore_nulls_condition

@CheckRegistry.register("is_not_in")
class BetweenCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str, ignore_nulls: bool) -> str:
        values = params["value"]
        values = str(values)
        values = values[1:-1]

        ignore_nulls_condition = SQLHelpers.get_ignore_nulls_condition(column, ignore_nulls)

        return f"{column} NOT IN ({values})" + ignore_nulls_condition
