'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    def maxHeight(self, C: List[List[int]]) -> int:
        l = []
        for x in C:
            l.append(sorted(x))
        l.sort(key = lambda x: x[0]*x[1]*x[2])
        mx =0
        dp = [h for _,_,h in l]
        for i in range(1,len(l)):
            mx=0
            for j in range(i):
                if l[j][0]<=l[i][0] and l[j][1]<=l[i][1] and l[j][2]<=l[i][2]:
                    mx = max(mx, dp[j]+dp[i])
            dp[i] = max(mx,dp[i])    
        return(max(dp))
                
