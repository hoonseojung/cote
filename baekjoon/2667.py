N = int(input()) # 지도의 크기

graph = [list(map(int, input())) for _ in range(N)] # 배열 생성
visited = [[0 for _ in range(N)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = []
cnt = 0

def dfs(x, y):
    global cnt
    if x < 0 or x >= N or y < 0 or y >= N:
        return
    if graph[x][y] == 1 and visited[x][y] == 0: # 연결되어 있고 방문하지 않았다면
        cnt += 1
        visited[x][y] = 1 # 방문했다는 표시
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == 0:
            dfs(i, j)
            count.append(cnt)
            cnt = 0

count = sorted(count)
print(len(count))
for i in range(len(count)):
    print(count[i])
