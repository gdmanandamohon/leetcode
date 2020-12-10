'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        mx = -1<<25
        cmax = -1<<25
        for i, x in enumerate(A):
            mx = max(mx, cmax+x-i)
            cmax = max(cmax, i+x)
        return mx
