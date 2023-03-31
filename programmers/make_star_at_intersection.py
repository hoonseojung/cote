from itertools import combinations
def solution(line):
    answer = []
    line_cb = list(combinations(line, 2))
    dots = []
    for cb in line_cb:
        if cb[0][0]*cb[1][1] - cb[0][1]*cb[1][0] != 0 : # 두 직선의 교점이 유일하게 존재
            x = (cb[0][1]*cb[1][2] - cb[0][2]*cb[1][1]) / (cb[0][0]*cb[1][1] - cb[0][1]*cb[1][0])
            y = (cb[0][2]*cb[1][0] - cb[0][0]*cb[1][2]) / (cb[0][0]*cb[1][1] - cb[0][1]*cb[1][0])
            if x == int(x) and y == int(y): # 정수인 점들만
                dots.append((int(x), int(y)))
    dots = list(set(dots))

    if len(dots) >= 2:
        min_x, min_y, max_x, max_y = min(dots, key=lambda x: x[0])[0], min(dots, key=lambda x: x[1])[1], max(dots, key=lambda x: x[0])[0], max(dots, key=lambda x: x[1])[1]
        
        for i in range(max_y-min_y+1):
            tmp = ''
            for j in range(max_x-min_x+1):
                if (min_x+j, max_y-i) in dots:
                    tmp += '*'
                else:
                    tmp += '.'
            answer.append(tmp)
    else: # dot 1개
        answer.append('*')
    return answer