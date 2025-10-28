def is_prime(n: int) -> bool:
    """Return True if n is a prime number (n >= 2)."""
    # TODO: implement using simple trial division
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
