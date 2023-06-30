def solution(N, stages):
    # 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
    answer = []
    temp = 0 # 스테이지 도달한 사람들 수 계산용
    people = len(stages)
    rank = {i:0 for i in range(1, N+1)}
    stages = sorted(stages, reverse=True)
    for stage in stages:
        if stage <= N:
            rank[stage] += 1
    for n in range(1, N+1):
        try:
            temp = rank[n]
            rank[n] /= people
            people -= temp
        except: # people = 0 -> 스테이지에 도달한 유저가 없는 경우
            rank[n] = 0
            
    rank = dict(sorted(rank.items(), key=lambda x: -x[1]))
    answer = list(rank.keys())
    return answer