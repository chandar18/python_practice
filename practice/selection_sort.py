import time

def selectionSort(arr):
	start_time = time.time()
	n = len(arr)
	for i in range(n):
		pos = i
		for j in range(i+1,n):
			if arr[j] < arr[i]:
				pos = j
		arr[pos], arr[i] = arr[i], arr[pos]

	print("%s seconds" % (time.time() - start_time))

arr = [64, 34, 25, 12, 22, 11, 90]
 
selectionSort(arr)

print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]),