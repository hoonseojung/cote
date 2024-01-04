# 어떠한 위치 a의 약수 중 천만 이하, 그리고 자신을 제외한 가장 큰 약수
def solution(begin, end):
    answer = []
    if begin == 1:
        answer.append(0)
        begin += 1
    for i in range(begin, end+1):
        temp = [1]
        for j in range(2, int(i**0.5)+1):
            if (i%j == 0) and (j <= 1e7):
                temp.append(j)
                if (i//j <= 1e7):
                    temp.append(i//j)
        answer.append(max(temp))
    return answer