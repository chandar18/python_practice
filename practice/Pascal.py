import math
def fact(num):
  if num == 1 or num == 0:
    return 1
  else:
    return num*fact(num-1)

def comb(u,l):
  number = fact(u)//(fact(l)*fact(u-l))
  return number
  
def Solution(A):
  arr = []
  if A%2 == 0:
    for i in range(A//2):
      num = comb(A-1,i)
      arr.append(num)
  
    for i in range(len(arr)-1,-1,-1):
      arr.append(arr[i])  
  else:
    for i in range((math.ceil(A/2))):
      num = comb(A-1,i)
      arr.append(num)
  
    for i in range(len(arr)-2,-1,-1):
      arr.append(arr[i])

  return arr

print("Enter the number")
num = int(input())
print(Solution(num))