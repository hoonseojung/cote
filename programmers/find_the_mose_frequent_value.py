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