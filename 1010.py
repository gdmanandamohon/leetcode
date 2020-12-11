'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    def numPairsDivisibleBy60(self, T: List[int]) -> int:
        dd = collections.defaultdict(list)
        c=0
        for x in T:
            r = x%60
            if 60 - r in dd:
                c+= dd[60-r]
            elif r ==0 and r in dd:
                c+= dd[0]
            if r not in dd:dd[r] =1
            else: dd[r]+=1
        return c
                
            
            
