import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

M, N = map(int, input().split())
travel_map = list()
for _ in range(M):
  travel_map.append(list(map(int, input().split())))
visited = [[-1 for _ in range(N)] for _ in range(M)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
  if x == N-1 and y == M-1:
    return 1
  
  if visited[y][x] != -1:
    return visited[y][x]
  
  visited[y][x] = 0

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
      continue
    if travel_map[ny][nx] < travel_map[y][x]:
      visited[y][x] += dfs(nx, ny)
  
  return visited[y][x]

print(dfs(0, 0))
# print(visited)
# [[3, 2, 2, 2, 1], 
#  [1, -1, -1, 1, 1], 
#  [1, -1, -1, 1, -1], 
#  [1, 1, 1, 1, -1]]
# 평범하게 DFS로 풀면 시간 초과가 나는 문제, visited 그래프를 dp 테이블로 이용해서 초기 값을 -1로 설정하고, 이동하면서 0으로 바꾸며 마지막 위치에 닿으면 1을 return하여 각 방법마다 경우의 수를 더해주는 방식