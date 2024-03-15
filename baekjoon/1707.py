import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

K = int(input())
answers = []

def dfs(x):
  global answer
  for i in graph[x]:
    if visited[i] == 1:
      if colors[i] == colors[x]:
        answer = False
        return
      else: continue
    else:
      visited[i] = 1
      colors[i] = colors[x] * (-1)
      dfs(i)
  
for _ in range(K):
  answer = True
  V, E = map(int, input().split())
  graph = [[] for _ in range(V+1)]
  visited = [0 for _ in range(V+1)]
  colors = [0 for _ in range(V+1)]
  for _ in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
  
  for i in range(1, V+1):
    if visited[i] == 0:
      visited[i] = 1
      colors[i] = 1
      dfs(i)
    if not answer:
      answers.append("NO")
      break
  else:
    answers.append("YES")

for ans in answers:
  print(ans)