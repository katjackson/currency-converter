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
        most_money_made = Currency(0, self.starting_currency)

        for key in old_currency_rates.currency_codes:
            old_amount = CurrencyConverter.convert(old_currency_rates, self.starting_currency, key)
            new_amount = CurrencyConverter.convert(new_currency_rates, self.starting_currency, key)

            money_made = new_amount - old_amount

            money_made_in_starting_currency = CurrencyConverter.convert(new_currency_rates, money_made, self.starting_currency.currency_code)

            print(old_amount)
            print(new_amount)
            print(money_made)
            print(money_made_in_starting_currency)

            if money_made_in_starting_currency > most_money_made:
                most_money_made = money_made_in_starting_currency
                return most_money_made.currency_code



april_rates = {'USD': 1.0, 'EUR': 0.87, 'JPY': 110.8, 'GBP': 0.69}
may_rates = {'USD': 1.0, 'EUR': 0.92, 'JPY': 114.11, 'GBP': 0.71}
starting_currency = Currency(50, 'USD')

ct = CurrencyTrader(april_rates, may_rates, starting_currency)
print(ct.find_best_investment())
