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


class TestSmall(unittest.TestCase):
    def test_are_numbers(self):
        assert are_numbers.__doc__ is not None
        assert not are_numbers(":-/")
        assert are_numbers([1, 2])
        assert are_numbers([1.1])
        assert not are_numbers([])
        assert not are_numbers(["1.2"])

    def test_are_strings(self):
        assert are_strings.__doc__ is not None
        assert are_strings(["A"])
        assert are_strings(["A", "B"])
        assert not are_strings("A")
        assert not are_strings(3.14)
        assert not are_strings(["A", 3.14])
        assert not are_strings([])

    def test_check_are_numbers(self):
        assert check_are_numbers.__doc__ is not None
        check_are_numbers([3.14])
        check_are_numbers([3.14, 42])
        has_thrown = False
        try:
            check_are_numbers("A")
        except RuntimeError:
            has_thrown = True
        assert has_thrown

    def test_check_different(self):
        assert check_different.__doc__ is not None
        check_different(1.2, 1.3)
        check_different(1.2, "A")

        has_thrown = False
        try:
            check_different(1.1, 1.1)
        except RuntimeError:
            has_thrown = True
        assert has_thrown

        has_thrown = False
        try:
            check_different("1.1", "1.1")
        except RuntimeError:
            has_thrown = True
        assert has_thrown

    def test_check_equal(self):
        assert check_equal.__doc__ is not None
        check_equal(1.2, 1.2)
        check_equal("A", "A")

        has_thrown = False
        try:
            check_equal(1.1, 1.2)
        except RuntimeError:
            has_thrown = True
        assert has_thrown

        has_thrown = False
        try:
            check_equal(1.1, "1.1")
        except RuntimeError:
            has_thrown = True
        assert has_thrown

    def test_check_is_number(self):
        assert check_is_number.__doc__ is not None
        check_is_number(1.2)

        has_thrown = False
        try:
            check_is_number( [1.1, 1.2] )
        except RuntimeError:
            has_thrown = True
        assert has_thrown

        has_thrown = False
        try:
            check_is_number("1.1")
        except RuntimeError:
            has_thrown = True
        assert has_thrown

    def test_check_is_probability(self):
        assert check_is_probability.__doc__ is not None
        check_is_probability(0.2)

        has_thrown = False
        try:
            check_is_probability( [0.1, 0.2] )
        except RuntimeError:
            has_thrown = True
        assert has_thrown

        has_thrown = False
        try:
            check_is_probability("0.1")
        except RuntimeError:
            has_thrown = True
        assert has_thrown

        has_thrown = False
        try:
            check_is_probability(123.456)
        except RuntimeError:
            has_thrown = True
        assert has_thrown

    def test_check_is_string(self):
        assert check_is_string.__doc__ is not None
        check_is_string("A")

        has_thrown = False
        try:
            check_is_string( ["A", "B"] )
        except RuntimeError:
            has_thrown = True
        assert has_thrown

        has_thrown = False
        try:
            check_is_string(3.14)
        except RuntimeError:
            has_thrown = True
        assert has_thrown

    def test_divide_safely(self):
        assert divide_safely.__doc__ is not None
        assert divide_safely(1.2, 0.3) > 0.0

        has_thrown = False
        try:
            divide_safely(1.1, 0.0)
        except RuntimeError:
            has_thrown = True
        assert has_thrown


    def test_is_dividable_by_three(self):
        assert is_dividable_by_three.__doc__
        assert not is_dividable_by_three(2)

        has_thrown = False
        try:
            is_dividable_by_three(3.14)
        except TypeError:
            has_thrown = True
        assert has_thrown

    def test_is_even(self):
        assert is_even.__doc__
        assert not is_even(1)

        has_thrown = False
        try:
            is_even(3.14)
        except TypeError:
            has_thrown = True
        assert has_thrown


    def test_is_number(self):
        assert is_number.__doc__
        assert is_number(42)
        assert is_number(3.14)
        assert not is_number("a string")

    def test_is_odd(self):
        assert is_odd.__doc__
        assert not is_odd(2)

        has_thrown = False
        try:
            is_odd(3.14)
        except TypeError:
            has_thrown = True
        assert has_thrown

    def test_is_probability(self):
        assert is_probability.__doc__
        assert is_probability(0.1)
        assert not is_probability(1.2)
        assert not is_probability(-1.2)

        has_thrown = False
        try:
            is_probability("I am a string")
        except TypeError:
            has_thrown = True
        assert has_thrown

    def test_is_string(self):
        assert is_string("Hello")
        assert not is_string({"Hello", "too much strings"})
        assert is_string.__doc__


    def test_is_zero(self):
        assert is_zero.__doc__
        assert is_zero(0)
        assert is_zero(0.0)
        assert not is_zero(1)

        has_thrown = False
        try:
            is_zero( { 1, 2 } )
        except TypeError:
            has_thrown = True
        assert has_thrown

        has_thrown = False
        try:
            is_zero("I am a string")
        except TypeError:
            has_thrown = True
        assert has_thrown
