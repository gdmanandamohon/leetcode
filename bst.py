'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    def search(self, N: List[int], target: int) -> int:
        idx = -1 
        lo, hi =0, len(N)-1
        while lo<=hi:
            md = lo+(hi-lo)//2
            if N[md]==target:
                idx = md
            if N[md]>target:
                hi = md-1
            else: lo=md+1
        return idx
