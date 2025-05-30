# Make String Analyzer (using Strings Methods at lest 5)
# print("String Analyzer (check differnt thing in your row data)")
# stringValue=input("Inser your Row Data :")
# print(stringValue)

# special_chars = "[!@<>@#$%^&*]"
# # number of character
# print(f"Number of Character : {len(stringValue.replace(" ",""))}")
# print(f"Number of Words : {len(stringValue.split())}")
# print(f"upperCase Text : {stringValue.upper()}")
# print(f"LowerCase Text : {stringValue.lower()}")
# print(f"Found Special character : {stringValue.find("!@<>@#$%^&*")}")
# print(f"Capitalize First Character{stringValue.title()}")
# print(special_chars is stringValue)
# # print(any(cha))


vowel="a,e,i,o,u" 
findword="p" 
changeType=str(49)
i=10      
# j=input("Enter the Index-number you want to remove ")
palind="mom"
data="i am adeel , a programmer"

#1 Reverse
print(f"Reverse String : {data[::-1]}")

#2 first half upper case
half=len(data)//2
print(len(data),half)
data1=str((data[:half]))
print(f"uppercase first half : {str(data1.upper())}")

#3 find vowel
print(f"is vowel  in string: {any(char in vowel for char in data)}")

#4 remove ith charcter
print(f"remove ith charcter {data[:i]+data[i+1:]}")

#5 title case
print(f"title case : {data.title()}")

#6 check palindrome
print(f"is this string is Palindrome : {data==data[::-1]}")

#7 replace a with k
print(f"replace a char with k : {data.replace('a','k')}")

#8 find a word
print(f"Find Word : {data.find(findword)}")

#9 change 49 in to str
print(f"change type of number : {type(str(49))}")


print('a' in data , 'e' in data ,'u' in data)

