#Program to perform all basic operations of queue namely enqueue, dequeue, peek and isEmpty
import sys

class Queue:

	def __init__(self, size):
		self.queue = []

	def display(self):
		if not self.isEmpty():
			print("The queue is:")
			for i in self.queue:
				print(i, end=" ")
			print("")
			self.end()
		else:
			print("The queue is empty...")

	def enqueue(self, element):
		self.queue.append(element)
		self.end()

	def dequeue(self):
		if not self.isEmpty():
			print("Element ",self.queue.pop(0)," is removed")
		else:
			print("Cannot perform operation as queue is empty...")
		self.end()

	def peek_from_first(self):
		if not self.isEmpty():
			print("First element of the queue is: ",self.queue[0])
		else:
			print("Cannot perform operation as queue is empty...")
		self.end()

	def peek_from_rear(self):
		if not self.isEmpty():
			last = len(self.queue)
			print("Last element of the queue is: ",self.queue[last-1])
		else:
			print("Cannot perform operation as queue is empty...")
		self.end()

	def isEmpty(self):
		if not self.queue:
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
	print("Enter the size of queue:")
	try:
		size = int(input())
		s = Queue(size)
		break
	except ValueError:
		print("Please enter integers only")
		Queue.end1()

while(True):
	print("Choose from below option:")
	print("1. Insert new element")
	print("2. Remove the first element")
	print("3. Show first element")
	print("4. Show last element")
	print("5. Display queue from left to right")
	print("6. Exit")

	input1 = int(input())
	if input1 == 1:
		if len(s.queue) == size:
			print("The queue is full...")
		else:
			try:
				el = input("Enter the element:")
				el = int(el)
				s.enqueue(el)
			except ValueError:
				print("Please enter integers only")
				Queue.end1()
	elif input1 == 2:
		s.dequeue()
	elif input1 == 3:
		s.peek_from_first()
	elif input1 == 4:
		s.peek_from_rear()
	elif input1 == 5:
		s.display();
	else:
		print("Exiting...")
		sys.exit()