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
