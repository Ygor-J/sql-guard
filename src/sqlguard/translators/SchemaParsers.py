from abc import ABC, abstractmethod
from sqlguard.translators import PanderaMapping
from sqlguard.validator.CheckBase import ValidationCheck
import logging

class SchemaParser(ABC):
    _registry = {}

    @classmethod
    def register_parser(cls, source_type: str):
        def decorator(subclass):
            cls._registry[source_type] = subclass
            return subclass
        return decorator

    @classmethod
    def get_parser(cls, source_type: str):
        parser = cls._registry.get(source_type)
        if not parser:
            raise ValueError(f"No parser registered for {source_type}")
        return parser()

    @abstractmethod
    def parse(self, schema) -> dict:
        """Convert framework-specific schema to universal rules"""
        pass

# # statistics are the raw check constraint values that are untransformed by the check object
#https://github.com/unionai-oss/pandera/blob/main/pandera/api/base/checks.py#L98


@SchemaParser.register_parser("pandera")
class PanderaParser(SchemaParser):
    def parse(self, schema) -> dict:
        # Convert pandera DataFrameSchema to dictionary of data rules
        data_rules = dict()

        for column_name, column_obj in schema.columns.items():
            validation_checks = list() # Store built-in ValidationChecks

            # Variable for ValidationCheck constructor. Others are inside for loop
            ignore_nulls = column_obj.nullable

            # Handle Column Type

            # Validate dtype for column extrating from Pandera DataTypes which use Numpy
            dtype_check = PanderaMapping.PANDERA_NUMPY_DTYPES_MAPPING.get(column_obj.__dict__["_dtype"].type.__class__)
            if dtype_check:
                dtype_check_name = dtype_check.get("check_name")
                if dtype_check_name:
                    validation_checks.append(ValidationCheck(check_name=dtype_check_name, ignore_nulls=ignore_nulls))
                else:
                    logging.warning(f"WARNING: DTYPE MISSING: {column_obj.__dict__['_dtype'].type} is not implemented to SQL. It will be ignored.")
            else:
                logging.warning(f"WARNING: DTYPE MISSING: It was not possible to convert {column_obj.__dict__['_dtype'].type} type to SQL constraints. It will be ignored. Either some error occurred or it's not implemented.")

            # Handle Column Checks
               
            checks = column_obj.__dict__["checks"]    
            for check in checks:

                pandera_check_map = PanderaMapping.PANDERA_CHECK_MAPPING.get(check.__dict__["name"])

                if pandera_check_map:
                    
                    # Variables for ValidationCheck constructor
                    check_name = pandera_check_map["check_name"]
                    params = pandera_check_map["param_mapper"](check.__dict__["statistics"])

                    validation_checks.append(ValidationCheck(check_name=check_name, params=params, ignore_nulls=ignore_nulls))
                else:
                    logging.warning(f"WARNING: CHECK MISSING:{check.__dict__['name']} for column {column_name} doesn't exist in built-in checks! It will be ignored!")


            data_rules[column_name] = validation_checks
        return data_rules