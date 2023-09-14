def rule(x):
    return 5*x + 1

def solution(word):
    answer = len(word) # 초기값, 자리수로부터 시작 단어로 초기 순서
    seq = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    r = [1]
    for _ in range(4):
        r.append(rule(r[-1]))
    r.reverse()
    # 781 156 31 6 1
    
    for i, w in enumerate(word):
        answer += r[i] * seq[w]
    return answer


# _ _ _ _ A -> _ _ _ _ E : 순서 + 1
# _ _ _  A -> _ _ _ E : 순서 + 6
# _ _ A -> _ _ E : 순서 + 31
# _ A -> _ E : 순서 + 156
# A -> E : 순서 + 781
# --> 규칙 : y = 5*x + 1
# 규칙 생성 후 주어진 단어 자리 수 ex) AAAE의 경우 4자리 수이므로 시작은 AAAA, EIO의 경우 3자리 수이므로 AAA부터 시작
# 초기 단어로부터 각 자리 단어가 얼마나 차이나는지 seq에서 값을 받아와 규칙의 값에 곱해준 결과를 answer에 더해주면 정답