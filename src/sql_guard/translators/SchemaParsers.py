from abc import ABC, abstractmethod
from sql_guard.translators import PanderaMapping
from sql_guard.validator.CheckBase import ValidationCheck

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

        for column_name, check_obj in schema.columns.items():
            checks = check_obj.__dict__["checks"]
            column_checks = list()
            for check in checks:
                validation_checks = list()

                #print(column_name, check.__dict__["name"], check.__dict__["statistics"])

                pandera_check_map = PanderaMapping.PANDERA_CHECK_MAPPING.get(check.__dict__["name"])

                if pandera_check_map:
                    #print(pandera_check_map["check_name"], pandera_check_map["param_mapper"](check.__dict__["statistics"]))
                    column_checks.append(ValidationCheck(check_name=pandera_check_map["check_name"], params=pandera_check_map["param_mapper"](check.__dict__["statistics"])))

            data_rules[column_name] = column_checks
        return data_rules