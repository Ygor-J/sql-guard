from sql_guard.validator.CheckBase import BaseCheck, CheckRegistry
from sql_guard.utils import SQLHelpers
from typing import Dict

@CheckRegistry.register("is_integer")
class IsIntegerCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str, ignore_nulls: bool) -> str:
        ignore_nulls_condition = SQLHelpers.get_ignore_nulls_condition(column, ignore_nulls)
        return f"SAFE_CAST({column} AS INT) IS NOT NULL" + ignore_nulls_condition

@CheckRegistry.register("is_string")
class IsStringCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str, ignore_nulls: bool) -> str:
        ignore_nulls_condition = SQLHelpers.get_ignore_nulls_condition(column, ignore_nulls)
        return f"SAFE_CAST({column} AS STRING) IS NOT NULL" + ignore_nulls_condition

@CheckRegistry.register("is_boolean")
class isBooleanCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str, ignore_nulls: bool) -> str:
        ignore_nulls_condition = SQLHelpers.get_ignore_nulls_condition(column, ignore_nulls)
        return f"SAFE_CAST({column} AS BOOL) IS NOT NULL" + ignore_nulls_condition

@CheckRegistry.register("is_float")
class IsFloatCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str, ignore_nulls: bool) -> str:
        ignore_nulls_condition = SQLHelpers.get_ignore_nulls_condition(column, ignore_nulls)
        return f"SAFE_CAST({column} AS FLOAT) IS NOT NULL" + ignore_nulls_condition

@CheckRegistry.register("is_date")
class IsDateCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str, ignore_nulls: bool) -> str:
        ignore_nulls_condition = SQLHelpers.get_ignore_nulls_condition(column, ignore_nulls)
        return f"SAFE_CAST({column} AS DATE) IS NOT NULL" + ignore_nulls_condition

@CheckRegistry.register("is_timestamp")
class IsTimestampCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str, ignore_nulls: bool) -> str:
        ignore_nulls_condition = SQLHelpers.get_ignore_nulls_condition(column, ignore_nulls)
        return f"SAFE_CAST({column} AS TIMESTAMP) IS NOT NULL" + ignore_nulls_condition

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
        return f"{column} = {value}" + ignore_nulls_condition

@CheckRegistry.register("not_equal")
class GreaterThanCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str, ignore_nulls: bool) -> str:
        value = params["value"]
        return f"{column} != {value}"

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
        return f"REGEXP_CONTAINS({column}, r'{value}')" + ignore_nulls_condition
    
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
        values = params['value']
        values = str(values)
        values = values[1:-1]

        ignore_nulls_condition = SQLHelpers.get_ignore_nulls_condition(column, ignore_nulls)

        return f"{column} IN ({values})" + ignore_nulls_condition

@CheckRegistry.register("is_not_in")
class BetweenCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str, ignore_nulls: bool) -> str:
        values = params['value']
        values = str(values)
        values = values[1:-1]

        ignore_nulls_condition = SQLHelpers.get_ignore_nulls_condition(column, ignore_nulls)

        return f"{column} NOT IN ({values})" + ignore_nulls_condition
