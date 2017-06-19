#Given a matrix, find the path from top left to bottom right with the greatest product by moving only down and right.
def Solution(A):
	maxi = [[0 for x in range(len(A[0]))] for y in range(len(A))]
	mini = [[0 for x in range(len(A[0]))] for y in range(len(A))]
	maxi[0][0] = A[0][0]
	mini[0][0] = A[0][0]
	for i in range(1,len(A[0])):
		maxi[0][i] = maxi[0][i-1]*A[0][i]
		maxi[i][0] = maxi[i-1][0]*A[i][0]
		mini[0][i] = mini[0][i-1]*A[0][i]
		mini[i][0] = mini[i-1][0]*A[i][0]
	
	for i in range(1,len(A)):
		for j in range(1,len(A)):
			top_maxi = max(A[i][j] * maxi[i-1][j], A[i][j] * mini[i-1][j])
			left_maxi = max(A[i][j] * maxi[i][j-1], A[i][j] * mini[i][j-1])
			top_mini = min(A[i][j] * mini[i-1][j], A[i][j] * maxi[i-1][j])
			left_mini = min(A[i][j] * mini[i][j-1], A[i][j] * maxi[i][j-1]) 
			maxi[i][j] = max(top_maxi, left_maxi)
			mini[i][j] = min(top_mini, left_mini)

	# print(maxi)
	# print(mini)
	return max(maxi[len(A)-1][len(A)-1], mini[len(A)-1][len(A)-1])
  
A = [[-1,2,3],[4,5,6],[7,8,9]]
print(Solution(A))
