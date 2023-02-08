def solution(survey, choices):
    answer = ''
    dic = dict()
    dic['R'] = dic['T'] = dic['C'] = dic['F'] = dic['J'] = dic['M'] = dic['A'] = dic['N'] = 0 # 초기화
    
    for i in range(len(choices)):
        if choices[i] < 4:
            dic[survey[i][0]] += 4 - choices[i]
        else: # >= 4
            dic[survey[i][1]] += choices[i] - 4

    if dic['R'] >= dic['T']: answer += 'R'
    else: answer += 'T'
    if dic['C'] >= dic['F']: answer += 'C'
    else: answer += 'F'
    if dic['J'] >= dic['M']: answer += 'J'
    else: answer += 'M'
    if dic['A'] >= dic['N']: answer += 'A'
    else: answer += 'N'
    return answer