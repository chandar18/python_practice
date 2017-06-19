import time

def queens_attack(n,k,r,c,obs):
	start_time = time.time()
	count = 0

	lrr_obst = n
	ludr_obst = n
	ucc_obst = n
	rudr_obst = n
	rrr_obst = n
	rldr_obst = n
	lcc_obst = n
	lldr_obst = n

	for obs_arr in obs:

		if obs_arr[0] == r and obs_arr[1] < c:
			dist = abs(c - obs_arr[1])-1
			if dist < lrr_obst:
				lrr_obst = dist
	
		if obs_arr[0] > r and obs_arr[1] < c:
			if (r - obs_arr[0]) == (c - obs_arr[1]):
				dist = abs(r - obs_arr[0])-1
				if dist < ludr_obst:
					lrr_obst = dist
					print("LUD",obs_arr)

		if obs_arr[0] > r and obs_arr[1] == c:
			print("UCC",obs_arr)
			dist = abs(r - obs_arr[0])-1
			if dist < ucc_obst:
				ucc_obst = dist

		if obs_arr[0] > r and obs_arr[1] > c:
			if (r - obs_arr[0]) == (c - obs_arr[1]):
				dist = abs(r - obs_arr[0])-1
				if dist < rudr_obst:
					rudr_obst = dist
					print("RUD",obs_arr)

		if obs_arr[0] == r and obs_arr[1] > c:
			print("RR",obs_arr)
			dist = abs(c - obs_arr[1])-1
			if dist < rrr_obst:
				rrr_obst = dist

		if obs_arr[0] < r and obs_arr[1] > c:
			if (r - obs_arr[0]) == (c - obs_arr[1]):
				dist = abs(r - obs_arr[0])-1
				if dist < rldr_obst:
					rldr_obst = dist
					print("RLD",obs_arr)

		if obs_arr[0] < r and obs_arr[1] == c:
			print("LC",obs_arr)
			dist = abs(r - obs_arr[0])-1
			if dist < lcc_obst:
				lcc_obst = dist

		if obs_arr[0] < r and obs_arr[1] < c:
			if (r - obs_arr[0]) == (c - obs_arr[1]):
				dist = abs(r - obs_arr[0])-1
				if dist < lldr_obst:
					lldr_obst = dist
					print("LLD",obs_arr)

	if lrr_obst == n:
		lrr_obst = abs(c-1)

	if ludr_obst == n:
		ludr_obst = min(abs(n-r),abs(c-1))

	if ucc_obst == n:
		ucc_obst = abs(n-r)

	if rudr_obst == n:
		rudr_obst = min(abs(n-r),abs(n-c))

	if rrr_obst == n:
		rrr_obst = abs(n-c)

	if rldr_obst == n:
		rldr_obst = min(abs(r-1),abs(n-c))

	if lcc_obst == n:
		lcc_obst = abs(r-1)

	if lldr_obst == n:
		lldr_obst = min(abs(r-1),abs(c-1))

	print(lrr_obst, ludr_obst, ucc_obst, rudr_obst, rrr_obst, rldr_obst, lcc_obst, lldr_obst)
	count = lrr_obst + ludr_obst + ucc_obst + rudr_obst + rrr_obst + rldr_obst + lcc_obst + lldr_obst

	print("%s seconds" % (time.time() - start_time))
	return count

n = 5
k = 3
r = 4
c = 3
#obs = [[2,2],[4,2],[7,1],[7,4],[6,6],[4,7],[2,6],[2,4]]
#obs=[[5,5],[4,2],[2,3],[2,2],[4,2],[7,1],[7,4],[6,6],[4,7],[2,6],[2,4]]
obs = [[5,5],[4,2],[2,3]]
#obs = []
result = queens_attack(n,k,r,c,obs)
print(result)