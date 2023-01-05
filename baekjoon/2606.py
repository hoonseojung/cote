from collections import deque

# n = 컴퓨터 개수, m = 쌍 개수
n = int(input())
m = int(input())

# 인접 0 행렬 생성 및 초기화
graph = [[0]*(n+1) for i in range(n+1)]

# 방문한 곳 체크할 리스트
visited = [0]*(n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a]+=[b]
    graph[b]+=[a]# 양방향 연결

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1
    # 큐 안에 데이터가 없을 때까지
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if(visited[i]==0):
                queue.append(i)
                visited[i] = 1
    print(sum(visited) - 2)

bfs(graph, 1, visited)