def solution(clothes):
    answer = 1
    dic = dict()
    for _, kind in clothes:
        dic[kind] = [] # 초기화
    for value, kind in clothes:
        dic[kind].append(value) 
    for key in dic.keys():
        answer *= (len(dic[key]) + 1)
    answer -= 1
    return answer