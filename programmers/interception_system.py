def solution(targets):
    answer = 1
    targets = sorted(targets, key=lambda x: [x[1], x[0]]) # 종료 시간이 빠른 순서대로, 같다면 시작 시간이 빠른 순서대로 정렬
    end = targets[0][1] # 현 미사일 종료
    for i in range(1, len(targets)):
        if end <= targets[i][0]: # 현 미사일 종료 시간이 다음 미사일 시작 시간 이하라면
            end = targets[i][1] # 현 미사일 갱신
            answer += 1
    return answer

# 백준의 회의실 배정 문제와 동일