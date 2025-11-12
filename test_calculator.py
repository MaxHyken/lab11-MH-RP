# https://github.com/MaxHyken/lab11-MH-RP/
# Partner 1: Max Hyken
# Partner 2: Rafael Penhas
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self): 
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-3, -4), -7)
        self.assertEqual(add(0, 0), 0)


    def test_subtract(self):
        self.assertEqual(sub(3, 4), -1)
        self.assertEqual(sub(-3, -4), 1)
        self.assertEqual(sub(5, 2), 3)

    def test_multiply(self): 
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-3, -4), 12)
        self.assertEqual(mul(-5, 4), -20)
        self.assertEqual(mul(0, 0), 0)

    def test_divide(self): 
        self.assertEqual(div(4, 8), 2)
        self.assertEqual(div(-5, 10), -2)
        self.assertEqual(div(2, 0), 0)

    def test_divide_by_zero(self): 
        with self.assertRaises(ZeroDivisionError):
            div(0, 2)

    def test_logarithm(self): 
        self.assertEqual(log(0, 2), 1)
        self.assertEqual(log(0, 10), 1)
        self.assertEqual(log(10, 1), 10)      

    def test_log_invalid_base(self): 
        with self.assertRaises(ValueError):
            log(-1, 10)
    
    
    # Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            log(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4),5)
        self.assertEqual(hypotenuse(30, 40), 50)
        self.assertEqual(hypotenuse(300, 400), 500)

    def test_sqrt(self):
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(9), 3)
        with self.assertRaises(ValueError):
            square_root(-1)
    

# Do not touch this
if __name__ == "__main__":
    unittest.main()
