import sys
def solution(A):
	highest = 2*(A//2)+1
	for i in range(A//2):
		elem = 2*i + 1
		left = (highest-elem)//2
		print(left*" " +elem*"*"+left*" " )

	print(A*"*")
	for i in range(A//2-1,-1,-1):
		elem = 2*i + 1
		left = (highest-elem)//2
		print(left*" " +elem*"*"+left*" " )

a = 7
solution(a)
