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
    def insert(self, index, item):
        self._shift_item_to_rigth(index)
        self.data[index] = item

    def _shift_item_to_rigth(self, index):
        for i in range(index, self.length):
            self.data[i+1] = self.data[i]
        self.length += 1


fruits = Array()
fruits.append("apple")
fruits.append("mango")
fruits.append("grape")
# fruits.pop()
fruits.insert(1, 'banana')
fruits.insert(2, 'peach')
print(fruits.length, fruits.data)
