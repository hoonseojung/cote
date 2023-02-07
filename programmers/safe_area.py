from collections import deque
def solution(board):
    answer = 0
    n = len(board)
    visited = [[0 for _ in range(n)] for _ in range(n)]
    dx = [-1, 1, 0, 0, -1, 1, -1, 1]
    dy = [0, 0, -1, 1, 1, -1, -1, 1]
    bomb = [(i, j) for i in range(n) for j in range(n) if board[i][j]==1]
    for r, c in bomb:
        q = deque()
        q.append((r, c))
        while q:
            x, y = q.popleft()
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                    board[nx][ny] = 1

    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                answer += 1

    return answer