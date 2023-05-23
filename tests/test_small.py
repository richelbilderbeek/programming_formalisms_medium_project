"""Tests all function in src.pfmp_richelbilderbeek.small."""
import unittest

from src.pfmp_richelbilderbeek.small import (
    are_numbers,
    are_strings,
    check_are_numbers,
    check_different,
    check_equal,
    check_is_number,
    check_is_probability,
    check_is_string,
    divide_safely,
    is_dividable_by_three,
    is_even,
    is_number,
    is_odd,
    is_probability,
    is_string,
    is_zero,
)


class TestSmall(unittest.TestCase): # noqa: D101
    def test_are_numbers(self: "TestSmall"): # noqa: D102
        self.assertIsNotNone(are_numbers.__doc__)
        self.assertFalse(are_numbers(":-/"))
        self.assertTrue(are_numbers([1, 2]))
        self.assertTrue(are_numbers([1.1]))
        self.assertFalse(are_numbers([]))
        self.assertFalse(are_numbers(["1.2"]))

    def test_are_strings(self): # noqa: D102
        self.assertIsNotNone(are_strings.__doc__)
        self.assertTrue(are_strings(["A"]))
        self.assertTrue(are_strings(["A", "B"]))
        self.assertFalse(are_strings("A"))
        self.assertFalse(are_strings(3.14))
        self.assertFalse(are_strings(["A", 3.14]))
        self.assertFalse(are_strings([]))

    def test_check_are_numbers(self): # noqa: D102
        self.assertIsNotNone(check_are_numbers.__doc__)
        check_are_numbers([3.14])
        check_are_numbers([3.14, 42])
        self.assertRaises(RuntimeError, check_are_numbers, "A")

    def test_check_different(self): # noqa: D102
        self.assertIsNotNone(check_different.__doc__)
        check_different(1.2, 1.3)
        check_different(1.2, "A")
        self.assertRaises(RuntimeError, check_different, 1.1, 1.1)
        self.assertRaises(RuntimeError, check_different, "1.1", "1.1")

    def test_check_equal(self): # noqa: D102
        self.assertIsNotNone(check_equal.__doc__)
        check_equal(1.2, 1.2)
        check_equal("A", "A")
        self.assertRaises(RuntimeError, check_equal, 1.1, 2.2)
        self.assertRaises(RuntimeError, check_equal, 1.1, "1.1")

    def test_check_is_number(self): # noqa: D102
        self.assertIsNotNone(check_is_number.__doc__)
        check_is_number(1.2)
        self.assertRaises(RuntimeError, check_is_number, [1.1, 2.2])
        self.assertRaises(RuntimeError, check_is_number, "0.1")

    def test_check_is_probability(self): # noqa: D102
        self.assertIsNotNone(check_is_probability.__doc__)
        check_is_probability(0.2)
        self.assertRaises(RuntimeError, check_is_probability, [0.1, 0.2])
        self.assertRaises(RuntimeError, check_is_probability, "0.1")
        self.assertRaises(RuntimeError, check_is_probability, 123.456)

    def test_check_is_string(self): # noqa: D102
        self.assertIsNotNone(check_is_string.__doc__)
        check_is_string("A")
        self.assertRaises(RuntimeError, check_is_string, ["A", "B"])
        self.assertRaises(RuntimeError, check_is_string, 3.14)

    def test_divide_safely(self): # noqa: D102
        self.assertIsNotNone(divide_safely.__doc__)
        self.assertTrue(divide_safely(1.2, 0.3) > 0.0) # noqa: PLR2004
        self.assertRaises(RuntimeError, divide_safely, 1.1, 0.0)

    def test_is_dividable_by_three(self): # noqa: D102
        self.assertIsNotNone(is_dividable_by_three)
        self.assertFalse(is_dividable_by_three(2))
        self.assertRaises(TypeError, is_dividable_by_three, 3.14)

    def test_is_even(self): # noqa: D102
        self.assertIsNotNone(is_even.__doc__)
        self.assertFalse(is_even(1))
        self.assertRaises(TypeError, is_even, 3.14)

    def test_is_number(self): # noqa: D102
        self.assertIsNotNone(is_number.__doc__)
        self.assertTrue(is_number(42))
        self.assertTrue(is_number(3.14))
        self.assertFalse(is_number("a string"))

    def test_is_odd(self): # noqa: D102
        self.assertIsNotNone(is_odd.__doc__)
        self.assertFalse(is_odd(2))
        self.assertRaises(TypeError, is_odd, 3.14)

    def test_is_probability(self): # noqa: D102
        self.assertIsNotNone(is_probability.__doc__)
        self.assertTrue(is_probability(0.1))
        self.assertFalse(is_probability(1.2))
        self.assertFalse(is_probability(-1.2))
        self.assertRaises(TypeError, is_probability, "I am a string")

    def test_is_string(self): # noqa: D102
        self.assertIsNotNone(is_string.__doc__)
        self.assertTrue(is_string("Hello"))
        self.assertFalse(is_string({"Hello", "too much strings"}))


    def test_is_zero(self): # noqa: D102
        self.assertIsNotNone(is_zero.__doc__)
        self.assertTrue(is_zero(0))
        self.assertTrue(is_zero(0.0))
        self.assertFalse(is_zero(1))
        self.assertRaises(TypeError, is_zero, {1, 2})
        self.assertRaises(TypeError, is_zero, "I am a string")

