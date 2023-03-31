def solution(keyinput, board):
    answer = [0, 0]
    can = [(board[0]-1)//2, (board[1]-1)//2] # 가로 세로 가능한 칸 수
    for key in keyinput:
        if key == "left":
            if answer[0] > -can[0]: # 움직일 수 있다면
                answer[0] -= 1
        elif key == "right":
            if answer[0] < can[0]:
                answer[0] += 1
        elif key == "up":
            if answer[1] < can[1]:
                answer[1] += 1
        else: # down
            if answer[1] > -can[1]:
                answer[1] -= 1
    return answer