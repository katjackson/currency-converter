class Currency():
    def __init__(self, amount, currency_code):
        self.amount = amount
        self.currency_code = currency_code

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


four_dollars = Currency(4, 'USD')
print(four_dollars.currency_code, four_dollars.amount)
five_dollars = Currency(5, 'USD')
print(four_dollars + five_dollars)
five_euros = Currency(5, 'Euros')
print(four_dollars * 5)

class DifferentCurrencyCodeError(Exception):
    pass
