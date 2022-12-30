def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reported = {x: 0 for x in id_list}

    for r in set(report):
        do, done = r.split()
        reported[done] += 1

    for r in set(report):
        do, done = r.split()
        if reported[done] >= k:
            answer[id_list.index(do)] += 1
            
    return answer