#Program to perform all basic operations of stack namely push, pop, peek/top and isEmpty
import sys

class Stack:

	def __init__(self, size):
		self.stack = []
		self.pos = -1

	def display(self):
		if not self.isEmpty():
			print("The stack is:")
			print(self.stack)
			self.end()
		else:
			print("The stack is empty...")

	def push(self, element):
		self.stack.append(element)
		self.pos += 1
		self.end()

	def pop(self):
		if not self.isEmpty():
			print("Element ",self.stack.pop(self.pos)," is removed")
			self.pos -= 1
		else:
			print("Cannot perform operation as stack is empty...")
		self.end()

	def peek(self):
		if not self.isEmpty():
			print("Top element of the stack is: ",self.stack[self.pos])
		else:
			print("Cannot perform operation as stack is empty...")
		self.end()

	def isEmpty(self):
		if not self.stack:
			return True
		else:
			return False
		self.end()

	def end(self):
		print("----------------------------------------------------------")

	@staticmethod
	def end1():
		print("----------------------------------------------------------")		

while(True):
	print("Enter the size of stack:")
	try:
		size = int(input())
		s = Stack(size)
		break
	except ValueError:
		print("Please enter integers only")
		Stack.end1()

while(True):
	print("Choose from below option:")
	print("1. Insert new element")
	print("2. Remove top element")
	print("3. Show top element")
	print("4. Display stack from top to bottom")
	print("5. Exit")

	input1 = int(input())
	if input1 == 1:
		if len(s.stack) == size:
			print("The stack is full...")
		else:
			try:
				el = input("Enter the element:")
				el = int(el)
				s.push(el)
			except ValueError:
				print("Please enter integers only")
				Queue.end1()
	elif input1 == 2:
		s.pop()
	elif input1 == 3:
		s.peek()
	elif input1 == 4:
		s.display();
	else:
		print("Exiting...")
		sys.exit()