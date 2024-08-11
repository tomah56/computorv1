import unittest
from computor import validate_input

# Assuming validate_input and the necessary imports and exceptions are defined as shown previously

class TestValidateInput(unittest.TestCase):

    def test_invalid_characters(self):
        with self.assertRaises(ValueError):
            validate_input("5 * Y^0 + 4 * X^1 = 1 * X^0")  # 'Y' is not allowed

    def test_missing_equal_sign(self):
        with self.assertRaises(SyntaxError):
            validate_input("5 * X^0 + 4 * X^1 - 9.3 * X^2")  # No '=' sign

    def test_multiple_equal_signs(self):
        with self.assertRaises(SyntaxError):
            validate_input("5 * X^0 = 4 * X^1 = 1 * X^0")  # More than one '=' sign

    def test_invalid_term_syntax(self):
        with self.assertRaises(SyntaxError):
            validate_input("5 * X^0 + 4 * X^ + 1 * X^0")  # Invalid exponent format

    def test_invalid_coefficient(self):
        with self.assertRaises(SyntaxError):
            validate_input("5 * X^0 + * X^1 = 1 * X^0")  # Missing coefficient

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            validate_input(5)  # Non-string input

    def test_correct_input(self):
        try:
            result = validate_input("5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0")
            self.assertEqual(result, "Input is valid")
        except Exception as e:
            self.fail(f"validate_input() raised {type(e).__name__} unexpectedly!")

if __name__ == '__main__':
    unittest.main()
