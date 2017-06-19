import time

def insertionSort(arr):
	start_time = time.time()
	n = len(arr)
	for i in range(1,n):
		key = arr[i]
		j = i-1
		while j>=0 and key < arr[j]:
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = key

	print("%s seconds" % (time.time() - start_time))

arr = [64, 34, 25, 12, 22, 11, 90]
# arr = [11, 12, 22, 25, 34, 64, 90]
 
insertionSort(arr)

print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]),