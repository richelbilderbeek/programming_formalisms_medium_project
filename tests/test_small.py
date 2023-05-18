import unittest
import src.pfmp

class TestAreNumbers(unittest.TestCase):

    def test_are_numbers(self):
        self.assertIsNotNone(pfmp.are_numbers.__doc__)
        self.assertFalse(pfmp.are_numbers(":-/"))
        self.assertTrue(pfmp.are_numbers([1, 2]))
        self.assertTrue(pfmp.are_numbers([1.1]))
        self.assertFalse(pfmp.are_numbers([ ]))
        self.assertFalse(pfmp.are_numbers(["1.2"]))

def test_are_strings():
    assert are_strings.__doc__
    assert are_strings(["A"])
    assert are_strings(["A", "B"])
    assert not are_strings("A")
    assert not are_strings(3.14)
    assert not are_strings(["A", 3.14])
    assert not are_strings([])

def test_check_are_numbers():
    assert check_are_numbers.__doc__
    check_are_numbers([3.14])
    check_are_numbers([3.14, 42])
    has_thrown = False
    try:
        check_are_numbers("A")
    except RuntimeError:
        has_thrown = True
    assert has_thrown

def test_check_different():
    assert check_different.__doc__
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

def test_check_equal():
    assert check_equal.__doc__
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

def test_check_is_number():
    assert check_is_number.__doc__
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

def test_check_is_probability():
    assert check_is_probability.__doc__
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

def test_check_is_string():
    assert check_is_string.__doc__
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

def test_divide_safely():
    assert divide_safely.__doc__
    assert divide_safely(1.2, 0.3) > 0.0
    
    has_thrown = False
    try:
        divide_safely(1.1, 0.0)
    except RuntimeError:
        has_thrown = True
    assert has_thrown


def test_is_dividable_by_three():
    assert is_dividable_by_three.__doc__
    assert not is_dividable_by_three(2)

    has_thrown = False
    try:
        is_dividable_by_three(3.14)
    except TypeError:
        has_thrown = True
    assert has_thrown

def test_is_even():
    assert is_even.__doc__
    assert not is_even(1)

    has_thrown = False
    try:
        is_even(3.14)
    except TypeError:
        has_thrown = True
    assert has_thrown


def test_is_number():
    assert is_number.__doc__
    assert is_number(42)
    assert is_number(3.14)
    assert not is_number("a string")

def test_is_odd():
    assert is_odd.__doc__
    assert not is_odd(2)

    has_thrown = False
    try:
        is_odd(3.14)
    except TypeError:
        has_thrown = True
    assert has_thrown

def test_is_probability():
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

def test_is_string():
    assert is_string("Hello")
    assert not is_string( { "Hello", "too much strings" } )
    assert is_string.__doc__
    

def test_is_zero():
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
