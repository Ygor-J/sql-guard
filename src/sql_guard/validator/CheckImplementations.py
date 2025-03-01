from CheckBase import BaseCheck, CheckRegistry
from typing import Dict

@CheckRegistry.register("is_integer")
class IsIntegerCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str) -> str:
        return f"SAFE_CAST({column} AS INT) IS NOT NULL"

@CheckRegistry.register("is_string")
class IsStringCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str) -> str:
        return f"SAFE_CAST({column} AS STRING) IS NOT NULL"

@CheckRegistry.register("is_boolean")
class isBooleanCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str) -> str:
        return f"SAFE_CAST({column} AS BOOL) IS NOT NULL"

@CheckRegistry.register("is_float")
class IsFloatCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str) -> str:
        return f"SAFE_CAST({column} AS FLOAT) IS NOT NULL"

@CheckRegistry.register("is_date")
class IsDateCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str) -> str:
        return f"SAFE_CAST({column} AS DATE) IS NOT NULL"

@CheckRegistry.register("is_timestamp")
class IsTimestampCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str) -> str:
        return f"SAFE_CAST({column} AS TIMESTAMP) IS NOT NULL"

@CheckRegistry.register("greater_than")
class GreaterThanCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str) -> str:
        value = params["value"]
        return f"{column} > {value}"

@CheckRegistry.register("greater_or_equal_than")
class GreaterThanCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str) -> str:
        value = params["value"]
        return f"{column} >= {value}"

@CheckRegistry.register("less_than")
class GreaterThanCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str) -> str:
        value = params["value"]
        return f"{column} < {value}"

@CheckRegistry.register("less_or_equal_than")
class GreaterThanCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str) -> str:
        value = params["value"]
        return f"{column} <= {value}"
    
@CheckRegistry.register("starts_with")
class StartsWithCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str) -> str:
        value = params["value"]
        return f"{column} LIKE '{value}%'"
    
@CheckRegistry.register("ends_with")
class EndsWithCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str) -> str:
        value = params["value"]
        return f"{column} LIKE '%{value}'"
    
@CheckRegistry.register("str_contains")
class EndsWithCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str) -> str:
        value = params["value"]
        return f"{column} LIKE '%{value}%'"
    
@CheckRegistry.register("regex_contains")
class EndsWithCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str) -> str:
        value = params["value"]
        return f"REGEXP_CONTAINS({column}, r'{value}')"
    
@CheckRegistry.register("between")
class BetweenCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str) -> str:
        min = params["min"]
        max = params["max"]

        return f"{column} BETWEEN {min} AND {max}"
    
@CheckRegistry.register("is_in")
class BetweenCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str) -> str:
        values = params['value']
        values = str(values)
        values = values[1:-1]

        return f"{column} IN ({values})"

@CheckRegistry.register("is_not_in")
class BetweenCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str) -> str:
        values = params['value']
        values = str(values)
        values = values[1:-1]

        return f"{column} NOT IN ({values})"
