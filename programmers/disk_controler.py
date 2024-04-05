# 가장 빠른 방법은 실행 시간이 짧은 것부터 실행시키는 방법
# 현재 실행 중인 작업이 있다면, 해당 작업이 끝나는 시간 전에 요청되는 작업들을 모두 힙큐에 넣어야함
import heapq
from collections import deque

def solution(jobs):
    disk = []
    n = len(jobs)
    jobs = deque(sorted(jobs, key=lambda x: (x[0], x[1])))
    end_time = jobs[0][0]+jobs[0][1] # 실행 중인 작업이 끝나는 시간
    answer = jobs[0][1] # 요청에서 종료까지 걸린 시간
    jobs.popleft()
    while True:
        while jobs and jobs[0][0] <= end_time:
            job = jobs.popleft()
            heapq.heappush(disk, (job[1], job[0], 0)) # 소요 시간이 적은 것부터, 0 = 제때 들어옴
        if disk:
            next_job = heapq.heappop(disk)
            end_time += next_job[0] + next_job[2]
            answer += (end_time - next_job[1])
        else: 
            if jobs:
                job = jobs.popleft()
                heapq.heappush(disk, (job[1], job[0], (job[0]-end_time))) # job[0]-end_time = 현재 수행 중인 작업이 끝나고 몇 초 뒤에 새로운 작업이 요청된 경우 끝나는 시간을 갱신해주기 위한 값
            else: break
    return int(answer/n)