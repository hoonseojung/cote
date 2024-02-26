def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for skil in skill:
        degree = skil[5] # 회복
        if skil[0] == 1: degree *= (-1) # 공격
        graph[skil[1]][skil[2]] += degree
        if skil[3] < (n-1): graph[skil[3]+1][skil[2]] += degree * (-1)
        if skil[4] < (m-1): graph[skil[1]][skil[4]+1] += degree * (-1)
        if (skil[3] < (n-1)) and (skil[4] < (m-1)): graph[skil[3]+1][skil[4]+1] += degree
    
    # 좌 -> 우 누적합
    for i in range(n):
        for j in range(1, m):
            graph[i][j] += graph[i][j-1]
    
    # 상 -> 하 누적합
    for j in range(m):
        for i in range(1, n):
            graph[i][j] += graph[i-1][j]
    
    # 최종 변화 결과
    for i in range(n):
        for j in range(m):
            if board[i][j] + graph[i][j] > 0: answer += 1
    return answer