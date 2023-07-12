def solution(n, left, right):
    answer = []
    l = left // n
    ld = left % n
    r = right // n
    rd = right % n
    for i in range(l+1, r+2):
        if l == r: # 한 줄에서만 가져오는 경우
            for j in range(ld, rd+1):
                answer.append(max(j+1, i))
        elif i == l+1: # 시작
            for j in range(ld, n):
                answer.append(max(j+1, i))
        elif i == r+1: # 마지막
            for j in range(rd+1):
                answer.append(max(j+1, i))
        else: # 중간
            for j in range(n):
                answer.append(max(j+1, i))
    return answer

# def solution(n, left, right):
#     answer = []
#     for i in range(left, right+1):
#         v = max(i//n, i%n) + 1 # x=i//n, y=i%n | x, y 중에 큰 수를 구해 +1을 해서 값으로 넣어줌
#         answer.append(v)
#     return answer