def Solution(A):
  for i in range(len(A)//2):
    for j in range(i,len(A)-i-1):
      print(i,j)
      pos = len(A)-1-i
      elem = len(A)-1-j
      temp = A[j][pos]
      A[j][pos] = A[i][j]
      A[i][j] = A[elem][i]
      A[elem][i] = A[pos][elem]
      A[pos][elem] = temp
      print(A)
  return A

A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# A = [[1,2],[3,4]]
print(Solution(A))