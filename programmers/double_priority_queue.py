import heapq
def solution(operations):
    answer = []
    for oper in operations:
        if oper[0] == 'I': # 최소힙 삽입
            heapq.heappush(answer, int(oper[2:]))
        elif oper[0] == "D": # 삭제
            if oper[2] == '-': # 최소값 삭제
                if len(answer) > 0:
                    heapq.heappop(answer)
            elif oper[2] == '1': # 최대값 삭제
                if len(answer) > 0:
                    answer.pop()

    if len(answer) == 0:
        return [0, 0]
    else:
        return [max(answer), min(answer)]