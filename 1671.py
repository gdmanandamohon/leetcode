'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

'''
[1,2,3,4,4,3,2,1]
[4,3,2,1,1,2,3,1]
[1,3,3,4,4,5,5,6,6,7,7,6,6,5,5,3,3,2,2,1,1]
[1,2,3,4,4,3,2,1]
[2,1,1,5,6,2,3,1]
[9,8,1,7,6,5,4,3,2,1]
'''
class Solution:
    def minimumMountainRemovals(self, N: List[int]) -> int:
        mn,l =10**9+7, len(N)
        inc=[1 for _ in range(l)]
        dec=[1 for _ in range(l)]
        for i in range(l):
            for j in range(i):
                if N[j]<N[i]: inc[i] = max(inc[i], inc[j]+1)
                if N[-j-1]<N[-i-1]: dec[-i-1] = max(dec[-i-1], dec[-j-1]+1)
                    
        for i in range(1, len(N)-1):
            t = i-inc[i]+1 + l-i-dec[i]
            mn = min(mn, t)
        return mn
