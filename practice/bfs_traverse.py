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

	def traverse(self, e):
		queue = [1]
		visited = [1]
		edges = 0
		arr = [1]
		while edges < e:
			elem = queue.pop(0)
			adj = self.dict1[elem]
			for vertex in adj:
				if vertex not in visited:
					visited.append(vertex)
					queue.append(vertex)
					arr.append(vertex)
					edges += 1
		print("Visiting pattern:",arr)

print("Enter number of vertices:")
v = int(input())
g = Graph(v)
print("Enter number of edges:")
e = int(input())
for _ in range(e):
	u,v = input().split(' ')
	u,v = int(u),int(v)
	g.add_edge(u,v)

g.traverse(e)