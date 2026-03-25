from calculate_grade import calculate_grade

def test_calculate_grade_A():
    assert calculate_grade(95) == 'A', "Expected grade A for score 95"

def test_calculate_grade_B():
    assert calculate_grade(85) == 'B', "Expected grade B for score 85"

def test_calculate_grade_C():
    """Test grade C."""
    assert calculate_grade(75) == 'C', "Expected grade C for score 75"

def test_calculate_grade_D():
    """Test grade D."""
    assert calculate_grade(65) == 'D', "Expected grade D for score 65"

def test_calculate_grade_F():
    """Test grade F."""
    assert calculate_grade(50) == 'F', "Expected grade F for score 50"

def test_calculate_grade_below_0():
    try:
        calculate_grade(-5)
        assert False, "Expected an error for score below 0"
    except ValueError:
        pass

def test_calculate_grade_above_100():
    try:
        calculate_grade(105)
        assert False, "Expected an error for score above 100"
    except ValueError:
        pass