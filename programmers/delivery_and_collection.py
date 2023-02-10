def solution(cap, n, deliveries, pickups):
    answer = 0
    box = [0, 0] # 배달, 수거
    # 물류 창고에서 출발해서 전부 배달하고, 돌아오는 길에 전부 회수하는 것으로 생각하면 배달과 회수는 다른 것으로 생각해도 무방
    for i in range(n-1, -1, -1): # 거리가 먼 곳부터 확인
        count = 0
        # 해당 지점에 배달 혹은 수거할 물건이 존재한다면 그만큼 뺌
        # 만약 해당 지점에 그런 물건이 없다면 box = 0
        box[0] -= deliveries[i]
        box[1] -= pickups[i]
        
        while box[0] < 0 or box[1] < 0: # 가용한만큼 더해서 몇 번만에 처리할 수 있나 확인
            box[0] += cap
            box[1] += cap
            count += 1 # 횟수
            
        answer += (i + 1) * 2 * count

    return answer