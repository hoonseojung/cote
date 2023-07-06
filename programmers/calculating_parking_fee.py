from collections import defaultdict
import math

def solution(fees, records):
    # fees : 기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)
    answer = []
    time = defaultdict(str)
    fee = defaultdict(int) # 누적 주차 시간을 구한 후 마지막에 주차 요금 계산하는 딕셔너리
    for record in records:
        record_l = record.split()
        if record_l[2] == 'IN': # 입차
            time[record_l[1]] = record_l[0]
        else: # 출차
            in_time = list(map(int, time[record_l[1]].split(':')))
            out_time = list(map(int, record_l[0].split(':')))
            if in_time[1] <= out_time[1]: # 분
                fee[record_l[1]] += (out_time[0] - in_time[0]) * 60 + (out_time[1] - in_time[1])
            else:
                fee[record_l[1]] += (out_time[0] - 1 - in_time[0]) * 60 + (out_time[1] + 60 - in_time[1])
            time[record_l[1]] = 0

    for c, t in time.items(): # 입차 후 출차 기록이 없는 차량 처리
        if t:
            in_time = list(map(int, t.split(':')))
            fee[c] += (23 - in_time[0]) * 60 + (59 - in_time[1])

    for c in fee: # 주차 요금 계산
        if fee[c] <= fees[0]: # 기본 시간 내
            fee[c] = fees[1] # 기본 요금
        else: # 기본 시간 초과
            fee[c] = fees[1] + math.ceil((fee[c] - fees[0]) / fees[2]) * fees[3]

    f = dict(sorted(fee.items()))
    answer = list(f.values())
    return answer