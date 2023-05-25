"""Test the functions in src.pfmp_richelbilderbeek.medium_solutions."""
from random import seed
import unittest

from src.pfmp_richelbilderbeek.medium_solutions import (
    flip_coin,
    get_digits,
)

class TestMediumSolutions(unittest.TestCase):

    """Class to test the functions in src.pfmp_richelbilderbeek.medium_solutions."""

    def test_flip_coin(self):
        """Test 'flip_coin'."""
        self.assertIsNotNone(flip_coin.__doc__)
        seed(2)
        self.assertFalse(flip_coin())
        seed(5)
        self.assertTrue(flip_coin())

    def test_get_digits(self):
        """Test 'get_digits'."""
        self.assertIsNotNone(get_digits.__doc__)
        self.assertRaises(TypeError, get_digits, "evil string")
        self.assertEqual(get_digits(1), [1])
        self.assertEqual(get_digits(0), [0])
        self.assertEqual(get_digits(12), [1, 2])
        self.assertEqual(get_digits(-12), [1, 2])
