import time

def mergeSort(arr,low,high):
	if low < high:
		mid  = (low + (high-1))//2
		mergeSort(arr, low, mid)
		mergeSort(arr, mid + 1, high)
		merge(arr, low, mid, high)

def merge(arr, l, m, h):
	b = [0] * len(arr)
	low = l
	med = m
	count = l - 1
	while low <= m and med+1 <= h:
		if arr[low] < arr[med+1]:
			count += 1
			b[count] = arr[low]
			low += 1
		else:
			count += 1
			b[count] = arr[med+1]
			med += 1

	if low <= m:
		for i in range(low,m+1):
			count +=1 
			b[count] = arr[i]
	elif med+1 <= h:
		for i in range(med+1,h+1):
			count +=1
			b[count] = arr[i]
	
	for i in range(l,h+1):
		arr[i] = b[i]

arr = [64, 34, 25, 12, 22, 11, 90]
 
start_time = time.time()
mergeSort(arr,0,len(arr)-1)
print("%s seconds" % (time.time() - start_time))

print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]),