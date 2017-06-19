def solution(A):
  slow = A[0];
  fast = A[A[0]];
  while (slow != fast):
    slow = A[slow];
    fast = A[A[fast]];
    # print("S",slow)
    # print("F",fast)
  # print(slow,fast)
  fast = 0;
  while (slow != fast):
    slow = A[slow];
    fast = A[fast];
    # print("S",slow)
    # print("F",fast)
  return slow;
A = [1,4,2,5,3,6,7,5]
print(solution(A))