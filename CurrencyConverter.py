class CurrencyConverter:
    def __init__(self, currency_codes):
        self.currency_codes = currency_codes

    def convert(self, currency, curency_code):
        pass


# a_code = CurrencyConverter('USD')
# print(a_code.currency_codes)
cc = CurrencyConverter({'USD': 1, 'EUR': 0.74})
print(cc.currency_codes)

cc.convert(5, 'USD')
