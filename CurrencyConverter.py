from currency import Currency

class CurrencyConverter:
    def __init__(self, currency_codes):
        self.currency_codes = currency_codes

    def convert(self, object_to_convert, new_currency_code):
        if object_to_convert.currency_code == new_currency_code:
            return object_to_convert
        else:
            new_object = object_to_convert * self.currency_codes[new_currency_code]
            return new_object

cc = CurrencyConverter({'USD': 1.0, 'EUR': 0.74, 'JPY': 120.0})
print(cc.currency_codes)

cc.convert(Currency(5, 'USD'), 'USD')
