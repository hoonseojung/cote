from collections import Counter
def solution(participant, completion):
    answer = ''
    dic = Counter(participant)
    for winner in completion:
        dic[winner] -= 1

    return dic.most_common(1)[0][0]

#######################################
    # answer = collections.Counter(participant) - collections.Counter(completion)
    # return list(answer.keys())[0]
# Counter 객체는 - 연산이 가능