'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
#O(V+E)
class Solution:
    def findOrder(self, N: int, P: List[List[int]]) -> List[int]:
        if not P: return [i for i in range(N)]
        mp = collections.defaultdict(list)
        mp_pre = collections.defaultdict(list)
        for c, p in P:
            mp[p].append(c)
            mp_pre[c].append(p)
        ans = []
        st = []
        vst = ['W']*N
        for i in range(N):
            if i not in mp_pre and i not in mp:ans.append(i)
            elif i not in mp_pre:
                st.append(i)    
        while st:
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
        return ans[::-1] if len(ans) ==N else []
                
            
        
