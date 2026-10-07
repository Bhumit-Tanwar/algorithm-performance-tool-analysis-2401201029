def single_loop(n):
    """Sum 0..n-1 using one loop."""
    total = 0
    for i in range(n):
        total += i
    return total

def nested_loop(n):
    """Count all (i, j) pairs."""
    total = 0
    for i in range(n):
        for j in range(n):
            total += 1
    return total
