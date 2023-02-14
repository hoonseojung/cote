from collections import Counter
def solution(weights):
    # (1, 1), (2, 3), (2, 4), (3, 4)
    # 같은 무게라도 다른 사람 취급
    answer = 0
    people = Counter(weights)
    for weight, num in people.items():
        # (1, 1) 본인을 제외한 같이 탈 수 있는 조합 (1 ~ n-1)까지의 합
        answer += num * (num - 1) // 2
        for d1, d2 in [(2, 3), (2, 4), (3, 4)]:
            answer += people[weight * d1 / d2] * num
    return answer