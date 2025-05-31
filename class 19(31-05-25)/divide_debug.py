# what should this code do ?
# This code defines a function to divide two numbers with debug mode enabled.
# If debug mode is on, it prints a debug message. It also checks if the denominator is zero and raises an assertion error if it is.


def divide(a, b):
    if __debug__:
        print("Debug Mode: ON ")

    # Assert to check denominator is not zero
    assert b != 0, " adeel say Cannot divide by zero!"

    return a / b


# Run the function
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
print("Result:", divide(num1, num2))




# example 

def average_marks(marks):
    if __debug__:
        print("Debug Mode: Checking for empty list...")

    assert len(marks) > 0, "❌ No marks provided!"

    return sum(marks) / len(marks)


marks_list = [int(x) for x in input("Enter marks separated by space: ").split()]
print("Average Marks:", average_marks(marks_list))


# example 2

