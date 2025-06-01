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


'''
# write a decorator measure_time that prints how long a function took to run.test it on a function simulate() that waits for 2 seconds and prints "simulation done!

'''

# Time deccorator

import time

def measure_time(func):
    def wrapper():
        print("Function has start here!")
        start_time = time.time()
        
        result = func()
        
        end_time = time.time()
        print("Function end here!")
        print(f"Execution Time: {end_time - start_time:.6f} seconds")
        
        return result
    return wrapper

@measure_time
def simulate():
    time.sleep(2)
    print("Simulation done!")
simulate()





# ================================ data decoarte ===========================

'''
we create a decporator that add a  fancy border around the output of a function.

'''
def ascii_art(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  
        border_length = len(result)  
        print("*" * border_length)
        print(result)  
        print("*" * border_length)
         
    return wrapper

@ascii_art
def greet(Fullname="Adeel"):
    return f"Hello, {Fullname}!"  # return a string

greet()
greet("Ali")
greet("Sara")
greet("John Doe")
greet("Jane Smith")
greet("Alice Johnson")


