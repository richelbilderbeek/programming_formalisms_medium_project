"""Test the functions in src.pfmp_richelbilderbeek.prime_solutions."""
import unittest

from src.pfmp_richelbilderbeek.prime_solutions import (
    is_prime,
)


class TestPrimeSolutions(unittest.TestCase):

    """Class to test the functions in src.pfmp_richelbilderbeek.prime_solutions."""

    def test_is_prime(self):
        """Test 'is_prime'."""
        self.assertIsNotNone(is_prime.__doc__)
        self.assertRaises(TypeError, is_prime, "I am a string")
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(11))
