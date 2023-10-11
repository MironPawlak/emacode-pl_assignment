import os
from os.path import dirname

DATA_BASE_PATH = os.path.join(dirname(dirname(os.path.realpath(__file__))), 'data')
JSON_DATABASE = os.path.join(DATA_BASE_PATH, 'database.json')
CURRENCY_RATES = os.path.join(DATA_BASE_PATH, 'example_currency_rates.json')
SQLITE_DATABASE = os.path.join(DATA_BASE_PATH, 'currency.sqlite3')
DATE_FORMAT = "%Y-%m-%d"
