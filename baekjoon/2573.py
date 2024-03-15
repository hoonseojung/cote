# import sys
# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline

# from collections import deque

# N, M = map(int, input().split())
# iceberg = list()
# for _ in range(N):
#   iceberg.append(list(map(int, input().split())))
# ices = deque() # 빙산의 좌표와 해당 좌표에서 바다에 얼마나 접해있는지

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def dfs_isone(x, y):
#   if iceberg[y][x] > 0 and visited[y][x] == 0:
#     visited[y][x] = 1
#     for i in range(4):
#       nx = x + dx[i]
#       ny = y + dy[i]
#       if nx < 0 or nx >= M or ny < 0 or ny >= N:
#         return
#       dfs_isone(nx, ny)

# for i in range(M):
#   for j in range(N):
#     if iceberg[j][i] > 0:
#       sea = 0
#       for k in range(4):
#         ni = i + dx[k]
#         nj = j + dy[k]
#         if iceberg[nj][ni] == 0: sea += 1
#       ices.append([i, j, sea])

# def melting():
#   melted = [[0 for _ in range(M)] for _ in range(N)]
#   ices_len = len(ices)
  
#   for _ in range(ices_len):
#     ice = ices.popleft()
#     if iceberg[ice[1]][ice[0]] <= ice[2]:
#       iceberg[ice[1]][ice[0]] = 0
#       for i in range(4):
#         nx = ice[0] + dx[i]
#         ny = ice[1] + dy[i]
#         melted[ny][nx] += 1
#       ices_len -= 1
#     else:
#       iceberg[ice[1]][ice[0]] -= ice[2]
#       ices.append(ice)
  
#   if ices_len == 0: return False
  
#   for _ in range(ices_len):
#     ice = ices.popleft()
#     ice[2] += melted[ice[1]][ice[0]]
#     ices.append(ice)

#   return True

# year = 1

# while True:
#   count = 0
  
#   if not melting():
#     print(0)
#     break
  
#   visited = [[0 for _ in range(M)] for _ in range(N)]
  
#   for ice in ices:
#       if visited[ice[1]][ice[0]] == 0:
#         dfs_isone(ice[0], ice[1])
#         count += 1
  
#   if count >= 2:
#     print(year)
#     break

#   year += 1

import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
iceberg = list()
for _ in range(N):
  iceberg.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs_isone(x, y):
  if iceberg[y][x] > 0 and visited[y][x] == 0:
    visited[y][x] = 1
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= M or ny < 0 or ny >= N:
        return
      dfs_isone(nx, ny)

def melting(iceberg):
  seas = deque([])
  for i in range(1, M-1):
    for j in range(1, N-1):
      if iceberg[j][i] > 0:
        check_list = [iceberg[j-1][i], iceberg[j+1][i], iceberg[j][i-1], iceberg[j][i+1]]
        seas.append(check_list.count(0))

  for i in range(1, M-1):
      for j in range(1, N-1):
        if iceberg[j][i] > 0:
          sea = seas.popleft()
          iceberg[j][i] -= sea
          if iceberg[j][i] < 0: iceberg[j][i] = 0
  
  return iceberg
          

year = 1

while True:
  count = 0
  
  iceberg = melting(iceberg)
  
  visited = [[0 for _ in range(M)] for _ in range(N)]
  
  for i in range(M):
    for j in range(N):
      if iceberg[j][i] > 0 and visited[j][i] == 0:
        dfs_isone(i, j)
        count += 1
    
  if count >= 2:
    print(year)
    break

  if sum(map(sum, iceberg)) == 0:
    print(0)
    break

  year += 1