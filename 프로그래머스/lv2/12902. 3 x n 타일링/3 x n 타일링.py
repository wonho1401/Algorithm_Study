def solution(n):
    dp = [0]* 5001
    dp[2] = 3
    dp[4] = 11
    for i in range(6, 5001):
        dp[i] = (dp[i-2]*4 - dp[i-4]) % 1000000007
    return dp[n]