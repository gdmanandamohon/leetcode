'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
class Solution:
    def summaryRanges(self, N: List[int]) -> List[str]:
        if not N: return N
        ans,i,l=[],0,len(N)
        while i<l:
            j=i+1
            while j<l and N[j]-N[j-1]==1:j+=1
            if j-i>1:ans.append(str(N[i])+'->'+str(N[j-1]))
            else:ans.append(str(N[i]))
            i=j
        return ans
