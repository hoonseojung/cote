from itertools import combinations

def isPrime(num):
    if num >= 2:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

def solution(nums):
    answer = 0
    for comb in combinations(nums, 3):
        if isPrime(sum(comb)):
            answer += 1
    return answer