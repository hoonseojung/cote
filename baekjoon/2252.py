from collections import deque
n, m = map(int, input().split()) # n명, m번 비교
arr = []
inDegree = [0 for _ in range(32001)] # 최대 32000명, 연결되어 있는 위상 수, 앞에 오는 사람
graph = [[] for _ in range(32001)] # 뒤에 오는 사람
queue = deque()

for _ in range(m):
    a, b = map(int, input().split()) # 비교한 두 사람
    arr.append([a, b])

for a, b in arr:
    inDegree[b] += 1 # 위상 + 1
    graph[a].append(b) # 참조하고 있는 = 뒤에 오는 값 append

for i in range(1, n + 1): # 1번부터 n + 1명
    if inDegree[i] == 0: # 위상이 0인 경우 = 앞에 오는 값이 정해지지 않은 경우
        queue.append(i) # queue에 넣음

while queue:
    people = queue.popleft() #indegree가 0인 정점을 제거하고
    for j in graph[people]:
        inDegree[j] -= 1 # 해당 정점이 참조하고있던 점들의 indegree를 감소시킴
        if inDegree[j] == 0: # 이 점도 위상이 0이 된다면 queue에 append
            queue.append(j)
    print(people, end = ' ')