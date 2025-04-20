'''
i want to print like like pattren in python

*   *
 * * 
  *  
 * * 
*   *    

plz print this pattern in python
'''


print('\n============> Pattern 1 <=======================')

n=5
for i in range(n): # this line print 0,1
    for j in range(n): #0,1,2
        if i == j or j == n-1-i : #0==0 true,1!=0,21=0
            print('*',end='') #*(0index of i),so empty print (1st index of 1),same empty,
        else:
            print(' ',end='')
    print()




'''
🥇 Level 1: Basic Easy Patterns
Solid Rectangle

****
****
****


'''

print('\n=============> Pattern 2 <====================')

n=4
for i in range(n-1): #0,
    for j in range(n): #0,
      if(j<n): #0<3 
          print('*',end='')
      else:
          print('',end='')

    print()



'''
3) Right-Angle Triangle


*
**
***
****


'''

print('\n=============> Pattern 2 <====================')


for i in range(1,5):
    print("*" * i)





'''
invert triangle 

****
***
**
*
'''



print('==========> pattern 3 <============')

n = 4
for i in range(n):
    for j in range(n - i):
        print('*', end='')
    print()


'''
2). Hollow Square
****
*  *
*  *
****


5). Right-Angle Triangle (Right Side)
   *
  **
 ***
****


6). Inverted Right-Angle Triangle (Right Side)
****
 ***
  **
   *



7). Pyramid
   *
  ***
 *****
*******



8). Inverted Pyramid
*******
 *****
  ***
   *


9). Half Pyramid using Numbers
1
12
123
1234



10). Inverted Half Pyramid using Numbers
1234
123
12
1


11). Floyd's Triangle
1
2 3
4 5 6
7 8 9 10



12). 0-1 Triangle
1
0 1
1 0 1
0 1 0 1



13). Solid Rhombus
   ****
  ****
 ****
****



14). Hollow Rhombus
   ****
  *  *
 *  *
****



15). Number Pyramid
   1
  2 2
 3 3 3
4 4 4 4



16). Palindromic Number Pattern
   1
  121
 12321
1234321


17). Diamond Pattern (Stars)
   *
  ***
 *****
*******
 *****
  ***
   *



18). Alphabet Triangle
A
A B
A B C
A B C D


19). Inverted Alphabet Triangle
A B C D
A B C
A B
A


'''    