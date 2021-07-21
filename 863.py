'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    def distanceK(self, R: TreeNode, T: TreeNode, k: int) -> List[int]:
        if k ==0:return [T.val]
        st = [[None, R]]
        adj_mp = collections.defaultdict(list)
        while st:
            #print(st)
            p, cur = st.pop()
            if cur.left:
                st.append([cur, cur.left])
                adj_mp[cur.val].append(cur.left.val)
            if cur.right:
                st.append([cur, cur.right])
                adj_mp[cur.val].append(cur.right.val)
            if p:adj_mp[cur.val].append(p.val)
        #print(adj_mp)        
        vst = [False for _ in range(501)]
        q = [[T.val, 0]]
        vst[T.val] = True
        ans = []
        while q:
            cur, d = q.pop(0)
            for adj in adj_mp[cur]:
                if d+1==k and not vst[adj]:ans.append(adj)
                elif d+1<k and not vst[adj]:
                    q.append([adj, d+1])
                    vst[adj] = True
        return ans
