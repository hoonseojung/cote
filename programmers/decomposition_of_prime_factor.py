def solution(n):
    answer = []
    for i in range(2, n+1):
        if n % i == 0:
            while n % i == 0:
                n //=i
            answer.append(i)
        if n == 1:
            break
    return answer