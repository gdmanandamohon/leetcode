'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    def topKFrequent(self, N: List[str], K: int) -> List[str]:
        M = collections.Counter(N)
        return [ k for k, _ in sorted(M.items(), key=lambda item: (-item[1], item[0]))[:K]]
        
