
"""
The Currency class holds amount and currency_code as attributes for currency
objects. Standard dunder functions have been overwritten to allow currency
objects to interact with each other as expected.
"""


class Currency():
    currency_symbols = {'$': 'USD', '¥': 'JPY', '€': 'EUR'}

    """
    A currency object is initialized with an amount and a currency code. If a
    currency code is supplied in the format (amount, currency_code) (4, USD),
    these attributes are automatically set. If a single argument is supplied
    ('$4'), the internal function check_currency is used to strip the amount
    from the currency and determine the proper code.
    """

    def __init__(self, amount, currency_code=''):
        self.currency_code = currency_code
        if self.is_number(amount):
                self.amount = round(amount, 2)
        else:
            self.amount, self.currency_code = self.check_currency(amount)

    def check_currency(self, amount):
        for key in self.currency_symbols:
            if amount.startswith(key):
                self.amount = float(amount.strip(key))
                return self.amount, self.currency_symbols[key]

    def is_number(self, amount):
        try:
            float(amount)
            return True
        except:
            return False

    def __eq__(self, other):
        return (self.currency_code == other.currency_code and
                self.amount == other.amount)

    def __ne__(self, other):
        return (self.currency_code != other.currency_code or
                self.amount != other.amount)

    def __gt__(self, other):
        if self.currency_code == other.currency_code:
            return self.amount > other.amount
        else:
            raise DifferentCurrencyCodeError()

    def __lt__(self, other):
        if self.currency_code == other.currency_code:
            return self.amount < other.amount
        else:
            raise DifferentCurrencyCodeError()

    def __add__(self, other):
        if self.currency_code == other.currency_code:
            return Currency((self.amount + other.amount), self.currency_code)
        else:
            raise DifferentCurrencyCodeError()

    def __sub__(self, other):
        if self.currency_code == other.currency_code:
            return Currency((self.amount - other.amount), self.currency_code)
        else:
            raise DifferentCurrencyCodeError()

    def __mul__(self, num):
        return Currency((self.amount * num), self.currency_code)

    def __str__(self):
        return str(self.amount) + ' ' + self.currency_code


class DifferentCurrencyCodeError(Exception):
    pass
