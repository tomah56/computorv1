import unittest

class TestPolynomialParser(unittest.TestCase):
    
    def test_basic_polynomial(self):
        expression = "-4 * X^0 + 3 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
        expected = {
            'lhs': {'X^0': -1, 'X^1': 4, 'X^2': -9.3},
            'rhs': {'X^0': 1}
        }
        result = parse_polynomial(expression)
        self.assertEqual(result, expected)
    
    def test_polynomial_with_zero_coefficients(self):
        expression = "0 * X^0 + 5 * X^1 = 5 * X^1"
        expected = {
            'lhs': {'X^0': 0, 'X^1': 5},
            'rhs': {'X^1': 5}
        }
        result = parse_polynomial(expression)
        self.assertEqual(result, expected)

    def test_polynomial_with_negative_coefficients(self):
        expression = "-2 * X^0 + 3 * X^1 - 4 * X^2 = -3 * X^0"
        expected = {
            'lhs': {'X^0': -2, 'X^1': 3, 'X^2': -4},
            'rhs': {'X^0': -3}
        }
        result = parse_polynomial(expression)
        self.assertEqual(result, expected)

    def test_polynomial_with_large_numbers(self):
        expression = "1e6 * X^0 + 2e6 * X^1 = 1e6 * X^0"
        expected = {
            'lhs': {'X^0': 1e6, 'X^1': 2e6},
            'rhs': {'X^0': 1e6}
        }
        result = parse_polynomial(expression)
        self.assertEqual(result, expected)

    def test_invalid_format(self):
        expression = "2 * X^0 + X^1 = 3 * X^0 +"
        with self.assertRaises(ValueError):
            parse_polynomial(expression)

    def test_empty_expression(self):
        expression = ""
        with self.assertRaises(ValueError):
            parse_polynomial(expression)

# Add more tests as needed

if __name__ == '__main__':
    unittest.main()
