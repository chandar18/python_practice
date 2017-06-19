#Works in Python 2.7.... copied
class Solution:
	# @param A : tuple of integers
	# @return a strings
	def largestNumber(self, A):
		a = map(str, A)
		a.sort(cmp_items, reverse = True)
		return ''.join(a).lstrip('0') or '0'
    
def cmp_items(a, b):
	if int(a+b) > int(b+a):
		return 1
	elif int(a+b) == int(b+a):
		return 0
	else:
		return -1

sols = Solution()
A = [3, 34, 30 ,5, 9]
print(sols.largestNumber(A))