def solution(order):
    answer = 0
    cb = 1
    sub_cb = []
    for o in order:
        if o == cb:
            cb += 1
            answer += 1
        else:
            if o < cb:
                if sub_cb[-1] == o:
                    _ = sub_cb.pop()
                    answer += 1
                else:
                    return answer
            else: # o > cb
                for i in range(cb, o):
                    sub_cb.append(i)
                cb = o + 1
                answer += 1
    return answer