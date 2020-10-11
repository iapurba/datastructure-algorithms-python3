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
        """Adds an item to the beginning of the linked list"""
        new_node = {
            'value': value,
            'next': self.head
        }
        self.head = new_node
        self.length += 1
        return self

    def append(self, value):
        """Adds an item to the end of the linked list"""
        new_node = {
            'value': value,
            'next': None
        }
        self.tail['next'] = new_node
        self.tail = new_node
        self.length += 1
        return self

    def insert(self, index, value):
        """Adds an item to the given index in the linked list"""
        new_node = {
            'value': value,
            'next': None
        }
        if index == 0:
            self.prepend(value)
            return self
        if index >= self.length:
            self.append(value)
            return self
        leader = self._traverse_to_index(index - 1)
        new_node['next'] = leader['next']
        leader['next'] = new_node
        self.length += 1
        return self

    def remove(self, index):
        """remove the node of the given index"""
        if index == 0:
            unwanted_node = self.head
            self.head = unwanted_node['next']
            del unwanted_node
            self.length -= 1
            return self
        if index >= self.length:
            return None
        leader = self._traverse_to_index(index - 1)
        unwanted_node = leader['next']
        leader['next'] = unwanted_node['next']
        del unwanted_node
        self.length -= 1
        return self

    def search(self, value):
        current_node = self.head
        while current_node:
            if current_node['value'] == value:
                return True
            current_node = current_node['next']
        return False

    def _traverse_to_index(self, index):
        """Traverses through the linked list and returns the node to the given index"""
        counter = 0
        current_node = self.head
        while counter != index:
            current_node = current_node['next']
            counter += 1
        return current_node

## linked list operations
# my_linked_list = LinkedList(10)
# my_linked_list.prepend(6)
# my_linked_list.prepend(22)
# my_linked_list.append(26)
# my_linked_list.insert(2, 56)
# my_linked_list.insert(4, 8)
# my_linked_list.remove(11)
# print(my_linked_list.search(52))
print(f"length: {my_linked_list.length}\nhead: {my_linked_list.head}\ntail: {my_linked_list.tail}")
