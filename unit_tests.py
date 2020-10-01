import unittest
import random
from program import exponencial
class ProgramTestMethods(unittest.TestCase):
    def test_n_zero(self):
        """
        Test the resut when param "n" is 0 no matter what "x" value is
        """
        x = random.randint(0,100)
        self.assertEqual(exponencial(x,0),1)

    def test_n_below_zero(self):
        """
        Test the result when param "n" is below 0 no matter what "x" value is
        """
        x = random.randint(0,100)
        self.assertEqual(exponencial(x,-1),"Sorry, no numbers below zero")
    def test_x_zero(self):
        """
        Test the result when param "x" is 0 no matter what "n" value is
        """
        n = random.randint(0,10)
        self.assertEqual(exponencial(0,n),1)

unittest.main()