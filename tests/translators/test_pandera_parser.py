from sqlguard.translators.SchemaParsers import SchemaParser
from sqlguard.validator.CheckBase import ValidationCheck
import pandera as pa
import pytest

class TestPanderaParser:
    @pytest.fixture
    def pandera_parser(self):
        return SchemaParser.get_parser("pandera")

    def test_empty(self, pandera_parser):
        pandera_schema = pa.DataFrameSchema({})
        assert pandera_parser.parse(pandera_schema) == {}

    # Test dtypes
    def test_integer_column(self, pandera_parser):
        schema = pa.DataFrameSchema({"age": pa.Column(int)})
        expected = {
            "age": [
                ValidationCheck(
                    check_name="is_integer",
                    params=None,
                    error_msg=None,
                    ignore_nulls=False
                )
            ]
        }
        assert pandera_parser.parse(schema) == expected
    
    def test_string_column(self, pandera_parser):
        schema = pa.DataFrameSchema({"name": pa.Column(str)})
        expected = {
            "name": [
                ValidationCheck(
                    check_name="is_string",
                    params=None,
                    error_msg=None,
                    ignore_nulls=False
                )
            ]
        }
        assert pandera_parser.parse(schema) == expected

    def test_float_column(self, pandera_parser):
        schema = pa.DataFrameSchema({"price": pa.Column(float)})
        expected = {
            "price": [
                ValidationCheck(
                    check_name="is_float",
                    params=None,
                    error_msg=None,
                    ignore_nulls=False
                )
            ]
        }
        assert pandera_parser.parse(schema) == expected

    def test_boolean_column(self, pandera_parser):
        schema = pa.DataFrameSchema({"active": pa.Column(bool)})
        expected = {
            "active": [
                ValidationCheck(
                    check_name="is_boolean",
                    params=None,
                    error_msg=None,
                    ignore_nulls=False
                )
            ]
        }
        assert pandera_parser.parse(schema) == expected

    def test_datetime_column(self, pandera_parser):
        schema = pa.DataFrameSchema({"created_at": pa.Column(pa.DateTime)})
        expected = {
            "created_at": [
                ValidationCheck(
                    check_name="is_date",
                    params=None,
                    error_msg=None,
                    ignore_nulls=False
                )
            ]
        }
        assert pandera_parser.parse(schema) == expected

    # Test comparison function

    def test_greater_than_check(self, pandera_parser):
        schema = pa.DataFrameSchema({
            "score": pa.Column(int, checks=pa.Check.greater_than(50))
        })
        expected = {
            "score": [
                ValidationCheck(
                    check_name="is_integer",
                    params=None,
                    error_msg=None,
                    ignore_nulls=False
                ),
                ValidationCheck(
                    check_name="greater_than",
                    params={"value": 50},
                    error_msg=None,
                    ignore_nulls=False
                )
            ]
        }
        assert pandera_parser.parse(schema) == expected

    def test_less_than_check(self, pandera_parser):
        schema = pa.DataFrameSchema({
            "temperature": pa.Column(float, checks=pa.Check.less_than(100.0))
        })
        expected = {
            "temperature": [
                ValidationCheck(
                    check_name="is_float",
                    params=None,
                    error_msg=None,
                    ignore_nulls=False
                ),
                ValidationCheck(
                    check_name="less_than",
                    params={"value": 100.0},
                    error_msg=None,
                    ignore_nulls=False
                )
            ]
        }
        assert pandera_parser.parse(schema) == expected

    def test_equal_to_check(self, pandera_parser):
        schema = pa.DataFrameSchema({
            "status": pa.Column(str, checks=pa.Check.equal_to("active"))
        })
        expected = {
            "status": [
                ValidationCheck(
                    check_name="is_string",
                    params=None,
                    error_msg=None,
                    ignore_nulls=False
                ),
                ValidationCheck(
                    check_name="equal",
                    params={"value": "active"},
                    error_msg=None,
                    ignore_nulls=False
                )
            ]
        }
        assert pandera_parser.parse(schema) == expected

    def test_in_range(self, pandera_parser):
        pandera_schema = pa.DataFrameSchema({"age": pa.Column(int, checks=pa.Check.in_range(min_value=15, max_value=150))})
        
        expected = {'age':[ValidationCheck(check_name='is_integer',
                            params=None,
                            error_msg=None,
                            ignore_nulls=False),
                        ValidationCheck(check_name='between',
                                    params={'min': 15, 'max': 150},
                                    error_msg=None,
                                    ignore_nulls=False)
                        ]
                    }
        
        assert expected == pandera_parser.parse(pandera_schema)
    
    def test_regex_contains(self, pandera_parser):
        pandera_schema = pa.DataFrameSchema({"name": pa.Column(str, checks=pa.Check.str_matches(r"^[A-Z].*"))})

        expected = {'name': [ValidationCheck(check_name='is_string',
                            params=None,
                            error_msg=None,
                            ignore_nulls=False),
            ValidationCheck(check_name='regex_contains',
                            params={'value': '^[A-Z].*'},
                            error_msg=None,
                            ignore_nulls=False)]}
        
        assert expected == pandera_parser.parse(pandera_schema)

    def test_str_contains_check(self, pandera_parser):
        schema = pa.DataFrameSchema({
            "email": pa.Column(str, checks=pa.Check.str_contains("@"))
        })
        expected = {
            "email": [
                ValidationCheck(
                    check_name="is_string",
                    params=None,
                    error_msg=None,
                    ignore_nulls=False
                ),
                ValidationCheck(
                    check_name="str_contains",
                    params={"value": "@"},
                    error_msg=None,
                    ignore_nulls=False
                )
            ]
        }
        assert pandera_parser.parse(schema) == expected
    
    def test_isin_check(self, pandera_parser):
        schema = pa.DataFrameSchema({
            "category": pa.Column(str, checks=pa.Check.isin(["A", "B", "C"]))
        })
        expected = {
            "category": [
                ValidationCheck(
                    check_name="is_string",
                    params=None,
                    error_msg=None,
                    ignore_nulls=False
                ),
                ValidationCheck(
                    check_name="is_in",
                    params={"value": ["A", "B", "C"]},
                    error_msg=None,
                    ignore_nulls=False
                )
            ]
        }
        assert pandera_parser.parse(schema) == expected

    # Others funcs

    # Nullable
    
    def test_nullable_column(self, pandera_parser):
        schema = pa.DataFrameSchema({
            "optional": pa.Column(str, nullable=True)
        })
        expected = {
            "optional": [
                ValidationCheck(
                    check_name="is_string",
                    params=None,
                    error_msg=None,
                    ignore_nulls=True
                )
            ]
        }
        assert pandera_parser.parse(schema) == expected

    # Multiples

    def test_multiple_checks(self, pandera_parser):
        schema = pa.DataFrameSchema({
            "age": pa.Column(
                int,
                checks=[
                    pa.Check.greater_than(0),
                    pa.Check.less_than(120)
                ]
            )
        })
        expected = {
            "age": [
                ValidationCheck(
                    check_name="is_integer",
                    params=None,
                    error_msg=None,
                    ignore_nulls=False
                ),
                ValidationCheck(
                    check_name="greater_than",
                    params={"value": 0},
                    error_msg=None,
                    ignore_nulls=False
                ),
                ValidationCheck(
                    check_name="less_than",
                    params={"value": 120},
                    error_msg=None,
                    ignore_nulls=False
                )
            ]
        }
        assert pandera_parser.parse(schema) == expected

    def test_multiple_columns(self, pandera_parser):
        schema = pa.DataFrameSchema({
            "id": pa.Column(int),
            "name": pa.Column(str),
            "price": pa.Column(float)
        })
        expected = {
            "id": [
                ValidationCheck(
                    check_name="is_integer",
                    params=None,
                    error_msg=None,
                    ignore_nulls=False
                )
            ],
            "name": [
                ValidationCheck(
                    check_name="is_string",
                    params=None,
                    error_msg=None,
                    ignore_nulls=False
                )
            ],
            "price": [
                ValidationCheck(
                    check_name="is_float",
                    params=None,
                    error_msg=None,
                    ignore_nulls=False
                )
            ]
        }
        assert pandera_parser.parse(schema) == expected