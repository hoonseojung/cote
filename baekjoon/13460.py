from pprint import pprint
n, m = map(int,input().split())
MAP = []
for _ in range(n):
    MAP.append(list(map(str,input())))

def move(x, y, dx, dy):
    cnt = 0 # 움직인 횟수 - 빨간 공과 파란 공이 겹쳤을 때 분리해주기 위해 기억
    nx, ny = x, y
    while MAP[nx + dx][ny + dy] != '#' and MAP[nx][ny] != 'O': # 다음 좌표가 벽이 아니고 현재 좌표가 구멍이 아니면
        # = 다음 좌표가 벽이거나 현재 좌표가 구멍일 때까지 반복
        nx += dx
        ny += dy
        cnt += 1
    return nx, ny, cnt

for r in range(n):
    for c in range(m):
        if MAP[r][c] == 'R':
            # 빨간 공 시작 좌표
            rsx, rsy = r, c
        if MAP[r][c] == 'B':
            # 파란 공 시작 좌표
            bsx, bsy = r, c
        if MAP[r][c] == 'O':
            # 구멍 좌표
            ox, oy = r, c

def solution():
    visited = [[[] for _ in range(m)] for _ in range(n)] # 빨간 공 방문 좌표
    moves = [(-1,0),(1,0),(0,-1),(0,1)] # 상 하 좌 우
    visited[rsx][rsy] = 1 # 현재 빨간 공 위치
    s = [[rsx, rsy, bsx, bsy, 0]]

    while s:
        rx, ry, bx, by, cnt = s.pop()
        if cnt >= 10: # 10번째 움직였는데 반복문을 돌고 있다면 10번 이하로 움직여서 공을 꺼낼 수 없다는 뜻
            pprint(visited)
            return -1

        for dx, dy in moves:
            rrx, rry, rcnt = move(rx, ry, dx, dy)
            bbx, bby, bcnt = move(bx, by, dx, dy)

            if MAP[bbx][bby] != 'O': # 파란 공이 구멍에 들어가지 않았다면
                if rrx == ox and rry == oy:
                    pprint(visited)
                    return cnt + 1

                if rrx == bbx and rry == bby: # 두 공이 겹칠 수 없으므로, 겹친다면 공 별 움직인 횟수 확인해서 분리하기
                    if rcnt > bcnt: # 빨간 공이 더 움직였다면
                        rrx, rry = rrx-dx, rry-dy # 한 번 덜 움직이기
                    else: # 파란 공이 더 움직였다면
                        bbx, bby = bbx-dx, bby-dy # 한 번 덜 움직이기

                if visited[rrx][rry]: # 전에 갔던 위치라면 돌아가서 다른 방향으로 움직이기
                    continue
                else:
                    visited[rrx][rry] = 1 # 처음 간 위치라면 방문 체크
                    s.append([rrx, rry, bbx, bby, cnt+1]) # 새로운 위치와 현재까지 움직인 횟수 append
    pprint(visited)
    return -1

print(solution())