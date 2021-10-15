'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    def productExceptSelf(self, N: List[int]) -> List[int]:
        lft = []
        rht = []
        rht_prd = 1
        lft_prd = 1
        for i in range(len(N)):
            lft_prd *= N[i]
            rht_prd *= N[~i]
            lft.append(lft_prd)
            rht.insert(0, rht_prd)
        ans =[]
        l = len(N)
        for i in range(l):
            if i ==0: ans.append(rht[i+1])
            elif i == l-1: ans.append(lft[i-1])
            else:ans.append(lft[i-1]*rht[i+1])
        return ans
