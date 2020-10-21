#!/usr/bin/env python3

class BinarySearchTree:
    def __init__(self):
        self.root = None


    def insert(self, value):
        """Inserts a new node into the tree on the right position"""
        new_node = {
            'value': value,
            'left': None,
            'right': None
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
                    # traverse right
                    if not current_node['right']:
                        current_node['right'] = new_node
                        return self
                    current_node = current_node['right']


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
                    if not current_node['right']:
                        return False
                    current_node = current_node['right']
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
            if current_node['right']:
                queue.append(current_node['right'])
        return list


    def dfs_preorder(self):
        def traverse_preorder(node, list):
            list.append(node['value'])
            if node['left']:
                traverse_preorder(node['left'], list)
            if node['right']:
                traverse_preorder(node['right'], list)
            return list
        return traverse_preorder(self.root, [])


    def dfs_inorder(self):
        def traverse_inorder(node, list):
            if node['left']:
                traverse_inorder(node['left'], list)
            list.append(node['value'])
            if node['right']:
                traverse_inorder(node['right'], list)
            return list
        return traverse_inorder(self.root, [])


    def dfs_postorder(self):
        def traverse_postorder(node, list):
            if node['left']:
                traverse_postorder(node['left'], list)
            if node['right']:
                traverse_postorder(node['right'], list)
            list.append(node['value'])
            return list
        return traverse_postorder(self.root, [])


myBST = BinarySearchTree()

myBST.insert(36)
myBST.insert(22)
myBST.insert(30)
myBST.insert(49)
myBST.insert(15)
myBST.insert(40)
myBST.insert(52)

# print(myBST.__dict__)
#       36
#       /\
#    22    49
#   /\      /\
# 15  30  40  52

# print(myBST.breadth_first_search())  # [36, 22, 49, 15, 30, 40, 52]
print(myBST.dfs_inorder())  #Inorder: [15, 22, 30, 36, 40, 49, 52]
print(myBST.dfs_preorder())  #Preorder: [15, 22, 30, 36, 40, 49, 52]
print(myBST.dfs_postorder())  #postorder: [15, 30, 22, 40, 52, 49, 36]
