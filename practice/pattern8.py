import sys
def solution(A):
	for i in range(A):
		left = i+1
		space = A-left
		highest = A-i
		gap = i*2
		print(left*"*" + space*" " + highest*"*" + gap*" " + highest*"*" + space*" " + left*"*")

a = 8
solution(a)

# *       *****************       *
# **      ********  *******      **
# ***     *******    ******     ***
# ****    ******      *****    ****
# *****   *****        ****   *****
# ******  ****          ***  ******
# ******* ***            ** *******
# **********              *********