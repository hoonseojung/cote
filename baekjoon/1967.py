import sys
sys.setrecursionlimit(10**5)

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
  p, c, w = map(int, input().split())
  tree[p].append([c, w])
  tree[c].append([p, w])

visited = [-1 for _ in range(n+1)]

def dfs(x, c):
  if x > n: return
  for v, w in tree[x]:
    if tree[v] != [] and visited[v] == -1:
      visited[v] = c+w
      dfs(v, c+w)

visited[1] = 0
dfs(1, 0)
# print(visited) -> [-1, 0, 3, 2, 8, 13, 11, 9, 15, 28, 17, 17, 21]
max_v = [0, 0] # [v, w]
for i in range(2, n+1):
  if visited[i] > max_v[1]: max_v = [i, visited[i]]

visited = [-1 for _ in range(n+1)]
visited[max_v[0]] = 0
dfs(max_v[0], 0)
print(max(visited))