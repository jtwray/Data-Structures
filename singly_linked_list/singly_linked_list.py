class Node : 
    def __init__(self, value=None, next_node=None):
        #the value at this linked list node
        self.value= value
        #reference to the next node in the list
        self.next_node= next_node
    def get_value(self):
        return self.value
    def get_next(self):
        return self.next_node
        # def get(self,get):
        #     return self.get
        #__getattribute__(self, get)
    def set_next(self,new_next,__getAttr__):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head =None
        self.tail = None
        self.length = None
    
    def add_to_head(self, value):
        new_node =Node(value, self.head)
        self_head = new_node
        if self.length == 0:
            self.tail=new_node
        self.length += 1
    def add_to_tail(self):
        new_node = Node(value)
        
