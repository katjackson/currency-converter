from currency import Currency

class CurrencyConverter:
    def __init__(self, currency_codes):
        self.currency_codes = currency_codes

    def is_in_code_dict(self, currency_to_convert, new_currency_code):
        return currency_to_convert.currency_code in self.currency_codes and new_currency_code in self.currency_codes

    def get_currency_rate(self, currency_to_convert, new_currency_code):
        return currency_to_convert * (self.currency_codes[currency_to_convert.currency_code])

    def convert(self, currency_to_convert, new_currency_code):
        if currency_to_convert.currency_code == new_currency_code:
            return currency_to_convert
        elif not self.is_in_code_dict(currency_to_convert, new_currency_code):
            raise UnknownCurrencyCodeError
        else:
            new_object = self.get_currency_rate(currency_to_convert, new_currency_code)
            # new_object = Currency(new_amount, new_currency_code)
            return new_object

cc = CurrencyConverter({'USD': 1.0, 'EUR': 0.88, 'JPY': 111.25})


class UnknownCurrencyCodeError(Exception):
    pass
