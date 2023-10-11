import argparse
from logging import getLogger

from task.connectors.database.json import JsonFileDatabaseConnector
from task.connectors.database.sqlalchemy import SqlFileDatabaseConnector
from task.connectors.local.json_interface import JsonCurrency
from task.connectors.local.nbp_interface import NbpCurrency
from task.currency_converter import PriceCurrencyConverterToPLN

logger = getLogger(__name__)

# try:
#
#     logger.info("Job done!")
# except Exception as err:
#     pass
CURRENCY_INPUT = {
    'json': JsonCurrency,
    'nbp': NbpCurrency,
}
DATABASE_OUTPUT = {
    'dev': JsonFileDatabaseConnector,
    'prod': SqlFileDatabaseConnector,
}

parser = argparse.ArgumentParser(description='Convert amount of currency to PLN')
parser.add_argument('amount', metavar='N', type=int, nargs=1, help='Amount of currency to convert')
parser.add_argument('currency', metavar='Str', type=str, nargs=1, help='Currency name ex. usd')
parser.add_argument('-s', '--source', default='json', choices=('json', 'nbp'), type=str,
                    help='Currency source. Default is json.')
parser.add_argument('-t', '--type', default='dev', choices=('dev', 'prod'), type=str,
                    help='The mode in which the script will run. Default is dev.')
args = parser.parse_args()
currency_value = CURRENCY_INPUT[args.source]().get_currency_value(args.currency[0])
converted_price_pln = PriceCurrencyConverterToPLN().convert_to_pln(currency=args.currency[0],
                                                                   currency_rate=currency_value, price=args.amount[0])
DATABASE_OUTPUT[args.type]().save(converted_price_pln)
