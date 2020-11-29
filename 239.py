'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    def maxSlidingWindow(self, N: List[int], k: int) -> List[int]:
        if len(N)<=k:return [max(N)]
        elif k ==1: return N
        ans=[]
        dq=[ [0,N[0]]]
        for i in range(1,len(N)):
            if i-dq[0][0]>=k: dq.pop(0)
            if dq and  dq[-1][1]>N[i]:dq.append([i,N[i]])
            else:
                while dq and  dq[-1][1]<N[i]:dq.pop()
                dq.append([i,N[i]])
            if i>=k-1: ans.append(dq[0][1])
        return ans
