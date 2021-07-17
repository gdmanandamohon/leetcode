'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    def triangleNumber(self, N: List[int]) -> int:
        cou = 0
        N.sort(reverse=True)
        for k, x in enumerate(N):
            j = k+1
            i = len(N)-1
            while j<i:
                if N[i]+N[j]<=N[k]:
                    i-=1
                else:
                    cou+=i-j
                    j+=1
        return cou
