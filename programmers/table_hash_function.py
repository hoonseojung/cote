def solution(data, col, row_begin, row_end):
    answer = 0
    result = []
    data = sorted(data, key = lambda x: (x[col-1], -x[0]))
    for i in range(row_begin, row_end+1):
        tmp = []
        for j in range(len(data[0])):
            tmp.append(data[i-1][j] % i)
        result.append(sum(tmp))
    answer = result[0] # 첫 번째 값
    for i in range(1, len(result)):
        answer ^= result[i]
    return answer