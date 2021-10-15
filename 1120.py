'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.mx = -1
        def dfs(r):
            if not r: return [0,0.0]  #t_v, n_c
            l_n,lsum = dfs(r.left)
            r_n, rsum = dfs(r.right)
            ttl_n = l_n+r_n+1
            ttl_v = lsum+rsum+r.val
            self.mx = max(self.mx, ttl_v /ttl_n)
            return [ttl_n, ttl_v]
        dfs(root)
        return self.mx
