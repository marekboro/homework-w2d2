import unittest

# from src.calculator_test import add, divide, multiply, subtract
from src.calculator import add, divide, multiply, subtract, raise_to_power, factorial


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(5, add(2, 3))

    def test_divide(self):
        self.assertEqual(13, divide(39, 3))

    def test_multiply(self):
        self.assertEqual(15, multiply(5, 3))

    def test_subtract(self):
        self.assertEqual(11, subtract(15, 4))
    
    def test_raise_to_power(self):
        self.assertEqual(125, raise_to_power(5, 3))

    def test_factorial(self):
        self.assertEqual(120, factorial(5))