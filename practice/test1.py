from functools import cmp_to_key
class Solution:
	# @param {integer[]} nums
	# @return {string}
	def largestNumber(self, nums):
		sorted_nums = sorted(map(str, nums), key=cmp_to_key(lambda x, y: int(y + x) - int(x + y)))
		result = ''.join(sorted_nums).lstrip('0')
		return result or '0'
if __name__ == "__main__":
	print(Solution().largestNumber([3, 30, 34, 5, 9]) == '9534330')