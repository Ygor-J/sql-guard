from typing import Dict, List
from sqlguard.validator.CheckBase import ValidationCheck
from sqlguard.validator.CheckImplementations import CheckRegistry
import logging

class SQLValidator:

    def __init__(self, data_rules: Dict[str, List[ValidationCheck]], sql_dialect: str = "GoogleSQL"):
        '''
        Create a SQLValidator object that can create SQL validations based on data quality rules.

        :param data_rules: Dictionary of data quality rules
        :param sql_dialect: SQL Dialect of SQL query. GoogleSQL is default. Other option is DuckDBSQL.

        '''
        self.data_rules = data_rules
        if sql_dialect not in ("GoogleSQL", "DuckDBSQL"):
            logging.warning("WARNING: SQLDIALECT: Only have support for GoogleSQL so far. Default value will be set to GoogleSQL!")
            self.sql_dialect = "GoogleSQL"
        else:
            self.sql_dialect = sql_dialect
        self._validate_schema()
        self.column_sql_rules, self.data_sql_rules = self._build_sql_conditions()

    def _validate_schema(self):
        '''Pre-validating schema passed into SQL Validator class'''
        for column, checks in self.data_rules.items():
            if not isinstance(checks, list):
                raise ValueError(f"Invalid data rules for column {column}")
            for check in checks:
                if not isinstance(check, ValidationCheck):
                    raise ValueError(f"Invalid ValidationCheck for column {column}")
    
    def _build_sql_conditions(self):
        val_conditions = list()

        data_sql_rules = list()

        for column, rules in self.data_rules.items():
            column_conditions = list()
            for rule in rules:
                registry_obj = CheckRegistry.get_check(rule.check_name)
                sql_condition = registry_obj.to_sql(column, rule.params, self.sql_dialect, rule.ignore_nulls)
          
                column_conditions.append(f"({sql_condition})")
                data_sql_rules.append(tuple([column, rule.check_name, rule.params, rule.error_msg, rule.ignore_nulls, sql_condition]))

            if column_conditions:
                val_conditions.append(f"({' AND '.join(column_conditions)})")

        return val_conditions, data_sql_rules

    def generate_sql(self, from_source: str="your_table", wrong_values: bool = False) -> str:
        '''
        Create a sql query based on data quality rules to return either wrong or correct values.

        :param from_source: the origin table of the FROM clause.
        :param wrong_values: Flag for getting either the wrong or correct data.

        '''

        if wrong_values:
            sql_query = f"""

            SELECT * FROM {from_source}
            WHERE NOT ({' AND '.join(self.column_sql_rules)})

            """
            return sql_query.strip()


        sql_query = f"""

            SELECT * FROM {from_source}
            WHERE {' AND '.join(self.column_sql_rules)}

        """
        
        return sql_query.strip()
    
    def generate_sql_report(self, from_source: str = "your_table", n_wrong_values: bool = False) -> str:
        '''
        Generate a SQL query that returns a report of failed validation checks.

        :param from_source: The origin table of the FROM clause.
        :param n_wrong_values: Flag for getting number of wrong values instead of the actual values.
        '''
        union_queries = []

        cast_function = "SAFE_CAST" if self.sql_dialect == "GoogleSQL" else "TRY_CAST"
        cast_type_wrong_value = "STRING" if self.sql_dialect == "GoogleSQL" else "VARCHAR"

        for column, check_name, params, error_msg, ignore_nulls, sql_condition in self.data_sql_rules:

            if self.sql_dialect == "GoogleSQL":
                _params = "NULL" if params is None else f"\"{params}\""
            else:
                if params is None:
                    _params = "NULL"
                else:
                    params = str(params).replace("'", "\"")
                    _params = "NULL" if params is None else f"'{params}'"

            _error_msg = "NULL" if error_msg is None else error_msg

            query = f"""
                SELECT
                    '{column}' AS column_name,
                    '{check_name}' AS check_name,
                    {_params} AS params,
                    {_error_msg} AS error_msg,
                    {ignore_nulls} AS ignore_nulls,
                    {cast_function}({column} AS {cast_type_wrong_value}) AS wrong_value
                FROM {from_source}
                WHERE NOT ({sql_condition})
            """
            union_queries.append(query)

        union_query = "\nUNION ALL\n".join(union_queries)

        if n_wrong_values:
            sql_query = f"""

            WITH

            tb AS (

                {union_query}

            )

            SELECT column_name, check_name, params, error_msg, ignore_nulls, COUNT(wrong_value) AS n_wrong_values FROM tb
            GROUP BY ALL

            """

            return sql_query.strip()

        sql_query = f"""

        WITH

        tb AS (

            {union_query}

        )

        SELECT DISTINCT * FROM tb

        """

        return sql_query.strip()
    

        


