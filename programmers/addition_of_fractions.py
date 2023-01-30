def solution(numer1, denom1, numer2, denom2):
    answer = []
    denom = denom1 * denom2 # 분모
    numer = (numer1 * denom2) + (numer2 * denom1) # 분자
    if denom % numer == 0: # 2/6
        denom /= numer
        answer = [1, denom]
    elif numer % denom == 0: # 6/2
        numer /= denom
        answer = [numer, 1]
    else:
        for i in range(2, int(denom ** 0.5)+1): # 소수 판별
            if denom % i == 0 and numer % i == 0: # 분모의 약수이고 분자도 나눠진다면
                    numer /= i
                    denom /= i
        answer = [numer, denom]
    return answer
###################################################################################
# 최대공약수 찾아 나누기
# for i in range(min(denom, numer), 1, -1):
#     if denom % i == 0 and numer % i == 0:
#         numer /= i
#         denom /= i
#         break