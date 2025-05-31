'''
What are Type Hints in Python?
Type Hints Python mein likhne ka tareeqa hai jisme hum batate hain:
“Yeh variable ya function kis type ka data expect kar raha hai.”

Yeh Python ko strongly typed language banane ka ek tareeqa hai.
Jaise: int, str, list, float, bool, etc.

'''


def add(a: int, b: int) -> int:
    return a + b



# type hint in dictionary

def student_info(data: dict[str, int]) -> None:
    for name, age in data.items():
        print(f"{name} is {age} years old.")





