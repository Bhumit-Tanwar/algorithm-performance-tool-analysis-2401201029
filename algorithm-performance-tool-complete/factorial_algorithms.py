def factorial_recursive(n):
    """Return n! using recursion."""
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    """Return n! using an iterative loop."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
