#!/usr/bin/env python3

# Recursive Aproach
def factorialRecursive(num):
    #base case
    if num <= 1:
        return 1
    return num * factorialRecursive(num - 1)


# Iterative Aproach
def factorialIterative(num):
    result = 1
    while(num >= 1):
        result *= num
        num -= 1
    return result

# print(factorialRecursive(6)) # returns 720
# print(factorialIterative(6)) # returns 720
