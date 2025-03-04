from dataclasses import dataclass
from typing import Optional, Dict, List
from abc import ABC, abstractmethod

@dataclass
class ValidationCheck:
    """Base class for validation checks"""
    check_name: str
    params: dict = None
    error_msg: Optional[str] = None
    ignore_nulls: bool = False

class BaseCheck(ABC):
    """Abstract base class for all data quality checks"""
    
    @abstractmethod
    def to_sql(self, column: str, params: Dict, dialect: str) -> str:
        pass

class CheckRegistry:
    """Registry pattern for check implementations"""
    _registry = {}

    @classmethod
    def register(cls, name: str):
        def decorator(check_class):
            cls._registry[name] = check_class()
            return check_class
        return decorator

    @classmethod
    def get_check(cls, name: str) -> BaseCheck:
        return cls._registry[name]
    
    @classmethod
    def get_all_checks(cls) -> List[str]:
        """
        Returns the name of all checks registered.

        """
        return cls._registry.keys()