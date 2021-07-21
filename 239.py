'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    def maxSlidingWindow(self, N: List[int], k: int) -> List[int]:
        dq, ans = [], []
        for i, x in enumerate(N):
            if dq and i+1-dq[0][0]>k:dq.pop(0)
            if not dq or (dq and dq[-1][1]>x):dq.append([i,x])
            else:
                while dq and dq[-1][1]<x: dq.pop()
                dq.append([i,x])
            if i>=k-1:ans.append(dq[0][1])
        return ans
