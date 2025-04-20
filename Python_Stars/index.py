'''
This Python program is a word-based puzzle game where the player has to guess the correct word from a scrambled version. The game demonstrates the use of core Python concepts in an interactive and fun way. It is designed to reinforce topics like data structures, control flow, functions, and user input.


'''
import random

WORDS = {"python", "jumble", "scramble", "function", "tuple", "dictionary", "loop", "set", "comprehension", "variable"}

word_list = [tuple(word) for word in WORDS]

game_stats = {
    "score": 0,
    "attempts": 0,
    "correct_words": [],
    "wrong_words": []
}

def scramble(word_tuple):
    word = list(word_tuple)
    random.shuffle(word)
    return word  
def show_menu():
    print("\n🔘 Menu:")
    print("1. Play Game")
    print("2. View Stats")
    print("3. Reset Game")
    print("4. Exit")

def play_game(rounds=5):
    guessed_words = set()
    print("\n🎮 Starting the Word Scramble Game!")
    for i in range(rounds + 1):  
        word_tuple = random.choice(word_list)
        while word_tuple in guessed_words:
            continue  
        guessed_words.add(word_tuple)
        
        original_word = ''.join(word_tuple)
        scrambled = scramble(word_tuple)

        print(f"\n🔤 Scrambled Word: {scrambled}")
        guess = input("👉 Your Guess: ").strip().lower()

        game_stats["attempts"] += 1

        if guess == original_word:
            print("✅ Correct!")
            game_stats["score"] += 1
            game_stats["correct_words"].add(original_word) 
        else:
            print(f"❌ Wrong! The correct word was: {original_word}")
            game_stats["wrong_words"].add(original_word)   
def show_stats():
    print("\n📊 Game Stats:")
    print(f"• Total Attempts: {game_stats['attempts']}")
    print(f"• Score: {game_stats['score']}")
    accuracy = (game_stats['score'] / game_stats['attempts']) * 100
    print(f"• Accuracy: {accuracy:.2f}%")
    print(f"• Words Guessed Correctly: {[word for word in game_stats['correct_words']]}")
    print(f"• Words Missed: {[word for word in game_stats['wrong_words']]}")

def reset_game():
    game_stats["score"] = 0
    game_stats["attempts"] = 0
    game_stats["correct_words"].clear()
    game_stats["wrong_words"].clear()
    print("\n🔄 Game has been reset!")

def main():
    while True:
        show_menu()
        choice = input("Select an option (1-4): ").strip()
        
        if choice == "1":
            play_game()
        elif choice == "2":
            show_stats()
        elif choice == "3":
            reset_game()
        elif choice == "5": 
            print("👋 Exiting... Thanks for playing!")
            break
        else:
            print("❗ Invalid choice. Please try again.")

main()