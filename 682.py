'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res = []
        for x in ops:
            if x =='C':res.pop()
            elif x =='D':  res.append(res[-1]*2)
            elif x == '+': res.append(res[-1]+res[-2])
            else: res.append(int(x))
        return sum(res)
