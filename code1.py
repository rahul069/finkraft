def common(X,Y):
    # using X dp array of size
    n = len(X)
    m = len(Y)
    dp = [[0 for i in range(m+1)] for i in range(n+1)]
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if X[i] == Y[j]:
                dp[i][j] = dp[i+1][j+1]+1
            else:
                dp[i][j] = max(dp[i+1][j],dp[i][j+1])
    return dp[0][0]

print(common("aaaabbbbc","aaaaab"))