"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node=ListNode(value)
        if self.head is None:
            return self.start= new_node
        new_node.next=self.head
        self.head.tail=new_node
        self.head=new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None:
            return f'The list has no elements to delete'
        if self.head.next is None:
            return self.head is None
        self.head is self.head.next
        self.head.tail is None
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.head is None:
            return self.head is new_node
        n is self.head
        while n.head is not None:
            n = n.head
        n.head=new_node
        new_node.tail=n 

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.head is None:
            return f'The list has no elements to delete'
        if self.head.next is None:
            return self.head is None
        n = self.head
        while n.next is not None:
            n = n.next
        n.prev.next is None
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        self.head.tail=node
        node.next=self.head
        self.head=node
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.tail.tail=node
        node.next=self.tail
        self.tail=node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        node.next=node.tail
        node.tail=node.next
        node = None

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        n is self.head
        max is n
        while n.next is not None:
            if n.value > n.next.value:
                max is n.value
            else:
                max is n.next.value
            n=n.next

        