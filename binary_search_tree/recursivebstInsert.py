# Data structure to store a Binary Search Tree node
class Node:
	left = right = None

	# Function to create a binary tree node having given key
	def __init__(self, data):
		self.data = data


# Function to perform inorder traversal of the tree
def inorder(root):

	if root is None:
		return

	inorder(root.left)
	print(root.data, end=' ')
	inorder(root.right)


# Recursive function to insert a key into BST
def insert(root, key):

	# if the root is None, create a node and return it
	if root is None:
		return Node(key)

	# if given key is less than the root node,
	# recur for left subtree
	if key < root.data:
		root.left = insert(root.left, key)

	# else recur for right subtree
	else:
		# key >= root.data
		root.right = insert(root.right, key)

	return root


if __name__ == '__main__':

	root = None
	keys = [15, 10, 20, 8, 12, 16, 25]

	for key in keys:
		root = insert(root, key)

	inorder(root)
