N = int(input()) # 지도의 크기

graph = [list(map(int, input())) for _ in range(N)] # 배열 생성
# visited = [[0 for _ in range(N)] for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

count = []
cnt = 0

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y > N:
        return
    global cnt
    # 재귀
    for i in range(N):
        for j in range(N):
            if graph[i][j]==1: # 아직 방문하지 않았고, 단지 내에 연결되어 있다면
                cnt += 1
                graph[i][j] = 0
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    dfs(nx, ny)
    count.append(cnt)
    cnt = 0

dfs(0, 0)
count = sorted(count)
print(len(count))
print(count[i] for i in range(len(count)))