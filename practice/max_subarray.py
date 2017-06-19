def solution(A):
  max_so_far = max_ending_here = 0
  start = end = s = 0
  for i in A:
    max_ending_here += i
    if max_ending_here < 0:
      max_ending_here = 0
      s = i + 1
    else:
      if max_so_far < max_ending_here:
        max_so_far = max_ending_here
        end = A.index(i)
        start = s 

  if max_so_far == 0:
    max_so_far = max(A)
  print(start,end)
  return max_so_far

A = [1,2,3,-5,4]
A = [2, -1, 2, 3, 4, -5]
# A = [-1,-2,-3,-4]
print(solution(A))