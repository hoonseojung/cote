def solution(brown, yellow):
    answer = []
    k = 3
    total = brown + yellow
    while True:
        if (total % k == 0) and ((total//k-2)*(k-2) == yellow):
            answer = [total//k, k]
            break
        k += 1
    return answer