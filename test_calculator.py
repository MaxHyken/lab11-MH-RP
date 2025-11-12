import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self): 
        self.assertEqual(add(3, 4)) = 7
        self.assertEqual(add(-3, -4)) = -7
        self.assertEqual(add(0, 0)) = 0


    def test_subtract(self):
        self.assertEqual(sub(3, 4)) = -1
        self.assertEqual(sub(-3, -4)) = 1
        self.assertEqual(sub(5, 2)) = 3

    def test_multiply(self): 
        self.assertEqual(mul(3, 4)) = 12
        self.assertEqual(mul(-3, -4)) = 12
        self.assertEqual(mul(-5, 4)) = -20
        self.assertEqual(mul(0, 0)) = 0

    def test_divide(self): 
        self.assertEqual(div(8, 4)) = 2
        self.assertEqual(div(10, -5)) = -2
        self.assertEqual(div(0, 2)) = 0

    def test_divide_by_zero(self): 
        self.assertEqual(div(5, 0)) = self.assertRaises(ZeroDivisionError)

    def test_logarithm(self): 
        self.assertEqual(log(10, 2)) = 100
        self.assertEqual(log(0, 10)) = 1
        self.assertEqual(log(10, 1)) = 10       

    def test_log_invalid_base(self): 
        self.assertEqual(log(10, -1)) = self.assertRaises(ValueError)
    
    
    # Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        # fill in code

    def test_hypotenuse(self): # 3 assertions
        # fill in code

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        # fill in code
    

# Do not touch this
if __name__ == "__main__":
    unittest.main()