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

	def traverse(self, start):
		queue = []
		queue.append(start)
		visited = [False]*(self.vertices+1)
		visited[start] = True
		visiting_pattern = [start]

		while queue:
			elem = queue.pop(0)
			adj = self.dict1[elem]
			for vertex in adj:
				if visited[vertex] == False:
					visited[vertex] = True
					queue.append(vertex)
					visiting_pattern.append(vertex)
		print("Visiting pattern:",visiting_pattern)

	@staticmethod
	def end():
		print("----------------------------------------------------")

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

start = input("Enter the starting vertex:")
start = int(start)
g.traverse(start)