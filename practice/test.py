def segregate(A):
	j = 0
	for i in range(len(A)):
		if A[i] <= 0:
			A[i], A[j] = A[j], A[i]
			j += 1

	return j

def Solution(A):
	index = segregate(A)
	
	return num

A = [2, 3, 7, 6, 8, -1, -10, 15]
print(Solution(A))