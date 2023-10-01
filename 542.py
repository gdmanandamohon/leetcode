class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ax = [0,1,0,-1,0]
        q = deque([])
        r1, c1 = len(mat), len(mat[0])
        dp = [[float('inf')]*c1 for _ in range(r1)] 
        for i in range(r1):
            for j in range(c1):
                if mat[i][j] ==0: 
                    q.append([i, j])
                    dp[i][j] = 0
        while q:
            r, c = q.popleft()
            for i in range(4):
                c_r, c_c = r+ ax[i], c+ax[i+1]
                if 0<=c_r<r1 and 0<=c_c<c1  and dp[c_r][c_c]>dp[r][c]+1:
                    dp[c_r][c_c]= dp[r][c]+1
                    q.append([c_r, c_c])
        return dp