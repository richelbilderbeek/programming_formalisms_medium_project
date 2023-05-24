"""The functions from The Medium Project."""

def are_primes(xs):
    """Determine for each element in `xs` if it is prime.

    `xs`: a list of integers

    Returns a list of booleans with the same length as `xs`.
    Returns an empty list if `xs` is empty.
    Raises TypeError if `xs` is not a list of integers, nor an empty list.
    """
    return [is_prime(i) for i in xs]

def is_prime(x):
    """Determine if `x` is prime.

    Returns True if `x` is an integer that is prime.
    Returns False if `x` is an integer that is not prime.
    Raises a TypeError if `x` is not an integer
    """
    if not isinstance(x, int):
        message = "'x' must be an integer"
        raise TypeError(message)
    first_prime = 2
    if x < first_prime:
        return False
    return all(x % i != 0 for i in range(first_prime, x))
