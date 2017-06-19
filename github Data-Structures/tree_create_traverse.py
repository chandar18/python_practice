#Program to create tree from array  and traverse Tree with in-order, pre-order and post-order traversal
import sys

class Node():
	
	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value


def InOrder(root):
	if root:
		InOrder(root.left)
		print(root.value, end=" ")
		InOrder(root.right)

a = [1,2,3,4,5,6,7]
root = Node(a[0])
current = root
queue = []
queue.append(current)
i = 0
while queue:
	current = queue.pop(0)
	index = 2*i + 1
	if index < len(a):
		# queue.append(a[index])
		current.left = Node(a[index])
		queue.append(current.left)
	index = 2*i + 2
	if index < len(a):
		# queue.append(a[index])
		current.right = Node(a[index])
		queue.append(current.right)
	i += 1
# print(root.value)
# print(root.left.value)
# print(root.right.value)
# print(root.left.left.value)
# print(root.left.right.value)
# print(root.right.left.value)
# print(root.right.right.value)
InOrder(root)