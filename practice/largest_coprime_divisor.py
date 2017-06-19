def gcd(A,B):
	if A == 0:
		return B
	return gcd(B%A, A)

def Solution(A,B):
	while gcd(A,B) != 1:
		A = A/gcd(A,B)
	return int(A)

print(Solution(30,12))