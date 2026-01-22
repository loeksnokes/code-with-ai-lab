from buggy_calc import average

def test_average_basic():
    assert average([1, 2, 4]) == 2.3333333333333335

def test_average_floats():
    assert average([1.0, 2.0, 4.0]) == 2.3333333333333335

def test_average_empty():
    assert average([]) == 0
