'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    def frequencySort(self, N: List[int]) -> List[int]:
        hm = {}
        for x in N:
            if x not in hm: hm[x] = 1
            else: hm[x]+=1
        
        l = [[hm[k],k] for k in hm.keys()]
        l.sort(reverse =False, key = lambda x: (x[0],-x[1]))
        ans = []
        for i, v in l:
            for j in range(i):ans.append(v)
        return ans
         
