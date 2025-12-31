def longestPalindrome(s):
    n = len(s)
    dp = [[False]*n for _ in range(n)]
    start = maxlen = 0

    for i in range(n):
        dp[i][i] = True

    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i + l - 1
            if s[i] == s[j] and (l == 2 or dp[i+1][j-1]):
                dp[i][j] = True
                if l > maxlen:
                    start, maxlen = i, l
    return s[start:start+maxlen]

print(longestPalindrome("babad"))
