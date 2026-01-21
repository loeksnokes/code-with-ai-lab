def calculate_grade(score: float) -> str:
    """
    Convert a numerical score (0-100) to a letter grade.
    
    Args:
        score: The numerical score (0-100)
        
    Returns:
        Letter grade: 'A' [90-100], 'B' [80-90), 'C' [70-80), 
                      'D' [60-70), 'F' [0-60]
    """ 
    
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'