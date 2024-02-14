def solution(s):
    c_num = 0
    for c in s:
        if c == '(':
            c_num += 1
        else:
            if c_num > 0: c_num -= 1
            else: return False
    if c_num > 0: return False
    return True