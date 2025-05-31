# 🐍 Python Adventure Quest

Welcome to your Python Adventure Quest! This fun learning journey will guide you through Python concepts like custom classes, special methods, debugging, assertions, and more—all wrapped up in a playful game-style format. Let’s get started!

---

## 🧭 Part 1: Build Your MiniArray (`TreasureMap`) Class

Create a class `TreasureMap` to represent a 2D map with magical behaviors, similar to a NumPy array.

### ✅ What to implement:

- `__init__`: Initialize a 2D list.
- `__getitem__`: Handle indexing, slicing, and the Ellipsis (`...`) object.
  - Use `__debug__`, `Ellipsis`, and `isinstance` inside this method.
- `__repr__`: Provide a clean string representation of the map.

### 💡 Interactive Features:

- When accessing an item:  
  `print("You discovered a chest at location (1, 2)!")`

- When slicing a row:  
  `print("You found a secret path in row 1!")`

- When accessing with Ellipsis (`map[..., 0]`):  
  `print("You unlocked the ancient vertical treasure column!")`

---

## 🎲 Part 2: Callbacks & Type Hints

Add some randomness to your quest!

- Create a function `roll_dice()` that returns a random integer from 1 to 6.
- Use `Callable[..., int]` for proper type hinting.
- Create a function `test_your_luck(callback: Callable[..., int], n: int)` to roll the dice `n` times and print results.

---

## 🤖 Part 3: NotImplemented

Understand Python’s comparison mechanics:

- Create class `Robot`:
  - In `__eq__`, return `NotImplemented` if compared with a `Human`.

- Create class `Human`:
  - In `__eq__`, return `True` if compared with a `Robot`.

This teaches how to handle unsupported operations gracefully.

---

## 🐞 Part 4: Debugging with `__debug__`

- Sprinkle `if __debug__:` print statements throughout your code.
- These hints will only appear in **normal** (non-optimized) mode.
- When running Python with `-O` (optimize), these debug prints will be skipped.

---

## 🧩 Part 5: Ellipsis Puzzle

Create a function `solve_puzzle(*args)`:

- If `Ellipsis` (`...`) is in the arguments, print:  
  `"🧩 You triggered the secret Ellipsis puzzle!"`

This reinforces handling flexible arguments and special constants.

---

## 🛡️ Part 6: Final Battle – Debugging with `assert`

Create a function `check_numbers(numbers: list[int])`:

- Use `assert` to make sure all numbers are positive.
- Also use `__debug__` to print helpful messages if something seems off.

This shows how assertions are useful for catching logic errors.

---

## 🎉 Part 7: Random Surprise Generator

Create a function `surprise_me()` that randomly prints one of these messages:

- `"🎁 You found a treasure!"`
- `"💥 A trap! Try again!"`
- `"🧙 You meet a wise wizard. He gives you +10 wisdom!"`

Use `random.choice()` to pick messages and keep the game fun!

---

## 🚀 How to Run with Debug Mode

Run normally for full debug info:
```bash
python adventure.py
