from abc import ABC, abstractmethod

from task.currency_converter import ConvertedPricePLN


class DatabaseConnector(ABC):

    @abstractmethod
    def save(self, conversion: ConvertedPricePLN) -> int:
        pass
