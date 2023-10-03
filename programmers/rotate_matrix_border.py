# 추출하는 과정을 시계 방향으로 추출한다면 바뀐 리스트를 추론할 때도 결국 마지막 원소를 맨 앞으로 보낸 리스트가 결과가 됨
#     {2 2} (2 3) (2 4)
#     (3 2)       (3 4)
#     (4 2)       (4 4)
#     (5 2) (5 3) {5 4}

#     (3 2) {2 2} (2 3)
#     (4 2)       (2 4)
#     (5 2)       (3 4)
#     (5 3) {5 4} (4 4)

#     {2 2} (2 3) (2 4) (3 4) (4 4) {5 4} (5 3) (5 2) (4 2) (3 2) -> 기존
#     (3 2) {2 2} (2 3) (2 4) (3 4) (4 4) {5 4} (5 3) (5 2) (4 2) -> 회전
#     --> deque의 rotate 사용

from collections import deque
def solution(rows, columns, queries):
    answer = []
    graph = [[j*columns+i for i in range(1, columns+1)] for j in range(rows)]
    for query in queries:
        target = deque() # 바꿀 원소들 좌표
        values = deque()
        for i in range(query[3]-query[1]+1): # 0 1 2
            target.append((query[0]-1, query[1]+i-1)) # {2 2} (2 3) (2 4)
            values.append(graph[query[0]-1][query[1]+i-1])
        for i in range(1, query[2]-query[0]): # 1 2
            target.append((query[0]+i-1, query[3]-1)) # (3 4) (4 4)
            values.append(graph[query[0]+i-1][query[3]-1])
        for i in range(query[3]-query[1]+1):
            target.append((query[2]-1, query[3]-i-1)) # {5 4} (5 3) (5 2)
            values.append(graph[query[2]-1][query[3]-i-1])
        for i in range(1, query[2]-query[0]):
            target.append((query[2]-i-1, query[1]-1)) # (4 2) (3 2)
            values.append(graph[query[2]-i-1][query[1]-1])
        # {2 2} (2 3) (2 4) (3 4) (4 4) {5 4} (5 3) (5 2) (4 2) (3 2)
        answer.append(min(values)) # 최소값
        values.rotate(1)
        
        for pair in zip(target, values):
            graph[pair[0][0]][pair[0][1]] = pair[1] # 회전
        
    return answer
