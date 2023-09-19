def solution(n):
    answer = ''
    while n > 0:
        n, m = n // 3, str(n % 3)
        answer += m
    answer = int(answer, 3)
    return answer