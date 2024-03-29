import sys
sys.setrecursionlimit(10**6)

def dfs(x):
    global count
    visited[x] = True
    teamed.append(x)
    if visited[students[x]]:
        if students[x] in teamed:
            count -= len(teamed[teamed.index(students[x]):])
        return
    else: dfs(students[x])

T = int(input())
for _ in range(T):
  n = int(input())
  students = list(map(int, input().split()))
  students.insert(0, 0)
  visited = [False for _ in range(n+1)]
  count = n
  for i in range(1, n+1):
    if not visited[i]:
       teamed = list()
       dfs(i)
  
  print(count)