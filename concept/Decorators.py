'''
Simple Meaning:
Decorator ek function hota hai jo kisi doosre function ka behavior badal deta hai, bina us function ko modify kiye.


Socho ek simple cake bana hua hai.
Ab tum us cake pe icing (cream, decorations) karte ho — cake andar se same hai, lekin bahar se naya lag raha hai!

Waise hi decorator function ko decorate karta hai — extra functionality add karta hai, bina usko badle.



decorator is apply by @


syntax:
def my_decorator(func):
    def wrapper(*args, **kwargs):
        # Do something before calling the function
        result = func(*args, **kwargs)
        # Do something after calling the function
        return result
    return wrapper

'''


def my_decorator(func):
    def wrapper(name):
        print("Function is about to be called!")
        result = func(name)
        print("Function has been called!")
        return result
    return wrapper


@my_decorator
def greet(name):
    return f"Hello, {name}!"

print(greet("Adeel"))
