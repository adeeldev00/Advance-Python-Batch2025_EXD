print('========> class 12 <=======')
print('\n===> today we learn function <====')


'''
function make code reuseable and easy to use and learn 

1) functionis strted by function definTION 
  def func(argument)  ,,, def is the function defination we alway start with def
'''


def mysum(a,b):
    total=a+b
    return total

rev=mysum(10,45)

print(rev)


# we have a requirement to update


def mylen(a):
    count = 0
    for item in a:
        count = count + 1
    return count

num1 = [1, 2, 3, 4, 5, 7]
print('sum of list of number',mylen(num1))  # Output: 6



str1="helo i am adeel"
print('length of string .',mylen(str1))



# function for sum three number :

def mysum(a,b,c):
    d=a+b+c
    return d


print('sum of three number is :',mysum(45,5,5))


# get user input and + 2 in to this number 
# def sum2(a):
#     b=a+2
#     return b

# userRes=int(input('\nPlz Enter a number :'))
# print(sum2(userRes))



# function k under agr hum kuch nahi milta to hum parameter ki deafult value bi set karva sakty hai...

'''
we can assign value like that  sum2(a=45) if we get no value then 45 is deafult value is getten plus with 
'''


def welcome(a='Guest'):
    print("Hello", a)

welcome()
welcome("Adeel")




# create simple doc string ya basically ya return kary ga k ya fun kis liy use hota hai

def mysum(a,b,c):
    '''
    This function is basically take's 3 parameter as a int type and then sum this number and return the sum
    '''
    d=a+b+c
    return d
print(mysum.__doc__,mysum(45,5,5))




# functon me jaha bi hum retyurn dy dy to mean waha par ya function end ho gaya 




'''
agr hum function me return use na kary to wo humy kuch return nahi kary ga 
'''

def greet(name):
    print("Hello", name)

result = greet("Ali")
print(result)  # this simple return us "none" return beacuse function return nothing ...



'''

return multiple value together and print the result

'''

def fun():
    str1='hello'
    str2='Adeel'
    str3='By'
    return str1 , str2 ,str3
rv1,rv2,rv3=fun()
print(rv1)
print(rv2)
print(rv3)
rv=list(fun())
print(rv)
print(type(rv))




# function that get the three number as a argument

def mysum3(a,b,c):
    f'''
    calculate and return the sum of three number.
    a- first number
    b- second number
    c- third number
    '''
    total=a+b+c
    return total

print((mysum3.__doc__))
print(mysum3(10,46,70))





# A function that received a list and  return a number


def fun(mylist):
    squares = []
    typeOfNum=[]
    for item in mylist:
        print(f'number {item} and type of this :',type(item))
        typeOfNum.append(type(item))
        print(typeOfNum)
        square = item ** 2
        squares.append(square)
    sum_of_squares = sum(squares)
    print("Sum of square:", sum_of_squares)

# Call the function
fun([1, 2, 3, 4, 5])







''''

user input check number is even is odd 

'''
# input1=int(input('Enter your number check it even or odd :'))



# def checkEven(a):
#     if(a%2==0):
#         print(f'that is even number : {a}')
#         return True
#     elif(a%2==1):
#         print(f"provide number is odd : {a}")  
#         return False

# print(type(checkEven(input1)))      









# 

def fun(x,y,r,z):
    a=x+1
    b=y+1
    c=z+1
    r=r+1
    print(a,b,c,r)
    return a,b,c,r

a=10
b=20
c=30
r=78

print('before function',a,b,c,r)
fun(a,b,c,r)
print('after function ',a,b,c,r)




# create a algoritum

'''
i have a given list
step1=>
    # first ak loop chaly ga jo har value ko dehky ga , or append karva dy ga ak empty list me ,,, and ak or condition chaly gi jo dehky gi agr next value item +1 < item sy to list k start me append kar dy or agr wo value bari hai to last me bj dy ... 
'''

def bubble_sort(my_list):
    n = len(my_list)
    for i in range(n):
        for j in range(0, n - 1):
            if my_list[j] > my_list[j + 1]:
                # Swap values
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list

# Example usage
my_numbers = [5, 2, 8, 1, 3]
sorted_list = bubble_sort(my_numbers)
print("Sorted list:", sorted_list)




# task jo ghr sy kar k ana  hai selecttion short






# functions with default arguments

def display(name="Adeel",age=20):
    print(f"my name is {name} and my age is this {age}") 
    return
display('naveed',10)
display()
print(display())



# ============================> that is name toi key argument <===================
# named amd key argument mean if we have pre deafult argument already and i want to pass the 2nd argument and i want want first aRGUMENT IS USED AS deafult so what should i


# so here come name and key argument 
display(age=45)

# agr to hum first argument only deta hai that is fine
display("lengend")


# agr hum 2nd argument only dety hai 

# display(,45) # it's give us the synatx error basically ,,, for avoiding this error we used name to kay methode



import time

def timer(a):
   time.sleep(a)
   print(f'response is print after {a} sec ')
  

timeinput=int(input("Enter the time in sec :"))
timer(timeinput)    



def timeCalculate():
    start_time=time.time()
    for i in range(1,100):
        print(i)
    end_time=time.time()

    time_taken=end_time-start_time 

    print('time taken for excuted this loop',time_taken,'sec')  

timeCalculate()    





# greate a simple chatbot 

dic = {
    'hello': "hello Adeel how are you?",
    'python': "I am good in Python. Do you want to learn Python?",
}

def chatbot(a):
    if a.lower() == 'yes':
        q1 = input('How can I assist you? ')
        if q1.lower() in dic:
            print(dic[q1.lower()])
        else:
            print("Sorry, I don't understand that.")
    else:
        print("Okay, have a great day!")

userChat = input('Welcome to Adeel GPT! Do you want to talk? (yes/no): ')
chatbot(userChat)

