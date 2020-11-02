'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    def canFormArray(self, A: List[int], P: List[List[int]]) -> bool:
        for j,a in enumerate(P):
            idx = None
            for i, v in enumerate(a):
                if v not in A: return False
                elif v in A and i==0:
                    idx = A.index(v)
                    continue
                else:
                    if v in a and A.index(v) != A.index(A[idx])+1:return False
                    else: idx = A.index(v)
        return True
                    
                
                
                
