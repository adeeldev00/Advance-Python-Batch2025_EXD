# fibonacci series
 
n=int(input('Enter count of fibonacci number you want to print: '))
i=1
if n<1:
    fib=[]
elif n==1:
    fib=[0]
elif n==2:
    fib=[0,1]
elif n > 2:
    fib=[0,1]
    while(i<n-1):
        fib.append(fib[i]+fib[i-1])
        i +=1
print('required series:',fib)        