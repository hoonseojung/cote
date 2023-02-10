def solution(numbers, hand):
    answer = ''
    hands = [[3, 0], [3, 2]] # 왼손 *, 오른손 #
    # 1, 2, 3 = [0, 0], [0, 1], [0, 2]
    # 4, 5, 6 = [1, ]
    # 7, 8, 9 = [2, ]
    # *, 0, # = [3, ]
    left_h = [1, 4, 7]
    right_h = [3, 6, 9]
    middle = [2, 5, 8, 0]
    for n in numbers:
        if n in left_h:
            hands[0] = [n//3, 0]
            answer += "L"
        elif n in right_h:
            hands[1] = [n//4, 2]
            answer += "R"
        elif n in middle:
            if n != 0: k = n//3
            else: k = 3
            ld = abs(k - hands[0][0]) + abs(1 - hands[0][1])
            rd = abs(k - hands[1][0]) + abs(1 - hands[1][1])
            if (ld < rd) or (ld == rd and hand == "left"):
                hands[0] = [k, 1]
                answer += "L"
            elif (rd < ld) or (rd == ld and hand == "right"):
                hands[1] = [k, 1]
                answer += "R"
    return answer