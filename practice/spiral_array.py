def spiralOrder(A):
  result = []
  ## Actual code to populate result
  m = len(A)
  n = len(A[0])
  k = 0
  l = 0
  while k < m and l < n:
    #Print the first row from the remaining rows
    for i in range(l,n):
        result.append(A[k][i])
    k += 1

    #Print the last column from the remaining columns */
    for i in range(k,m):
        result.append(A[i][n-1])
    n -= 1

    #Print the last row from the remaining rows */
    if (k<m):
        for i in range(n-1,l-1,-1):
            result.append(A[m-1][i])
        m -= 1

    #Print the first column from the remaining columns */
    if (l<n):
      for i in range(m-1,k-1,-1):
          result.append(A[i][l])
      l += 1
    
  return result

#A = [[1,2,3],[4,5,6],[7,8,9]]
#A = [[1,2]]
A = [[313, 157, 290, 113, 119, 118, 187, 360, 104, 365, 197, 103, 355, 240, 337, 174, 138, 252]]
#A = [[335, 401, 128, 384, 345, 275, 324, 139, 127, 343, 197, 177, 127, 72, 13, 59],[102, 75, 151, 22, 291, 249, 380, 151, 85, 217, 246, 241, 204, 197, 227, 96],[261, 163, 109, 372, 238, 98, 273, 20, 233, 138, 40, 246, 163, 191, 109, 237],[179, 213, 214, 9, 309, 210, 319, 68, 400, 198, 323, 135, 14, 141, 15, 168]]
print(spiralOrder(A))