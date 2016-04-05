import unittest
from currency import *
from CurrencyConverter import *

class CurrencyConverterTest(unittest.TestCase):

    four_dollars = Currency('$4')
    four_euros = Currency(4, 'EUR')
    currency_codes = ({'USD': 1.0, 'EUR': 0.88, 'JPY': 111.25})

    def test__init__(self):
        cc = CurrencyConverter(self.currency_codes)
        self.assertEqual(cc.currency_codes, {'USD': 1.0, 'EUR': 0.88, 'JPY': 111.25})

    def test_convert(self):
        converted = CurrencyConverter.convert(self, self.four_dollars, 'USD')
        self.assertEqual(converted, self.four_dollars)

        converted = CurrencyConverter.convert(self, self.four_dollars, 'EUR')
        self.assertEqual(converted, Currency(3.52, 'EUR'))

        converted = CurrencyConverter.convert(self, self.four_euros, 'USD')
        self.assertEqual(converted, Currency(4.55, 'USD'))

        converted = CurrencyConverter.convert(self, self.four_euros, 'JPY')
        self.assertEqual(converted, Currency(505.68, 'JPY'))

    def test_convert(self):
        self.assertRaises(UnknownCurrencyCodeError, CurrencyConverter.convert, self, Currency(5, 'BEF'), 'EUR')
        self.assertRaises(UnknownCurrencyCodeError, CurrencyConverter.convert, self, Currency(5, 'EUR'), 'BEF')


if __name__ == '__main__':
    unittest.main()
