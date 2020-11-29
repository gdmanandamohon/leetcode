'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    def solve(self, B: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not B:return B
        ax, c, r = [1,0,-1,0,1], len(B[0]), len(B)
        v = [ [False for _ in range(len(B[0]))] for _ in range(len(B))]
        st = []
        for i in range(len(B)):
            for j in range(len(B[i])):
                if (i ==0 or j ==0 or i==r-1 or j==c-1) and B[i][j] =='O':
                    st.append([i,j])
                    v[i][j] = True
        while st:
            x, y = st.pop()
            for i in range(4):
                tx,ty = x+ax[i], y+ax[i+1]
                if 0<=tx<r and 0<=ty<c and B[tx][ty]=='O'and  v[tx][ty]==False:
                    st.append([tx,ty])
                    v[tx][ty]= True
        for i in range(len(B)):
            for j in range(len(B[i])):
                if v[i][j] == True: B[i][j] = 'O'
                else:B[i][j] = 'X'
        return B
            
        
