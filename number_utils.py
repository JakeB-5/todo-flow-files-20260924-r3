def safe_divide(numerator, denominator, fallback=None):
    """Divide by a nonzero denominator, or return fallback for zero."""
    if denominator == 0:
        return fallback
    return numerator / denominator
