AUTHOR = 'M ADEEL'
BATCH = '2025'
print("Hello world")
def myfactorial(num):
    """Calculate factorial of a number"""
    if num < 0:
        return "Factorial is not defined for negative numbers"
    elif num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result

def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(limit):
    """Generate Fibonacci sequence up to limit"""
    a, b = 0, 1
    sequence = []
    while a <= limit:
        sequence.append(a)
        a, b = b, a + b
    return sequence

def reverse_string(text):
    """Reverse a string"""
    return text[::-1]

def calculate_area(shape, *args):
    """Calculate area of different shapes"""
    if shape == "circle":
        radius = args[0]
        return 3.14159 * radius * radius
    elif shape == "rectangle":
        length, width = args
        return length * width
    elif shape == "triangle":
        base, height = args
        return 0.5 * base * height
    else:
        return "Invalid shape"