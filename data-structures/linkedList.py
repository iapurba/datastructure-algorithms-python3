#!/usr/bin/env python3

class LinkedList:
    def __init__(self, value):
        self.head = {
            'value': value,
            'next': None
        }
        self.tail = self.head
        self.length = 1
    def prepend(self, value):
        """adds an item to the beginning of the linked list"""
        new_node = {
            'value': value,
            'next': self.head
        }
        self.head = new_node
        self.length += 1
    def append(self, value):
        """adds an item to the end of the linked list"""
        new_node = {
            'value': value,
            'next': None
        }
        self.tail['next'] = new_node
        self.tail = new_node
        self.length += 1

my_linked_list = LinkedList(10)
my_linked_list.prepend(6)
my_linked_list.prepend(22)
my_linked_list.append(26)

print(f"length: {my_linked_list.length}\nhead: {my_linked_list.head}\ntail: {my_linked_list.tail}")
