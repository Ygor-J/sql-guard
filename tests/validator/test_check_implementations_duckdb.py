import duckdb
import pytest
from sqlguard.validator.CheckBase import CheckRegistry

@pytest.fixture
def test_database():
    """Fixture that sets up a temporary DuckDB with test data"""
    conn = duckdb.connect(":memory:")
    
    # Create test tables with various data types
    conn.execute("""
        CREATE TABLE users (
            id INTEGER,
            name VARCHAR,
            age INTEGER,
            salary FLOAT,
            is_active BOOLEAN,
            join_date DATE,
            last_login TIMESTAMP
        );
        
        INSERT INTO users VALUES
            (1, 'Alice', 25, 75000.50, TRUE, '2020-01-15', '2023-01-01 09:30:00'),
            (2, 'Bob', 15, 45000.75, FALSE, '2021-05-20', '2023-01-02 14:15:00'),
            (3, 'Charlie', NULL, NULL, NULL, NULL, NULL),
            (4, 'David', 30, 90000.00, TRUE, '2019-11-01', '2023-01-03 08:45:00');
        
        CREATE TABLE products (
            id INTEGER,
            name VARCHAR,
            price FLOAT,
            category VARCHAR,
            in_stock BOOLEAN
        );
        
        INSERT INTO products VALUES
            (101, 'Laptop', 999.99, 'Electronics', TRUE),
            (102, 'Desk Chair', 149.99, 'Furniture', TRUE),
            (103, 'Monitor', 199.99, 'Electronics', FALSE),
            (104, 'Notebook', 4.99, 'Stationery', NULL);
    """)
    
    yield conn  # Provide connection for tests
    
    # Cleanup
    conn.close()

# Basic Type Checks
def test_is_integer_condition(test_database):
    check = CheckRegistry.get_check("is_integer")
    condition = check.to_sql("age", {}, "DuckDBSQL", False)
    
    result = test_database.execute(f"""
        SELECT name FROM users 
        WHERE {condition}
        ORDER BY id
    """).fetchall()
    
    assert result == [('Alice',), ('Bob',), ('David',)]  # Should exclude NULL (Charlie)

def test_is_string_condition(test_database):
    check = CheckRegistry.get_check("is_string")
    condition = check.to_sql("name", {}, "DuckDBSQL", False)
    
    result = test_database.execute(f"""
        SELECT id FROM users 
        WHERE {condition}
        ORDER BY id
    """).fetchall()
    
    assert result == [(1,), (2,), (3,), (4,)]  # All have valid strings

# Comparison Checks
def test_greater_than_condition(test_database):
    check = CheckRegistry.get_check("greater_than")
    condition = check.to_sql("age", {"value": 20}, "DuckDBSQL", False)
    
    result = test_database.execute(f"""
        SELECT name FROM users 
        WHERE {condition}
        ORDER BY id
    """).fetchall()
    
    assert result == [('Alice',), ('David',)]  # Ages 25 and 30

def test_between_condition(test_database):
    check = CheckRegistry.get_check("between")
    condition = check.to_sql("salary", {"min": 50000, "max": 80000}, "DuckDBSQL", False)
    
    result = test_database.execute(f"""
        SELECT name FROM users 
        WHERE {condition}
        ORDER BY id
    """).fetchall()
    
    assert result == [('Alice',)]  # Only Alice's salary is in range

# String Operations
def test_starts_with_condition(test_database):
    check = CheckRegistry.get_check("starts_with")
    condition = check.to_sql("name", {"value": "A"}, "DuckDBSQL", False)
    
    result = test_database.execute(f"""
        SELECT id FROM users 
        WHERE {condition}
    """).fetchall()
    
    assert result == [(1,)]  # Only Alice starts with 'A'

# NULL Handling Tests
def test_null_handling_with_ignore(test_database):
    check = CheckRegistry.get_check("is_integer")
    condition = check.to_sql("age", {}, "DuckDBSQL", True)  # ignore_nulls=True
    
    result = test_database.execute(f"""
        SELECT COUNT(*) FROM users 
        WHERE {condition}
    """).fetchone()[0]
    
    assert result == 4  # All rows (including NULL) pass due to ignore_nulls

def test_null_handling_without_ignore(test_database):
    check = CheckRegistry.get_check("is_integer")
    condition = check.to_sql("age", {}, "DuckDBSQL", False)  # ignore_nulls=False
    
    result = test_database.execute(f"""
        SELECT COUNT(*) FROM users 
        WHERE {condition}
    """).fetchone()[0]
    
    assert result == 3  # Only non-NULL ages

# Date/Time Tests
def test_is_date_condition(test_database):
    check = CheckRegistry.get_check("is_date")
    condition = check.to_sql("join_date", {}, "DuckDBSQL", False)
    
    result = test_database.execute(f"""
        SELECT name FROM users 
        WHERE {condition}
        ORDER BY id
    """).fetchall()
    
    assert result == [('Alice',), ('Bob',), ('David',)]  # Charlie has NULL date

# Complex Combined Conditions
def test_combined_conditions(test_database):
    age_check = CheckRegistry.get_check("greater_than")
    salary_check = CheckRegistry.get_check("greater_than")
    
    age_cond = age_check.to_sql("age", {"value": 20}, "DuckDBSQL", False)
    salary_cond = salary_check.to_sql("salary", {"value": 50000}, "DuckDBSQL", False)
    
    result = test_database.execute(f"""
        SELECT name FROM users 
        WHERE {age_cond} AND {salary_cond}
        ORDER BY id
    """).fetchall()
    
    assert result == [('Alice',), ('David',)]  # Both meet both conditions
