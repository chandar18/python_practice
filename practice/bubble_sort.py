import time

def bubbleSort(arr):
	start_time = time.time()
	n = len(arr)
	for i in range(n):
		for j in range(n-1-i):
			if arr[j] > arr[j+1]:
				temp = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp

	print("%s seconds" % (time.time() - start_time))

arr = [64, 34, 25, 12, 22, 11, 90]
 
bubbleSort(arr)

print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]),