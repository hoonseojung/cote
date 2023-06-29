def solution(dartResult):
    answer = 0
    score = []
    temp = 0
    for d in dartResult:
        if d.isdigit(): # 점수
            if temp == 1 and d == '0':    
                temp = 10
            else: temp = int(d)
        else: # S D T * #
            if d == 'S':
                score.append(temp)
            elif d == 'D':
                score.append(temp**2)
            elif d == 'T':
                score.append(temp**3)
            elif d == '*':
                if len(score) >= 2:
                    score[-2] *= 2
                score[-1] *= 2
            else: # #
                score[-1] *= -1
    answer = sum(score)
    return answer