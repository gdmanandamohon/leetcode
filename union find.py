'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
p = [i for i in range(n)]
def find(x):
	if p[x] ==x: return x
	p[x] = find(p[x])
    return p[x]
        
i, edge=0,0
while i<len(E) and edge !=n-1:
	u, v = E[i]
	p_u = find(u)
	p_v = find(v)
	if p_u !=p_v:
		p[p[v]] = p[u]
