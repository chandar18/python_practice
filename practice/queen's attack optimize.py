import time

def queens_attack(n,k,r,c,obs):
	start_time = time.time()
	arr = []
	count = 0
	obs_count = 0

	i = r
	j = c-1
	while j >= 1:
		if [i,j] not in obs:
			count += 1
			j -= 1
		else:
			obs.remove([i,j])
			break
	print(count)

	i = r+1
	j = c-1
	while i <=n and j >= 1:
		if [i,j] not in obs:
			count += 1
			j -= 1
			i += 1
		else:
			obs.remove([i,j])
			break
	print(count)

	i = r+1
	j = c
	while i <= n:
		if [i,j] not in obs:
			count += 1
			i += 1
		else:
			obs.remove([i,j])
			break
	print(count)

	i = r+1
	j = c+1
	while i <=n and j <= n:
		if [i,j] not in obs:
			count += 1
			j += 1
			i += 1
		else:
			obs.remove([i,j])
			break
	print(count)

	i = r
	j = c+1
	while j <= n:
		if [i,j] not in obs:
			count += 1
			j += 1
		else:
			obs.remove([i,j])
			break
	print(count)

	i = r-1
	j = c+1
	while i >= 1 and j <= n:
		if [i,j] not in obs:
			count += 1
			j += 1
			i -= 1
		else:
			obs.remove([i,j])
			break
	print(count)

	i = r-1
	j = c
	while i >= 1:
		if [i,j] not in obs:
			count += 1
			i -= 1
		else:
			obs.remove([i,j])
			break
	print(count)

	i = r-1
	j = c-1
	while i >= 1 and j >= 1:
		if [i,j] not in obs:
			count += 1
			i -= 1
			j -= 1
		else:
			obs.remove([i,j])
			break
	print(count)
	
	length = len(arr)
	#print(arr)
	print("%s seconds" % (time.time() - start_time))
	return count

n = 100000
k = 3
r = 4
c = 3
#obs = [[2,2],[4,2],[7,1],[7,4],[6,6],[4,7],[2,6],[2,4]]
obs=[[5,5],[4,2],[2,3],[2,2],[4,2],[7,1],[7,4],[6,6],[4,7],[2,6],[2,4]]
#obs = [[],[5,5],[4,2],[2,3]]
result = queens_attack(n,k,r,c,obs)
print(result)