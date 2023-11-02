import sys
import math
input = sys.stdin.readline

def dist_cal(a, b):
    m = (y1 - y2) / (x1 - x2)
    c = y1 - (m * x1)
    return abs(m*a - b + c)/math.sqrt(m**2 + 1)

def new_dot(a, b): # 선대칭
    m = (y1 - y2) / (x1 - x2)
    c = y1 - (m * x1)
    nx = a - 2*m*(m * a - b + c) / (m**2 + 1)
    ny = b + 2*(m * a - b + c) / (m**2 + 1)
    return (nx, ny)

def x_intercept(a, b, c, d, e): # (a, b) (c, d) 두 점을 지나는 직선의 x 절편 
    m = (d - b) / (c - a)
    f = b - (m * a)
    return (e-f)/m
    

x, y = map(int, input().split())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
area = x * y

if x1 == x2: # 직선 |
    if x1 <= (x-x1):
        area -= (x1 * y)
    else:
        area -= ((x-x1) * y)
elif y1 == y2: # 직선 -
    if y1 <= (y-y1):
        area -= (x * y1)
    else:
        area -= (x * (y-y1))
elif (y1-y2)/(x1-x2) < 0: # 기울기 음수-> 원점, (x, y) 거리 비교
    if dist_cal(0, 0) > dist_cal(x, y):
        nx, ny = new_dot(x, y) # (x, y) 선대칭한 점
        if x1 > x2:
            area -= (x-x2)*(y-y1)*1/2
        else:
            area -= (x-x1)*(y-y2)*1/2

        if ny < 0: # 밖으로 튀어 나옴
            x_1 = x_intercept(nx, ny, x1, y1, 0)
            x_2 = x_intercept(nx, ny, x2, y2, 0)
            x_dist = abs(x_2 - x_1)
            area += (x_dist * (-ny) * 1/2)
    elif dist_cal(0, 0) < dist_cal(x, y):
        nx, ny = new_dot(0, 0) # (x, y) 선대칭한 점
        if x1 > x2:
            area -= x1*y2*1/2
        else:
            area -= x2*y1*1/2

        if ny > y: # 밖으로 튀어 나옴
            x_1 = x_intercept(nx, ny, x1, y1, y)
            x_2 = x_intercept(nx, ny, x2, y2, y)
            x_dist = abs(x_2 - x_1)
            area += (x_dist * (ny-y) * 1/2)
    else: # dist_cal(0, 0) == dist_cal(x, y)
        그대로 접어 올리기
print(area)