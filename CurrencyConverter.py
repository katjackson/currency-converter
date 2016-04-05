from currency import Currency

class CurrencyConverter:
    def __init__(self, currency_codes):
        self.currency_codes = currency_codes

    def convert(self, currency_to_convert, new_currency_code):
        if currency_to_convert.currency_code == new_currency_code:
            return currency_to_convert
        if currency_to_convert.currency_code not in self.currency_codes or new_currency_code not in self.currency_codes:
            raise UnknownCurrencyCodeError
        else:
            new_amount, old_currency_code = currency_to_convert * (self.currency_codes[new_currency_code] / self.currency_codes[currency_to_convert.currency_code])
            new_object = Currency(new_amount, new_currency_code)
            return new_object

cc = CurrencyConverter({'USD': 1.0, 'EUR': 0.88, 'JPY': 111.25})


class UnknownCurrencyCodeError(Exception):
    pass
