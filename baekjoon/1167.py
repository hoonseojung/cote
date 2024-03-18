V = int(input())
trees = [[] for _ in range(V+1)]
visited = [-1 for _ in range(V+1)]

for i in range(V):
  infos = list(map(int, input().split()))
  for j in range(1, len(infos)-1, 2):
    trees[infos[0]].append((infos[j], infos[j+1]))

def dfs(x, dist):  
  for v, d in trees[x]:
    if visited[v] == -1:
      visited[v] = dist + d
      dfs(v, dist+d)

visited[1] = 0
dfs(1, 0)

tmp = [0, 0] # v, d
for i in range(1, V+1):
  if visited[i] > tmp[1]:
    tmp[1] = visited[i]
    tmp[0] = i

visited = [-1 for _ in range(V+1)]
visited[tmp[0]] = 0
dfs(tmp[0], 0)
print(max(visited))