"""
The Currency Converter class takes a dictinary of currency codes and their
current values. Once initialized, the functions within can be used to convert
currency objects from one currency code to another.
"""
from currency import *


class CurrencyConverter:
    def __init__(self, currency_codes):
        self.currency_codes = currency_codes

    # is_in_code_dict checks if there is enough info to complete conversion
    def is_in_code_dict(self, currency_to_convert, new_currency_code):
        return (currency_to_convert.currency_code in self.currency_codes and
                new_currency_code in self.currency_codes)

    # get_currency_rate returns a float equal to the adjusted amount
    def get_currency_rate(self, currency_to_convert):
        return (currency_to_convert.amount *
                (1 / self.currency_codes[currency_to_convert.currency_code]))

    # convert returns a new currency object in the new currrency code
    def convert(self, currency_to_convert, new_currency_code):
        if currency_to_convert.currency_code == new_currency_code:
            return currency_to_convert
        elif not self.is_in_code_dict(currency_to_convert, new_currency_code):
            raise UnknownCurrencyCodeError
        else:
            new_amount = (self.get_currency_rate(currency_to_convert) *
                          self.currency_codes[new_currency_code])
            return Currency(new_amount, new_currency_code)


# cc = CurrencyConverter({'USD': 1.0, 'EUR': 0.88, 'JPY': 111.25})
# four_dollars = Currency(4, 'USD')
# print(cc.convert(four_dollars, 'EUR'))


class UnknownCurrencyCodeError(Exception):
    pass
