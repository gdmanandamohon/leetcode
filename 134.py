'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
class Solution:
    def canCompleteCircuit(self, G: List[int], C: List[int]) -> int:
        mn, s_idx, l,dif = 1<<29, 0, len(G),0
        for i,x in enumerate(G):
            dif += G[i]-C[i]
            if dif<mn:
                mn = dif
                s_idx =i
        s_idx=(s_idx+1)%l
        dif = 0
        for i in range(l):
            c_idx = (s_idx+i)%l
            dif += G[c_idx]
            if dif<C[c_idx]:return -1
            dif -= C[c_idx]
        return -1 if dif<0 else s_idx
