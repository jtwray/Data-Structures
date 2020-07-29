"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when link list has a pop and append time complexity of o(n) 
the deque method has 0(1) constant for pop and append methods
   implementing a Stack?

   the main advantage of useing a LL over an array to implement a stack is 
   the ablity to change the size of the list dynamically making overflow not possible
"""

# stack last in first out
'''
push the newest value onto the top of the stack 
like pancakes
last on top of my plate is first to be eaten

push pancake on top of my stack

pop pancake off top


'''
'''list stack
stackoverflow inevitable 
--kinda
'''


class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = ?
        self.storage = []

    def __len__(self):
        return f'{len(self.storage)}'
        # return f'{self.size}'

    def push(self, value):
        self.storage.append(value)
        self.size += 1
        return len(self.storage)

    def pop(self):
        if len(self.self.storage) > 0:
            self.size -= 1
            return f'{self.storage.pop()}'
        elif len(self.storage is 0):
            return f'error Pop top from empty stack'


'''LL stack
stackoverflow not possible 
new nodes are dynamically allocated
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LLStack:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head is Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
            
        # remove the element that is tht current head aka the top
        def pop(self):
            if self.head is None:
                return None
            else:
                poppedNode = self.head
                self.head = self.head.next
                poppednode.next = None
                return poppednode.data
                # removes the head node and makes the preceeding one the new head

        def __len__(self):
            temp = self.head.next
            count = 0
            while (temp):
                count += 1
                temp = temp.next()
            return count
