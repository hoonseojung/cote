from collections import Counter
def solution(array):
    dict = Counter(array)
    if len(dict) == 1:
        return array[0]
    else:
        dict_list = sorted(dict.items(), key=lambda x: x[1], reverse=True)
        if dict_list[0][1] > dict_list[1][1]:
            return dict_list[0][0]
        else:
            return -1
###########################################################################################
def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0:
            return a
    return -1

# set을 통해 array 내의 원소 간 중복 없이 1개씩 없애고, enumerate의 해당 회차를 모두 돌고 난 뒤에 i = 0으로 끝났다면 즉, 원소가 1 종류만 있다면 해당 값이 최빈값
# array = [1, 2, 2, 3, 3, 3, 4, 4]
# 0 1 [1, 2, 2, 3, 3, 3, 4, 4]
# 1 2 [2, 2, 3, 3, 3, 4, 4]
# 2 3 [2, 3, 3, 3, 4, 4]
# 3 4 [2, 3, 3, 4, 4]
# 0 2 [2, 3, 3, 4]
# 1 3 [3, 3, 4]
# 2 4 [3, 4]
# 0 3 [3]
# 3