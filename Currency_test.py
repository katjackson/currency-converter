import unittest
from currency import *

class CurrencyTest(unittest.TestCase):

    four_dollars = Currency(4, 'USD')
    five_dollars = Currency(5, 'USD')
    five_euros = Currency(5, 'EUR')

    def test__init__(self):
        Currency.__init__(self, 3, 'USD')
        self.assertEqual(self.currency_code, 'USD')
        self.assertEqual(self.amount, 3)

    def test__init__(self):
        Currency.__init__(self, '$3')
        self.assertEqual(self.currency_code, 'USD')
        self.assertEqual(self.amount, 3)

    def test__init__(self):
        Currency.__init__(self, 3.5, 'USD')
        self.assertEqual(self.currency_code, 'USD')
        self.assertEqual(self.amount, 3.5)

    def test__init__(self):
        c = Currency('$3.5')
        self.assertEqual(self.currency_code, 'USD')
        self.assertEqual(self.amount, 3.5)



    def test__eq__(self):
        self.assertFalse(Currency.__eq__(four_dollars, five_dollars))
        self.assertTrue(Currency.__eq__(four_dollars, (Currency(4, 'USD'))))

    def test__ne__(self):
        self.assertTrue(Currency.__ne__(four_dollars, five_dollars))
        self.assertFalse(Currency.__ne__(four_dollars, (Currency(4, 'USD'))))
        self.assertTrue(Currency.__ne__(four_dollars, (Currency(4, 'EUR'))))

    def test__add__(self):
        result_1 = Currency.__add__((Currency(3, 'USD')), five_dollars)
        self.assertEqual(result_1, (8, 'USD'))
        self.assertEqual(five_dollars + four_dollars, (9, 'USD'))
        self.assertRaises(DifferentCurrencyCodeError, Currency.__add__, five_dollars, five_euros)

    def test__sub__(self):
        result = Currency.__sub__(five_dollars, four_dollars)
        self.assertEqual(result, (1, 'USD'))
        self.assertRaises(DifferentCurrencyCodeError, Currency.__sub__, five_dollars, five_euros)

    def test__mul__(self):
        self.assertEqual((five_dollars * 4), (20, 'USD'))


if __name__ == '__main__':
    unittest.main()
