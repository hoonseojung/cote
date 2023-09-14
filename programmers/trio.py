from itertools import combinations
def solution(number):
    answer = 0
    bro = list(combinations(number, 3))
    for b in bro:
        if sum(b) == 0:
            answer += 1
    return answer