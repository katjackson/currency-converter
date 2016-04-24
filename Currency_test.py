"""
This is a suite of tests for the Currency, CurrencyConverter, and
CurrencyTrader classes.
"""

import unittest
from currency import *
from CurrencyConverter import *
from CurrencyTrader import *


class CurrencyTest(unittest.TestCase):

    four_dollars = Currency(4, 'USD')
    five_dollars = Currency(5, 'USD')
    five_euros = Currency(5, 'EUR')
    twenty_dollars = Currency(20, 'USD')
    currency_symbols = {'$': 'USD', '¥': 'JPY', '€': 'EUR'}

    def test_simple_init(self):
        c = Currency(3, 'USD')
        self.assertEqual(c.currency_code, 'USD')
        self.assertEqual(c.amount, 3)

    def test_tricky_init(self):
        c = Currency('$3')
        self.assertEqual(c.currency_code, 'USD')
        self.assertEqual(c.amount, 3)

    def test_float_init(self):
        c = Currency(3.5, 'USD')
        self.assertEqual(c.currency_code, 'USD')
        self.assertEqual(c.amount, 3.5)

    def test_float_tricky_init(self):
        c = Currency('$3.5')
        self.assertEqual(c.currency_code, 'USD')
        self.assertEqual(c.amount, 3.5)

    def test_eur_init(self):
        c = Currency('€3.5')
        self.assertEqual(c.currency_code, 'EUR')
        self.assertEqual(c.amount, 3.5)

    def test_check_currency(self):
        self.assertEqual(Currency.check_currency(self, '€3.5'), (3.5, 'EUR'))

    def test__eq__(self):
        self.assertFalse(self.four_dollars == self.five_dollars)
        self.assertTrue(self.four_dollars == (Currency(4, 'USD')))

    def test__ne__(self):
        self.assertTrue(self.four_dollars != self.five_dollars)
        self.assertFalse(self.four_dollars != (Currency(4, 'USD')))
        self.assertTrue(self.four_dollars != (Currency(4, 'EUR')))

    def test__gt__(self):
        self.assertTrue(self.five_dollars > self.four_dollars)
        self.assertFalse(self.four_dollars > self.five_dollars)
        self.assertRaises(DifferentCurrencyCodeError, Currency.__gt__,
                          self.five_euros, self.five_dollars)

    def test__lt__(self):
        self.assertTrue(self.four_dollars < self.five_dollars)
        self.assertFalse(self.five_dollars < self.four_dollars)
        self.assertRaises(DifferentCurrencyCodeError, Currency.__lt__,
                          self.four_dollars, self.five_euros)

    def test__add__(self):
        result_1 = Currency.__add__((Currency(3, 'USD')), self.five_dollars)
        self.assertEqual(result_1, Currency(8, 'USD'))
        self.assertEqual(type(result_1), Currency)
        self.assertEqual(self.five_dollars + self.four_dollars,
                         Currency(9, 'USD'))
        self.assertRaises(DifferentCurrencyCodeError, Currency.__add__,
                          self.five_dollars, self.five_euros)

    def test__sub__(self):
        result = self.five_dollars - self.four_dollars
        self.assertEqual(result, Currency(1, 'USD'))
        self.assertEqual(type(result), Currency)
        self.assertRaises(DifferentCurrencyCodeError, Currency.__sub__,
                          self.five_dollars, self.five_euros)

    def test__mul__(self):
        self.assertEqual((self.five_dollars * 4), Currency(20, 'USD'))

    def test__str__(self):
        print(self.five_dollars)
        self.assertEqual(str(self.five_dollars), '5 USD')


class CurrencyConverterTest(unittest.TestCase):

    four_dollars = Currency('$4')
    four_euros = Currency(4, 'EUR')
    currency_codes = ({'USD': 1.0, 'EUR': 0.88, 'JPY': 111.25})
    cc = CurrencyConverter(currency_codes)

    def test__init__(self):
        print('This ran inside new file')
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


class CurrencyTraderTest(unittest.TestCase):

    old_rates = {'USD': 1.0, 'EUR': 2, 'JPY': 3, 'GBP': 2}
    new_rates = {'USD': 1.0, 'EUR': 3, 'JPY': 4, 'GBP': 2.5}

    def test__init__(self):
        pass

    def test_find_best_investment(self):
        result = CurrencyTrader.find_best_investment(self.old_rates,
                                                     self.new_rates, 'USD')
        self.assertEqual(result, 'EUR')

if __name__ == '__main__':
    unittest.main()
