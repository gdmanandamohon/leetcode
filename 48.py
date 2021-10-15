'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

#Traspose then Rotate
class Solution:
    def rotate(self, M: List[List[int]]) -> None:
        r, c = len(M), len(M[0])
        for i in range(r):
            for j in range(i+1, c):
                M[i][j],M[j][i] = M[j][i], M[i][j]
        d = c//2
        for i in range(r):
            for j in range(d):
                M[i][j], M[i][c-j-1] = M[i][c-j-1], M[i][j]
            
