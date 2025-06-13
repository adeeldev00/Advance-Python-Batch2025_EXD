'''
What is Callable in Python?
ak type hint hai jo batata hai:
ya function ya variable ak callable hai 


basic syntax:
Callable[[Arg1Type, Arg2Type, ...], ReturnType]





'''



from typing import Callable

def greet(name: str) -> str:
    return f"Hello {name}"

f: Callable[[str], str] = greet  # ✅ OK

print(f("Adeel"))  # Output: Hello Adeel





# example 2

from typing import Callable

def multiply(x: int, y: int) -> int:
    return x * y

def add(x:int,y:int)->int:
    return x + y

calc: Callable[[int, int], int] = multiply
calc1:Callable[[int,int],int]=add
print('exmaple 2')
print(calc(5, 3))  # Output: 15
print(calc1(4,96))




# ================= Real-life example: Callback handler ================================


from typing import Callable

def run_callback(cb: Callable[..., int]):
    print("Running...")
    result = cb()
    print("Result:", result)

def my_func() -> int:
    return 100

run_callback(my_func)



# ================= lambda function as Callable ================================

from typing import Callable

my_lambda: Callable[[int, int], int] = lambda x, y: x + y
print(my_lambda(3, 4))  # Output: 7



# ==================real-life example: Event handler ================================

from typing import Callable

def on_click(callback: Callable[[], None]):
    print("Button clicked!")
    callback()

def say_hello():
    print("Hello, Adeel!")

on_click(say_hello)





# ========================= Real-life example: Dynamic Behavior Change ================================

from typing import Callable

def apply_discount(price: float, strategy: Callable[[float], float]) -> float:
    return strategy(price)

def ten_percent(price: float) -> float:
    return price * 0.9

def fixed_discount(price: float) -> float:
    return price - 99.90

print(apply_discount(500, ten_percent))       
print(apply_discount(500, fixed_discount))    




# ========================== real-life example: sort logic ================================

from typing import Callable

def sort_students(students: list[dict], key_func: Callable[[dict], int]) -> list[dict]:
    return sorted(students, key=key_func)

students = [
    {"name": "Ali", "marks": 88},
    {"name": "Adeel", "marks": 92},
    {"name": "Ahmed", "marks": 75},
]

def sort_by_marks(student: dict) -> int:
    return student["marks"]

sorted_list = sort_students(students, sort_by_marks)
print(sorted_list)



# ========================== real life example: delay excuation ================================

from typing import Callable
import time

def schedule_task(task: Callable[[], None], delay: int):
    print(f"Task will run after {delay} seconds...")
    time.sleep(delay)
    task()

def say_hello():
    print("Hello from scheduled task!")

schedule_task(say_hello, 3)


