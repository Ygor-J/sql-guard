from typing import Dict, List
from sql_guard.validator.CheckBase import ValidationCheck
from sql_guard.validator.CheckImplementations import CheckRegistry

class SQLValidator:

    def __init__(self, data_rules: Dict[str, List[ValidationCheck]], sql_dialect: str = "GoogleSQL"):
        '''
        Create a SQLValidator object that can create SQL validations based on data quality rules.

        :param data_rules: Dictionary of data quality rules
        :param sql_dialect: SQL Dialect of SQL query. GoogleSQL is default.

        '''
        self.data_rules = data_rules
        self.sql_dialect = sql_dialect
        self._validate_schema()

    def _validate_schema(self):
        '''Pre-validating schema passed into SQL Validator class'''
        for column, checks in self.data_rules.items():
            if not isinstance(checks, list):
                raise ValueError(f"Invalid data rules for column {column}")
            for check in checks:
                if not isinstance(check, ValidationCheck):
                    raise ValueError(f"Invalid ValidationCheck for column {column}")


    def to_sql(self, from_source: str="your_table", wrong_values: bool = False) -> str:
        '''
        Create a sql query based on data quality rules.

        :param from_source: the origin table of the FROM clause.
        :param wrong_values: Flag for getting either the wrong or correct data.

        '''

        val_conditions = list()

        for column, rules in self.data_rules.items():
            column_conditions = list()
            for rule in rules:
                registry_obj = CheckRegistry.get_check(rule.check_name)
                sql_condition = registry_obj.to_sql(column, rule.params, self.sql_dialect, rule.ignore_nulls)
                column_conditions.append(f"({sql_condition})")

            if column_conditions:
                val_conditions.append(f"({' AND '.join(column_conditions)})")

        if wrong_values:
            sql_query = f"""

            SELECT * FROM {from_source}
            WHERE NOT ({' AND '.join(val_conditions)})

            """
            return sql_query


        sql_query = f"""

            SELECT * FROM {from_source}
            WHERE {' AND '.join(val_conditions)}

        """
        
        return sql_query
    
