def solution(s):
    tmp = ""
    check = 0
    answer = 0
    dic = dict()
    if len(s) == 1: # 길이가 1이면 바로 1 return
        return 1
    for i, ss in enumerate(s): # 문자 한 개씩 돌며
        if ss not in dic: # 나온적이 없다면 딕셔너리에 추가
            dic[ss] = 1
        else: # 나온적이 있다면 횟수 +1
            dic[ss] += 1
        tmp += ss # 현재까지 읽은 문자열
        x = tmp[0] # 현재까지 읽은 문자열의 첫번째 글자
        for d in dic: # 딕셔너리를 돌며
            if d != x: # 첫 번째 글자가 아닌 다른 글자들에 대해서
                check += dic[d] # 나온 횟수 카운트
        if check == dic[x]: # 카운트가 첫 번째 글자가 나온 횟수와 같다면
            answer += 1 # answer += 1
            tmp = "" # tmp 초기화
            dic = dict() # 딕셔너리 초기화
        check = 0 # 횟수가 같던 같지 않던 카운트 초기화
        if i == len(s)-1 and tmp != "": # 횟수가 다른 상태에서 더 이상 읽을 글자가 없다면
            answer += 1 # 마지막 문자열 분리하기에 answer += 1
    return answer