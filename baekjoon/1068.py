N = int(input())
tree = [[] for _ in range(N)]
deleted = [False for _ in range(N)]
root = -1
count = 0
infos = list(map(int, input().split()))
V = int(input())
deleted[V] = True
for v, info in enumerate(infos):
  if info == -1: 
    root = v
    continue
  if v == V: continue
  if deleted[info]: deleted[v] = True
  else: tree[info].append(v)

def dfs(x):
  global count
  for v in tree[x]:
    if tree[v] == []: count += 1
    else: dfs(v)

if root == V: print(0)
elif tree[root] == []: print(1)
else:
  dfs(root)
  print(count)