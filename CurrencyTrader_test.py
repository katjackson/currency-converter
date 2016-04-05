import unittest
from CurrencyTrader import *

class CurrencyTraderTest(unittest.TestCase):

    old_rates = {'USD': 1.0, 'EUR': 2, 'JPY': 3, 'GBP': 2}
    new_rates = {'USD': 1.0, 'EUR': 3, 'JPY': 4, 'GBP': 2.5}


    def test__init__(self):
        pass

    def test_find_best_investment(self):
        result = CurrencyTrader.find_best_investment(self.old_rates, self.new_rates, 'USD')
        self.assertEqual('EUR')



if __name__ == '__main__':
    unittest.main()
