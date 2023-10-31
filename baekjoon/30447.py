import sys
input = sys.stdin.readline

x, y = map(int, input().split())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

a = 0 # 기울기
if x1 == x2: # 직선 |
    if x1 <= (x-x1)