import heapq
def solution(n, k, enemy):
    answer = 0
    if k >= len(enemy): # 무적권으로 전부 처리 가능하다면
        return len(enemy)
    h = []
    for ene in enemy:
        if n >= 0:
            heapq.heappush(h, -ene) # 최대힙
            n -= ene
            while n < 0 and k > 0: # 더 못 지나간다면
                n += -heapq.heappop(h) # 가장 최대값 빼고
                k -= 1
            if n >= 0: # 막아냈다면
                answer += 1

    return answer