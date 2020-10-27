'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False for _ in range(n+1)]
        dp[1] =True
        for i in range(int(math.sqrt(n))): dp[i*i] = True
        for i in range(2, n+1):
            c = True
            for j in range(1, int(pow(i, 0.5))+1):
                c = c & dp[j*j] & dp[i-j*j]
                if not c:break
            if not c: dp[i] = True
            #print(dp[1:])
        return dp[n]
            
        
                
        
