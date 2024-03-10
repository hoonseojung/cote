import sys
sys.setrecursionlimit(1000000)

# 상 / 하 / 좌 / 우 / 우하 / 좌하 / 우상 / 좌상
dx = [0, 0, -1, 1, 1, -1, 1, -1]
dy = [-1, 1, 0, 0, 1, 1, -1, -1]

def dfs(x, y, w, h):
  if x < 0 or x >= h or y < 0 or y >= w:
    return
  if island[x][y] == 1 and visited[x][y] == 0:
    visited[x][y] = 1
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      dfs(nx, ny, w, h)

while True:
  w, h = map(int, input().split())
  if (w==0) and (h==0): break
  count = 0
  visited = [[0 for _ in range(w)] for _ in range(h)]
  island = list()
  for _ in range(h):
    island.append(list(map(int, input().split())))

  for i in range(h):
    for j in range(w):
      if island[i][j] == 1 and visited[i][j] == 0:
        dfs(i, j, w, h)
        count += 1
  
  print(count)