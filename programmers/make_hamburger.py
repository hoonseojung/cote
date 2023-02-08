def solution(ingredient):
    answer = 0
    check = []
    count = 0
    for i in ingredient:
        check.append(i)
        if i == 1 and len(check) >= 4 and check[-4:] == [1, 2, 3, 1]:
            for _ in range(4):
                check.pop()
            answer += 1
    return answer