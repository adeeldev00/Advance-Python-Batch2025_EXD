from typing import Callable,List
import random

class TreasureMap:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return '\n'.join([' '.join(row) for row in self.data])

    def __getitem__(self, index):  # Correctly indented inside the class
        if __debug__:
            print(f"[DEBUG] Accessing index: {index}")

        if index == (..., 0):
            print("You unlocked the ancient vertical treasure column!")
            return [row[0] for row in self.data]

        elif isinstance(index, int):
            print(f"You found a secret path in row {index}!")
            return self.data[index]

        elif isinstance(index, tuple) and all(isinstance(i, int) for i in index):
            row, col = index
            if __debug__:
                print(f"[DEBUG] Accessing single item at ({row}, {col})")
            print(f"You discovered a chest at location ({row}, {col})!")
            return self.data[row][col]

        else:
            return self.data[index]
        
# ======================= Step 2 ==========================
# Step 1: Dice Roller
def roll_dice() -> int:
    return random.randint(1, 6)

# Step 2: Luck Tester
def test_your_luck(callback: Callable[..., int], N: int) -> List[int]:
    results = []
    for _ in range(N):
        results.append(callback())  # Roll dice N times
    return results




# ========================= step 3 ==========================

class Robot:
    def __eq__(self, other):
        if isinstance(other, Human):
            return NotImplemented  # "I don't know—ask the Human!"
        return super().__eq__(other)  # Default behavior (not needed here)

class Human:
    def __eq__(self, other):
        if isinstance(other, Robot):
            return True  # Humans always say robots are equal!
        return super().__eq__(other)

# Test
robot = Robot()
human = Human()



# ================================ step 4=====================


# Example Usage

map_data = [
    ["🌲", "💎", "🌲"],
    ["🌲", "🪙", "🌲"],
    ["🌲", "🌲", "👑"]
]

my_map = TreasureMap(map_data)

# Test all features in one go
print("===== FULL DEMO =====")
print("\n1. Full Map:")
print(my_map)

print("\n2. Single Row (Row 0):")
print(my_map[0])

print("\n3. Single Cell (Row 2, Column 2):")
print(my_map[2, 2])

print("\n4. First Column:")
print(my_map[..., 0])

print("\n5. Debug Check (Run without -O flag):")
print(my_map[1, 1])  # Shows debug message if __debug__ is True


luck_results = test_your_luck(roll_dice, 3)
print(luck_results)  # e.g., [4, 1, 6]


print(robot == human)  # Output: True (Python asks Human.__eq__)
print(human == robot)  # Output: True (Human.__eq__ says yes)

