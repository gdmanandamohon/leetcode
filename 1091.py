'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
#O(n*n log(n))
class Solution:
    def shortestPathBinaryMatrix(self, G: List[List[int]]) -> int:
        pq = [[1, 0,0]]
        ax = [0,1,1,-1,0,-1,-1,1,0]
        r, c = len(G), len(G[0])
        if G[r-1][c-1] ==1 or G[0][0] ==1 :return -1
        vs = [[ True for _ in range(c) ] for _ in range(r)]
        vs[0][0] = False
        heapq.heapify(pq)
        while pq:
            d, x, y =  heapq.heappop(pq)
            if x ==r-1 and y == c-1: return d
            for dt in range(8):
                tx, ty = x+ax[dt], y+ax[dt+1] 
                if 0<=tx<r and 0<=ty<c and G[tx][ty] ==0 and vs[tx][ty]:
                    heapq.heappush(pq, [d+1, tx,ty])
                    vs[tx][ty] = False
        return -1
            
