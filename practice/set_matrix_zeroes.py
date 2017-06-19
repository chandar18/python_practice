def Solution(A):
  if A is None or len(A) == 0:
    return

  first_row = False
  first_col = False

  if A[0][0] == 0:
    first_row = True
    first_col = True
  else:
    # for i in range(1,len(A[0])):
      # if A[0][i] == 0:
    if 0 in A[0]:
      first_row = True
        # break
    for i in range(1,len(A)):
      if A[i][0] == 0:
        first_col = True
        break

  for i in range(1,len(A)):
    for j in range(1,len(A[0])):
      if A[i][j] == 0:
        A[i][0] = 0
        A[0][j] = 0

  for i in range(1,len(A)):
    for j in range(1,len(A[0])):
      if A[i][0] == 0 or A[0][j] == 0:
        A[i][j] = 0

  print("A",first_col,first_row)
  if first_row:
    A[0] = [0]*len(A[0])
  if first_col:
    for i in range(len(A)):
      A[i][0] = 0
  return A

A = [[0,1,1,0],[1,1,0,1],[1,1,1,1]]
# A = [[0,0,0],[0,0,1]]
A = [[1,1],[0,0]]
print(Solution(A))