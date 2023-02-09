def solution(n):
    answer = 0
    tmp = []
    check = 0
    j = 0
    for i in range(n):
        tmp.append(i+1)
        
    while len(tmp) > 0:
        check += tmp[j]
        j += 1
        if check >= n:
            if check == n:
                answer += 1
            check = 0
            tmp.pop(0)
            j = 0
        
    return answer
# 리스트에 n까지 전부 넣고 아래서부터 하나씩 더해가며 확인하고 조건을 만족하거나 불만족 시 가장 아래를 pop(0)을 통해 제껴주고, 다시 처음부터 더하면서 확인
# ex_ 1부터 쭉 더해가다 n이 되거나 넘으면 pop, 2부터 다시 확인