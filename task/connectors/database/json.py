import json
from typing import TypedDict

from ...config import JSON_DATABASE
from ...currency_converter import ConvertedPricePLN


class ConversionJson(TypedDict):
    id: int
    currency: str
    rate: float
    price_in_pln: float
    date: str


class JsonFileDatabaseConnector:
    def __init__(self) -> None:
        self._data = self._read_data()

    @staticmethod
    def _read_data(json_path: str = JSON_DATABASE) -> dict:
        try:
            with open(json_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    @staticmethod
    def _write_data(data: dict[int, ConversionJson], json_path: str = JSON_DATABASE, ) -> None:
        with open(json_path, "w") as file:
            json.dump(data, file, indent=4)

    def mapConvertedPriceToJson(self, converted_price: ConvertedPricePLN, highest_id: int) -> ConversionJson:
        return {
            "id": highest_id,
            'currency': converted_price.currency,
            'rate': converted_price.currency_rate,
            'price_in_pln': converted_price.price_in_pln,
            'date': converted_price.currency_rate_fetch_date
        }

    def find_highest_id(self) -> int:
        return int(max(self._data.keys(), default=0))

    def save(self, conversion: ConvertedPricePLN) -> None:
        highest_id = self.find_highest_id() + 1
        conversion_json = self.get_all()
        conversion_json[highest_id] = self.mapConvertedPriceToJson(conversion, highest_id)
        self._write_data(conversion_json)
        self._data = self._read_data()

    def get_all(self) -> dict[int, ConversionJson]:
        return self._data
