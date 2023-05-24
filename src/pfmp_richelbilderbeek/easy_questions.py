"""Easy general-purpose functions.

'Easy' means:
 * a cyclomatic complexity of 1 to 4
 * no for-loops
 * maximally one variable modified

Name                          |Purpose
------------------------------|-----------------------------------------------------------------------
`is_even(x)`                  |Returns `True` if `x` is even
`is_odd(x)`                   |Returns `True` if `x` is odd
`is_probability(p)`           |Returns `True` if `p` is a probability
                              |(i.e. a chance of something happening)
`is_zero(x)`                  |Returns `True` if `x` is zero

Extra:

Name                          |Purpose
------------------------------|-----------------------------------------------------------------------
`are_numbers(x)`              |Returns `True` if `x` is zero, one or more numbers
`are_strings(x)`              |Returns `True` if `x` is zero, one or more strings
`is_dividable_by_three(x)`    |Returns `True` if `x` is dividable by 3
`is_number(x)`                |Returns `True` if `x` is a number
`is_string(x)`                |Returns `True` if `s` is a string

"""

def is_zero(x):
    """Determine if `x` is zero.

    If `x` is not a number, a `TypeError` is raised.

    Returns `True` if `x` is zero
    """
    if not isinstance(x, (int, float)):
        msg = "'number' must be a number. "
        raise TypeError(
            msg,
            "Actual type of 'number': ", type(x),
        )
    return x == 0
