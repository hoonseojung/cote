def solution(s):
    answer = ''
    idx = 0
    for ss in s:
        if ss == ' ': 
            answer += ' '
            idx = 0
        else:
            if idx % 2 == 1: answer += ss.lower()
            else: answer += ss.upper()
            idx += 1
    return answer