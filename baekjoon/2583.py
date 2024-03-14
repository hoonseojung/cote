import sys
sys.setrecursionlimit(10**6)

M, N, K = map(int, input().split())
paper = [[0 for _ in range(N)] for _ in range(M)]
visited = [[0 for _ in range(N)] for _ in range(M)]

for _ in range(K):
  x1, y1, x2, y2 = map(int, input().split())
  for i in range(y1, y2):
    for j in range(x1, x2):
      paper[i][j] = 1

areas = []
count = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
      
def dfs(x, y):
  global count
  if x < 0 or x >= N or y < 0 or y >= M:
    return
  if paper[y][x] == 0 and visited[y][x] == 0:
    visited[y][x] = 1
    count += 1
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      dfs(nx, ny)

for i in range(N):
  for j in range(M):
    if paper[j][i] == 0 and visited[j][i] == 0:
      dfs(i, j)
      areas.append(count)
      count = 0

areas = sorted(areas)
print(len(areas))
for area in areas:
  print(area, end=' ')