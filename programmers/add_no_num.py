def solution(numbers):
    answer = 0
    dic = {i:False for i in range(10)}
    for n in numbers:
        dic[n] = True
    for d in dic:
        if not dic[d]:
            answer += d
    return answer