'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
#O(nlogn)
class Solution:
    def heightChecker(self, H: List[int]) -> int:
        N = sorted(H)
        c=0
        for i in range(len(H)):
            if H[i] !=N[i]:c+=1
        return c
