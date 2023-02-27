def solution(k, m, score):
    answer = 0
    count = len(score) // m # 상자 개수
    score = sorted(score, reverse=True) # 가격 낮은 순서대로 정렬
    for i in range(count): # 상자 개수마다
        answer += score[i*m+(m-1)] * m # 2, 5, 8, 11
    return answer