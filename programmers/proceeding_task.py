# 시간 -> 분
def convert_to_minutes(time):
    hours, minutes = map(int, time.split(':'))
    return (hours * 60 + minutes)
    
def solution(plans):
    plans = sorted(plans, key=lambda x: x[1], reverse=True)
    stop = []
    answer = []
    while len(plans) >= 2:
        name = plans[-1][0]
        start = convert_to_minutes(plans[-1][1])
        playtime = int(plans[-1][2])

        next_start = convert_to_minutes(plans[-2][1])  # 다음 과제의 시작 시간
        spare_time = next_start - (start + playtime) # 현재 과제를 마치고 남은 시간
        
        if spare_time >= 0:
            answer.append(name)
            plans.pop()
            while spare_time > 0 and stop:
                if spare_time >= stop[-1][1]:
                    spare_time -= stop[-1][1]
                    answer.append(stop.pop()[0])
                else:
                    stop[-1][1] -= spare_time
                    break
        # 남은 시간이 부족하다면 현재 과제를 잠시 멈추고 stop에 추가
        else:
            stop.append([name, playtime-(next_start-start)])
            plans.pop()
    answer.append(plans.pop()[0])
    answer.extend(name for name, playtime in reversed(stop))

    return answer