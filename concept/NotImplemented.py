'''
What is NotImplemented in Python?
otImplemented is a special constant in Python.

It’s used in operator overloading methods like:

 - `__add__`

 - `__eq__`

 - `__mul__`

 - `__sub__`

 - etc.
    
It tells Python:

    "I don’t know how to handle this operation, maybe the other object does."

If a method like `__eq__` or `__add__` returns NotImplemented, Python will try the other side’s method.

If both sides say NotImplemented, Python raises a TypeError.




'''


class A:
    def __eq__(self, other):
        if isinstance(other, B):
            return NotImplemented  # A and B are never equal (A thinks so)
        return False  # Let other handle it
class B:
    def __eq__(self, other):
        if isinstance(other, A):
            return NotImplemented  # B thinks they are equal
        return NotImplemented
a = A()
b = B()

print(a == b)  # What happens here?
#print(b == a)

# print return flase beacuse a == equal to b 