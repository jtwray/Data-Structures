"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

#stack last in first out
'''
push the newest value onto the top of the stack 
like pancakes
last on top of my plate is first to be eaten

push pancake on top of my stack

pop pancake off top


'''

class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = ?
        self.storage=[]

    def __len__(self):
        return len(self.storage)
        return self.size

    def push(self, value):
        self.storage.append(value)
        return len(self.storage)  
        pass

    def pop(self):
        self.storage.pop()
        return len(self.storage)
        pass

class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = ?
        self.storage=[]

    def __len__(self):
        return f'{len(self.storage)}'
        #return f'{self.size}'

    def push(self, value):
        self.storage.append(value)
        return len(self.storage)  
        pass

    def pop(self):
        if len(self.self.storage)>0:
            return f'{self.storage.pop()}'
        elif len(self.storage is 0):
            return f'error Pop top from empty stack'


