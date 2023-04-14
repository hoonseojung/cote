def solution(wallpaper):
    answer = [0, 0, 0, 0]
    files = []
    for i in range(len(wallpaper)): # h
        for j in range(len(wallpaper[0])): # w
            if wallpaper[i][j] == '#':
                files.append([i, j])
    files = sorted(files, key=lambda x: x[0])
    answer[0] = files[0][0]
    answer[2] = files[-1][0] + 1
    files = sorted(files, key=lambda x: x[1])
    answer[1] = files[0][1]
    answer[3] = files[-1][1] + 1
    return answer