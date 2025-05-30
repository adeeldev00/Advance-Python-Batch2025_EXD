def fibonacci(limit):
    """Generate Fibonacci sequence up to limit"""
    a, b = 0, 1
    sequence = []
    while a <= limit:
        sequence.append(a)
        a, b = b, a + b
    return sequence
