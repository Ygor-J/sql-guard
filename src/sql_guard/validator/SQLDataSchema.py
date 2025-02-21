from typing import Dict, List, Optional
from dataclasses import dataclass

@dataclass
class ValidationCheck:
    '''Base class for validation checks'''
    check_name: str
    params: dict
    error_msg: Optional[str] = None

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


    def to_sql(self, from_source: str='your_table') -> str:

        val_conditions = list()
        invalid_values = list()

        for column, rules in self.data_rules.items():
            column_conditions = list()
            for rule in rules:
                check_name = rule.check_name
                if check_name == 'is_integer':
                    column_conditions.append(f'SAFE_CAST({column} AS INT) IS NULL')
                if check_name == 'is_string':
                    column_conditions.append(f'SAFE_CAST({column} AS STRING) IS NULL')
                if check_name == 'is_boolean':
                    column_conditions.append(f'SAFE_CAST({column} AS BOOL) IS NULL')
                if check_name == 'is_float':
                    column_conditions.append(f'SAFE_CAST({column} AS FLOAT) IS NULL')
                if check_name == 'is_date':
                    column_conditions.append(f'SAFE_CAST({column} AS DATE) IS NULL')
                if check_name == 'is_timestamp':
                    column_conditions.append(f'SAFE_CAST({column} AS TIMESTAMP) IS NULL')
                elif check_name == 'greater_than':
                    value = rule.params['value']
                    column_conditions.append(f"{column} <= {value}")
                elif check_name == 'starts_with':
                    value = rule.params['value']
                    column_conditions.append(f"{column} NOT LIKE '{value}%'")
                elif check_name == 'ends_with':
                    value = rule.params['value']
                    column_conditions.append(f"{column} NOT LIKE '%{value}'")
                elif check_name == 'str_contains':
                    value = rule.params['value']
                    column_conditions.append(f"{column} NOT LIKE '%{value}%'")
                elif check_name == 'regex_contains':
                    value = rule.params['value']
                    column_conditions.append(f"NOT REGEXP_CONTAINS({column}, '{value}'")

            if column_conditions:
                val_conditions.append(' OR '.join(column_conditions))
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
                        'There were ' || wrong_count || ' columns wrong'
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
        )
    ],
    "email": [
        ValidationCheck(
            check_name="starts_with",
            params={"value": "user_"},
            error_msg="Invalid email format"
        )
    ]
}

myTableSChema = SQLValidator(rules)

print(myTableSChema.to_sql())