'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    def champagneTower(self, P: int, row: int, col: int) -> float:
        mx = 100
        dp = [[0 for _ in range(mx)] for _ in range(mx) ]
        dp[0][0] = P
        for x in range(mx):
            for y in range(x+1):
                nx, ny1, ny2 = x+1, y, y+1
                if dp[x][y]>1 and nx<mx and ny1<mx and ny2<mx:
                    r = abs(dp[x][y] -1)
                    dp[x][y] = 1.0
                    r /=2
                    dp[nx][ny1] +=r
                    dp[nx][ny2] +=r
        return 1.0 if dp[row][col]>1 else dp[row][col]
