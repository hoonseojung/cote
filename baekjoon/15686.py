from itertools import combinations
N, M = map(int, input().split()) # N x N 격자, M개의 치킨집 선택
graph = [list(map(int, input().split())) for _ in range(N)]
dist = [] # 치킨 거리

house = [(x, y) for x in range(N) for y in range(N) if graph[x][y] == 1] # 전체 집
chicken_house = [(x, y) for x in range(N) for y in range(N) if graph[x][y] == 2] # 전체 치킨집
chicken_cb = list(combinations(chicken_house, M)) # 그 중 M개 선택

for cb in chicken_cb: # 모든 조합에 대해
    total = 0
    for h in house: # 집 별로 살펴보며
        distance = 99 # 초기값
        for i in range(M):
            distance = min((abs(h[0]-cb[i][0]) + abs(h[1] - cb[i][1])), distance) # 집 별 최소 치킨 거리
        total += distance # 한 조합에 대한 치킨 거리의 최솟값
    dist.append(total) # 각 집 별 최소 거리

print(min(dist))