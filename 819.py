'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
#O(M+N)
class Solution:
    def mostCommonWord(self, P: str, B: List[str]) -> str:
        B= set(B)
        P = P.lower()
        P= re.split('\W+', P)
        mp = collections.defaultdict(int)
        mx, mx_occ = 0, None
        for x in P:
            if x not in B:
                mp[x]+=1
                if mp[x]>mx:
                    mx = mp[x]
                    mx_occ = x
        #print(mp)
        return mx_occ
