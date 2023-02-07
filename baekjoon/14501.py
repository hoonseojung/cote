n = int(input())
counsel = []
for _ in range(n):
    counsel.append(list(map(int, input().split())))
dp = [0] * (n+1)
for i in range(n-1, -1, -1):
    if (counsel[i][0] + i) > n: # 기간 + 상담일 >= 퇴사일
        dp[i] = dp[i+1] # 상담 x
    else: # 기간 내에 상담이 가능하다면
        dp[i] = max(dp[i+1], (dp[i + counsel[i][0]] + counsel[i][1])) # 해당 일에 상담을 한 것과 안 하고 진행한 것 중 더 큰 값

print(dp[0])