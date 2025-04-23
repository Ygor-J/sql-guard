import pytest
from sqlguard.validator.CheckBase import CheckRegistry
from typing import Dict

class TestSQLConditionGeneration:
    # Helper method to get check instance
    def get_check(self, check_name):
        return CheckRegistry.get_check(check_name)

    # Test data for parameterized tests
    TEST_DATA = [
        # (check_name, params, expected_google, expected_duckdb)
        ("is_integer", {}, 
         "SAFE_CAST(column AS INT) IS NOT NULL", 
         "TRY_CAST(column AS BIGINT) IS NOT NULL"),
        
        ("is_string", {}, 
         "SAFE_CAST(column AS STRING) IS NOT NULL", 
         "TRY_CAST(column AS VARCHAR) IS NOT NULL"),
        
        ("is_boolean", {}, 
         "SAFE_CAST(column AS BOOL) IS NOT NULL", 
         "TRY_CAST(column AS BOOLEAN) IS NOT NULL"),
        
        ("is_float", {}, 
         "SAFE_CAST(column AS FLOAT64) IS NOT NULL", 
         "TRY_CAST(column AS DOUBLE) IS NOT NULL"),
        
        ("is_date", {}, 
         "SAFE_CAST(column AS DATE) IS NOT NULL", 
         "TRY_CAST(column AS DATE) IS NOT NULL"),
        
        ("is_timestamp", {}, 
         "SAFE_CAST(column AS TIMESTAMP) IS NOT NULL", 
         "TRY_CAST(column AS TIMESTAMP) IS NOT NULL"),
        
        ("greater_than", {"value": 10}, 
         "column > 10", 
         "column > 10"),
        
        ("greater_or_equal_than", {"value": 10}, 
         "column >= 10", 
         "column >= 10"),
        
        ("equal", {"value": 10}, 
         "column = 10", 
         "column = 10"),
        
        ("equal", {"value": "text"}, 
         "column = 'text'", 
         "column = 'text'"),
        
        ("not_equal", {"value": 10}, 
         "column != 10", 
         "column != 10"),
        
        ("less_than", {"value": 10}, 
         "column < 10", 
         "column < 10"),
        
        ("less_or_equal_than", {"value": 10}, 
         "column <= 10", 
         "column <= 10"),
        
        ("starts_with", {"value": "prefix"}, 
         "column LIKE 'prefix%'", 
         "column LIKE 'prefix%'"),
        
        ("ends_with", {"value": "suffix"}, 
         "column LIKE '%suffix'", 
         "column LIKE '%suffix'"),
        
        ("str_contains", {"value": "middle"}, 
         "column LIKE '%middle%'", 
         "column LIKE '%middle%'"),
        
        ("regex_contains", {"value": "pattern"}, 
         "REGEXP_CONTAINS(column, r'pattern')", 
         "REGEXP_MATCHES(column, E'pattern')"),
        
        ("between", {"min": 1, "max": 10}, 
         "column BETWEEN 1 AND 10", 
         "column BETWEEN 1 AND 10"),
        
        ("is_in", {"value": [1, 2, 3]}, 
         "column IN (1, 2, 3)", 
         "column IN (1, 2, 3)"),
        
        ("is_not_in", {"value": [1, 2, 3]}, 
         "column NOT IN (1, 2, 3)", 
         "column NOT IN (1, 2, 3)")
    ]

    @pytest.mark.parametrize("check_name,params,expected_google,expected_duckdb", TEST_DATA)
    def test_sql_generation(self, check_name, params, expected_google, expected_duckdb):
        check = self.get_check(check_name)
        
        # Test GoogleSQL dialect
        google_result = check.to_sql("column", params, "GoogleSQL", False)
        assert google_result == expected_google
        
        # Test DuckDBSQL dialect
        duckdb_result = check.to_sql("column", params, "DuckDBSQL", False)
        assert duckdb_result == expected_duckdb

    # Test null handling
    def test_null_handling(self):
        check = self.get_check("is_integer")
        
        # Without null handling
        result = check.to_sql("column", {}, "GoogleSQL", False)
        assert result == "SAFE_CAST(column AS INT) IS NOT NULL"
        
        # With null handling
        result = check.to_sql("column", {}, "GoogleSQL", True)
        assert result == "SAFE_CAST(column AS INT) IS NOT NULL OR column IS NULL"

    # Test unsupported dialect
    def test_unsupported_dialect(self):
        check = self.get_check("is_integer")
        
        with pytest.raises(ValueError, match="ERROR: MySQL dialect is not supported"):
            check.to_sql("column", {}, "MySQL", False)

    # Test special cases
    def test_boolean_value_handling(self):
        check = self.get_check("equal")
        
        # Boolean true
        result = check.to_sql("column", {"value": True}, "GoogleSQL", False)
        assert result == "column = True"
        
        # Boolean false
        result = check.to_sql("column", {"value": False}, "GoogleSQL", False)
        assert result == "column = False"

    def test_float_value_handling(self):
        check = self.get_check("equal")
        
        result = check.to_sql("column", {"value": 3.14}, "GoogleSQL", False)
        assert result == "column = 3.14"