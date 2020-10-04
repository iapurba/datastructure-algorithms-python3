#!/usr/bin/env python3

class Array:
    def __init__(self):
        self.length = 0
        self.data = {}

    def append(self, value):
        self.data[self.length] = value
        self.length += 1

    def get(self, index):
        return self.data[index]

    def pop(self):
        lastItem = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        print(lastItem)
        return lastItem

# fruits = Array()
# fruits.append("apple")
# fruits.append("mango")
# fruits.append("grape")
# fruits.pop()
# print("length =", fruits.length,"\ndata =", fruits.data)
