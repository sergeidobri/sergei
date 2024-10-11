import numpy as np
import matplotlib.pyplot as plt
from random import randint

def factorial(n):
     m=1
     for i in range(1,n+1):
          m=m*i
     return m

def random(n):
     sum = 0
     for i in range(n):
          a=randint(1,11)
          sum+=a
          print(a, end= ' + ')
     return sum

def average(n):
     sum = 0
     for i in range(n):
          a = int(input())
         sum+


# newton(30,10)
print(factorial(5))
print(random(10))
# m = [[1,2],
#      [10,5]]
# print(matrix(m))
# print(average(2))