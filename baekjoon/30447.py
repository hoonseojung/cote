import sys
import math
input = sys.stdin.readline

def dist_cal(a, b): # (x1, y1), (x2, y2) 두 점을 지나는 직선과 점 (a, b)의 거리
    m = (y1 - y2) / (x1 - x2)
    c = y1 - (m * x1)
    return abs(m*a - b + c)/math.sqrt(m**2 + 1)

def new_dot(a, b): # (x1, y1), (x2, y2) 두 점을 지나는 직선에 대해 점 (a, b) 선대칭
    m = (y1 - y2) / (x1 - x2)
    c = y1 - (m * x1)
    nx = a - 2*m*(m * a - b + c) / (m**2 + 1)
    ny = b + 2*(m * a - b + c) / (m**2 + 1)
    return (nx, ny)

def x_intercept(a, b, c, d, e): # (a, b) (c, d) 두 점을 지나는 직선의 y=e일 때 x 값
    m = (d - b) / (c - a)
    f = b - (m * a) # -> y = mx + f
    return (e-f)/m

x, y = map(int, input().split())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
area = x * y

# 가로가 더 길고, x1 > x2라는 전제 하에
# 기울기가 음수에서
# 중점이 접는 선 위에 있으면 접는 선을 중점에 대해 점대칭 시키고,
# 중점이 접는 선 아래에 있으면 (0, 0)을 선대칭시키고, 시킨 결과 점(nx, ny)이
# 1. nx > x, ny < y
#   - (x1 + x2) * y * 1/2
#   + (0, y) 점을 선대칭시킨 (x', y')와 (nx, ny) 두 점을 지나는 직선이 Y=y와 만나는 (x 좌표 - x2) * (y'-y) * 1/2
#   + (위 직선이 X=x와 만나는 y좌표 - (nx, ny), (x1, 0) 두 점을 지나는 직선이 X=x와 만나는 y좌표) * (nx-x) * 1/2

# 2. nx <= x, ny <= y
#   접는 선보다 (0, y)가 아래에 있다면
#   - (x1 + x2) * y * 1/2
#   + (0, y) 점을 선대칭시킨 (x', y')와 (nx, ny) 두 점을 지나는 직선이 Y=y와 만나는 (x 좌표 - x2) * (y'-y) * 1/2

#   접는 선보다 (0, y)가 위에 있다면
#       접는 선보다 (x, 0)이 아래에 있다면
#       - (y1 + y2) * x * 1/2
#       + (x, 0) 점을 선대칭 시킨 (x'', y'')와 (nx, ny) 두 점을 지나는 직선이 X=x와 만나는 (y 좌표 - y1) * (x''-x) * 1/2

#       접는 선보다 (x, 0)이 위에 있다면
#       - x1 * y2 * 1/2

# 3. nx < x, ny > y
#   접는 선보다 (0, y)가 아래에 있다면
#   - (x1 + x2) * y * 1/2
#   + (nx, ny)와 (x1, 0) 두 점을 지나는 직선이 Y=y와 만나는 x 좌표 = x_라고 할 때 (x_, y)와 (nx, ny) 두 점 사이의 (거리 + x2) * y * 1/2

#   접는 선보다 (0, y)가 위에 있다면
#       접는 선보다 (x, 0)이 아래에 있다면
#       - (y1 + y2) * x * 1/2
#       + ((nx, ny)와 (0, y2) 두 점을 지나는 직선이 Y=y와 만나는 x 좌표 - (x, 0) 점을 선대칭 시킨 (x'', y'')와 (nx, ny) 두 점을 지나는 직선이 Y=y와 만나는 x 좌표) * (ny-y) * 1/2
#       + (x, 0) 점을 선대칭 시킨 (x'', y'')와 (nx, ny) 두 점을 지나는 직선이 X=x와 만나는 (y 좌표 - y2) * (x''-x) * 1/2

#       접는 선보다 (x, 0)이 위에 있다면
#       - x1 * y2 * 1/2
#       + ((nx, ny)와 (0, y2) 두 점을 지나는 직선이 Y=y와 만나는 x 좌표 - (x1, 0)과 (nx, ny) 두 점을 지나는 직선이 Y=y와 만나는 x 좌표) * (ny-y) * 1/2






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
        nx, ny = new_dot(0, 0) # (0, 0) 선대칭한 점
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
        nx, ny = new_dot(0, 0)
        area -= x*y*1/2
        # 직선의 방정식 : y = (ny/nx-x) * (X-x)
        area += (y/(ny/nx-x) + x) * (ny-y) * 1/2 # 해당 직선에서 y=y(높이)일 때의 x값 * 높이 * 1/2  
else: # (y1-y2)/(x1-x2) > 0: # 기울기 양수-> (x, 0), (0, y) 거리 비교
    if dist_cal(x, 0) > dist_cal(0, y):
        nx, ny = new_dot(0, y) # (x, y) 선대칭한 점
        if x1 > x2:
            area -= x1*(y-y2)*1/2
        else:
            area -= x2*(y-y1)*1/2

        if ny < 0: # 밖으로 튀어 나옴
            x_1 = x_intercept(nx, ny, x1, y1, 0)
            x_2 = x_intercept(nx, ny, x2, y2, 0)
            x_dist = abs(x_2 - x_1)
            area += (x_dist * (-ny) * 1/2)
    elif dist_cal(x, 0) < dist_cal(0, y):
        nx, ny = new_dot(x, 0) # (0, 0) 선대칭한 점
        if x1 > x2:
            area -= (x-x2)*y1*1/2
        else:
            area -= (x-x1)*y2*1/2

        if ny > y: # 밖으로 튀어 나옴
            x_1 = x_intercept(nx, ny, x1, y1, y)
            x_2 = x_intercept(nx, ny, x2, y2, y)
            x_dist = abs(x_2 - x_1)
            area += (x_dist * (ny-y) * 1/2)
    else: # dist_cal(0, 0) == dist_cal(x, y)
        nx, ny = new_dot(x, 0)
        area -= x*y*1/2
        # 직선의 방정식 : Y = (ny/nx) * X
        area += (x - y/(ny/nx)) * (ny-y) * 1/2 # 해당 직선에서 Y=y(높이)일 때의 x값 * 높이 * 1/2

print(int(area))