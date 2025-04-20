'''
Given two integer variables a and b, and a boolean variable flag. The task is to
check the status and return accordingly.
Return True for the following cases:
 Either a or b (not both) is non-negative and the flag is false.
 Both a and b are negative and the flag is true.
Otherwise, return False.
'''

flag = True

def checkStatus2(a, b):
    global flag
    if a < 0 and b < 0:
        flag = True
    elif (a < 0 and b >= 0) or (a >= 0 and b < 0):
        flag = False
    else:
        flag = True

checkStatus2(-10, -10)
print('\n', flag)




tup = {}
tup[(1,2,4)] = 8
tup[(4,2,1)] = 10
tup[(1,2)] = 12
sum1 = 0
for k in tup:
    sum1 += tup[k]
print(len(tup) + sum1)