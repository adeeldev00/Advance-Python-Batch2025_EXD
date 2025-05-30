# first of all string immutable hota hai

a='iamadeel'
print(id(a))
a='iamadeel1'
print (id(a))

# string ko conceatenate karne k liye hum + operator use karte hain
a='iamadeel'
b='iamadeel1'
c=a+b
print (c)

# string ko slice karne k liye hum [start:end] ka syntax use karte hain
a='i am adeel'
b=a[0:4]
print (b)

# string ko slice karne k liye hum [start:end:step] ka syntax use karte hain
a='i am adeel'
b=a[0:4:2]
print (b)

# =============> operation on string <==================
print(a.upper())
print(a.lower())
print(a.title())
print(a.capitalize())
print(a.count('a'))
print(a.find('a'))
print(a.index('a'))
print(a.replace('a','A'))
print(a.split(' '))
print(a.split('a',1))
print(a.isalpha())
print(a.startswith('i'))
print(a.endswith('k'))
print(a.find("o")) # -1 return kare ga kyun k o string me nahi hai

