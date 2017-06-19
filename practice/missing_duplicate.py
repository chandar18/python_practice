def duplicate(A):
  xors = 0
  for i in range(1,len(A)+1):
    xors = xors ^ i
  for i in A:
    xors = xors ^ i
  x = y = 0
  print("XOR",xors)
  arr = []
  v = xors & (~(xors-1))
  print("V",v)
  for i in A:
    if i & v:
      arr.append(i)
      x = x ^ i
    else:
      y = y ^ i

  for i in range(1,len(A)+1):
    if i & v:
      arr.append(i)
      x = x ^ i
    else:
      y = y ^ i
  print(arr)
  print("Repeating X",x)
  print("Missing Y",y)

A = [1, 2, 6, 3, 6, 4]
duplicate(A)