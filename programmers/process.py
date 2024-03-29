from collections import deque
def solution(priorities, location):
    answer = 0
    prios = {i: v for i, v in enumerate(priorities)}
    prios = deque(sorted(prios.items(), key=lambda x: -x[1]))
    _, cur_prio = prios.popleft()
    priorities = deque((i, p) for i, p in enumerate(priorities))
    while True:
        idx, process = priorities.popleft()
        if process == cur_prio:
            answer += 1
            if idx == location: break
            _, cur_prio = prios.popleft()
        else: priorities.append((idx, process))
    return answer