# Part 1: assert in Python
'''
Kya hota hai assert?
assert ek testing tool hota hai jo Python mein use hota hai check lagane ke liye.

Agar condition True hai ➤ program aage chalta hai
Agar condition False hai ➤ Error (AssertionError) deta hai

syntax: assert condition, "Error message (optional)"
'''



x = 5
assert x > 0, "x must be positive"


# assert x > 6, "x is less then 6"




'''
Debug ka matlab kya hota hai?
Debugging ka matlab hai:
"Galti dhundhna aur samajhna program mein."
'''



'''
is ko run karna python -O concept/assert_debug.py (optimization mode) se hota hai na assert statement run hoti hai na hi debug message print hota hai
# agar hum ise bina -O flag ke run karte hai to debug message print hota hai

'''



# when run simple python file name to debug on hota hai and sort karva dy ga  

def my_sort(arr):
    if __debug__:
        print("Debug mode is ON!")
    else:
        print("Optimized mode: Debug OFF!")
    return sorted(arr)

print(my_sort([3, 2, 1]))

# when run with -O flag
# python -O concept/assert_debug.py
# Output: Optimized mode: Debug OFF!