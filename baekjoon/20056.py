N, M, K = map(int, input().split()) # N:격자, M:파이어볼 개수, K:이동 횟수

graph = [[[] for _ in range(N)] for _ in range(N)] # N x N 격자
fire_ball = [] # x, y, 중량, 속력, 방향
for i in range(M):
    x, y, m, s, d = list(map(int, input().split()))
    fire_ball.append([x-1, y-1, m, s, d])

def init_graph():
    global graph
    graph = [[[] for _ in range(N)] for _ in range(N)]

def ball_move():
    init_graph()
    for i in range(M):
        # x 좌표
        if fire_ball[i][4] == 1 or fire_ball[i][4] == 2 or fire_ball[i][4] == 3:
            fire_ball[i][1] += fire_ball[i][3]
            fire_ball[i][1] %= N # N번 행과 1번 행 연결
        elif fire_ball[i][4] == 5 or fire_ball[i][4] == 6 or fire_ball[i][4] == 7:
            fire_ball[i][1] -= fire_ball[i][3]
            if fire_ball[i][1] <= 0:    
                fire_ball[i][1] += N # 1번 행과 N번 행 연결
        # y 좌표
        if fire_ball[i][4] == 3 or fire_ball[i][4] == 4 or fire_ball[i][4] == 5:
            fire_ball[i][0] += fire_ball[i][3]
            fire_ball[i][0] %= N # N번 열과 1번 열 연결
        elif fire_ball[i][4] == 0 or fire_ball[i][4] == 1 or fire_ball[i][4] == 7:
            fire_ball[i][0] -= fire_ball[i][3]
            if fire_ball[i][0] <= 0:    
                fire_ball[i][0] += N # 1번 열과 N번 열 연결
        graph[fire_ball[i][0]][fire_ball[i][1]].append([fire_ball[i][2], fire_ball[i][3], fire_ball[i][4]]) # 무게, 속력, 방향
    
    # for i in range(M): # 겹치는지 확인
    #     tmp = [] # 겹치는 파이어볼
    #     for j in range(M):
    #         if i == j:
    #             continue
    #         if check[fire_ball[i][0]-1][fire_ball[i][1]-1] == 0: # 아직 비교 안 해본 좌표이고
    #             if fire_ball[i][0] == fire_ball[j][0]: # x 좌표가 겹치는데
    #                 if fire_ball[i][1] == fire_ball[j][1]: # y 좌표도 겹치는게 있다면
    #                     graph[fire_ball[j][0]-1][fire_ball[j][1]-1] += fire_ball[j][2]
    #                     tmp.append(j)
    #     if graph[fire_ball[i][0]-1][fire_ball[i][1]-1] != 0:
    #         graph[fire_ball[i][0]-1][fire_ball[i][1]-1] += fire_ball[i][2]
    #         tmp.append(i)
    #         check[fire_ball[i][0]-1][fire_ball[i][1]-1] = tmp # 해당 좌표에 겹치는 파이어볼
    
    # for i in range(M):
    #     for j in range(M):
    #         if graph[i][j] != 0: # 겹치는게 있는 좌표라면
    
    # m, s = 0
    # for i in range(M):
    #     if len(check[fire_ball[i][0]][fire_ball[i][1]]) > 1: # 겹치는게 있다면
    #         for j in range(len(check[fire_ball[i][0]][fire_ball[i][1]])):
    #             m += fire_ball[check[fire_ball[i][0]][fire_ball[i][1]][j]][2]
    #             s += fire_ball[check[fire_ball[i][0]][fire_ball[i][1]][j]][3]
    #         m = int(m/5)
    #         s = int(s/len(check[fire_ball[i][0]][fire_ball[i][1]]))
    #         if m > 0:
    #             for j in range(len(check[fire_ball[i][0]][fire_ball[i][1]])): # 겹치는게 있다면
    #                 fire_ball.pop(check[fire_ball[i][0]][fire_ball[i][1]][j])
    #             fire_ball.append([fire_ball[i][0], fire_ball[i][1], m, ])
    for x in range(N):
        for y in range(N):
            if len(graph[x][y]) > 1: # 겹치는게 있다면
                m, s, o, e = 0, 0, 0, 0 # 무게, 속력, 방향(짝수), 방향(홀수)
                for i in range(len(graph[x][y])):
                    m += graph[x][y][i][0]
                    s += graph[x][y][i][1]
                    if graph[x][y][i][2] % 2: # 홀수
                        o += 1
                    else: # 짝수
                        e += 1
                m = int(m/5)
                s = int(s/len(graph[x][y]))
                if o == len(graph[x][y]) or e == len(graph[x][y]): # 방향이 전부 짝수이거나 홀수인 경우
                    d = [0, 2, 4, 6]
                else:
                    d = [1, 3, 5, 7]
                
                for ball in fire_ball[::]: # 해당 좌표에서 합쳐진 파이어볼 제거
                    if ball[0] == x and ball[1] == y:
                        fire_ball.remove(ball)
                if m > 0:
                    for i in range(4): # 4개로 쪼개진 파이어볼 추가
                        fire_ball.append([x, y, m, s, d[i]])

for _ in range(K):
    ball_move()

print(fire_ball)
print(sum(ball[2] for ball in fire_ball))