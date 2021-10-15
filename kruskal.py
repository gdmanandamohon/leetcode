'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

		def cruskal(nds, E):
            def find(x):
                if p[x] == x: return x
                p[x] = find(p[x])
                return p[x]
            
            p=[i for i in range(nds)]
            ans =0
            while E:
                c, u, v = heapq.heappop(E)
                p_u =find(u)
                p_v =find(v)
                if p_u != p_v:
                    p[p[v]] = p[u]
                    ans+= c
            return ans
        cost = []
        heapq.heapify(cost)
