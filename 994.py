'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
#O(M*N)
class Solution:
    def orangesRotting(self, G: List[List[int]]) -> int:
        axis = [0,1,0,-1,0]
        pq = []
        col, row = len(G[0]), len(G)
        for i in range(row):
            for j in range(col):
                if G[i][j]==2:
                    heapq.heappush(pq, [0, i,j])
        mx = 0
        while pq:
            c, ax, ay = heapq.heappop(pq)
            mx = max(mx, c)
            for i in range(4):
                tx, ty = ax+axis[i], ay+axis[i+1]
                if 0<=tx<row and 0<=ty<col and G[tx] [ty]==1:
                    heapq.heappush(pq, [c+1, tx,ty])
                    G[tx] [ty] = 2
        for i in range(row):
            for j in range(col):
                if G[i][j]==1: return -1
        return mx  
                    
