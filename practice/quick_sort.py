import time

def quickSort(arr,low,high):
	if low < high:
		pi = partition(arr, low, high)
		quickSort(arr, low, pi)
		quickSort(arr, pi + 1, high)

def partition(arr, low, high):
	pivot = arr[low]
	i = low
	for j in range(low+1,high):
		if arr[j] <= pivot:
			i += 1
			arr[j], arr[i] = arr[i], arr[j]
	arr[low], arr[i] = arr[i], arr[low]
	return i


arr = [64, 34, 25, 12, 22, 11, 90]
 
start_time = time.time()
quickSort(arr,0,len(arr))
print("%s seconds" % (time.time() - start_time))

print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]),