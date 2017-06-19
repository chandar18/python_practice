def Solution(A):
  ans = []
  A = sorted(A)
  for i in range(1,len(A),2):
    ans.append(A[i])
    ans.append(A[i-1])

  if(len(A)%2 == 1):
    ans.append(A[len(A)-1])
  return ans

A = [ 11, 8, 7, 9, 2, 10, 2 ]
print(Solution(A))