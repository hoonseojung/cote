import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def bfs(N, tree):
	q = deque([1])
	parent = [0 for _ in range(N+1)]

	while q:
		now = q.popleft()
		for i in tree[now]:
			if (parent[i] == 0) and (i != 1):
				parent[i] = now
				q.append(i)
	for i in range(2, N+1):
		print(parent[i])

N = int(input())
tree = defaultdict(list)

for _ in range(N-1):
  n1, n2 = map(int, input().split())
  tree[n1].append(n2)
  tree[n2].append(n1)

bfs(N, tree)