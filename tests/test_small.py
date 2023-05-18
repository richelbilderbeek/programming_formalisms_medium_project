import unittest

from src.pfmp_richelbilderbeek.small import are_numbers
from src.pfmp_richelbilderbeek.small import are_strings
from src.pfmp_richelbilderbeek.small import check_are_numbers
from src.pfmp_richelbilderbeek.small import check_different
from src.pfmp_richelbilderbeek.small import check_equal
from src.pfmp_richelbilderbeek.small import check_is_number
from src.pfmp_richelbilderbeek.small import check_is_probability
from src.pfmp_richelbilderbeek.small import check_is_string
from src.pfmp_richelbilderbeek.small import divide_safely
from src.pfmp_richelbilderbeek.small import is_dividable_by_three
from src.pfmp_richelbilderbeek.small import is_even
from src.pfmp_richelbilderbeek.small import is_number
from src.pfmp_richelbilderbeek.small import is_odd
from src.pfmp_richelbilderbeek.small import is_probability
from src.pfmp_richelbilderbeek.small import is_string
from src.pfmp_richelbilderbeek.small import is_zero



class TestSmall(unittest.TestCase):
    def test_are_numbers(self):
        self.assertIsNotNone(are_numbers.__doc__)
        self.assertFalse(are_numbers(":-/"))
        self.assertTrue(are_numbers([1, 2]))
        self.assertTrue(are_numbers([1.1]))
        self.assertFalse(are_numbers([ ]))
        self.assertFalse(are_numbers(["1.2"]))

    def test_are_strings(self):
        self.assertIsNotNone(are_strings.__doc__)
        self.assertTrue(are_strings(["A"]))
        self.assertTrue(are_strings(["A", "B"]))
        self.assertFalse(are_strings("A"))
        self.assertFalse(are_strings(3.14))
        self.assertFalse(are_strings(["A", 3.14]))
        self.assertFalse(are_strings([]))

    def test_check_are_numbers(self):
        self.assertIsNotNone(check_are_numbers.__doc__)
        check_are_numbers([3.14])
        check_are_numbers([3.14, 42])
        has_thrown = False
        try:
            check_are_numbers("A")
        except RuntimeError:
            has_thrown = True
        self.assertTrue(has_thrown)

    def test_check_different(self):
        self.assertIsNotNone(check_different.__doc__)
        check_different(1.2, 1.3)
        check_different(1.2, "A")
        
        has_thrown = False
        try:
            check_different(1.1, 1.1)
        except RuntimeError:
            has_thrown = True
        self.assertTrue(has_thrown)

        has_thrown = False
        try:
            check_different("1.1", "1.1")
        except RuntimeError:
            has_thrown = True
        self.assertTrue(has_thrown)

    def test_check_equal(self):
        self.assertIsNotNone(check_equal.__doc__)
        check_equal(1.2, 1.2)
        check_equal("A", "A")
        
        has_thrown = False
        try:
            check_equal(1.1, 1.2)
        except RuntimeError:
            has_thrown = True
        self.assertTrue(has_thrown)

        has_thrown = False
        try:
            check_equal(1.1, "1.1")
        except RuntimeError:
            has_thrown = True
        self.assertTrue(has_thrown)

    def test_check_is_number(self):
        self.assertIsNotNone(check_is_number.__doc__)
        check_is_number(1.2)
        
        has_thrown = False
        try:
            check_is_number( [1.1, 1.2] )
        except RuntimeError:
            has_thrown = True
        self.assertTrue(has_thrown)

        has_thrown = False
        try:
            check_is_number("1.1")
        except RuntimeError:
            has_thrown = True
        self.assertTrue(has_thrown)

    def test_check_is_probability(self):
        self.assertIsNotNone(check_is_probability.__doc__)
        check_is_probability(0.2)
        
        has_thrown = False
        try:
            check_is_probability( [0.1, 0.2] )
        except RuntimeError:
            has_thrown = True
        self.assertTrue(has_thrown)

        has_thrown = False
        try:
            check_is_probability("0.1")
        except RuntimeError:
            has_thrown = True
        self.assertTrue(has_thrown)

        has_thrown = False
        try:
            check_is_probability(123.456)
        except RuntimeError:
            has_thrown = True
        self.assertTrue(has_thrown)

    def test_check_is_string(self):
        self.assertIsNotNone(check_is_string.__doc__)
        check_is_string("A")
        
        has_thrown = False
        try:
            check_is_string( ["A", "B"] )
        except RuntimeError:
            has_thrown = True
        self.assertTrue(has_thrown)

        has_thrown = False
        try:
            check_is_string(3.14)
        except RuntimeError:
            has_thrown = True
        self.assertTrue(has_thrown)

    def test_divide_safely(self):
        self.assertIsNotNone(divide_safely.__doc__)
        self.assertTrue(divide_safely(1.2, 0.3) > 0.0)
        
        has_thrown = False
        try:
            divide_safely(1.1, 0.0)
        except RuntimeError:
            has_thrown = True
        self.assertTrue(has_thrown)


    def test_is_dividable_by_three(self):
        self.assertTrue(is_dividable_by_three.__doc__)
        self.assertFalse(is_dividable_by_three(2))

        has_thrown = False
        try:
            is_dividable_by_three(3.14)
        except TypeError:
            has_thrown = True
        self.assertTrue(has_thrown)

    def test_is_even(self):
        self.assertTrue(is_even.__doc__)
        self.assertFalse(is_even(1))

        has_thrown = False
        try:
            is_even(3.14)
        except TypeError:
            has_thrown = True
        self.assertTrue(has_thrown)


    def test_is_number(self):
        self.assertTrue(is_number.__doc__)
        self.assertTrue(is_number(42))
        self.assertTrue(is_number(3.14))
        self.assertFalse(is_number("a string"))

    def test_is_odd(self):
        self.assertTrue(is_odd.__doc__)
        self.assertFalse(is_odd(2))

        has_thrown = False
        try:
            is_odd(3.14)
        except TypeError:
            has_thrown = True
        self.assertTrue(has_thrown)

    def test_is_probability(self):
        self.assertTrue(is_probability.__doc__)
        self.assertTrue(is_probability(0.1))
        self.assertFalse(is_probability(1.2))
        self.assertFalse(is_probability(-1.2))
        
        has_thrown = False
        try:
            is_probability("I am a string")
        except TypeError:
            has_thrown = True
        self.assertTrue(has_thrown)

    def test_is_string(self):
        self.assertTrue(is_string("Hello"))
        self.assertFalse(is_string( { "Hello", "too much strings" } ))
        self.assertTrue(is_string.__doc__)
        

    def test_is_zero(self):
        self.assertTrue(is_zero.__doc__)
        self.assertTrue(is_zero(0))
        self.assertTrue(is_zero(0.0))
        self.assertFalse(is_zero(1))
        
        has_thrown = False
        try:
            is_zero( { 1, 2 } )
        except TypeError:
            has_thrown = True
        self.assertTrue(has_thrown)

        has_thrown = False
        try:
            is_zero("I am a string")
        except TypeError:
            has_thrown = True
        self.assertTrue(has_thrown)
