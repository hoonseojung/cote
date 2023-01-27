t = int(input())
p = [1, 1, 1, 2, 2]
for _ in range(t):
    n = int(input())
    length = n - 5
    if length <= 0: # p 배열 내에 수가 있다면
        print(p[n-1])
    else:    
        for i in range(length): # 배열의 길이가 n이 될 때까지
            p.append(p[-1]+p[-5]) # 맨 마지막 값과 그 수보다 4번 앞의 수 합
        print(p[n-1])