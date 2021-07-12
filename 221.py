'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

#O(M.N)
class Solution:
    def maximalSquare(self, M: List[List[str]]) -> int:
        cl,rw = len(M[0])+1, len(M)+1
        dp = [[0]*cl for _ in range(rw)]    
        mx = 0
        for r in range(1, rw):
            for c in range(1, cl):
                if M[r-1][c-1]== '1':
                    dp[r][c] = min(dp[r-1][c-1], dp[r][c-1], dp[r-1][c])+1
                    #print(dp)
                    mx = max(mx, dp[r][c])
        return mx*mx
