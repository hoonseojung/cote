# 1 1 1 2 2 3 4 5 7 9  12 16 21 28 37
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
#                         7 11
#                           8 12
#                               9 13


t = int(input())
p = [1, 1, 1, 2, 2]
for _ in range(t):
    n = int(input())
    length = n - 5
    if length <= 0:
        print(p[n-1])
    else:    
        for i in range(length):
            p.append(p[-1]+p[-5])
        print(p[n-1])