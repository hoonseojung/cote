from collections import deque
import sys

sys.setrecursionlimit(10000)

def solution(maps):
    def dfs(x, y):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        count = 0
        if (x < 0) or (y < 0) or (x >= h) or (y >= w): # 범위 이외
            return count
        if maps[x][y] != 'X' and visited[x][y] is False: # 방문하지 않은 섬이면,
            visited[x][y] = True # 방문
            for i in range(4): # 상하좌우 확인
                count += dfs(x + dx[i], y + dy[i])
            return (int(maps[x][y]) + count) # 남아있는 일 추가
        return count

    answer = []
    h = len(maps)
    w = len(maps[0])
    visited = [[False for _ in range(w)] for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if maps[i][j] != 'X' and visited[i][j] is False:
                answer.append(dfs(i, j))
    
    if len(answer) == 0: answer.append(-1)
    
    return sorted(answer)