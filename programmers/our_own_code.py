def solution(s, skip, index):
    answer = []
    s_l = [ord(i) for i in s] # ASCII 코드로 십진수로 변환
    skip_l = [ord(i) for i in skip]
    # a ~ z = 97 ~ 122
    for alpha in s_l:
        k = 0
        while k < index:
            alpha += 1
            if alpha > 122:
                alpha = 97
            if alpha not in skip_l:
                k += 1
        alpha = chr(alpha) # 문자로 변환
        answer.append(alpha)
    return ''.join(answer)