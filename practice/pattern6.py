import sys
def solution(A):
	highest = A*2
	for i in range(A):
		elem = (i*2 + 2)//2
		print(elem*"*" + " " +elem*"*")

a = 5
solution(a)
