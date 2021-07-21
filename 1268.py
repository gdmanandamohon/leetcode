'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
class Solution:
    def suggestedProducts(self, P: List[str], sW: str) -> List[List[str]]:
        P.sort()
        prfx, ans  = '', []
        for c in sW:
            prfx+=c
            i = bisect.bisect_left(P, prfx)
            ans.append([ x  for x in P[i:i+3] if x.startswith(prfx)])
        return ans
