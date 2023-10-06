def solution(triangle):
    dp = [[0 for _ in range(len(triangle))] for _ in range(len(triangle))] 
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            dp[i][j] = triangle[i][j]
    for i in range(len(triangle)):
        if i == 0:
            continue
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] += dp[i-1][j]
            elif j == len(triangle[i]):
                dp[i][j] += dp[i-1][j-1]
            else:
                dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
    return max(dp[len(triangle)-1])