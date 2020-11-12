'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    def maxProfit(self, I: List[int], O: int) -> int:
        def chkfn(ll):
            sm = 0
            for n in I:
                if n>ll: sm+= n-ll
                else: break
            return sm
        
        def sum_al(ll):
            sm,i = 0,0
            for idx, n in enumerate(I):
                if n>ll:
                    sm+= n*(n+1)//2 - ll*(ll+1)//2
                    i+=n-ll
                    sm %=mod
                    I[idx] = ll
                else: break
            return sm,i
        
        def add_remain(ans, tot):
            i,l=0,len(I)
            while tot<O:
                if i==0 and I[i] ==0:break
                ans  = ans+I[i]
                I[i] = I[i]-1
                i, tot = (i+1)%l, tot+1
                ans %=mod
            return ans%mod
 
        I.sort(reverse=True)
        lo,hi,mod,tot,cur = 1,max(I), 10**9+7, 0,1
        while lo<=hi:
            md = lo+(hi-lo)//2
            if chkfn(md)>=O: lo = md+1
            else: hi = md-1
        
        ans, tot= sum_al(lo)
        return add_remain(ans, tot)
            
                
