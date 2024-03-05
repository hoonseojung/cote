import sys
sys.setrecursionlimit(1000000)

N = int(input())
area = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
  area.append(list(map(int, input().split())))

min_val = 101
max_val = 0
safe_area = [1]

for i in range(N):
  for j in range(N):
    if area[i][j] > max_val: max_val = area[i][j]
    if area[i][j] < min_val: min_val = area[i][j]

print(max_val, min_val)
for ref in range(min_val, max_val):
  count = 0
  visited = [[0 for _ in range(N)] for _ in range(N)]
  
  def dfs(x, y):
      if x < 0 or x >= N or y < 0 or y >= N:
          return
      if area[x][y] > ref and visited[x][y] == 0:
          visited[x][y] = 1
          for i in range(4):
              nx = x + dx[i]
              ny = y + dy[i]
              dfs(nx, ny)

  for i in range(N):
    for j in range(N):
      if area[i][j] > ref and visited[i][j] == 0:
         dfs(i, j)
         count += 1

  safe_area.append(count)

print(max(safe_area))