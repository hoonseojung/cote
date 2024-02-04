from collections import deque

dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
INF = float('inf')

def solution(board):
    n, m = len(board), len(board[0])
    for y in range(n):
        for x in range(m):
            if board[y][x] == 'R': # 시작점
                s_y, s_x = y, x
            elif board[y][x] == 'G': # 타겟
                t_y, t_x = y, x

    counts = [[INF] * m for _ in range(n)]
    counts[s_y][s_x] = 0
    dq = deque([[s_y, s_x, 0]])
    while dq:
        if counts[t_y][t_x] != INF:
            return counts[t_y][t_x]

        cur_y, cur_x, cur_count = dq.popleft()

        for dy, dx in dxy:
            p_y, p_x, p_count = cur_y, cur_x, cur_count
            moved = False
            while (0 <= p_y + dy < n) and (0 <= p_x + dx < m) and board[p_y + dy][p_x + dx] != 'D':
                p_y += dy
                p_x += dx
                moved = True
            if moved:
                p_count += 1
                if p_count < counts[p_y][p_x]:
                    counts[p_y][p_x] = p_count
                    dq.append([p_y, p_x, p_count])

    return -1