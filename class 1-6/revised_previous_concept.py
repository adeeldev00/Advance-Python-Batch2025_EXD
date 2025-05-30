print("Revised Concept")
print('Arithmetic Operations')
print(f"addition :{2+7+9}")
print(f'subtraction :{110-99}')
print(f'multiplication :{110*64}')
print(f"True division :{100/7}")
print(f'float division :{100//7}')
print(f'modulus :{100%7}')
print(f'power :{5**3}\n')


# Format String 
print('(Learn about Format string)')
age = 4
name = "Aaraiz"
print("Hello Mr. %s,  you are %s years old.\n" %(name, age))



#Escape sequence
print('(Learn About Escape sequence)')
# a single or double quote has special meanings, i.e., are used to define a string. To make them part of a string you have to suppress the special meaning by preceding the character by a back slash \
print('It\'s my birthday\n')


# seprator
print('(Learn About seprator)')
print(name, age, sep=' : ')
age = 4
name = "Aaraiz"
print(name, age, sep=' * ')



# print end parameter
print('\n(Learn About print End parameter)')
print(name, end=' ')
print(age)


#check datatype
print('\n(Learn About type check)')
print(type(name))
print(type(age))



#we learn about variable refernce
print('\n(Learn About variable refence)')
a = 10
b = 10
print(id(a), id(b) )


# we learn about dir() and del() key
print('\n(Learn About dir() , del())')
print(dir())



# we import math function .. 
print('\n(Learn About import math)')
import math
print(dir(math))


# data type 
print('\n(Learn About Data type)')
x = '21'
print(type(x))
a = 2.6
b = 3.2
x = complex(a,b)
type(x), x


# Learn about operating system
print('\n(Learn About operating system)')
x = 10
y = 3
print('x + y =',x+y)
print('x - y =',x-y)
print('x * y =',x*y)
print('x / y =',x/y)
print('x // y =',x//y)
print('x ** y =',x**y)
print('x % y =',x%y)



# Comparison Operators
print('\n(Learn About Comparison Operators )')
print('x > y is',x>y)
print('x < y is',x<y)
print('x == y is',x==y)
print('x != y is',x!=y)


#Logical operators
print('\n(Learn About Logical Operators )')
x = True
y = False

print('x and y is',x and y)

print('x or y is',x or y)

print('not x is',not x)

# create a simple variable and print 
# swap two variable and assign third varible in singal line
# Assign 3 variables in a single line
# Declare two string variables and then concatenate
#incriment a variable by 5 
#check datatype
#convert a variable type to another data type 
#create a variable and delete 
# 9) split string after first comma
# 10) create 2 variables and apply all maths operations.
# 11) calculate the area of the circle
# 12) convert temperature (Celsius to Fahrenheit)
# 13) check if two numbers is equal.
# 14) check two strings are Equal 
# 15) find a greater number in a list 
# 16) check if the number is greater than or equals to another 
# 17) compare user age for voting eligibility 
# 18) check if 2 lists are equal 
# 19) check if a number is between 2 values.