import unittest
import random
from program import exponencial
class ProgramTestMethods(unittest.TestCase):
    def test_n_as_string(self):
        """
        Test result when n is a number passed as a string
        """
        x = random.randint(0,100)
        exp = str(random.randint(0,100))
        self.assertEqual(factorial(x, exp), 'Please insert a valid input for n')

    def test_x_as_string(self):
        """
        Test result when x is a number passed as a string
        """
        x = str(random.randint(0,100))
        exp = random.randint(0,100)
        self.assertEqual(exponencial(x, exp), "Please insert a valid input for x")

    def test_n_null(self):
        """
        Test result when n is null
        """
        x = random.randint(0,100)
        self.assertEqual(exponencial(x, None), 'Please inser a valid input for n')

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
