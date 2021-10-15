'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

def breakPalindrome(self, P: str) -> str:
        if len(P)==1:return ""
        mp = collections.Counter(P)
        if len(mp.keys()) ==1 and 'a' in mp: return P[:len(P)-1]+'b'

        mdk = None
        for k in mp.keys():
            if mp[k] ==1:
                mdk =k
                break
        idx= None
        for i,c in enumerate(P):
            #print(c, not mdk, mdk == c)
            if c =='a':continue
            elif c !='a' and (not mdk or mdk != c):
                idx = i
                break
            else:
                pass
        if idx is None:return P[:len(P)-1]+'b'
        else: return P[:idx]+'a'+P[idx+1:]
        
        
 
 
 class Solution:
    def breakPalindrome(self, P: str) -> str:
        if len(P)==1:return ""
        i, l = 0, len(P)
        while i<(l//2):
            if P[i] !='a':return P[:i]+'a'+P[i+1:]
            i+=1
        return P[:len(P)-1]+'b'
