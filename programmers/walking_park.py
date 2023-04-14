def solution(park, routes):
    x = []
    for i in range(len(park)): # 4
        for j in range(len(park[0])): # 3
            if park[i][j] == 'S':
                cur = [i, j] # 시작점
            elif park[i][j] == 'X':
                x.append([i, j]) # 장애물
    for route in routes:
        direct, val = route.split()
        temp = cur.copy()
        if direct == 'N':
            for _ in range(int(val)):
                temp[0] -= 1
                if (temp in x) or (temp[0] < 0):
                    break
            else:
                cur = temp
        elif direct == 'S':
            for _ in range(int(val)):
                temp[0] += 1
                if (temp in x) or (temp[0] > len(park) - 1):
                    break
            else:
                cur = temp
        elif direct == 'W':
            for _ in range(int(val)):
                temp[1] -= 1
                if (temp in x) or (temp[1] < 0):
                    break
            else:
                cur = temp
        else: # E
            for _ in range(int(val)):
                temp[1] += 1
                if (temp in x) or (temp[1] > len(park[0]) - 1):
                    break
            else:
                cur = temp
    return cur