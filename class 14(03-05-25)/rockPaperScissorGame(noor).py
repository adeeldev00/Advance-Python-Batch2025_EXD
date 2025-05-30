import random
import sys

def rps():
    moves = ["rock", "paper", "scissors"]
    
    if len(sys.argv) != 2 or sys.argv[1].lower() not in moves:
        print("Usage: python game.py <rock|paper|scissors>")
        return
    
    user_move = sys.argv[1].lower()
    
    computer_move = random.choice(moves)
    
    if user_move == computer_move:
        result = "Tie!"
    elif (user_move == "rock" and computer_move == "scissors") or (user_move == "paper" and computer_move == "rock") or (user_move == "scissors" and computer_move == "paper"):
         result = "You win!"
    else:
        result = "Computer wins!"
    
    print(f"You: {user_move}\nComputer: {computer_move}\nResult: {result}")


rps()