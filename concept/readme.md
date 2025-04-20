🔹 Introductory Comment
python
Copy
Edit
'''
This Python program is a word-based puzzle game where the player has to guess the correct word from a scrambled version.
...
'''
🔸 Ye comment hai (multi-line comment). Isme bataya gaya hai ke ye program:

Ek game hai jo words ko scramble karta hai.

User ko guess karna hota hai.

Is game se aap Python ke concepts jaise list, function, loops, etc. ko practice kar sakte ho.

🔹 Modules Import
python
Copy
Edit
import random
🔸 random module import kiya gaya hai jo random values generate karne ke liye use hota hai. Hum ise words ko randomly pick karne aur shuffle karne ke liye use karenge.

🔹 WORDS Set
python
Copy
Edit
WORDS = {"python", "jumble", "scramble", "function", "tuple", "dictionary", "loop", "set", "comprehension", "variable"}
🔸 Yeh ek set hai jisme kuch English words diye gaye hain.

Set ka matlab: unordered collection of unique items.

Har word ek puzzle ka part ban sakta hai.

🔹 Tuple Conversion
python
Copy
Edit
word_list = [tuple(word) for word in WORDS]
🔸 Har word ko tuple mein convert kiya gaya hai.

tuple(word) ka matlab: "python" → ('p', 'y', 't', 'h', 'o', 'n')

word_list ab ek list hai jisme tuples of characters hain.

Tuple isliye liya gaya taake har letter alag alag shuffle ho sake.

🔹 Game Stats Dictionary
python
Copy
Edit
game_stats = {
    "score": 0,
    "attempts": 0,
    "correct_words": [],
    "wrong_words": []
}
🔸 Ye ek dictionary hai jisme game ka status save hota hai:

score: Kitne correct answers diye.

attempts: Total guesses.

correct_words: Jo sahi guess hue.

wrong_words: Jo galat hue.

🔹 Word Scramble Function
python
Copy
Edit
def scramble(word_tuple):
    word = list(word_tuple)
    random.shuffle(word)
    return word
🔸 Ye function ek word ko shuffle karta hai:

Tuple ko list banate hain (list(word_tuple)) taake usme changes ho saken.

random.shuffle(word) se letters ghuma diye jate hain.

Return karta hai shuffled word list.

🔹 Show Menu Function
python
Copy
Edit
def show_menu():
    print("\n🔘 Menu:")
    print("1. Play Game")
    print("2. View Stats")
    print("3. Reset Game")
    print("4. Exit")
🔸 Ye function sirf user ko ek menu show karta hai options ke sath.

🔹 Main Game Logic
python
Copy
Edit
def play_game(rounds=5):
🔸 Game 5 rounds ke liye chalti hai by default.

python
Copy
Edit
    guessed_words = set()
🔸 Ye set track karta hai ke kaunse words already use ho chuke hain taake repeat na ho.

python
Copy
Edit
    for i in range(rounds + 1):
🔸 Loop chal raha hai rounds + 1 times (yahan 6 times chalega, small bug hai).

python
Copy
Edit
        word_tuple = random.choice(word_list)
        while word_tuple in guessed_words:
            continue
        guessed_words.add(word_tuple)
🔸 Random word pick kiya gaya hai.

Agar wo word pehle se guess ho chuka ho to continue hota hai (yahan loop infinite ho sakta hai, ye bug hai).

Naya word set me add karte hain.

python
Copy
Edit
        original_word = ''.join(word_tuple)
        scrambled = scramble(word_tuple)
🔸 Original word tuple ko string banaya gaya hai.

''.join(('p','y')) → 'py'

Word ko scramble kiya.

python
Copy
Edit
        print(f"\n🔤 Scrambled Word: {scrambled}")
        guess = input("👉 Your Guess: ").strip().lower()
🔸 Scrambled word user ko dikhaya.

User se input liya, clean kiya (spaces remove) aur lowercase banaya.

python
Copy
Edit
        game_stats["attempts"] += 1
🔸 Har guess ke baad attempts 1 se badh jaata hai.

🔹 User Answer Check
python
Copy
Edit
        if guess == original_word:
            print("✅ Correct!")
            game_stats["score"] += 1
            game_stats["correct_words"].add(original_word)
🔸 Agar guess sahi ho:

Print karega “Correct”

Score badha dega

Word correct_words list me daal dega 🟥 ⚠️ Bug: correct_words is a list, but add() set ke liye hota hai, isko append() hona chahiye tha.

python
Copy
Edit
        else:
            print(f"❌ Wrong! The correct word was: {original_word}")
            game_stats["wrong_words"].add(original_word)
🔸 Agar guess galat ho:

Correct word print hoga

Word wrong_words me chala jayega 🟥 ⚠️ Bug: Yahan bhi add() ke bajaye append() hona chahiye.

🔹 Stats Display Function
python
Copy
Edit
def show_stats():
🔸 Game ka poora record show karta hai.

python
Copy
Edit
    print("\n📊 Game Stats:")
    print(f"• Total Attempts: {game_stats['attempts']}")
    print(f"• Score: {game_stats['score']}")
🔸 Attempts aur score print hotay hain.

python
Copy
Edit
    accuracy = (game_stats['score'] / game_stats['attempts']) * 100
    print(f"• Accuracy: {accuracy:.2f}%")
🔸 Accuracy percentage nikal ke print ki jati hai.

python
Copy
Edit
    print(f"• Words Guessed Correctly: {[word for word in game_stats['correct_words']]}")
    print(f"• Words Missed: {[word for word in game_stats['wrong_words']]}")
🔸 Correct aur Wrong guesses list print hoti hain.

🔹 Reset Game Function
python
Copy
Edit
def reset_game():
🔸 Game ke sare scores aur lists reset kar deta hai.

python
Copy
Edit
    game_stats["score"] = 0
    game_stats["attempts"] = 0
    game_stats["correct_words"].clear()
    game_stats["wrong_words"].clear()
    print("\n🔄 Game has been reset!")
🔸 Har cheez zero aur empty kar di jati hai.

🔹 Main Loop
python
Copy
Edit
def main():
    while True:
        show_menu()
        choice = input("Select an option (1-4): ").strip()
🔸 Menu baar baar show hota hai jab tak user "Exit" na kare.

python
Copy
Edit
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
🟥 ⚠️ Bug: Menu me likha hai option 4 → Exit, lekin choice == "5" likha hai. Isko choice == "4" hona chahiye.

🔚 End
python
Copy
Edit
main()
🔸 Program ka starting point — ye main() function ko call karta hai.

🔧 Bugs / Improvements:

Bug	Fix
.add() used on list	Replace with .append()
Infinite loop in while word_tuple in guessed_words	Add a new random word inside the loop
Exit option number is wrong	Change choice == "5" to choice == "4"
✅ Summary (Simple):

Concept	Use
set()	Unique words store karne ke liye
tuple(word)	Har word ko tuple banake scramble karna
random.shuffle()	Word ko random letters me ghumana
dict	Score and game info store karna
functions	Har feature alag function me likha gaya
input()	User se guess lena
loop	Game repeat karne ke liye
