def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr)):
        tmp = arr[i]
        if answer[-1] != tmp:
            answer.append(tmp)
    return answer

# pop(0)은 효율성 테스트에서 굉장히 불리