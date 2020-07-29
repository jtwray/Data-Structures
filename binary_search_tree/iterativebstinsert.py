# Data structure to store a Binary Search Tree node
class Node:
	# Function to create a binary tree node having given key
	def __init__(self, key):

		self.data = key
		self.left = self.right = None


# Function to perform inorder traversal of the tree
def inorder(root):

	if root is None:
		return

	inorder(root.left)
	print(root.data, end=' ')
	inorder(root.right)


# Iterative function to insert a key into BST.
def insertIterative(root, key):

	# if tree is empty, create a node and set root
	if root is None:
		return Node(key)

	# start with root node
	curr = root

	# pointer to store parent node of current node
	parent = None


	# traverse the tree and find parent node of key
    # while curr is not None
	while curr:

		# update parent node as current node
		parent = curr

		# if given key is less than the current node,
		# go to left subtree else go to right subtree
		if key < curr.data:
			curr = curr.left
		else:
			curr = curr.right

	# construct a node and assign to appropriate parent pointer
	if key < parent.data:
		parent.left = Node(key)
	else:
		parent.right = Node(key)

	return root


if __name__ == '__main__':

	root = None
	keys = [15, 10, 20, 8, 12, 16, 25]

	for key in keys:
		root = insertIterative(root, key)

	inorder(root)
