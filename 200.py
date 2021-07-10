'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

#O(M.N)
class Solution:
    def numIslands(self, G: List[List[str]]) -> int:
        ones = []
        ax = [0,1,0,-1,0]
        row, col = len(G), len(G[0])
        c = 0
        def dfs(c,r):
            st = [[c,r]]
            G[c][r] = "0"
            while st:
                x, y = st.pop()
                for dxy in range(4):
                    tx, ty = x +ax[dxy], y+ax[dxy+1]
                    if 0<=tx<row and 0<=ty<col and G[tx][ty] =='1':
                        G[tx][ty] = "0"
                        st.append([tx, ty])
                        
                
        for i in range(len(G)):
            for j in range(len(G[0])):
                if G[i][j] == '1': ones.append([i,j])
        for x, y in ones:
            if G[x][y] =="1":
                dfs(x,y)
                c+=1
        return c
                    
        
