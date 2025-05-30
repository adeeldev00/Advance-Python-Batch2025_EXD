# class Student:
#     def __init__(self, name, age, favSub):
#         self.name = name
#         self.age = age
#         self.favSub = favSub

# s1 = Student("Adeel", 78, "computer")
# s2=Student("naveed",67,"bio")

# print(f"data of student : {s2.name , s2.age,s2.favSub}")

'''
class is alway created by capital letter and class is blueprint and template to create object , actually class 
'''



"use another function init"


class Student:
    def __init__(self, name, age, favSub):
        self.name = name
        self.age = age
        self.favSub = favSub

    def display(self):
        print(self.name,self.age,self.favSub)


s3=Student("Bil",67,"bio")
s3.display()




# Create a Bank Class

class BankAcount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance

    def deposit(self,Amount):
        self.balance += Amount
        return self.balance

    def currentBalance(self):
        print(self.owner ,self.balance)

    def withdraw(self,Amount):
        if Amount > self.balance:
            return "insuficient Fund"
        else:
            self.balance -= Amount
            return self.balance      
        

user1=BankAcount("Adeel")

user1.currentBalance()

user1.deposit(10000)

user1.currentBalance()




# Rectangular class 

class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
         return self.width*self.height    
    def perimeter(self):
        return 2*(self.width+self.height)
    
    def __str__(self):
        return f"Rectangular Area(Width={self.width},height={self.height})"
    
rect=Rectangle(5,10)
totalArea=rect.area()
print(f"{rect} = {totalArea}")
