#-*- coding: utf-8-*
"""
 Created on Fri Sep 21 09:29:05 2018
 @filename: arithmetic.py
 @author: Jay Parmar
 """
def addition(a, b):
  return a + b
def multiply(a, b):
 """Returns the product of two numbers"""
 return a * b
def division(dividend, divisor):
 """
 Performs the division operation between the dividend
 and divisor
 """
 return dividend / divisor
def factorial(n):
 """Returns the factorial of n"""
 i = 0
 result = 1
 while(i != n):
  i = i + 1
  result = result * i
 return result

def loger():
 print('i am imported for other file')