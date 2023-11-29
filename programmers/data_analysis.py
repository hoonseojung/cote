def solution(data, ext, val_ext, sort_by):
    answer = []
    case = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}
    
    for d in data:
        if d[case[ext]] < val_ext:
            answer.append(d)
    
    answer = sorted(answer, key=lambda x: x[case[sort_by]])
    return answer