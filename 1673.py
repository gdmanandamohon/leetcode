'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    def mostCompetitive(self, N: List[int], k: int) -> List[int]:
        q, l = [], len(N)
        for i, x in enumerate(N):
            if not q: q.append(x)
            else:
                if  q[-1]> x:
                    while q and len(q) + (l-i)>k and q[-1]> x:
                        q.pop()
                q.append(x)
            #print(q)
        return q[:k]
                
