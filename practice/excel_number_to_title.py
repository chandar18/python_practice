def squareSum(A):
	str1 = ""
	while A > 26:
		rem = A%26
		if rem == 0:
			rem = 26
		str1 += chr(rem+64)
		A = (A-1)//26
	
	str1 += chr(A+64)
	str1 = str1[::-1]
	return str1

val = 943566
#BAQTZ
#ZTQBA
print(squareSum(val))