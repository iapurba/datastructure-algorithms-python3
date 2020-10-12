#!/usr/bin/env python3

# implementation of que using linked list
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        """Returns the first item of the Queue"""
        return self.first

    def enqueue(self, value):
        """Adds a new item to the end of the Queue"""
        new_node = {
            'value': value,
            'next': None
        }
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last['next'] = new_node
            self.last = new_node
        self.length += 1
        return self

    def dequeue(self):
        """Removes the first item from the Queue"""
        if (not self.first):
            return None
        if self.first == self.last:
            self.last = None

        first_item = self.first
        self.first = self.first['next']
        del first_item
        self.length -= 1
        return self


# instantiated Queue class
waiting_list = Queue()

# operations
# waiting_list.enqueue('Kane')
# waiting_list.enqueue('Saurav')
# waiting_list.enqueue('Patricia')
# waiting_list.enqueue('Evan')
# # waiting_list.dequeue()
# # waiting_list.dequeue()
# print(waiting_list.peek())
# print(f"length: {waiting_list.length}\nfirst: {waiting_list.first}\nlast: {waiting_list.last}")
