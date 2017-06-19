from collections import defaultdict
n,m = input().split(' ')
n,m = int(n),int(m)
dict1 = defaultdict(lambda: [])
for ed in range(m):
  a,b = input().split(' ')
  a,b = int(a),int(b)
  if a not in dict1:
    dict1[a] = []
  if b not in dict1:
    dict1[b] = []
  dict1[a].append(b)
  dict1[b].append(a)

print(dict1)
print("Enter the query:")
q = int(input())
arr = []
for que in range(q):  
  a,b = input().split(' ')
  a,b = int(a),int(b)
  edge = []
  edge.append(a)
  edge.append(b)
  arr.append(edge)

for i in arr:
  if i[0] in dict1[i[1]]:
    print("YES")
  else:
    print("NO")

queue = [0]
visited = [0]
while queue:
  print(queue)
  vertex = queue.pop(0)
  con_ver = dict1[vertex]
  for i in con_ver:
    if i not in visited:
      visited.append(i)
      queue.append(i)

print(visited)