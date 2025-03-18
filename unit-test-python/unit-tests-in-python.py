import unittest
from unittest.mock import MagicMock
from parameterized import parameterized

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class TestCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setup TestCalculator class")
        cls.calc = Calculator()

    @classmethod
    def tearDownClass(cls):
        print("Cleanup TestCalculator class")

    @parameterized.expand([
        (2, 3, 5),
        (10, 5, 15),
        (-1, 1, 0)
    ])
    def test_addition(self, a, b, expected):
        self.assertEqual(self.calc.add(a, b), expected)

    def test_subtraction(self):
        test_cases = [(10, 5, 5), (0, 0, 0), (-5, -5, 0)]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b, expected=expected):
                self.assertEqual(self.calc.subtract(a, b), expected)

    @parameterized.expand([
        (2, 3, 6),
        (10, 5, 50),
        (-1, 1, -1)
    ])
    def test_multiplication(self, a, b, expected):
        self.assertEqual(self.calc.multiply(a, b), expected)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(self.calc.add(2, 2), 5)

    def test_mock_example(self):
        mock_calc = MagicMock()
        mock_calc.add.return_value = 10
        self.assertEqual(mock_calc.add(4, 6), 10)


if __name__ == "__main__":
    unittest.main()
