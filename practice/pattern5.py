import sys
def solution(A):
	for i in range(A):
		elem = i + 1
		left = A-elem
		print(left*" " +elem*"*")

a = 7
solution(a)
