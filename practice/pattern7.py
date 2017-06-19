import sys
def solution(A):
	print(A*"*")
	dist = A-2
	for i in range(A-2):
		print("*" + dist*" " + "*")
	print(A*"*")
a = 7
solution(a)
