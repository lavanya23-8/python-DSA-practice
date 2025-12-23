def maxCoins(nums):
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0]*n for _ in range(n)]

    for length in range(2, n):
        for l in range(0, n-length):
            r = l + length
            for k in range(l+1, r):
                dp[l][r] = max(dp[l][r],
                               nums[l]*nums[k]*nums[r] + dp[l][k] + dp[k][r])
    return dp[0][n-1]

print(maxCoins([3,1,5,8]))
