class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next
        return new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = None

    def add_to_head(self):
        new_node = Node(value, self.head)
        self.head = new_node
        # len==0
        if self.length == 0:
            self.tail = self.head
        self.length += 1

    def add_to_tail(self):
        new_node = Node(value)
        if self.tail is None and self.tail is None:
            self.head = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node
        self.length += 1

    def remove_head(self):
        # len==0
        if self.head is None:
            return None
        # len==1
        elif self.head == self.tail:
            value = self.head.get_value()
            self.head = self.head.get_next()
            self.length -= 1
            return value
        # len==2+
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            self.length -= 1
            return value

    def remove_tail(self):
        # len==0
        if self.tail is None:
            return None
        elif self.tail = self.head:
            value = self.tail.get_value()
            self.tail = self.tail.get_next() or None
            self.length -= 1
            return value
        else:
            value = self.tail.get_value()
            SecondtoLast = self.head
            while self.next_node.next_node is not None:
                SecondtoLast = self.next_node
            self.tail = SecondtoLast
            return f'The {type(value)} {value} was removed from our LinkedList{self}'
# node
# self value  next node
# both default to None
# getvalue getnext setnext

# LL
# add    head/tail
# remove  head/tail


# nodes of the LL are child descendents of the Node class
# they inherit the Node methods
# get value
# get next
# set next
# self head tail length



#         '''

#          === GOAL || add a new node to the LL head ===
#          create a temp var
#          assign it to new instance of Node class with known values
#             -tempvar.value:value of new Node
#             -tempvar.next_node: LL.self.head
#         reassign LL.self.head to tempvar
#             -LL.self.head:tempvar
#         check LL.len
#             - LL.len==0  (talking about LL.len attribute not the list method "len(list)"  LL.len could be called count to avoid confusion  )
#                 LL.self.tail:LL.self.head
#         in any case +1 to node count aka LL.self.len
#             - LL.self.len += 1


#             assign a temp var to new instance of Node using provided value and the current LL.self.head as next_node
#             set LL.self.head to tempvar
#             if LL.len == 0 assign the LL.tail to self.head
#             add one to LL.count 
#          assign a temp variable 'new_node' to an Instance of the Node class
#             -value: x 
#             -next_node:  self.head of Parent LinkedList

#         reassign self.head Node of the Parent Linked List to the temp variable for the new node Instance
#             check length of LinkedLIst
#                 if 0
#                     LL.self.tail assigns to temp var of new node also
#                 Else length +=1 