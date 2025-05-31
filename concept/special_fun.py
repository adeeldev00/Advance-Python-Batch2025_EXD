'''
*args (Arbitrary Positional Arguments)
Purpose: Accepts any number of positional arguments (stored in a tuple).

Use Case: When you don’t know how many arguments will be passed.


**kwargs (Arbitrary Keyword Arguments)
Purpose: Accepts any number of keyword arguments (stored in a dictionary).

Use Case: When you want to handle named arguments dynamically.


'''



def sum_numbers(*args) -> int:
    total = 0
    for num in args:
        total += num
    return total

print(sum_numbers(1, 2, 3))  # Output: 6
print(sum_numbers(10, 20))    # Output: 30




def print_user_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_user_details(name="Alice", age=25, city="New York")