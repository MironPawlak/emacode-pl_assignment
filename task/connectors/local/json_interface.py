import datetime
import json
from task.connectors.local.currency_interface import Currency, CurrencyError
from ...config import CURRENCY_RATES, DATE_FORMAT


class JsonCurrency(Currency):
    def __init__(self) -> None:
        self._data = self._read_data()

    @staticmethod
    def _read_data(json_path: str = CURRENCY_RATES) -> dict:
        with open(json_path, "r") as file:
            return json.load(file)

    def get_rates_list(self, currency: str) -> list:
        rate_list = self._data.get(currency.upper())
        if rate_list is None:
            raise CurrencyError(f'Can not find {currency} in json file')
        return rate_list

    def get_currency_value(self, currency: str) -> float:
        return max(self.get_rates_list(currency), key=lambda x: datetime.datetime.strptime(x['date'], DATE_FORMAT)).get(
            'rate')
