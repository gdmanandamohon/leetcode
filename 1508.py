'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
#Complexity max(n^2, Alog(A))  ~  N^2

class Solution:
    def rangeSum(self, N: List[int], n: int, LF: int, RH: int) -> int:
        l,mod = [],10**9+7
        cum = [N[0]]
        [cum.append(N[i]+cum[i-1]) for i in range(1, len(N))]
        for i in range(len(N)):
            for j in range(i, len(N)):
                if i ==0:
                    l.append(cum[j])
                else:
                    if i==j:l.append(cum[i]-cum[i-1])
                    else:l.append(cum[j]-cum[i-1])
        l.sort()
        return sum(l[LF-1:RH])%mod
