from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    menu = defaultdict(int)
    menu_len = {i:0 for i in course}
    for order in orders:
        for i in range(2, len(order)+1):
            order_l = list(combinations(order, i))
            for o in order_l:
                o = sorted(o)
                menu[''.join(o)] += 1
    menu = dict(sorted(menu.items(), key=lambda x: x[1], reverse=True))

    for k, v in menu.items():
        l = len(k)
        if l in course:
            if menu_len[l] > 0:
                if menu_len[l] == v:
                    answer.append(k)
            else:
                if v >= 2:
                    answer.append(k)
                    menu_len[l] = v
    answer = sorted(answer)
    
    return answer