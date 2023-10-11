from abc import ABC, abstractmethod


class CurrencyError(Exception):
    """Raised when currency doesn't exist"""
    pass


class Currency(ABC):

    @abstractmethod
    def get_currency_value(self, currency: str) -> float:
        pass
