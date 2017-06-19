from collections import defaultdict

class Graph:

	dict1 = {}
	
	def __init__(self,v):
		self.vertices = v

	def add_edge(self, u, v):
		if u not in self.dict1:
			self.dict1[u] = []
		if v not in self.dict1:
			self.dict1[v] = []
		self.dict1[u].append(v)
		self.dict1[v].append(u)

	def traversing(self, v):
		visited[v] = True
		arr.append(v)
		for vertex in self.dict1[v]:
			if visited[vertex] == False:
				self.traversing(vertex)

	def traverse(self):
		for v in range(1,self.vertices+1):
			if visited[v] == False:
				self.traversing(v)

print("Enter number of vertices:")
V = int(input())
g = Graph(V)
print("Enter number of edges:")
e = int(input())
print("Enter the pair of edges in format <<source destination>> with 1 as the lowest vertex:")
# for _ in range(e):
count = 0
while(count < e):
	u,v = input().split(' ')
	try:
		u,v = int(u),int(v)
		if u > V or v > V:
			print("Vertex cannot be greater than",V)
			Graph.end()
			print("Please re-enter the valid edge input")
		else:
			g.add_edge(u,v)
			count += 1
	except ValueError:
		print("Please enter integers only")

arr = []
visited = [False]*(V+1)
g.traverse()
print("Visiting pattern:",arr)