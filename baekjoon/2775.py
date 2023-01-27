t = int(input())
for _ in range(t):
    k = int(input()) # 층
    n = int(input()) # 호
    people = [[0 for _ in range(n)] for _ in range(k+1)] # 층은 0층부터, 호는 1호부터
    for i in range(k+1):
        for j in range(n):
            if i == 0:
                people[i][j] = j+1 # 0층 1, 2, 3...
            else: # 1층 ~
                for a in range(j+1): # 해당 호까지
                    people[i][j] += people[i-1][a] # 아래 층의 사람들 수 모두 더하기
    print(people[k][n-1]) # k층 n호