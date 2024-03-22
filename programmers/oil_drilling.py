import sys
sys.setrecursionlimit(1000000)

def solution(land):
    answer = list()
    oils = list()
    
    n = len(land)
    m = len(land[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    count = 0
    
    def dfs(x, y, l):
        nonlocal count
        if x < 0 or x >= m or y < 0 or y >= n: return
        if land[y][x] == 1 and visited[y][x] == 0:
            visited[y][x] = l
            count += 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                dfs(nx, ny, l)
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visited[i][j] == 0:
                l = len(oils)+1
                dfs(j, i, l)
                oils.append(count)
                count = 0
    
    for i in range(m):
        total = set()
        for j in range(n):
            total.add(visited[j][i])
        total = list(total)
        for i in range(len(total)):
            if total[i] > 0: total[i] = oils[total[i]-1]
        answer.append(sum(total))
    
    return max(answer)