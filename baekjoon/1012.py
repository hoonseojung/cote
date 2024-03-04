import sys
sys.setrecursionlimit(100000)

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(T):
  m, n, k = map(int, input().split()) # 가로, 세로, 배추 개수
  garden = [[0 for _ in range(m)] for _ in range(n)]
  visited = [[0 for _ in range(m)] for _ in range(n)]
  for _ in range(k):
    x, y = map(int, input().split())
    garden[y][x] = 1

  count = 0

  def dfs(x, y):
      global cnt
      if x < 0 or x >= n or y < 0 or y >= m:
          return
      if garden[x][y] == 1 and visited[x][y] == 0: # 연결되어 있고 방문하지 않았다면
          visited[x][y] = 1 # 방문했다는 표시
          for i in range(4):
              nx = x + dx[i]
              ny = y + dy[i]
              dfs(nx, ny)

  for i in range(n):
      for j in range(m):
          if garden[i][j] == 1 and visited[i][j] == 0:
              dfs(i, j)
              count += 1

  print(count)