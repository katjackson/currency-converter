import unittest
from currency import *

class CurrencyTest(unittest.TestCase):

    four_dollars = Currency(4, 'USD')
    five_dollars = Currency(5, 'USD')
    five_euros = Currency(5, 'EUR')
    twenty_dollars = Currency(20, 'USD')
    currency_symbols = {'$': 'USD', '¥': 'JPY', '€': 'EUR'}

    def test__init__(self):
        c = Currency(3, 'USD')
        self.assertEqual(c.currency_code, 'USD')
        self.assertEqual(c.amount, 3)

    def test__init__(self):
        c = Currency('$3')
        self.assertEqual(c.currency_code, 'USD')
        self.assertEqual(c.amount, 3)

    def test__init__(self):
        c = Currency(3.5, 'USD')
        self.assertEqual(c.currency_code, 'USD')
        self.assertEqual(c.amount, 3.5)

    def test__init__(self):
        c = Currency('$3.5')
        self.assertEqual(c.currency_code, 'USD')
        self.assertEqual(c.amount, 3.5)

    def test__init__(self):
        c = Currency('€3.5')
        self.assertEqual(c.currency_code, 'EUR')
        self.assertEqual(c.amount, 3.5)

    def test_check_currency(self):
        self.assertEqual(Currency.check_currency(self, '€3.5'), (3.5, 'EUR'))


    def test__eq__(self):
        self.assertFalse(Currency.__eq__(self.four_dollars, self.five_dollars))
        self.assertTrue(Currency.__eq__(self.four_dollars, (Currency(4, 'USD'))))

    def test__ne__(self):
        self.assertTrue(Currency.__ne__(self.four_dollars, self.five_dollars))
        self.assertFalse(Currency.__ne__(self.four_dollars, (Currency(4, 'USD'))))
        self.assertTrue(Currency.__ne__(self.four_dollars, (Currency(4, 'EUR'))))

    def test__add__(self):
        result_1 = Currency.__add__((Currency(3, 'USD')), self.five_dollars)
        self.assertEqual(result_1, Currency(8, 'USD'))
        self.assertEqual(type(result_1), Currency)
        self.assertEqual(self.five_dollars + self.four_dollars, Currency(9, 'USD'))
        self.assertRaises(DifferentCurrencyCodeError, Currency.__add__, self.five_dollars, self.five_euros)

    def test__sub__(self):
        result = Currency.__sub__(self.five_dollars, self.four_dollars)
        self.assertEqual(result, Currency(1, 'USD'))
        self.assertEqual(type(result), Currency)
        self.assertRaises(DifferentCurrencyCodeError, Currency.__sub__, self.five_dollars, self.five_euros)

    def test__mul__(self):
        self.assertEqual((self.five_dollars * 4), (20, 'USD'))


if __name__ == '__main__':
    unittest.main()
