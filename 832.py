'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for x in A:
            i=0
            while i<len(x)/2:
                x[i], x[-i-1] =  x[-i-1]^1, x[i]^1
                i+=1
        return A
