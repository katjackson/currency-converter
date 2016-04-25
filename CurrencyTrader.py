"""
The CurrencyTrader class is initialized with two different CurrencyConverter
objects and a starting Currency object and gives you the tools to calculate the
best investment.
"""
from currency import *
from CurrencyConverter import *


class CurrencyTrader():

    def __init__(self, old_currency_rates, new_currency_rates, currency):
        self.old_cc = old_currency_rates
        self.new_cc = new_currency_rates
        self.starting_c = currency

    # Returns the currency code of the best investment based on changing rates.
    def find_best_investment(self):
        potential = []
        for key in self.old_cc.currency_codes:
            potential.append(Currency((self.new_cc.currency_codes[key] -
                             self.old_cc.currency_codes[key]), key))

        most_money_made = 0
        best_investment = ''
        for x in potential:
            growth = self.new_cc.convert(x, self.starting_c.currency_code)
            if growth.amount > most_money_made:
                most_money_made = growth.amount
                best_investment = x.currency_code

        return best_investment


april_rates = CurrencyConverter({
                                'USD': 1.0,
                                'EUR': 0.87,
                                'JPY': 110.8,
                                'GBP': 0.69
                                })

may_rates = CurrencyConverter({
                              'USD': 1.0,
                              'EUR': 0.92,
                              'JPY': 114.11,
                              'GBP': 0.71
                              })

starting_currency = Currency(50, 'EUR')

ct = CurrencyTrader(april_rates, may_rates, starting_currency)
print(ct.find_best_investment())
