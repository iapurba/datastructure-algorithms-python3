#!/usr/bin/env python3

# Iterative Aproach
# time complexity of this function is linear O(n)
def fibonacciIterative(number):
    sequence = [0,1]
    for i in range(2, number+1):
        sequence.append(sequence[i-2] + sequence[i-1])
    return sequence[number]


# Recursive Aproach
# This is a bad aproach because time complexity is O(2^n)
def fibonacciRecursive(number):
    #base case
    if number < 2:
        return number
    return fibonacciRecursive(number - 1) + fibonacciRecursive(number - 2)


print(fibonacciIterative(40)) # took only 40 operations
print(fibonacciRecursive(40)) # took 1099511627776 operations
