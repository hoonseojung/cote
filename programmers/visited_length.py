def solution(dirs):
    x, y = 0, 0
    dxy = {'U': [0, 1], 'D': [0, -1], 'R': [1, 0], 'L': [-1, 0]}

    road = []

    for w in dirs:
        nx, ny = x + dxy[w][0], y + dxy[w][1]
        
        if (-5 <= nx <= 5) and (-5 <= ny <= 5):
            if ([x, y, nx, ny] not in road) and ([nx, ny, x, y] not in road):
                road.append([x, y, nx, ny])
            x, y = nx, ny

    return len(road)
