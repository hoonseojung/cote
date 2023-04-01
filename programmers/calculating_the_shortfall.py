def solution(price, money, count):
    answer = money - price * (count * (count + 1) / 2)
    if answer >= 0:
        return 0
    else:
        return abs(answer)