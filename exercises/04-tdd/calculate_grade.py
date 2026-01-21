def calculate_grade(score: float) -> str:
    """
    Convert a numerical score (0-100) to a letter grade.
    
    Args:
        score: The numerical score (0-100)
        
    Returns:
        Letter grade: 'A' (90-100), 'B' (80-89), 'C' (70-79), 
                      'D' (60-69), 'F' (0-59)
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