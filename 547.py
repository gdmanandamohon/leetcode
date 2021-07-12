'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    def findCircleNum(self, G: List[List[int]]) -> int:
        mp = collections.defaultdict(list)
        for i in range(len(G)):
            for j in range(len(G[0])):
                if G[i][j] == 1:
                    mp[i].append(j)
        #print(mp)
        v = [0 for _ in range(len(G))]
        c = 0
        for i in range(len(G)):
            #print('for node', i)
            if v[i] ==1:continue
            else:
                st, flag = [i], True
                v[i] = 1
                while st:
                    cur = st.pop()
                    for n in mp[cur]:
                        if v[n] ==0:
                            st.append(n)
                        v[n] = 1
                c+=1
        return c
                
                    
