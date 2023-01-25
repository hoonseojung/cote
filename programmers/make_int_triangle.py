def solution(triangle):
    answer = 0
    dp = [[0] * len(i) for i in triangle]
    dp[0][0] = triangle[0][0]
    for i in range(len(dp)-1):
        for j in range(len(dp[i])):
            dp[i+1][j] = max(dp[i][j] + triangle[i+1][j], dp[i+1][j])
            dp[i+1][j+1] = max(dp[i][j] + triangle[i+1][j+1], dp[i+1][j+1])
            # j의 범위가 len(dp[i])까지이므로 마지막 원소를 확인하기 위해 j+1까지 확인
    answer = max(dp[len(dp)-1])
    return answer