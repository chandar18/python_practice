#Program to perform all basic operations of single Linked list namely insert, delete, Search
import sys

class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList():

	def __init__(self):
		self.head = None

	def display(self):
		temp = self.head
		if temp is None:
			print("The list is empty...")
		else:
			print("The list is:")
			if temp.next is None:
				print(temp.data, end=" ")
				print("")
				return
			while(True):
				print(temp.data, end=" ")
				temp = temp.next
				if temp == self.head:
					break
			print("")

	def push_start(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			new_node.next = new_node
			return
		temp = self.head
		while(temp.next != self.head):
			temp = temp.next
		temp.next = new_node
		new_node.next = self.head
		self.head = new_node

	def push_end(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			new_node.next = new_node
		else:
			temp = self.head
			while(temp.next != self.head):
				temp = temp.next
			temp.next = new_node
			new_node.next = self.head

	def push_after(self, old_data, new_data):
		new_node = Node(new_data)
		temp = self.head
		while(temp.data != old_data):
			temp = temp.next
		if temp is None:
			return False
		else:
			new_node.next = temp.next
			temp.next = new_node

	def delete_start(self):
		if self.head is None:
			print("The list is empty...")
			return
		temp = self.head
		if temp.next == self.head:
			self.head = None
			return
		while(temp.next != self.head):
			temp = temp.next
		temp.next = self.head.next
		self.head = self.head.next

	def delete_end(self):
		if self.head is None:
			print("The list is empty...")
			return
		temp = self.head
		if temp.next == self.head:
			self.head = None
			return
		while(temp.next.next != self.head):
			temp = temp.next
		temp.next = self.head

	def delete_element(self, data):
		temp = self.head
		if temp is None:
			print("The list is empty...")
			return
		if temp.next == self.head:
			self.head = None
			return
		if temp.data == data:
			while(temp.next != self.head):
				temp = temp.next
			self.head = self.head.next
			temp.next = self.head
		else:
				while(temp.next != self.head and temp.next.data != data):
					temp = temp.next
				if temp.next is None:
					print("No such element found...")
					return
				else:
					temp.next = temp.next.next
		print("Element",data,"is deleted...")

	def delete_position(self, position):
		if self.head is None:
			print("The list is empty...")
			return
		if position == 1:
			temp = self.head
			if temp.next == self.head:
				self.head = None
			else:
				while(temp.next != self.head):
					temp = temp.next
				self.head = self.head.next
				temp.next = self.head
			print("Position",position,"is remove...")
			return
		else:
			temp = self.head
			count = 1
			while(temp.next != self.head and count != position-1):
				temp = temp.next
				count += 1
			if temp.next == self.head:
				print("No such position...")
				return
			else:
				temp.next = temp.next.next
		print("Position",position,"is remove...")

	def find(self, position):
		temp = self.head
		count = 1
		while(count != position and temp):
			temp = temp.next
			count += 1
		if temp is None:
			print("There is no element at position",position)
		else:
			print("The data at position",position,"is:",temp.data)

	def end(self):
		print("------------------------------------------------------")

llist = LinkedList()
while(True):
	print("Choose from below option:")
	print("1. Insert new element at the beginning")
	print("2. Insert new element at the end")
	print("3. Insert new element after desired data")
	print("4. Delete element from the beginning")
	print("5. Delete element from the end")
	print("6. Delete element with value")
	print("7. Delete element with position")
	print("8. Show element at desired position")
	print("9. Display the list")
	print("10. Exit")

	input1 = int(input())
	if input1 == 1:
		input1 = input("Enter the element:")
		llist.push_start(int(input1))
		llist.end()
	elif input1 == 2:
		input1 = input("Enter the element:")
		llist.push_end(int(input1))
		llist.end()
	elif input1 == 3:
		old_data = input("Enter the element after which to be inserted:")
		new_data = input("Enter the new element:")
		llist.push_after(int(old_data),int(new_data))
		llist.end()
	elif input1 == 4:
		llist.delete_start()
		llist.end()
	elif input1 == 5:
		llist.delete_end()
		llist.end()
	elif input1 == 6:
		delete_data = input("Enter the element to be deleted:")
		llist.delete_element(int(delete_data))
		llist.end()
	elif input1 == 7:
		delete_pos = input("Enter the position to be removed:")
		llist.delete_position(int(delete_pos))
		llist.end()
	elif input1 == 8:
		pos = input("Enter the position:")
		llist.find(int(pos))
		llist.end()
	elif input1 == 9:
		llist.display()
		llist.end()
	else:
		print("Exiting...")
		sys.exit()