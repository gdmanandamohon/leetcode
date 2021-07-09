'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
#O(??)
class Solution:
    def chk_func(self, k, M, c_p, row, col):
        count = 0 
        c = col-1
        for r in range(row):
            while c >= 0 and M[r][c] > c_p:
                c -= 1
            count += c +1       
        return count
        
    
    def kthSmallest(self, M: List[List[int]], k: int) -> int:
        lo, hi = M[0][0], M[-1][-1]
        row, col = len(M), len(M[0])
        ans = -1
        while lo <= hi:
            mid = (lo+hi)//2
            if self.chk_func(k, M, mid, row, col)>=k:
                ans = mid
                hi = mid-1
            else: lo = mid+1
        return ans
