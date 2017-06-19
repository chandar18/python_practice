#Node class
class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def printList(self):
    temp = self.head
    while(temp):
      print(temp.data)
      temp = temp.next

  def push_start(self,new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node

  def push_after(self,prev_node,new_data):
    if prev_node is None:
      print("No such node")
      return
    new_node = Node(new_data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  def push_end(self,new_data):
    new_node = Node(new_data)
    if self.head is None:
      self.head = new_node
      return
    temp = self.head
    while(temp.next):
      temp = temp.next

    temp.next = new_node

if __name__=='__main__':
  llist = LinkedList()
  llist.head = Node(1)
  second = Node(2)
  third = Node(3)

  llist.head.next = second
  second.next = third

  print("Before Insert")
  llist.printList()
  llist.push_start(4)
  print("After Insert at start")
  llist.printList()
  print("After Insert after node")
  llist.push_after(second,5)
  llist.printList()
  print("After Insert at last")
  llist.push_end(6)
  llist.printList()