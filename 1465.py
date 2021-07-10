'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    def maxArea(self, h: int, w: int, H: List[int], W: List[int]) -> int:
        H.sort()
        W.sort()
        h_max= max(H[0], h-H[-1])
        w_max= max(W[0], w-W[-1])
        for i in range(1, len(H)):
            h_max = max(h_max, H[i]-H[i-1])
        for i in range(1, len(W)):
            w_max = max(w_max, W[i]-W[i-1])
        print(h_max, w_max)
        return (w_max*h_max)%(pow(10,9)+7)
