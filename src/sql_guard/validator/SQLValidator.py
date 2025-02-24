from typing import Dict, List, Optional
from dataclasses import dataclass
from CheckBase import ValidationCheck
from CheckImplementations import CheckRegistry

class SQLValidator:

    def __init__(self, data_rules: Dict[str, List[ValidationCheck]], sql_dialect: str = "GoogleSQL"):
        '''
        Create a SQLValidator object that can create SQL validations based on data quality rules.

        :param data_rules: Dictionary of data quality rules
        :param sql_dialect: SQL Dialect of SQL query

        '''
        self.data_rules = data_rules
        self.sql_dialect = sql_dialect
        self._validate_schema()

    def _validate_schema(self):
        '''Pre-validating schema passed into SQL Validator class'''
        for column, checks in self.data_rules.items():
            if not isinstance(checks, list):
                raise ValueError(f"Invalid data constraints for column {column}")
            for check in checks:
                if not isinstance(check, ValidationCheck):
                    raise ValueError(f"Invalid ValidationCheck for column {column}")


    def to_sql(self, from_source: str="your_table") -> str:

        val_conditions = list()
        invalid_values = list()

        for column, rules in self.data_rules.items():
            column_conditions = list()
            for rule in rules:
                registry_obj = CheckRegistry.get_check(rule.check_name)
                sql_condition = registry_obj.to_sql(column, rule.params, "GoogleSQl")
                column_conditions.append(sql_condition)

            if column_conditions:
                val_conditions.append(" OR ".join(column_conditions))
                invalid_values.append(f"IFNULL(ARRAY_AGG(IF({' OR '.join(column_conditions)}, SAFE_CAST({column} AS STRING), NULL) IGNORE NULLS), [])")


        sql_query = f'''
            WITH validation AS (
                SELECT 
                    COUNT(*) AS wrong_count,
                    ARRAY_CONCAT({', '.join(invalid_values)}) AS wrong_values
                FROM {from_source}
                WHERE {' OR '.join(val_conditions)}
            )
            SELECT 
                CASE 
                    WHEN wrong_count > 0 THEN 
                        'There were ' || wrong_count || ' values wrong'
                    ELSE 
                        'All values are valid'
                END AS validation_result,
                wrong_values
            FROM validation;
            '''
        
        return sql_query.strip()
    

rules = {
    "age": [
        ValidationCheck(
            check_name="is_integer",
            params={},
            error_msg="Age must be an integer"
        ),
        ValidationCheck(
            check_name="greater_than",
            params={"value": 0},
            error_msg="Age must be positive"
        ),
         ValidationCheck(
            check_name="between",
            params={"min": 0, 'max': 10}
        )
    ],
    "email": [
        ValidationCheck(
            check_name="starts_with",
            params={"value": "user_"},
            error_msg="Invalid email format"
        ),
        ValidationCheck(
            check_name="regex_contains",
            params={"value": "^[^@]+@[^@]+\.[^@]+$"},
            error_msg="Invalid regex email format"
        )
    ]
}

myTableSChema = SQLValidator(rules)

print(myTableSChema.to_sql())