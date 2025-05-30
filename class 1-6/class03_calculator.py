# create a simple calculator

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def maltiply(a,b):
    return a*b
def divide(a,b):
    if b!=0:
     return a/b
    else:
       return "Error: Divide by Zero"
def power(a,b):
    return a**b
def modulo(a,b):
   return a%b


num1=int(input('Enter first number : '))
print(num1)
num2=int(input('Enter second number : '))
print(num2)

while True:
  print("select operator")
  print("1. Add")
  print("2. subtract")
  print("3. Multiply")
  print("4. Division")
  print("5. power")
  print("6. Modulo")
  print("7. Exit")
  choice=input("Enter choice (1/2/3/4/5/6/7): ")
  if choice=='7':
     print("Exiting the program")
     break
  elif choice=='1':
     print(f"Result: {add(num1,num2)}")
     break
  elif choice=='2':
     print(f"Result: {subtract(num1,num2)}")
     break
  elif choice=='3':
     print(f"Result: {maltiply(num1,num2)}")
     break
  elif choice=='4':
     print(f"Result: {divide(num1,num2)}")
     break
  elif choice=='5':
     print(f"Result: {power(num1,num2)}")
     break
  elif choice=='6':
     print(f"Result: {modulo(num1,num2)}")
     break
  else:
     print("Invalid choice! Please Select a valid Option.")
     break
