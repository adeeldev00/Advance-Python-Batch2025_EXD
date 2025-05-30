# # Error Version (with comments explaining issues)
# # def process_data(data_list, config):
# #     results = {}
    
# #     # ❌ Error: 'len(data_list)' needs to be wrapped inside 'range()'
# #     for i in len(data_list):  # ❌
# #         item = data_list[i]

# #         # ❌ SyntaxError: missing colon ':'
# #         if item['value'] > 100 or item['value'] < 0  # ❌
# #             results[item['id']] = "Invalid"

# #         # ❌ '=' used instead of '==' for comparison
# #         elif item['value'] = 50:  # ❌
# #             # ❌ Used '==' instead of '=' for assignment
# #             results[item['id']] == "Perfect"  # ❌

# #         else:
# #             # ❌ Dictionary object does not have 'append', should use 'results[item["id"]] = value'
# #             results.append(item['value'])  # ❌

# #     # ❌ Using fixed range 'while j < 10' instead of iterating actual list length
# #     j = 0
# #     while j < 10:
# #         if data_list[j]['status']:
# #             print("Active item")
# #         j += 1

# #     final_output = []
# #     for key, val in results.items():
# #         # ❌ insert() needs both index and value, and key is not index
# #         if config['options']:
# #             final_output.insert(key)  # ❌

# #     if len(final_output) > 0:
# #         if len(final_output) > 5:
# #             print("Many results")
# #         # ❌ 'else if' is not valid Python syntax
# #         else if len(final_output) > 2:  # ❌
# #             print("Some results")
# #         else:
# #     print("Few results")  # ❌ Incorrect indentation

# #     # ❌ 'concat()' does not exist in Python lists
# #     return final_output.concat(results)  # ❌

# # # ❌ Function called with extra undefined argument 'extra'
# # output = process_data(data, config, extra=True)  # ❌

# # # ❌ 'data_list' is not defined here, should use 'data'
# # values = {k: v for k, v in data_list}  # ❌










# # ------------------------------------------------------------------
# # Corrected Version
# def process_data(data_list, config):
#     results = {}
#     # Process data_list
#     for i in range(len(data_list)):
#         item = data_list[i]
#         if item['value'] > 100 or item['value'] < 0:
#             results[item['id']] = "Invalid"
#         elif item['value'] == 50:
#             results[item['id']] = "Perfect"
#         else:
#             results[item['id']] = item['value']  # Store value in dictionary

#     # Check status 
#     for j in range(len(data_list)):
#         if data_list[j].get('status', False):
#             print("Active item")

#     # Build final_output
#     final_output = []
#     for key, val in results.items():
#         if config.get('options', False):
#             final_output.append(val)  # Append value instead of insert

#     # Print based on final_output length
#     if len(final_output) > 0:
#         if len(final_output) > 5:
#             print("Many results")
#         elif len(final_output) > 2:
#             print("Some results")
#         else:
#             print("Few results")

#     return final_output  # Return only final_output

# # Sample data and config
# data = [
#     {'id': 1, 'value': 75, 'status': True},
#     {'id': 2, 'value': 50, 'status': False},
#     {'id': 3, 'value': -5, 'status': False},
#     {'id': 'four', 'value': 200, 'status': True},
# ]

# config = {
#     'threshold': 'high',
#     'options': True
# }

# # Call function
# output = process_data(data, config)
# print("Final output:", output)

# # Post-processing
# for item in output:
#     if isinstance(item, str):
#         print("String found")
#         break
#     else:
#         print("Processing")

# # Create dictionary from data_list
# values = {item['id']: item['value'] for item in data}
# print("Values:", values)


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