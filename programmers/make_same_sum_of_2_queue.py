from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    q1_s = sum(q1)
    q2_s = sum(q2)
    if (q1_s + q2_s) % 2 == 1: # 모든 원소의 합이 홀수일 때
        return -1
    limit = len(q1) + len(q2)
    count = 0
    while q1_s != q2_s:
        if count >= limit:
            return -1
        while q2 and q1_s < q2_s:
            tmp = q2.popleft()
            q1.append(tmp)
            count += 1
            q2_s -= tmp
            q1_s += tmp

        while q1 and q1_s > q2_s:
            tmp = q1.popleft()
            q2.append(tmp)
            count += 1
            q1_s -= tmp
            q2_s += tmp

    return count