'''
l4zyc0d3r /// 1631 /// Sun Oct 25, 2020
'''
class Solution:
    def minimumEffortPath(self, G: List[List[int]]) -> int:
        ax = [ [1,0],[-1,0],[0,1],[0,-1]]
        r,c = len(G),len(G[0])
        
        def isvalid(i,j):
            if 0<=i<r and 0<=j<c: return True
            return False

        import heapq             
        ans = 1<<32 
        vs = [ [ True for v in col] for col in G]
        q, mn = [], 1<<32 
        q.append((0, G[0][0], 0, 0,  G[0][0]))  
        heapq.heapify(q)

        while q:
            mxcost, cost, x, y,  prev_cost = heapq.heappop(q)
            vs[x][y] = False
            if x==r-1 and y ==c-1:
                return mxcost
            for tx,ty in ax:
                if isvalid(tx+x,ty+y) and vs[tx+x][ty+y]:
                    heapq.heappush(q, (max(mxcost, abs(prev_cost-G[tx+x][ty+y])), cost+G[tx+x][ty+y], tx+x,ty+y,  G[tx+x][ty+y]))
            #print(q)
                        
                        
        return ans
        
