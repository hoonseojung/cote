tc = int(input())
for test_case in range(1, tc+1):
    chess_board = []
    looks = 0
    flag = False
    i_s = [0] * 8
    j_s = [0] * 8
    for _ in range(8):
        chess_board.append(list(input()))
    for i in range(8):
        for j in range(8):
            if flag: break
            if chess_board[i][j] == 'O':
                looks += 1
                if (i_s[i] == 0) and (j_s[j] == 0) and (looks <= 8):
                    i_s[i] = 1
                    j_s[j] = 1
                else: flag = True
        if flag: break
    if not flag and (looks == 8): print('#{} yes'.format(test_case))
    else: print('#{} no'.format(test_case))