'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
#O(n)
class Solution:
    def missingNumber(self, N: List[int]) -> int:
        ans = len(N)
        for i in range(len(N)):
            ans = ans^i^N[i]
        return ans
