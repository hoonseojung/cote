import sys
input = sys.stdin.readline
from collections import deque

def bfs(usado, start):
    q = deque()
    q.append(start)
    visited = [0] * (N+1)
    visited[start] = 1
    result = 0
    while q:
        curNode = q.popleft()
        for nextNode, value in node[curNode]:
            if visited[nextNode] == 0: # 연결된 다음 노드가 아직 방문 전이고
                if value >= usado: # 기준 값 이상이면
                    result += 1
                    q.append(nextNode)
                    visited[nextNode] = 1
    return result

N, Q = map(int, input().split())
node = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    node[a].append((b, c))
    node[b].append((a, c)) # (node, value)

for _ in range(Q):
    k, v = map(int, input().split())
    print(bfs(k, v))