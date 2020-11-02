'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    def maxWidthOfVerticalArea(self, P: List[List[int]]) -> int:
        P.sort()
        x, y = P[0]
        mx = 0
        #print(P)
        for nx,ny in P:
            #print(nx, x)
            if nx ==x: continue
            else:
                mx = max(nx-x, mx)
                x = nx
        return mx
                
