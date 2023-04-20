def solution(arr):
    answer = [0, 0]
    check = 0 # 모두 같은지 확인
    for i in range(len(arr)):
        for j in range(len(arr)):
            check += arr[i][j]
    if check == 0:
        answer[0] += 1
    elif check == len(arr)*len(arr):
        answer[1] += 1
    else:
        quarter_graph = [arr[i][0:len(arr)//2] for i in range(0, len(arr)//2)]
        answer = [x + y for x, y in zip(answer, solution(quarter_graph))] # 그냥 += 해버리면 [1, 2] + [3, 4] = [1, 2, 3, 4] -> [4, 6]
        
        quarter_graph = [arr[i][len(arr)//2:len(arr)] for i in range(0, len(arr)//2)]
        answer = [x + y for x, y in zip(answer, solution(quarter_graph))]
        
        quarter_graph = [arr[i][0:len(arr)//2] for i in range(len(arr)//2, len(arr))]
        answer = [x + y for x, y in zip(answer, solution(quarter_graph))]
        
        quarter_graph = [arr[i][len(arr)//2:len(arr)] for i in range(len(arr)//2, len(arr))]
        answer = [x + y for x, y in zip(answer, solution(quarter_graph))]
        
    return answer