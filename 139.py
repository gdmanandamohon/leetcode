'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
class Solution:
    def __init__(self):
        self.hm = {}
        self.S =None
        self.memo = None
    def dp(self, idx):
        if idx == len(self.S): return True
        if self.memo[idx]!=-1: return self.memo[idx]
        cur ="" 
        res = False 
        for j in range(idx, len(self.S)):
            cur+=self.S[j]
            if cur in self.hm:
                #print("find", cur)
                res = res | self.dp(j+1)
        self.memo[idx] = res
        #print(cur, self.memo)
        return self.memo[idx]
            
    def wordBreak(self, S: str, wD: List[str]) -> bool:
        for x in wD:
            self.hm[x]=1
        self.S = S
        self.memo = [-1 for _ in S]
        return self.dp(0)
            
