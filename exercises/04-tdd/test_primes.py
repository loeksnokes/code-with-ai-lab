from primes import is_prime

def test_small_primes():
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(1)

def test_composites():
    assert not is_prime(4)
    assert not is_prime(9)

def test_larger_prime():
    assert is_prime(97)
