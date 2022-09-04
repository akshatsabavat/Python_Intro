from itertools import product
import sys
from array import *
sys.setrecursionlimit(10000)

def power_of_number(number,power):
    if power == 0:
        return 1
    elif power == 1:
        return number
    else:
        return number * power_of_number(number, power - 1)

# print(power_of_number(2,5))

dataSet = [2,3,4,6,11,9]
def arrayProd(array):
    product = 1
    for i in array:
        product = product * i
    return product

# print(arrayProd(dataSet))

def recursiveRange(n):
    if n == 0:
        return 0
    else:
        return n + recursiveRange(n - 1)

# print(recursiveRange(5))

def fibonacci(n):
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(5))

def sumOfDigits(n):
    assert n >= 0 and int(n) == n, "N should be +ve and an integer for the code"

    if n == 0:
        return 0
    else:
        return int(n/10) + sumOfDigits(int(n%10))

# print(sumOfDigits(145))