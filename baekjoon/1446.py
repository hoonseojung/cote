# n, d = map(int, input().split()) # d = 고속도로 길이
# arr = []
# answer = 0
# for _ in range(n):
#     start, end, dist = map(int, input().split())
#     if (end-start) < dist:
#         continue
#     arr.append([start, end, dist])

# arr = sorted(arr, key=lambda x: (x[0], -x[1], x[2]))
# print(arr)

# start = arr[0][0] # 시작
# end = arr[0][1] # 종료
# if start > 0:
#     answer += start
# for i in range(1, len(arr)):
#     if arr[i][1] < d:
#         continue
#     if end <= arr[i][0]: # 다음 시작점이 전 끝점보다 나중 = 선택 가능
#         answer += arr[i][2] + (arr[i][0] - end) # 지름길 사용 + 다음 진입점까지의 거리
#         end = arr[i][1] # 끝 갱신
# print(end)
# if end < d:
#     answer += d-end

# print(answer)  

#########################################################################################

N, D = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(N)]
dis = [i for i in range(D+1)]
for i in range(D+1):
    if i > 0:
        dis[i] = min(dis[i], dis[i-1]+1)
    for s, e, d in li: # 시작, 끝, 지름길 거리
        if i == s and e <= D and dis[i]+d < dis[e]:
			# 시작점이고 끝점이 고속도로 내에 있으며 지름길 이용이 그냥 1씩 간 것보다 작다면
            dis[e] = dis[i]+d # 지름길 이용
print(dis[D])

########################################################################################
# heaqp 사용 풀이

import heapq

n, d = map(int, input().split())
road = [[]*(10001) for _ in range(10001)]
heap = []
dist = [i for i in range(10001)]

for _ in range(n):
    start, end, cost = map(int, input().split())
    heapq.heappush(heap, (end, start, cost)) # 힙큐 생성

while heap:
    newEnd, newStart, newCost = heapq.heappop(heap)

    if newCost > (dist[newEnd] - dist[newStart]) or newEnd > d:
		# 만약 지름길을 이용하는 것이 손해거나 끝점이 고속도로 밖에 있다면
        continue # 무시

    distance = dist[newStart] + newCost # 그게 아니라면 시작점까지의 dist 값 + 지름길 이용 값

    if dist[newEnd] > distance: # 지름길을 이용한 도착점의 dist값이 위에서 구한 distance 값보다 크다면
        dist[newEnd] = distance # 더 작은 값으로 갱신

    for i in range(newEnd+1, d+1): # d에 도착할 때까지 dist 값 구하기
        dist[i] = min(dist[i], dist[i-1]+1)

print(dist[d])