"""
This is a suite of tests for the CurrencyConverter class.
"""
import unittest
from currency import *
from CurrencyConverter import *


class CurrencyConverterTest(unittest.TestCase):

    four_dollars = Currency('$4')
    four_euros = Currency(4, 'EUR')
    currency_codes = ({'USD': 1.0, 'EUR': 0.88, 'JPY': 111.25})
    cc = CurrencyConverter(currency_codes)

    def test__init__(self):
        cc = CurrencyConverter(self.currency_codes)
        self.assertEqual(cc.currency_codes,
                         {'USD': 1.0, 'EUR': 0.88, 'JPY': 111.25})

    def test_convert_same(self):
        converted = cc.convert(self.four_dollars, 'USD')
        self.assertEqual(converted, self.four_dollars)

    def test_convert_d_to_e(self):
        converted = cc.convert(self.four_dollars, 'EUR')
        print(converted)
        self.assertEqual(converted, Currency(3.52, 'EUR'))

    def test_convert_e_to_d(self):
        converted = cc.convert(self.four_euros, 'USD')
        self.assertEqual(converted, Currency(4.55, 'USD'))

    def test_convert_e_to_j(self):
        converted = cc.convert(self.four_euros, 'JPY')
        print(converted)
        self.assertEqual(converted, Currency(505.68, 'JPY'))

    def test_convert_error(self):
        cc = CurrencyConverter(self.currency_codes)
        self.assertRaises(UnknownCurrencyCodeError, CurrencyConverter.convert,
                          cc, Currency(5, 'BEF'), 'EUR')
        self.assertRaises(UnknownCurrencyCodeError, CurrencyConverter.convert,
                          cc, Currency(5, 'EUR'), 'BEF')


if __name__ == '__main__':
    unittest.main()
