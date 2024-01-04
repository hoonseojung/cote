# case 1 : 서로 주고 받은 수가 다름
# 더 적게 받은 사람 줌
# case 2 : 서로 안 주고 받았거나 같은 수를 주고 받음
# 선물 지수 따짐
# 선물 지수 = 이번 달까지 자신이 친구들에게 준 선물의 수 - 받은 선물의 수
# 선물 지수가 더 작은 사람이 큰 사람에게 하나 줌
# 선물 지수도 같으면 서로 안 주고 받음
def solution(friends, gifts):
    answer = 0
    gift_index = {} # 선물 지수
    for friend in friends:
        gift_index[friend] = [0, {i: 0 for i in friends}]
    for gift in gifts:
        A, B = gift.split()
        gift_index[A][0] += 1
        gift_index[A][1][B] += 1 # A가 B에게 준 선물 개수
        gift_index[B][0] -= 1 

    for giver, info in gift_index.items():
        get = 0
        for reciever, num in info[1].items():
            if giver == reciever: continue
            if num > gift_index[reciever][1][giver]: # 더 많이 줬으면, 하나 받기
                get += 1
            elif num == gift_index[reciever][1][giver]: # 같은 수를 주거나 서로 안 주고 받았다면, 선물 지수 확인
                if gift_index[giver][0] > gift_index[reciever][0]: # 선물 지수가 더 크다면, 하나 받기
                    get += 1
        answer = max(answer, get)
    return answer