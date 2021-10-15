'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
#O(n log(n))
class Solution:
    def connectSticks(self, S: List[int]) -> int:
        if not S or len(S)<2:return 0
        heapq.heapify(S)
        c = 0
        while len(S)>1:
            x = heapq.heappop(S)+heapq.heappop(S)
            c+=x
            heapq.heappush(S, x)
        return c
