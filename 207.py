'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
#O(V+E)
class Solution:
    def canFinish(self, N: int, P: List[List[int]]) -> bool:
        mp = collections.defaultdict(list)
        mp_pre = collections.defaultdict(list)
        for c, p in P:
            mp[c].append(p)
            mp_pre[p].append(c)
        ans = []
        st = []
        vst = ['W']*N
        for i in range(N):
            if i not in mp_pre and i not in mp:ans.append(i)
            elif i not in mp_pre:
                st.append(i)
        #print(st)     
        while st:
            #print(st[-1], st, vst)
            cur = st[-1]
            if vst[cur] == 'W':
                for x in mp[cur]:
                    if vst[x]=='W':
                        st.append(x)
                    elif vst[x]=='G':return []
                vst[cur] = 'G'
            elif vst[cur] == 'G':
                vst[cur] = 'B'
                ans.append(cur)
                st.pop()                
            elif vst[cur] == 'B':st.pop()
        return True if len(ans) ==N else False
                
            
