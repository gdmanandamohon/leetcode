'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def failfunc(s):
            F= [0 for _ in s]
            i,j = 1, 0
            while i<len(s):
                if s[i] ==s[j]:
                    j+=1
                    F[i] = j
                    i+=1
                else: 
                    if j == 0: F[i],i = 0, i+1
                    else: j = F[j-1] 
            return F
        
        def find(F,H, N):
            i,j=0,0
            while i<len(H):
                if H[i] ==N[j]: i,j = i+1, j+1
                if j==len(N): return i-len(N)
                elif i<len(H) and H[i] != N[j]:
                    if j == 0: i+ = 1
                    else: j = F[j-1] 
            return -1
        
        if not needle: return 0
        if not haystack:return -1
        F = failfunc(needle)
        return find(F,haystack, needle)
