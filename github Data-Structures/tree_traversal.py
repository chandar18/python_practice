#Program to traverse Tree with in-order, pre-order and post-order traversal
import sys

class Node():

	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def InOrder(root):

	if root:
		InOrder(root.left)
		print(root.val, end=" ")
		InOrder(root.right)

def PreOrder(root):

	if root:
		print(root.val, end=" ")
		PreOrder(root.left)
		PreOrder(root.right)

def PostOrder(root):

	if root:
		PostOrder(root.left)
		PostOrder(root.right)
		print(root.val, end=" ")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print("In-order:")
InOrder(root)
print("")
print("Pre-order:")
PreOrder(root)
print("")
print("Post-order:")
PostOrder(root)