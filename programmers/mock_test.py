def solution(answers):
    answer = []
    # 1 2 3 4 5
    # 2 1 2 3 2 4 2 5
    # 3 3 1 1 2 2 4 4 5 5
    ans_len = len(answers) # 전체 문제 수
    a_len = ans_len // 5
    b_len = ans_len // 8
    c_len = ans_len // 10
    
    a_ans = [1, 2, 3, 4, 5] * (a_len + 1) # 1번 정답지
    b_ans = [2, 1, 2, 3, 2, 4, 2, 5] * (b_len + 1) # 2번 정답지
    c_ans = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (c_len + 1) # 3번 정답지
    
    result = {1: 0, 2: 0, 3: 0} # 1, 2, 3번 별 오답 개수
    
    for i in range(ans_len):
        if answers[i] != a_ans[i]:
            result[1] += 1
        if answers[i] != b_ans[i]:
            result[2] += 1
        if answers[i] != c_ans[i]:
            result[3] += 1
            
    result_l = list(sorted(result, key=lambda x : result[x])) # 적게 틀린 순으로 정렬
    
    for i in result_l:
        if result[i] == result[result_l[0]]: # 동점자
            answer.append(i)
        else: # 없기 시작하면
            break # 종료
    return answer