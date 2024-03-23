def solution(n, k, beg, end):
	answer -= 1
	building = [[] for _ in range(n+1)]
	visited = [0 for _ in range(n+1)]
	
	for i in range(k):
		building[beg[i]].append(end[i])
		building[end[i]].append(beg[i])
		
	def dfs(x):
		if x < 0 or x >= n+1: return
		connect = building[x]
		for i in connect:
			if building[i] != [] and visited[i] == 0:
				visited[i] = 1
				dfs(i)
	
	for i in range(1, n+1):
		if building[i] != [] and visited[i] == 0:
			dfs(i)
			answer += 1
		elif building[i] == [] and visited[i] == 0:
			visited[i] = 1
			answer += 1