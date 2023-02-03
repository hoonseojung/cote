def solution(lines):
    answer = 0
    table = [set([]) for i in range(200)] # -100 ~ 100
    for index, line in enumerate(lines):
        a, b = line
        for i in range(a, b):
            table[i + 100].add(index) # set이므로 각 선분 순서별로 해당 위치에 넣을 때 중복되지 않게 넣음
    for line in table:
        if len(line) > 1:
            answer += 1
    return answer