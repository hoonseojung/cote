import sys
input = sys.stdin.readline

R, C = map(int, input().split())

board = list()
for _ in range(R):
  board.append(list(map(str, input())))

visited = {chr(i):0 for i in range(65, 91)}
answer = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, count):
  global answer
  answer = max(answer, count)

  visited[board[x][y]] = 1
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx >= R or ny < 0 or ny >= C:
      continue
    if visited[board[nx][ny]] == 0:
      dfs(nx, ny, count+1)

  visited[board[x][y]] = 0
  
if visited[board[0][0]] == 0:
    dfs(0, 0, 1)
    print(answer)