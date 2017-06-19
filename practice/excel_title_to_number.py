def squareSum(A):
	sum1 = 0
	count = 0
	for i in range(len(A)-1,-1,-1):
		val = ord(A[i]) - 64
		sum1 += ((26**count)*val)
		count +=1
	return sum1

val = "CBA"
print(squareSum(val))