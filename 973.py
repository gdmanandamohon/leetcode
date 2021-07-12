'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    def kClosest(self, P: List[List[int]], K: int) -> List[List[int]]:
        mp = collections.defaultdict(list)
        for x, y in P:
            mp[x*x+y*y].append([x, y])
        ans = []
        for k in sorted(mp.keys())[:K]:
            ans +=mp[k]
        return ans[:K] 
