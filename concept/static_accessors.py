'''
“Static Accessors” ka matlab hota hai:
Aise functions jo class se directly access kiye jaate hain, bina object banaye.

basically there two type of static accessors in python:

1)@staticmethod

2)@classmethod


or is sy phele jo use hoty hai wo regular instance methods hoty hai


'''



'''
 _1.Static Method:_
- A method that doesn’t care about the class or the object.

- It’s like a utility function inside a class.

- Defined with @staticmethod.
'''


class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(2, 3))  



'''
###   _2.Class Method:_

 - A method that knows about the class but not about specific objects.

 - Can modify class-level data.

 - Defined with @classmethod.
'''


class Car:
    cars_made = 0

    @classmethod
    def make_car(cls):
        cls.cars_made += 1
        return f"Car #{cls.cars_made} created!"

print(Car.make_car())  
print(Car.make_car()) 


'''
| Type           | First Argument | Knows About | Used For                                |
| -------------- | -------------- | ----------- | --------------------------------------- |
| Regular Method | `self`         | Object      | Working with object data                |
| Class Method   | `cls`          | Class       | Working with class data                 |
| Static Method  | None           | Nothing     | Utility functions (math, helpers, etc.) |


'''



# ============> class methode use case <=================

'''
m ny Factory methode
me ya class methode use hota hai mean ak class behave like a differnt sceniors
'''

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    @classmethod
    def from_string(cls, info_str):
        title, pages = info_str.split(',')
        return cls(title.strip(), int(pages.strip()))

a = Book('Kiran',777)
b = Book.from_string("Python 101, 350")
print(b.title, b.pages)  # Python 101 350







# =========================================

class Donut:
    def __init__(self, flavor, size):
        self.flavor = flavor
        self.size = size

    @classmethod
    def default_donut(cls):
        return cls("Vanilla", "Medium")

    @classmethod
    def from_string(cls, donut_str):
        flavor, size = donut_str.split(", ")
        return cls(flavor, size)
# Making donuts in different ways
d1 = Donut("Chocolate", "Large")
d2 = Donut.default_donut()
d3 = Donut.from_string("Glazed, Medium")

print(d1.flavor, d1.size)  
print(d2.flavor, d2.size)  
print(d3.flavor, d3.size)  


