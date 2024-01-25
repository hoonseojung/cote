def solution(storey):
    answer = 0
    while storey:
        s = storey % 10
        storey //= 10
        if s > 5:
            answer += (10-s)
            storey += 1
        elif s < 5:
            answer += s
        elif (storey % 10) >= 5:
            answer += 5
            storey += 1
        else:
            answer += 5
    return answer