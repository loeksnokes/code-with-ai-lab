from buggy_calc import average

def test_average_basic():
    assert average([1, 2, 3]) == 2.0

def test_average_floats():
    assert average([1.0, 2.0, 3.0]) == 2.0

def test_average_empty():
    assert average([]) == 0
