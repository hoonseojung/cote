from itertools import product
from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    infomap = defaultdict(list)
    binarys = list(product((True, False), repeat=4))

    for inf in info:
        inf = inf.split()
        for binary in binarys:
            key = ''.join([inf[i] if binary[i] else '-' for i in range(4)]) 
            infomap[key].append(int(inf[4]))

    for k in infomap.keys():
        infomap[k].sort()

    answer = []
    for q in query:
        l, _, p, _, c, _, f, point = q.split()
        key = ''.join([l, p, c,f])
        i = bisect_left(infomap[key], int(point))
        answer.append(len(infomap[key]) - i)

    return answer