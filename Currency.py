class Currency():
    def __init__(self, *args):
        for arg in args:
            try:
                arg.isalpha()
                self.currency_code = arg
            except:
                if self.is_number(arg):
                    self.amount = arg
            else:
                self.amount, self.currency_code = self.check_currency(arg)

    def check_currency(self, arg):
        if arg.startswith('$'):
            self.amount = arg.strip('$')
            self.currency_code = 'USD'
        return self.amount, self.currency_code

    def is_number(self, arg):
        try:
            float(arg)
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



four_dollars = Currency(4, 'USD')
print(four_dollars.currency_code, four_dollars.amount)
six_dollars = Currency('$6')
print(six_dollars.amount, six_dollars.currency_code)
five_dollars = Currency(5, 'USD')
print(four_dollars + five_dollars)
five_euros = Currency(5, 'EUR')
print(four_dollars * 5)

class DifferentCurrencyCodeError(Exception):
    pass
