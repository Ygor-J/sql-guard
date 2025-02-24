from CheckBase import BaseCheck, CheckRegistry
from typing import Dict

@CheckRegistry.register("is_integer")
class IsIntegerCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str) -> str:
        return f"SAFE_CAST({column} AS INT) IS NULL"

@CheckRegistry.register("is_string")
class IsStringCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str) -> str:
        return f"SAFE_CAST({column} AS STRING) IS NULL"

@CheckRegistry.register("is_boolean")
class isBooleanCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str) -> str:
        return f"SAFE_CAST({column} AS BOOL) IS NULL"

@CheckRegistry.register("is_float")
class IsFloatCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str) -> str:
        return f"SAFE_CAST({column} AS FLOAT) IS NULL"

@CheckRegistry.register("is_date")
class IsDateCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str) -> str:
        return f"SAFE_CAST({column} AS DATE) IS NULL"

@CheckRegistry.register("is_timestamp")
class IsTimestampCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str) -> str:
        return f"SAFE_CAST({column} AS TIMESTAMP) IS NULL"

@CheckRegistry.register("greater_than")
class GreaterThanCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str) -> str:
        value = params["value"]
        return f"{column} <= {value}"
    
@CheckRegistry.register("starts_with")
class StartsWithCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str) -> str:
        value = params["value"]
        return f"{column} NOT LIKE '{value}%'"
    
@CheckRegistry.register("ends_with")
class EndsWithCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str) -> str:
        value = params["value"]
        return f"{column} NOT LIKE '%{value}'"
    
@CheckRegistry.register("str_contains")
class EndsWithCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str) -> str:
        value = params["value"]
        return f"{column} NOT LIKE '%{value}%'"
    
@CheckRegistry.register("regex_contains")
class EndsWithCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str) -> str:
        value = params["value"]
        return f"NOT REGEXP_CONTAINS({column}, '{value}')"
    
@CheckRegistry.register("between")
class BetweenCheck(BaseCheck):
    def to_sql(self, column: str, params: Dict, dialect: str) -> str:
        min = params["min"]
        max = params["max"]

        return f"{column} BETWEEN {min} AND {max}"
    