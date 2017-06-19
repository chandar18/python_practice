def solution(A):
  max_so_far = max_ending_here = 0
  start = end = s = l = 0
  last_end = 0
  len_so_far = 0
  for i in range(len(A)):
    if A[i] >= 0:
      max_ending_here += A[i]
      l += 1
      if i == len(A)-1:
        if max_so_far < max_ending_here:
          max_so_far = max_ending_here
          len_so_far = l
          end = i
        elif max_so_far == max_ending_here:
          if l > len_so_far:
            len_so_far = l
            end = i-1
    else:
      if max_so_far < max_ending_here:
        max_so_far = max_ending_here
        len_so_far = l
        end = i-1
      elif max_so_far == max_ending_here:
        if l > len_so_far:
          len_so_far = l
          end = i-1
      max_ending_here = 0
      l = 0

  start = end-len_so_far+1
  print(A[start:end+1])
  return max_so_far

A = [1,2,3,-5,4]
A = [4,5,-3,2,-1, 2, 3, 4,-5,2,5,2]
# A = [-1,-2,-3,-4]
A = [ -1, -1, -1, -1, -1 ]
print(solution(A))