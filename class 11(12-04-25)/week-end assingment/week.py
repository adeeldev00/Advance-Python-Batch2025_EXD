'''
Build a fun and interactive text-based quiz game in Python. The program will test the
user with a set of questions, evaluate their answers, assign grades, and provide feedback using
Python fundamentals.

Concepts Covered:
1. if-else conditions
2. loops
3. lists and dictionaries
4. list comprehension & dictionary comprehension
5. user input and loops

Assignment Scenario:
You are hired to create a mini "Quiz Master" game! This game will:
1. Ask multiple questions to the player.
2. Evaluate the answers and keep a score.
3. Assign a grade at the end based on performance.
4. Show which questions were correct or incorrect.
5. Allow the player to replay the quiz if they wish.

Assignment Instructions:
Task 1: Create the Question Bank
1. Create a Python dictionary named questions.
2. Keys should be the questions (strings) and values should be the correct answers (strings).
Task 2: Build the Quiz Logic
1. Loop through each question.
2. Prompt the user for an answer using input().
3. Use if-else to check if the answer is correct.
4. Keep a score counter for correct answers.

Task 3: Grade the User
1. After the quiz ends, assign grades based on this:
Correct Answers Grade
5 A+
4 A
3 B
2 C
1 or 0 F
Use if-else statements to determine the grade and display it.
Task 4: Use List Comprehension
1. Create a list of all questions the user got wrong using list comprehension.
2. Print this list at the end.
Task 5: Use Dictionary Comprehension
1. Create a dictionary with the question as the key and Correct/Incorrect as the value
depending on the user's answers.
Task 6: Add a Replay Feature
1. After each game session, ask the user if they'd like to play again.
2. Use a while loop to allow the game to restart if the answer is "yes".

Bonus:
1. Add a timer or a random question generator for extra fun.

Deliverables:
1. .py file with your code.
2. Screenshot of the game running.
3. (Optional) Your creative twists on the game (extra features or custom messages).
'''




# Quiz Master Game

# Task 1: Create the Question Bank
questions = {
    "What is the capital of France?": "Paris",
    "Which planet is known as the Red Planet?": "Mars",
    "What is 2 + 2?": "4",
    "What is the largest mammal?": "Blue Whale",
    "What color is the sky on a clear day?": "Blue"
}

# Task 6: Add a Replay Feature
play_again = "yes"

while play_again.lower() == "yes":
    # Task 2: Build the Quiz Logic
    score = 0
    user_answers = {}
    
    for question, correct_answer in questions.items():
        print(question)
        user_answer = input("Your answer: ")
        user_answers[question] = user_answer
        
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}")
    
    # Task 3: Grade the User
    if score == 5:
        grade = "A+"
    elif score == 4:
        grade = "A"
    elif score == 3:
        grade = "B"
    elif score == 2:
        grade = "C"
    else:
        grade = "F"
    
    print(f"\nYour score: {score}/5")
    print(f"Your grade: {grade}")
    
    # Task 4: Use List Comprehension
    wrong_questions = [q for q, a in user_answers.items() if a.lower() != questions[q].lower()]
    print("\nQuestions you got wrong:")
    if wrong_questions:
        for q in wrong_questions:
            print(q)
    else:
        print("None! Great job!")
    
    # Task 5: Use Dictionary Comprehension
    results = {q: "Correct" if a.lower() == questions[q].lower() else "Incorrect" for q, a in user_answers.items()}
    print("\nQuestion Results:")
    for question, result in results.items():
        print(f"{question}: {result}")
    
    # Ask to play again
    play_again = input("\nWould you like to play again? (yes/no): ")

print("Thanks for playing Quiz Master!")