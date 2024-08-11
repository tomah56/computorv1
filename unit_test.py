import unittest
import numpy as np
import math
from computor import computor

def assertComplexEqual(self, result, expected):
    """ Helper function to assert equality of complex numbers. """
    for r, e in zip(result, expected):
        self.assertAlmostEqual(r.real, e.real)
        self.assertAlmostEqual(r.imag, e.imag)

class TestFindRoots(unittest.TestCase):

    def test_two_real_roots(self):
        # Polynomial: 2 * X^2 - 8 * X + 6 = 0
        result = computor("2 * X^2 - 8 * X^1 + 6 * X^0 = 0")
        expected = (1.0, 3.0)
        self.assertEqual(sorted(result), sorted(expected))

    def test_one_real_root(self):
        # Polynomial: 1 * X^0 + 2 * X^1 - 1 * X^2 = 0
        # Simplified: X^2 - 2X - 1 = 0
        result = computor("1 * X^0 + 2 * X^1 - 1 * X^2 = 0")
        expected = (1 + math.sqrt(2), 1 - math.sqrt(2))
        # Compare results directly
        self.assertEqual(len(result), len(expected))  # Ensure the number of roots matches
        for r in result:
            self.assertIn(r, expected)

    def test_complex_roots(self):
        # Polynomial: 1 * X^0 + 1 * X^1 + 1 * X^2 = 0
        # Simplified: X^2 + X + 1 = 0
        result = computor("1 * X^0 + 1 * X^1 + 1 * X^2 = 0")
        expected = (complex(-0.5, math.sqrt(3)/2), complex(-0.5, -math.sqrt(3)/2))
        # Helper function to compare complex numbers
        self.assertComplexEqual(result, expected)

    def test_zero_coefficients(self):
        # Polynomial: 2 * X^2 = 0
        # Simplified: X^2 = 0
        result = computor("0 * X^0 + 0 * X^1 + 2 * X^2 = 0")
        expected = (0.0,)
        self.assertEqual(result, expected)

    def test_invalid_polynomial(self):
        with self.assertRaises(ValueError):
            computor("2 * X^3 - 4 * X^2 + 5 * X^1 = 1 * X^0")  # Not quadratic

    def assertComplexEqual(self, result, expected):
        """ Helper function to assert equality of complex numbers. """
        self.assertEqual(len(result), len(expected))
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r.real, e.real)
            self.assertAlmostEqual(r.imag, e.imag)

if __name__ == '__main__':
    unittest.main()