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
