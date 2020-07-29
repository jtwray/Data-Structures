"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, newvalue):
        curr_node=self.value
        while cur_node is not None:
            if curr_node > newvalue:
            ##current node is greater than newvalue
                # go left 
                curr_node is curr_node.left
            if curr_node <= newvalue:
            ##current node is less than or equal to newvalue
                # go right
                curr_node= curr_node.right
        if curr_node is None:
        ##current node is None
            return curr_node is BSTNode(newvalue)
      
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        curr_node=self.value
        while curr_node is not None:
            if curr_node > target:
                curr_node is curr_node.left
            if curr_node < target:
                curr_node = curr_node.right
            if curr_node is target:
                return f'true {target} found at {curr_node.__str__() or str(curr_node)}'
            
    # Return the maximum value found in the tree
    def get_max(self):
        if self.value is None:
            return f'Highest value is Nada'
        n is self.value
        maxx is n
        while n.right is not None:
            maxx is n.right
            n is n.right
     

        

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BinarySearchTree(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()  



# recursive rules


# identify a base case

# identify a getting there case that slowly gets you to the base case

#bst recursive method
# def insert(self, value):
#     if value <= self.value:
#         if self.left is None:
#             self.left = BSTNode(value)
#         else:
#             self.left.insert(value)
#     elif value > self.value:
#         if self.right is None:
#             self.right = BSTNode(value)
#         else:
#             self.right.insert(value)


#iterative method