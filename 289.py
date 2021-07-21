'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
class Solution:
    def gameOfLife(self, B: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        axis = [0,1,1,-1,0,-1,-1,1,0]
        r, c  = len(B), len(B[0])
        for i in range(r):
            for j in range(c):
                cur_cl = B[i][j]
                nbr_cl = 0
                for dx in range(8):
                    cx, cy = i+axis[dx], j+axis[dx+1]
                    if 0<=cx<r and 0<=cy<c:
                        nbr_cl  =nbr_cl + B[cx][cy]%2

                if B[i][j]==0 and nbr_cl ==3:
                    B[i][j]=2
                elif B[i][j]==1 and (nbr_cl <2 or nbr_cl>3):
                    B[i][j]=3

        for i in range(r):
            for j in range(c):
                if B[i][j]==2:B[i][j] =1
                elif B[i][j]==3: B[i][j] =0
        return B

