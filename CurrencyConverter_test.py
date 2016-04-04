import unittest
from currency import *
from CurrencyConverter import *

class CurrencyConverterTest(unittest.TestCase):

    four_dollars = Currency('$4')
    currency_codes = ({'USD': 1.0, 'EUR': 0.74, 'JPY': 120.0})

    def test__init__(self):
        pass

    def test_convert(self):
        self.assertEqual((CurrencyConverter.convert(self, four_dollars, 'USD')), four_dollars)
        self.assertEqual((CurrencyConverter.convert(self, four_dollars, 'EUR')), (2.96, 'EUR'))





if __name__ == '__main__':
    unittest.main()
