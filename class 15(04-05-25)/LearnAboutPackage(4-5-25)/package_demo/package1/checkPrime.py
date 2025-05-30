AUTHOR = 'M ADEEL'
BATCH = '2025'

# def myfactorial(num):
#     """Calculate factorial of a number"""
#     if num < 0:
#         return "Factorial is not defined for negative numbers"
#     elif num == 0 or num == 1:
#         return 1
#     else:
#         result = 1
#         for i in range(2, num + 1):
#             result *= i
#         return result

def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


