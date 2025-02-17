def convert_rules_to_sql(rules:str):

    sql = '''
        WITH 

        your_table AS (
        SELECT 12 AS column_a
        UNION ALL
        SELECT 0 AS column_a
        UNION ALL
        SELECT -5 AS column_a
        UNION ALL
        SELECT -100 AS column_a
        UNION ALL
        SELECT 40 AS column_a
        ),

        validation AS (
            SELECT 
                COUNT(*) AS wrong_count,
                ARRAY_AGG(column_a) AS wrong_values
            FROM your_table
            WHERE 
                SAFE_CAST(column_a AS INT) IS NULL -- Not a valid integer
                OR column_a < 0                  -- Not greater than 0
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

    print(sql)

    return sql