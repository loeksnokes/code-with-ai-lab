from calculate_grade import calculate_grade

def test_calculate_grade_A():
    assert calculate_grade(95) == 'A', "Expected grade A for score 95"