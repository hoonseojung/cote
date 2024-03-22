def check(i):
    if i % 5 == 2: return False
    elif i < 5: return True
    else: return check(i // 5)

def solution(n, l, r):
    answer = 0
    for i in range(l-1, r):
        if check(i): answer += 1
    return answer
# 0 -> 1 [0]
# 1 -> 11011 [0 1 3 4]
# 2 -> 11011 11011 00000 11011 11011 [0 1 3 4/5 6 8 9/15 16 18 19/20 21 23 24]
# 3 -> 11011 11011 00000 11011 11011 11011 11011 00000 11011 11011 00000 00000 00000 00000 00000 11011 11011 00000 11011 11011 11011 11011 00000 11011 11011