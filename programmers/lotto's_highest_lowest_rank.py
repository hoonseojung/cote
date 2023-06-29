def solution(lottos, win_nums):
    answer = []
    flags = [0] * 45 # 1 ~ 45 = 0 ~ 44
    for num in win_nums:
        flags[num-1] = 1
    count = 0
    z = 0
    for lotto in lottos:
        if lotto == 0:
            z += 1
            continue
        if flags[lotto-1] == 1:
            count += 1
    high = 7 - count - z
    low = 7 - count
    if count == 0:
        low = 6
        if z == 0:
            high = 6

    answer = [high, low]
    return answer

# def solution(lottos, win_nums):

#     rank=[6,6,5,4,3,2,1]

#     cnt_0 = lottos.count(0)
#     ans = 0
#     for x in win_nums:
#         if x in lottos:
#             ans += 1
#     return rank[cnt_0 + ans],rank[ans]