from typing import Dict, List, Optional


class ValidationCheck:
    pass

class SQLValidator:

    def __init__(self, data_constraints: Dict[str, List[ValidationCheck]]):
        '''
        Create a SQLValidator object that can create SQL validations based on data quality rules.

        :param data_rules: Dictionary of data quality rules

        '''
        self.data_rules = data_constraints

    def __str__(self) -> str:
        return self.data_rules

    def __repr__(self) -> str:
        return f"SQLDataSchema({self.data_rules})" 

    def to_sql(self, from_source: str='your_table') -> str:

        val_conditions = list()
        invalid_values = list()

        for column, rules in self.data_rules.items():
            column_conditions = list()
            for rule in rules:
                rule, _, value = rule.partition(':')
                if rule == 'is_integer':
                    column_conditions.append(f'SAFE_CAST({column} AS INT) IS NULL')
                elif rule == 'greater_than':
                    column_conditions.append(f"{column} <= {value}")
                elif rule == 'starts_with':
                    column_conditions.append(f"{column} NOT LIKE '{value}%'")
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
    'column_a': ['is_integer'],
    'column_b': ['is_str', 'starts_with:a'],
    'column_c': ['is_integer', 'greater_than:0']
}

myTable = SQLDataSchema(rules)

print(myTable.to_sql())