def solution(k, score):
    answer = []
    legend = [] # 명예의 전당
    if len(score) <= k:
        for i in range(len(score)):
            legend.append(score[i])
            legend.sort(reverse = True) # 내림차순
            answer.append(legend[-1]) # 끝 값
    elif len(score) > k: # 점수가 더 남았다면
        for i in range(k):
            legend.append(score[i])
            legend.sort(reverse = True) # 내림차순
            answer.append(legend[-1]) # 끝 값
        for i in range(k, len(score)):
            if score[i] > legend[-1]:
                legend.pop()
                legend.append(score[i])
                legend.sort(reverse = True)
                answer.append(legend[-1])
            else:
                answer.append(legend[-1])
    return answer