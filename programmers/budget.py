def solution(d, budget):
    answer = 0
    d = sorted(d)
    for c in d:
        budget -= c
        if budget < 0:
            return answer
        else:
            answer += 1
    return answer