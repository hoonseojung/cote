def solution(N, road, K):
    answer = 0
    town = [[500001] * N for _ in range(N)]
    for r in road:
        if town[r[0]-1][r[1]-1] > r[2]: # 새로운 정보 or 같은 경로에 더 작은 값이 존재한다면
            town[r[0]-1][r[1]-1] = r[2]
            town[r[1]-1][r[0]-1] = r[2]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if (i != j) and (i != k) and (k != j):
                    if town[i][j] > town[i][k] + town[k][j]:
                        town[i][j] = town[i][k] + town[k][j]
    
    town[0][0] = 0 # 1번 마을은 항상 배달 가능
    answer = len([x for x in town[0] if x <= K])
    return answer