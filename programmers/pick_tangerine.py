from collections import Counter
def solution(k, tangerine):
    answer = 0
    count_t = Counter(tangerine).most_common()
    for idx, c in enumerate(count_t):
        if k <= 0: break
        k -= c[1]
        answer = idx+1
    return answer
