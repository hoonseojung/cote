def solution(road, n):
	answer = 0
	damage = []
	for i in range(len(road)):
		if road[i] == '0':
			damage.append(i)
	
	if len(damage) <= n: return len(road)
	if (len(damage) == len(road)) and n == 0: return 0
	for i in range(len(damage)-n+1):
		if i == 0: start = 0
		else: start = damage[i-1] + 1
		
		if i == len(damage)-n: end = len(road)-1
		else: end = damage[i+n] -1
		
		if (end-start+1) > answer: answer = (end-start+1)
	
	return answer