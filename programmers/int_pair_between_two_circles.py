# from math import sqrt

# def solution(r1, r2):
#     quar = 0
#     for i in range(0, r1): # r1 미만의 x 좌표에서의
#         quar += int(sqrt(r2**2 - i**2)) - int(sqrt(r1**2 - i**2 - 1)) # 두 원 사이의 점
#     for i in range(r1, r2): # r1 이상 r2 미만의 x 죄표에서의
#         quar += int(sqrt(r2**2 - i**2)) # r2의 점
#     return quar * 4

from math import floor, ceil, sqrt
def solution(r1, r2):
    answer = 0
    for x in range(1, r2 + 1):
        # y^2 >= r^2 - x^2
        max_y = floor(sqrt(r2**2 - x**2)) # r2에서 x 좌표 별 가능한 최대 y 값
        if x > r1:
            min_y = 0 # x 좌표가 r1보다 크면 x축에서부터 시작하면 되기에 최소값 = 0
        else:
            min_y = ceil(sqrt(r1**2 - x**2)) # x 좌표가 r1 이하인 경우 x 좌표 별 r1의 테두리 혹은 바로 그 이상부터 시작하면 되기에 ceil 사용
        answer += max_y - min_y + 1 # x 좌표 별 가능한 y 좌표의 개수
    return answer * 4

# 성능은 위의 코드가 조금 더 빠르지만 아래 코드가 좀 더 직관적