def isPrime(num):
    if num >= 2:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

def solution(n, k):
    answer = 0
    if k != 10:
        tmp = n
        n = ''
        while tmp:
            n = str(tmp % k) + n
            tmp //= k
    else:
        n = str(n)
    
    n = n.split('0')
    
    for num in n:
        if num:
            if isPrime(int(num)):
                answer += 1
    return answer