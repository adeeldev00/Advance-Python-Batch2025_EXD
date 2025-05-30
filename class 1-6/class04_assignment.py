# Importing required module
import time

# ANSI Escape Codes for Colors
BLUE = "\033[94m"
GREEN = "\033[92m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Taking input
name = input(BLUE + "Enter your name: " + RESET)
fav_fruit = input(GREEN + "Please tell us your favorite fruit: " + RESET)

# Stylish Greeting Message
print("\n" + BOLD + "=" * 50 + RESET)
time.sleep(0.5)  # Adding a slight delay for effect
print(f"{BOLD}🌟 Hello {name}, I hope you're doing well! 🌟{RESET}")
print(f"It's wonderful to know that you love {fav_fruit}! 🍎🍌🍓")
print(BOLD + "=" * 50 + RESET)

