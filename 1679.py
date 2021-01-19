'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''


'''
[3,1,3,4,3, 3,1,3,4,3]
6
[3,5,1,5]
2
[1,2,3,4]
5
[3,1,3,4,3]
6
'''
class Solution:
    def maxOperations(self, N: List[int], k: int) -> int:
        mp = collections.Counter(N)
        co=0
        for x in mp.keys():
            if k-x == x and mp[k-x]>1:
                co+= mp[x]//2
                mp[x]=0
            elif k-x in mp and k-x != x and mp[k-x]>0:
                mn = min(mp[k-x], mp[x])
                co+=mn
                mp[k-x]-=mn
                mp[x] -=mn
        return co
