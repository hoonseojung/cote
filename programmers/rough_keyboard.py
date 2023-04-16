def solution(keymap, targets):
    answer = []
    total = ''
    for keys in keymap:
        total += keys # 키패드 전체 종합
    keypads = dict.fromkeys(total) # 중복 제거하여 dict
    for key in keypads:
        min_k = 100 # 최대 index = 99
        for keys in keymap:
            if key in keys: # 해당 키에 존재한다면
                temp = keys.index(key)
                if min_k > temp: # 현재 인덱스보다 작다면
                    min_k = temp # 갱신
        keypads[key] = min_k + 1 # 인덱스이므로 누른 횟수 = index + 1

###################################
# 위의 문자열을 total로 받아 dict로 만드는 과정을 훨씬 간결하게 할 수 있는 코드

    keypads = {} # dict 생성
    for k in keymap: # keymap에 있는 키에서
        for i, char in enumerate(k): # 각 키의 문자 별
            keypads[char] = min((i + 1), keypads[char]) if char in keypads else (i + 1) 
            # 만약 keypads에 해당 문자가 아직 존재하지 않았다면 인덱스인 i + 1을 할당, 
            # 이미 존재한다면 해당 값과 현재 인덱스인 i + 1 중 더 작은 값을 할당
###################################

    for target in targets:
        press = 0 # 누른 횟수
        for char in target: # target의 문자 별로
            if char in keypads: # 만약 keypad에 해당 문자가 있다면
                press += keypads[char] # 해당 횟수 누르기
            else: # 못 만든다면
                press = -1
                break
        answer.append(press)

    return answer