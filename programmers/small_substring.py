def solution(t, p):
    answer = 0
    length = len(p)
    sub_str = [t[i:i+length] for i in range(0, len(t)-(length-1))]
    for num in sub_str:
        if int(num) <= int(p):
            answer += 1
    return answer