# buggy_calc.py — intentionally contains a bug
def average(values):
    """Return the average of numeric values. Returns 0 for empty list."""
    if not values:
        return 0
    # Bug: integer division-like behaviour
    total = sum(values)
    count = len(values)
    return total // count  # BUG: using integer division operator
