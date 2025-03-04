

def get_ignore_nulls_condition(column: str, ignore_nulls: bool) -> str:
    '''
    Create a SQL condition to ignore NULL values in a certain column.
    If ignore_nulls is False, then it returns a empty string.

    :param column: The column in which NULL values will be ignored.
    :param ignore_nulls: flag for ignoring NULL values.

    '''
    return f" OR {column} IS NULL" if ignore_nulls else ""