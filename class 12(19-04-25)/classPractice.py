print('===========> Class 12 <==================')


'''
1. Create a list of squares
- From 1 to 10, return a list of squares.
'''

squares = [i ** 2 for i in range(1, 11)]
print(squares)



'''
2. Extract first letters
- Given ["apple", "banana", "cherry"], return ["a", "b", "c"].
'''

given_list = ["apple", "banana", "cherry"]
first_letters = []

for i in given_list:
    first_letters.append(i[:1])

print(first_letters)



'''
3. Filter out odd numbers
- From a list of numbers 1 to 20, keep only the even ones.
'''

list_of_number=list(range(1,21))
print(list_of_number)
list_of_odd_number=[]

for i in list_of_number:
    if (i%2== 1):
        list_of_odd_number.append(i)

print('\nlist of odd Number between 1 to 20 :',list_of_odd_number)



'''
4. Map numbers to their squares
- From 1 to 5, create a dictionary like {1: 1, 2: 4, 3: 9, ...}

'''
numbers_and_square={}

for i in range(1, 5):
   numbers_and_square[i]=i**2

print(numbers_and_square)

'''
5) Map words to their lengths
- Given ["apple", "banana", "cherry"],
    return {"apple": 5, "banana": 6, "cherry": 6}.
'''

find_length={}


for i in given_list:
    find_length[i]=len(i)

print(find_length)




'''
6. Remove vowels from strings
- From ["hello", "world"], return ["hll", "wrld"].
'''

given_list_2 = ["hello", "world"]

vowels = ['a', 'e', 'i', 'o', 'u']

no_vowel_list = []

for word in given_list_2:
    no_vowel_word = ''
    for char in word:
        if char.lower() not in vowels:
            no_vowel_word += char
    no_vowel_list.append(no_vowel_word)

print(no_vowel_list)



'''
7. Filter dict entries by value
- Given {"a": 10, "b": 20, "c": 30}, return only items with value > 15.
'''

res = {}

given_dict = {"a": 10, "b": 20, "c": 30}

for i in given_dict:
    if given_dict[i] > 15:
        res[i] = given_dict[i]

print(res)

# we used dicctionary comprehension

given_dict = {"a": 10, "b": 20, "c": 30}

res = {k: v for k, v in given_dict.items() if v > 15}

print(res)

'''
8. Inverting a dictionary
- From {"a": 1, "b": 2, "c": 3}, return {1: "a", 2: "b", 3: "c"}.
'''

given_dict2 = {"a": 1, "b": 2, "c": 3}

# Create an empty dictionary to store the inverted version
inverted_dict = {}

for key in given_dict:
    value = given_dict[key]
    inverted_dict[value] = key

print(inverted_dict)



'''
9. Find palindromes
- From ["madam", "apple", "racecar", "python"], return only the palindromes.

'''

words = ["madam", "apple", "racecar", "python"]

palindromes = []

for word in words:
    if word == word[::-1]:
        palindromes.append(word)

print(palindromes)



# by list Comprehension

words = ["madam", "apple", "racecar", "python"]

palindromes = [word for word in words if word == word[::-1]]

print(palindromes)



# list comprehension usely short our code ...




