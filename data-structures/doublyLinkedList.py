#!/usr/bin/env python3

class DoublyLinkedList:
    def __init__(self, value):
        self.head = {
            'value': value,
            'next': None,
            'prev': None
        }
        self.tail = self.head
        self.length = 1


    def append(self, value):
        """Adds new item to the end of the linked list"""
        new_node = {
            'value': value,
            'next': None,
            'prev': None
        }
        self.tail['next'] = new_node
        new_node['prev'] = self.tail
        self.tail = new_node
        self.length += 1
        return self


    def prepend(self, value):
        """Adds new item to the beginning of the linked list"""
        new_node = {
            'value': value,
            'next': None,
            'prev': None
        }
        new_node['next'] = self.head
        self.head['prev'] = new_node
        self.head = new_node
        self.length += 1
        return self


    def insert(self, index, value):
        """Add new item to the given index of the linked list"""
        new_node = {
            'value': value,
            'next': None,
            'prev': None
        }
        if index == 0:
            self.append(value)
            return self

        if index >= self.length:
            self.prepend(value)
            return self

        current_node = self._traverse_to_index(index)
        leader = current_node['prev']
        new_node['next'] = current_node
        new_node['prev'] = leader
        leader['next'] = new_node
        current_node['prev'] = new_node
        self.length += 1
        return self


    def remove(self, index):
        """Removes the node on the given index"""
        if index >= self.length:
            return None

        if index == 0:
            #remove the first item
            unwanted_node = this.head
            self.head = self.head['next']
            self.head['prev'] = None
            del unwanted_node
            self.length -= 1
            return self

        if index == (self.length - 1):
            #remove the list item
            unwanted_node = self.tail
            self.tail = self.tail['prev']
            self.tail['next'] = None
            del unwanted_node
            self.length -= 1
            return self

        unwanted_node = self._traverse_to_index(index)
        leader = unwanted_node['prev']
        follower = unwanted_node['next']
        leader['next'] = follower
        follower['prev'] = leader
        del unwanted_node
        self.length -= 1
        return self


    def search(self, value):
        """Returns True if the given item exists in the linked list, False otherwise"""
        current_node = self.head
        while(current_node):
            if current_node['value'] == value:
                return True
            current_node = current_node['next']
        return False


    def _traverse_to_index(self, index):
        """Traverses through index and returns node of the given index"""
        middle_index = self.length // 2
        # if the given index is less than or equal to the middle index then traverse forward
        # other wise loop through backward to decrease number of iterations
        if index <= middle_index:
            counter = 0
            current_node = self.head
            while counter != index:
                current_node = current_node['next']
                counter += 1
            return current_node
        else:
            counter = self.length - 1
            current_node = self.tail
            while counter != index:
                current_node = current_node['prev']
                counter -= 1
            return current_node


#instantiated the DoublyLinkedList class
top_car_companies = DoublyLinkedList('Volkswagen')

## operations
# top_car_companies.append('Daimler AG')
# top_car_companies.append('Honda')
# top_car_companies.prepend('Toyota')
# top_car_companies.append('BMW')
# top_car_companies.insert(3, 'Ford')
# top_car_companies.insert(2, 'Fiat')
# top_car_companies.append('GM')
# top_car_companies.remove(2)   # Remove 'Fiat'
# print(top_car_companies.search('BMW')) #True
# print(f"length: {top_car_companies.length}\nhead: {top_car_companies.head}\ntail: {top_car_companies.tail}")
