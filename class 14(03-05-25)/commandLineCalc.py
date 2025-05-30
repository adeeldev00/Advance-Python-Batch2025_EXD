import math
import sys

userInput = sys.argv
print("Input received:", userInput)

if len(userInput) < 2:
    print("Error: Please specify an operation (add/sub/mul/div/sqrt)")
    sys.exit(1)

operator = userInput[1]

if operator == 'add':
    if len(userInput) != 4:
        print("Error: Addition requires 2 numbers")
        sys.exit(1)
    result = int(userInput[2]) + int(userInput[3])
    print("The result of addition is:", result)

elif operator == 'sub':
    if len(userInput) != 4:
        print("Error: Subtraction requires 2 numbers")
        sys.exit(1)
    result = int(userInput[2]) - int(userInput[3])
    print("The result of subtraction is:", result)

elif operator == 'mul':
    if len(userInput) != 4:
        print("Error: Multiplication requires 2 numbers")
        sys.exit(1)
    result = int(userInput[2]) * int(userInput[3])
    print("The result of multiplication is:", result)

elif operator == 'div':
    if len(userInput) != 4:
        print("Error: Division requires 2 numbers")
        sys.exit(1)
    try:
        result = int(userInput[2]) / int(userInput[3])
        print("The result of division is:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")

elif operator == 'sqrt':
    if len(userInput) != 3:
        print("Error: Square root requires 1 number")
        sys.exit(1)
    num = int(userInput[2])
    if num < 0:
        print("Error: Cannot calculate square root of negative number")
    else:
        result = math.sqrt(num)
        print("The square root is:", result)

else:
    print("Error: Unknown operation. Available operations: add, sub, mul, div, sqrt")