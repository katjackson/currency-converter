class Currency():
    currency_symbols = {'$': 'USD', '¥': 'JPY', '€': 'EUR'}

    def __init__(self, amount, currency_code = ''):
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
        return self.currency_code == other.currency_code and self.amount == other.amount

    def __ne__(self, other):
        return self.currency_code != other.currency_code or self.amount != other.amount

    def __add__(self, other):
        if self.currency_code == other.currency_code:
            return (self.amount + other.amount), self.currency_code
        else:
            raise DifferentCurrencyCodeError()

    def __sub__(self, other):
        if self.currency_code == other.currency_code:
            return (self.amount - other.amount), self.currency_code
        else:
            raise DifferentCurrencyCodeError()

    def __mul__(self, num):
        return (self.amount * num), self.currency_code



class DifferentCurrencyCodeError(Exception):
    pass
