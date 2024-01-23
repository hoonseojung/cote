import math

def get_limit(x, d):
    return math.floor(((d**2)-(x**2))**0.5)

def solution(k, d):
    answer = 0
    for x in range(0, d + 1, k):
        y = get_limit(x, d)
        answer += (y//k) + 1

    return answer