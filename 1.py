'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
class Solution:
    def twoSum(self, N: List[int], T: int) -> List[int]:
        s = {}
        for i,x in enumerate(N):
            if T-x in s:return [i, s[T-x]]
            else:s[x]=i
