def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()

    for lost_person in lost[:]:
        for people in reserve[:]:
            if people == lost_person: # 가져온 사람이 잃어버린 경우
                lost.remove(lost_person)
                reserve.remove(people)
                break

    for lost_person in lost[:]:
        for people in reserve[:]:
            if (people==lost_person-1) or (people==lost_person+1): # 본인 앞뒤
                lost.remove(lost_person)
                reserve.remove(people)
                break
                
    answer = n - len(lost)
    return answer