def fill_zero(b, n):
    return "0"*(n-len(b)) + b

def solution(n, arr1, arr2):
    answer = []
    for i, a in enumerate(arr1):
        b1 = format(a, 'b')
        if len(b1) < n:
            b1 = fill_zero(b1, n)
        b2 = format(arr2[i], 'b')
        if len(b2) < n:
            b2 = fill_zero(b2, n)

        secret_map = ""
        for j in range(n):
            if int(b1[j]) | int(b2[j]):
                secret_map += "#"
            else:
                secret_map += " "
        answer.append(secret_map)
    return answer
