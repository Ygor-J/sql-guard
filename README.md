# SQL Data Validator

A simple package for validating data using SQL. Only support for GoogleSQL at the moment.

## Problem to be Solved

I was using [Pandera](https://github.com/unionai-oss/pandera) for validating data in many tables located in BigQuery.  

The problem was that in order to validate data using Pandera, I first had to bring those tables into in-memory either Pandas, Polars or Dask DataFrames. 

But even tools like Polars or Dask face problems handling large volumes of data, for example, above 100GB (my case).

So instead of bringing that data to local memory, I thought it was just better to validate data inside BigQuery using SQL Manipulations, but in an easy way so that I can create data quality rules using Python.

## Conversion: SQL Guard x Pandera

So imagine I hava a table like below.

The ideia is to have each row as the grade of a student.  
```
name: Name of the student  
age: Age of the student  
major: Major of the student (for example, Computer Science, Electrical Engineering etc.)  
semester: Semester of university, for example 1S/2024 indicating the first semester of 2024  
course: Course, for example, Algorithms, Data Structures, Calculus I, Calculus II etc.  
grade: Grade for the course. for example: 0, 5, 10  
failed: Boolean to indicate if the student failed the course based on grade (>=5)  
```

| Name            | Age | Major            | Semester | Course      | Grade | Failed |
|-----------------|-----|------------------|----------|-------------|-------|--------|
| Daniel Carter   | 19  | Computer Science | 1S/2024  | Algorithms  | 8.5   | False  |
| Theo Hill       | 19  | Computer Science | 1S/2024  | Algorithms  | 9.0   | False  |
| Jessica Hall    | 19  | Computer Science | 1S/2024  | Algorithms  | 8.0   | False  |
| Liam Carter     | 19  | Computer Science | 1S/2024  | Algorithms  | 8.5   | False  |
| Zackary Hill    | 19  | Computer Science | 1S/2024  | Algorithms  | 7.0   | False  |


### I can either define data quality rules from scratch or use a pandera DataFrameSchema object:

From Scratch:
```
from sql_guard.validator.CheckBase import ValidationCheck


data_rules = {

    'name': [ValidationCheck(check_name='is_string',
                            params=None,
                            error_msg=None,
                            ignore_nulls=False),
            ValidationCheck(check_name='regex_contains',
                            params={'value': '^[A-Z].*'},
                            error_msg=None,
                            ignore_nulls=False)],
    'age': [ValidationCheck(check_name='is_integer',
                            params=None,
                            error_msg=None,
                            ignore_nulls=False),
            ValidationCheck(check_name='between',
                         params={'min': 15, 'max': 150},
                         error_msg=None,
                         ignore_nulls=False)]
    }
```
From Pandera:
```
import pandera as pa

pandera_schema = pa.DataFrameSchema({

    "name": pa.Column(str, checks=pa.Check.str_matches(r"^[A-Z].*")), # Starting with capital letter
    "age": pa.Column(int, checks=pa.Check.in_range(min_value=15, max_value=150)) # Age must be between 15 and 150
})
```

### I can convert DataFrameSchema to a compatible dictionary of data rules
```
from sql_guard.translators import SchemaParsers

panderaParser = SchemaParsers.SchemaParser.get_parser("pandera")
data_rules = panderaParser.parse(pandera_schema)
```

## Validating: SQL Guard x Pandera

As long as we have our `data_rules` dictionary, we can create a SQLValidator object that spits out a SQL query with your rules applied.

```
from sql_guard.validator.SQLValidator import SQLValidator

sql_schema = SQLValidator(data_rules)
validation_query = sql_schema.generate_sql_report(from_source=TABLE_PATH)

print(validation_query)
```

Given we have our query, we can just run it using BigQuery client for python.

```
from google.cloud import bigquery

query_job = client.query(validation_query)  # API request
query_result = query_job.result()  # Waits for query to finish

df = query_result.to_dataframe()

print("--------RUN_SQL_GUARD--------")
print(df.to_string())
print()
```

If result is too large, you can pass `n_wrong_counts=True` to group wrong values.
```
validation_query = sql_schema.generate_sql_report(from_source=TABLE_PATH, n_wrong_count=True)
```

## Comparison of Pandera Lazy Validation and SQL Guard Generated Report
**SQL GUARD**

| column_name | check_name | params                                             | error_msg | ignore_nulls | wrong_value            |
|-------------|------------|---------------------------------------------------|-----------|--------------|------------------------|
| course      | is_in      | {'value': ['Algorithms', 'Data Structures', 'Calculus I']} | <NA>      | False        | Calculus II            |
| course      | is_in      | {'value': ['Algorithms', 'Data Structures', 'Calculus I']} | <NA>      | False        | Circuit Analysis       |
| major       | is_in      | {'value': ['Computer Science']}                     | <NA>      | False        | Electrical Engineering |
| age         | between    | {'min': 15, 'max': 21}                             | <NA>      | False        | 22                     |

**PANDERA**
```
{
  "DATA": {
    "DATAFRAME_CHECK": [
      {
        "schema": null,
        "column": "age",
        "check": "in_range(15, 21)",
        "error": "Column 'age' failed element-wise validator number 0: in_range(15, 21) failure cases: 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22"
      },
      {
        "schema": null,
        "column": "major",
        "check": "isin(['Computer Science'])",
        "error": "Column 'major' failed element-wise validator number 0: isin(['Computer Science']) failure cases: Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering, Electrical Engineering"
      },
      {
        "schema": null,
        "column": "course",
        "check": "isin(['Algorithms', 'Data Structures', 'Calculus I'])",
        "error": "Column 'course' failed element-wise validator number 0: isin(['Algorithms', 'Data Structures', 'Calculus I']) failure cases: Calculus II, Calculus II, Calculus II, Calculus II, Calculus II, Calculus II, Calculus II, Calculus II, Calculus II, Circuit Analysis, Circuit Analysis, Circuit Analysis, Circuit Analysis, Circuit Analysis, Circuit Analysis, Circuit Analysis, Circuit Analysis, Circuit Analysis, Circuit Analysis, Circuit Analysis, Circuit Analysis, Circuit Analysis, Circuit Analysis, Circuit Analysis, Calculus II, Calculus II, Calculus II, Calculus II, Circuit Analysis, Circuit Analysis, Circuit Analysis, Circuit Analysis, Circuit Analysis, Circuit Analysis, Circuit Analysis, Circuit Analysis, Circuit Analysis, Circuit Analysis"
      }
    ]
  }
}
```

## Details

For detailed usage of package, visit `docs/` folder and take a look at two notebooks in order:
- demo.ipynb
- demo_duckdb.ipynb

## Install

Just create your virtual environment and run:  
`pip install sql-guard`



