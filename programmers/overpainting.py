def solution(n, m, section):
    answer = 0
    painted = section[0] - 1 # 현재 여기까지 칠해짐
    for sec in section:
        if sec > painted: # 안 칠해진 상태였던 sec가 painted보다 크다면
            answer += 1 # 덧칠하기
            painted = sec + m - 1 # s부터 롤러의 길이인 m만큼 칠했다고 표시
    return answer