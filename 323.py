'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
class Solution:
    def countComponents(self, N: int, E: List[List[int]]) -> int:
        mp = collections.defaultdict(list)
        mpr = collections.defaultdict(list)
        vst = [True for _ in range(N)]
        for s,d in E:
            mp[s].append(d)
            mpr[d].append(s)
        
        def dfs(r):
            st = [r]
            vst[r] = False
            while st:
                cur = st.pop()
                for n in mp[cur]:
                    if vst[n]:
                        st.append(n)
                        vst[n] = False
                for n in mpr[cur]:
                    if vst[n]:
                        st.append(n)
                        vst[n] = False
        c=0
        
        for k in range(N):
            if vst[k]:
                c+=1
                dfs(k)
        return c
