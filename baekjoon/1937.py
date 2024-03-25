import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
forest = list()
for i in range(n):
  forest.append(list(map(int, input().split())))

max_move = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0 for _ in range(n)] for _ in range(n)]

def dfs(x, y):
  if visited[y][x] > 0: return visited[y][x]
  visited[y][x] = 1
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < n and forest[ny][nx] > forest[y][x]:
      visited[y][x] = max(visited[y][x], dfs(nx, ny) + 1)
  return visited[y][x]

for i in range(n):
  for j in range(n):
    max_move = max(max_move, dfs(i, j))

print(max_move)

# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# n = int(input())
# forest = list()
# for i in range(n):
#   forest.append(list(map(int, input().split())))

# max_move = 0
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# visited = [[False for _ in range(n)] for _ in range(n)]

# def dfs(x, y, move):
#   global max_move
#   visited[y][x] = True
#   max_move = max(max_move, move)
#   for i in range(4):
#     nx = x + dx[i]
#     ny = y + dy[i]
#     if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
#     if not visited[ny][nx] and forest[ny][nx] > forest[y][x]:
#       dfs(nx, ny, move+1)
#   visited[y][x] = False

# for i in range(n):
#   for j in range(n):
#     dfs(i, j, 1)

# print(max_move)