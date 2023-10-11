import datetime
from dataclasses import dataclass

from task.config import DATE_FORMAT


@dataclass(frozen=True)
class ConvertedPricePLN:
    price_in_source_currency: float
    currency: str
    currency_rate: float
    currency_rate_fetch_date: str
    price_in_pln: float


class PriceCurrencyConverterToPLN:
    def convert_to_pln(self, *, currency: str, currency_rate: float,  price: float) -> ConvertedPricePLN:
        return ConvertedPricePLN(
            price,
            currency,
            currency_rate,
            datetime.datetime.today().strftime(DATE_FORMAT),
            round(currency_rate * price, 2)
        )
