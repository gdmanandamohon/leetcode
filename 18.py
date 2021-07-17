'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
class Solution:
    def fourSum(self, N: List[int], t: int) -> List[List[int]]:
        N.sort()
        st= []
        for i,x in enumerate(N):
            if i != 0 and N[i-1]==N[i]: #Similar value  Move ahead
                continue
            for j in range(i+1, len(N)):
                if j != i+1 and N[j-1] ==N[j]:continue  #Similar value  Move ahead
                k = j+1
                l = len(N)-1
                while k<l:
                    if x+N[j]+N[k]+N[l] ==t:
                        st.append([x,N[j],N[k],N[l]]) 
                        l-=1
                        k+=1
                        while k<l and  N[k-1]==N[k]:k+=1  #Similar Pointer Move ahead
                        while k<l and N[l]==N[l+1]:l-=1   #Similar Pointer Move ahead
                    elif x+N[j]+N[k]+N[l]>t: l-=1
                    else:k+=1
        return st
