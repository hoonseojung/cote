from collections import deque
# 마지막 트럭이 다리에 올라온 시간 + bridge_length
def solution(bridge_length, weight, truck_weights):
    answer = 1
    w = truck_weights[0] # 건너는 트럭들의 무게 합
    l = 1 # 건너는 트럭들의 수
    waiting = deque(truck_weights)
    crossing = deque([[waiting.popleft(), 1]])
    
    while waiting:
        answer += 1
        for _ in range(l):
            truck = crossing.popleft()
            if truck[1] == bridge_length:
                w -= truck[0]
                l -= 1
            else:
                truck[1] += 1
                crossing.append(truck)
        if l < bridge_length and w + waiting[0] <= weight:
            new_truck = waiting.popleft()
            w += new_truck
            l += 1
            crossing.append([new_truck, 1])
    return answer + bridge_length