'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    def removeDuplicates(self, N: List[int]) -> int:
        ptr, i = 0, 0 
        while i<len(N):
            j=i+1
            while j<len(N) and N[i]==N[j]:
                j+=1
            if j-i>=2:
                N[ptr], N[ptr+1]= N[i], N[i]
                ptr+=2
            else:
                N[ptr] = N[i]
                ptr+=1
            i=j
        return ptr
