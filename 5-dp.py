class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        ans = [0,0]
        dp = [[False]*l for i in range(l)]
        for i in range(l): dp[i][i] = True
        for i in range(l-1):
            if s[i] ==s[i+1]:
                dp[i][i+1] = True
                ans = [i, i+1]
        for mx in range(2, l):
            for i in range(l-mx):
                j = i+mx
                if s[i] == s[j] and dp[i+1][j-1]:
                    ans, dp[i][j] = [i,j], True
        return s[ans[0]: ans[1]+1]
            