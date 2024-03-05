import sys
sys.setrecursionlimit(1000000)

N = int(input())

picture = []
visible = [0, 0]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
colors = ['R', 'G', 'B']

for _ in range(N):
  picture.append(list(input()))

def dfs(x, y, color):
  if x < 0 or x >= N or y < 0 or y >= N:
    return
  if picture[x][y] == color and visited[x][y] == 0:
    visited[x][y] = 1
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      dfs(nx, ny, color)

for idx in range(2):
  for color in colors:
    count = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
      for j in range(N):
        if picture[i][j] == color and visited[i][j] == 0:
          dfs(i, j, color)
          count += 1

    visible[idx] += count
  
  if idx == 0: 
    colors.remove('G')
    for i in range(N):
      for j in range(N):
        if picture[i][j] == 'G': picture[i][j] = 'R'

for v in visible:
  print(v, end=' ')