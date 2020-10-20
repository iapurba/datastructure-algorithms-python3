#!/usr/bin/env python3

class BinarySearchTree:
    def __init__(self):
        self.root = None


    def insert(self, value):
        """Inserts a new node into the tree on the rigth position"""
        new_node = {
            'value': value,
            'left': None,
            'rigth': None
        }
        if not self.root:
            self.root = new_node
            return self
        else:
            current_node = self.root
            while True:
                if value < current_node['value']:
                    # traverse left
                    if not current_node['left']:
                        current_node['left'] = new_node
                        return self
                    current_node = current_node['left']
                else:
                    # traverse rigth
                    if not current_node['rigth']:
                        current_node['rigth'] = new_node
                        return self
                    current_node = current_node['rigth']


    def search(self, value):
        """Returns True if the value exists in the tree, otherwise returns False"""
        current_node = self.root
        while True:
            if value == current_node['value']:
                return True
            else:
                if value < current_node['value']:
                    # traverse left
                    if not current_node['left']:
                        return False
                    current_node = current_node['left']
                else:
                    if not current_node['rigth']:
                        return False
                    current_node = current_node['rigth']
        return False


    def breadth_first_search(self):
        current_node = self.root
        list = []
        queue = [] # keeps track of current node of the tree
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            list.append(current_node['value'])
            if current_node['left']:
                queue.append(current_node['left'])
            if current_node['rigth']:
                queue.append(current_node['rigth'])
        return list



myBST = BinarySearchTree()

myBST.insert(36)
myBST.insert(22)
myBST.insert(30)
myBST.insert(49)
myBST.insert(15)
myBST.insert(40)
myBST.insert(52)
print(myBST.breadth_first_search()) # [36, 22, 49, 15, 30, 40, 52]
#printing BinarySearchTree object as a dictionary
# print(myBST.__dict__)
#       36
#       /\
#    22    49
#   /\      /\
# 15  30  40  52
