"""
This is a suite of tests for the Currency class.
"""

import unittest
from currency import *


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


if __name__ == '__main__':
    unittest.main()
