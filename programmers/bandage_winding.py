# 체력 + (초당 회복량 * 공격 받기 전까지 지난 시간)
def solution(bandage, health, attacks):
    answer = health # 현재 체력
    cur_time = 0 # 시간
    continuous = 0 # 연속 성공
    for attack in attacks:
        continuous = attack[0] - cur_time - 1
        answer += continuous * bandage[1]
        while True: # 만약 지속 시간 동안 연속 성공 시, 체력 추가 회복
            if continuous >= bandage[0]:
                answer += bandage[2]
                continuous -= bandage[0]
            else: break
        if answer > health: answer = health # 체력이 최대 체력보다 높은 경우 최대 체력으로 리셋
        answer -= attack[1] # 공격 당함
        cur_time = attack[0]
        continuous = 0 # 연속 성공 초기화
        if answer <= 0: return -1
    return answer