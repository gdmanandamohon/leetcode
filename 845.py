'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

'''
[2,1,4,7,3,2,1]
[2,2,2]
[2,1,4,7]
[7,8,9,10]
[7,6,5,4,0]
[2,1,4,7,3,2,1,2,1,4,7,3,2,1]
[1,2,2,2,2,2,2,2,2,2,1]
[875,884,239,731,723,685]
'''
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        mx, i, l, peak =0, 0, len(A), False
        
        while i<l-1:
            if A[i]<A[i+1]:
                j=i
                while j<l-1 and A[j] < A[j+1]:
                    j+=1
                j=j+1
                while  j<l and  A[j-1]>A[j]:
                    j+=1
                    peak = True
                if peak: mx = max(mx, j-i)
                peak = False
                i=j-2
            i=i+1
        return mx
            
        
