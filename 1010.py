'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    def numPairsDivisibleBy60(self, T: List[int]) -> int:
        dc,c = collections.defaultdict(int),0
        for t in T:
            if t%60==0:
                c+=dc[t%60]
            elif 60 - t%60 in dc:
                c+=dc[60 - t%60]
            dc[t%60]+=1
        return c
            
            
