def solution(name, yearning, photo):
    answer = []
    for pho in photo:
        temp = 0
        for i in range(len(name)):
            if name[i] in pho:
                temp += yearning[i]
        answer.append(temp)
    return answer