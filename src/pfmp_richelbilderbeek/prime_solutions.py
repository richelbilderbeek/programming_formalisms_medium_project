"""The functions from The Medium Project."""

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
