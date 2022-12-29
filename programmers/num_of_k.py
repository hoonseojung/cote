def solution(i, j, k):
    nArray = []
    answer = 0
    for q in range(i, j+1):
        nArray.append(q)
    for num in nArray:
        x = [int(a) for a in str(num)]
        for y in x:
            if y == k:
                answer+=1
    return answer