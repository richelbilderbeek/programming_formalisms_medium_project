"""
These are all the simple functions of The Small Project
"""

def are_numbers(x):
    """
    Determine if `x` is one or more numbers.
    Numbers can be integer or floating point
    
    Returns `True` if `x` is one or more numbers.
    """
    if not isinstance(x, list):
        return False
    if len(x) == 0:
        return False
    for e in x:
        if not is_number(e):
            return False
    return True

def are_strings(x):
    """
    Determine if `x` is one or more strings.
    
    Returns `True` if `x` is one or more strings.
    """
    if not isinstance(x, list):
        return False
    if len(x) == 0:
        return False
    for e in x:
        if not is_string(e):
            return False
    return True

def check_are_numbers(x):
    """
    Determine if `x` is one or more numbers.
    If `x` is not one or more numbers, a `RuntimeError` is raised.
    
    Returns nothing.
    """
    if not are_numbers(x):
        raise RuntimeError(
            "'x' must be numbers. ",
            "Actual value of 'x': ", x
        )


def check_different(a, b):
    """
    Determine if `a` and `b` are different.
    
    Raises `RuntimeError` when not.
    
    Returns nothing.
    """
    if a == b:
        raise RuntimeError(
            "'a' and 'b' must be different. ",
            "Value of 'a': ", a
        )

def check_equal(a, b):
    """
    Determine if `a` and `b` are equal.
    
    Raises `RuntimeError` when not.
    
    Returns nothing.
    """
    if not a == b:
        raise RuntimeError(
            "'a' and 'b' must be equal. ",
            "Value of 'a': ", a, ". ",
            "Value of 'b': ", b
        )

def check_is_number(x):
    """
    Determine if `x` is a number.
    If `x` is not a number, a `RuntimeError` is raised.
    
    Returns nothing.
    """
    if not is_number(x):
        raise RuntimeError(
            "'x' must be a number. ",
            "Actual value of 'x': ", x
        )

def check_is_probability(x):
    """
    Determine if `x` is a probability.
    If `x` is not a probability, a `RuntimeError` is raised.
    
    Returns nothing.
    """
    check_is_number(x)
    if not is_probability(x):
        raise RuntimeError(
            "'x' must be a probability. ",
            "Actual value of 'x': ", x
        )

def check_is_string(x):
    """
    Determine if `x` is a string.
    If `x` is not a string, a `RuntimeError` is raised.
    
    Returns nothing.
    """
    if not is_string(x):
        raise RuntimeError(
            "'x' must be a string. ",
            "Actual value of 'x': ", x
        )

def divide_safely(a, b):
    """
    Divide `a` by `b`.
    If `a` or `b` are not a floating point number, a `TypeError` is raised.
    If `b` is `0.0`, a `RuntimeError` is raised.
    
    Returns `a` divided by `b`
    """
    if b == 0.0:
        raise RuntimeError(
            "'b' must not be zero"
        )
    return a / b

def is_dividable_by_three(x):
    """
    Determine if `x` is dividable by three.
    If `x` is not an integer number, a `TypeError` is raised.
    
    Returns `True` if `x` is dividable by three
    """
    if not isinstance(x, int):
        raise TypeError(
            "'number' must be a number. Actual type of 'number': ", type(x) 
        )
    return x % 3 == 0

def is_even(x):
    """
    Determine if `x` is even.
    If `x` is not an integer number, a `TypeError` is raised.
    
    Returns `True` if `x` is even
    """
    if not isinstance(x, int):
        raise TypeError(
            "'number' must be a number. Actual type of 'number': ", type(x) 
        )
    return x % 2 == 0

def is_number(x):
    """
    Determine if `x` is one number,
    for example, '42' or '3.14.
    
    Returns `True` if `x` is one number
    """
    return isinstance(x, (int, float) )

def is_odd(x):
    """
    Determine if `x` is odd.
    If `x` is not an integer number, a `TypeError` is raised.
    
    Returns `True` if `x` is odd
    """
    return not is_even(x)

def is_probability(x):
    """
    Determine if `x` is a probability,
    i.e. a value between 0.0 and 1.0, including both 0.0 and 1.0.
    If `x` is not a floating point number, a `TypeError` is raised.
    
    Returns `True` if `x` is a probability
    """
    if not isinstance(x, float):
        raise TypeError(
            "'number' must be a floating point number. ",
            "Actual type of 'number': ", type(x) 
        )
    return x >= 0.0 and x <= 1.0

def is_string(x):
    """
    Determine if `x` is one string
    
    Returns `True` if `x` one string
    """
    return isinstance(x, str)

def is_zero(x):
    """
    Determine if `x` is zero.
    If `x` is not a number, a `TypeError` is raised.
    
    Returns `True` if `x` is zero
    """
    if not isinstance(x, (int, float)):
        raise TypeError(
            "'number' must be a number. ",
            "Actual type of 'number': ", type(x) 
        )
    return x == 0