import bisect

def lis(nums):
    dp = []
    for x in nums:
        i = bisect.bisect_left(dp, x)
        if i == len(dp):
            dp.append(x)
        else:
            dp[i] = x
    return len(dp)

print(lis([10,9,2,5,3,7,101,18]))
