import random

def play_game():
    score = 0
    while True:
        statements = []
        print("Enter three statements (one should be true, but don't tell which!):")
        for i in range(3):
            statement = input(f"Enter statement {i+1}: ")
            statements.append(statement)
        
        true_statement_index = random.randint(0, 2)
        
        print("\nComputer has chosen one statement as true. Here are the statements:")
        for i, stmt in enumerate(statements, 1):
            print(f"{i}. {stmt}")
        print("Which statement is true? (Enter 1, 2, or 3)")
        
        while True:
            try:
                user_guess = int(input("Your guess (1, 2, or 3): ")) - 1
                if 0 <= user_guess <= 2:
                    break
                else:
                    print("Please enter 1, 2, or 3.")
            except ValueError:
                print("Invalid input. Please enter a number (1, 2, or 3).")
        
        if user_guess == true_statement_index:
            print(f"Correct! Statement {user_guess + 1} is true.")
            score += 1
        else:
            print(f"Wrong! Statement {true_statement_index + 1} was true.")
        print(f"Your score: {score}")
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print(f"Game over! Final score: {score}")
            break

if __name__ == "__main__":
    play_game()