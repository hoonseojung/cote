def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    def dfs(x):
        visited[x] = True
        for idx, computer in enumerate(computers[x]):
            if idx == x: continue
            if computer == 1 and not visited[idx]:
                dfs(idx)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    return answer