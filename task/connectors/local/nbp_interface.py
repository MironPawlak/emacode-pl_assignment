import requests

from task.connectors.local.currency_interface import Currency, CurrencyError


class NbpCurrency(Currency):

    def get_currency_value(self, currency: str) -> float:
        res = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/a/{currency}/?format=json')
        if res.status_code != 200:
            raise CurrencyError(f'Can not find {currency} on NBP servers')
        return res.json()['rates'][0]['mid']
