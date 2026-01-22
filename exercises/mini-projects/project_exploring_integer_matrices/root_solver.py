# Root Solver

def newton_method(f, df, x0, tol=1e-6, max_iter=100):
    """
    Find root using Newton's method
    
    Args:
        f: Function to find root of
        df: Derivative of f
        x0: Initial guess
        tol: Tolerance for convergence
        max_iter: Maximum number of iterations
        
    Returns:
        Root of the equation
    """
    x = x0
    # Apply newton's method
    return x