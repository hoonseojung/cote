# from collections import deque
# def solution(prices):
#     answer = [0 for _ in range(len(prices))]
#     stock = deque()
#     for idx, price in enumerate(prices):
#         if idx == 0: stock.append([price, idx])
#         else:
#             if price >= stock[-1][0]: stock.append([price, idx])
#             else:
#                 while True:
#                     p, i = stock.popleft()
#                     if p > price: answer[i] = idx-i
#                     else: stock.append([p, i])
#                     if i == idx-1: break
#                 stock.append([price, idx])
#     while stock:
#         p, i = stock.popleft()
#         answer[i] = len(prices)-i-1
#     return answer

def solution(prices):
    prices_len = len(prices)
    answer = [0 for _ in range(prices_len)]
    stock = [[0, prices[0]]]
    for i in range(1, prices_len-1):
        if prices[i] >= stock[-1][1]: stock.append([i, prices[i]]) # 상승장
        else: # 하락장
            while stock != [] and stock[-1][1] > prices[i]:
                idx, p = stock.pop()
                answer[idx] = i-idx
            stock.append([i, prices[i]])
    while stock:
        idx, p = stock.pop()
        answer[idx] = prices_len-idx-1
    return answer