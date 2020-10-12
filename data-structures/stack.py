#!/usr/bin/env python3

# way1: implementation of stack using linked list
class Stack1:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        """Returns the top item of the stack"""
        return self.top

    def push(self, value):
        """Adds a new element on top of the stack"""
        new_node = {
            'value': value,
            'next': None
        }
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node['next'] = self.top
            self.top = new_node
        self.length += 1
        return self

    def pop(self):
        """Removes the top element from the stack"""
        if self.length == 0:
            return None
        elif self.length == 1:
            top_node = self.top
            self.top = None
            self.bottom = None
            del top_node
            self.length -= 1
            return self
        else:
            top_node = self.top
            self.top = self.top['next']
            del top_node
            self.length -= 1
            return self

    def search(self, value):
        """Returns True if the given item exists in the stack, if not returns False"""
        current_node = self.top
        while(current_node):
            if current_node['value'] == value:
                return True
            current_node = current_node['next']
        return False

    def isEmpty(self):
        """Returns True if stack is empty, False otherwise"""
        if self.length == 0:
            return True
        return False

# way2: implementation of stack using Array
class Stack2:
    def __init__(self):
        self.stack = []

    def peek(self):
        """Returns the last item from the stack"""
        length = len(self.stack)
        if length > 0:
            return self.stack[length - 1]
        return None

    def push(self, value):
        """Adds a new item on top of the stack"""
        self.stack.append(value)
        return self

    def pop(self):
        """Removes the top most item from the stack"""
        if len(self.stack) > 0:
            self.stack.pop()
            return self
        return None


# instantiated Stack1 class
website = Stack1()

## stack operations
# website.push('airbnb')
# website.push('amazon')
# website.push('netflix')
# website.pop()
# website.push('ibm')
# print(website.search('amazon'))
# print(f"length: {website.length}\ntop: {website.top}\nbottom: {website.bottom}")

# instantiated Stack2 class
books = Stack2()
#
# books.push("Rich Dad Poor Dad")
# books.push("The Alchemist")
# books.push("Think And Grow Rich")
# books.push("A Century Is Not Enough")
# books.push("Wings Of Fire")
# books.pop()
# print(books.peek())
# print(books.stack)
