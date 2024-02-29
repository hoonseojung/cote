from collections import Counter

def solution(want, number, discount):
    answer = 0
    buy = {w: n for w, n in zip(want, number)}

    for i in range(len(discount)):
        if buy == Counter(discount[i:i+10]): answer += 1

    return answer