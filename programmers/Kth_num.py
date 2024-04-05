def solution(array, commands):
    answer = []
    for command in commands:
        cutting = array[command[0]-1:command[1]]
        cutting = sorted(cutting)
        answer.append(cutting[command[2]-1])
    return answer