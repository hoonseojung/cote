def mineral_water_num(num):
    k = 0
    for i in range(1, int(num ** 0.5)+1):
        if num % i == 0:
            k += 1
            if i ** 2 != num: # 제곱수가 아니라면
                k += 1 # 약수들은 짝이 있음
    return k

def solution(number, limit, power):
    answer = 0
    count = [1] # 약수의 개수
    for num in range(2, number+1):
        tmp = mineral_water_num(num)
        if tmp > limit: tmp = power
        count.append(tmp)
    return sum(count)