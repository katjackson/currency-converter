from currency import *
from CurrencyConverter import *

class CurrencyTrader(CurrencyConverter):

    def __init__(self, old_currency_rates, new_currency_rates, currency):
        self.old_currency_rates = old_currency_rates
        self.new_currency_rates = new_currency_rates
        self.starting_currency = currency

    def find_best_investment(self):
        old_currency_rates = CurrencyConverter(self.old_currency_rates)
        new_currency_rates = CurrencyConverter(self.new_currency_rates)

        for key in old_currency_rates.currency_codes:
            old_amount = CurrencyConverter.convert(old_currency_rates, self.starting_currency, key)
            new_amount = CurrencyConverter.convert(new_currency_rates, self.starting_currency, key)


            money_made = new_amount - old_amount

            print(type(money_made))
            money_made = Currency(money_made)
            print(money_made)

            money_made_in_starting_currency = CurrencyConverter.convert(new_currency_rates, money_made, key)
            print(old_amount.amount, old_amount.currency_code)
            print(new_amount.amount, new_amount.currency_code)
            print(money_made.amount, money_made.currency_code)

        print(old_currency_rates.currency_codes)


april_rates = {'USD': 1.0, 'EUR': 0.87, 'JPY': 110.8, 'GBP': 0.69}
may_rates = {'USD': 1.0, 'EUR': 0.92, 'JPY': 114.11, 'GBP': 0.71}
starting_currency = Currency(50, 'USD')

ct = CurrencyTrader(april_rates, may_rates, starting_currency)
print(ct.find_best_investment())
