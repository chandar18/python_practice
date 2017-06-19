#Program to create tree from array  and traverse Tree with in-order, pre-order and post-order traversal
import sys

class Node():
	
	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value


def InOrder(root):
	stack = []
	elem = root
	while True:
		if elem:
			stack.append(elem)
			elem = elem.left
		else:
			if stack:
				elem = stack.pop()
				print(elem.value)
				elem = elem.right
			else:
				break
			

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

InOrder(root)