def solution(babbling):
    answer = 0
    can = ["aya", "ye", "woo", "ma"] # 발음 가능
    while len(babbling) != 0:
        babb = babbling.pop(0) # 하나씩 pop
        check = []
        for speak in can:
            if speak in babb: # 문자열에 발음 가능한 단어들이 존재한다면
                check.append(1) # 발음 가능한 단어 순서에 1
            else: # 없다면
                check.append(0) # 0
        for i in range(4): # 전부 확인하며
            if check[i] == 1: # 발음 가능한 단어가 존재한다면
                babb = babb.replace(can[i], " ") # 공백으로 치환
        if len(babb.strip()) == 0: # 공백을 제거해 전부 발음 가능한 단어로만 이루어졌다면
            answer += 1 # 정답
    return answer