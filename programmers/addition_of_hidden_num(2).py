def solution(my_string):
    answer = 0
    tmp = []
    s_l = list(my_string)
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(len(s_l)):
        n = s_l[i] # 처음부터 확인
        if n in num:
            tmp.append(n)
            if i == len(s_l)-1:
                answer += int(''.join(tmp))
        else: # 숫자가 아닌 경우
            if len(tmp) > 0: # 배열에 뭔가 존재한다면
                print(tmp)
                answer += int(''.join(tmp)) # 있는 숫자 더하기
                tmp = [] # 배열 초기화
    return answer