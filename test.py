from sql_guard.validator.SQLValidator import SQLValidator
from sql_guard.validator.CheckBase import ValidationCheck

rules = {
    "age": [
        ValidationCheck(
            check_name="is_integer",
            params={},
            error_msg="Age must be an integer",
            ignore_nulls=True
        ),
        ValidationCheck(
            check_name="greater_or_equal_than",
            params={"value": 18},
            error_msg="Age must be over 18",
            ignore_nulls=True
        )
    ],
    "name": [
        ValidationCheck(
            check_name="is_in",
            params={"value": ['Joseph', 'Mario', 'user_Flash', 'user_Superman']},
            error_msg="Invalid name format"
        )
    ]
}

myTableSChema = SQLValidator(rules)

print(myTableSChema.to_sql(wrong_values=False))