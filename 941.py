'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    def validMountainArray(self, M: List[int]) -> bool:
        lo, hi = 0, len(M)-1
        if hi<2:return False
        while lo<=hi:
            mdl = lo + (hi-lo)//3
            mdr = hi - (hi-lo)//3
            if M[mdl] <M[mdr]: lo = mdl+1
            else: hi = mdr-1
        if lo==len(M)-1 or lo==0:return False
        for i in range(lo):
            if M[i]>=M[i+1]:return False

        for i in range(lo, len(M)-1):
            if M[i]<=M[i+1]:return False
        return True
            
        
