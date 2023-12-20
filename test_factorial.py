import unittest
from factorial import calculate_factorial

class TestFactorialFunction(unittest.TestCase):

    def test_factorial_of_zero(self):
        result = calculate_factorial(0)
        self.assertEqual(result, 1)

    def test_factorial_of_one(self):
        result = calculate_factorial(1)
        self.assertEqual(result, 1)

    def test_factorial_of_positive_integer(self):
        result = calculate_factorial(5)
        self.assertEqual(result, 120)

    def test_factorial_of_negative_integer(self):
        with self.assertRaises(ValueError):
            calculate_factorial(-3)

if __name__ == '__main__':
    unittest.main()