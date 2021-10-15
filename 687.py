'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
class Solution:
    def longestUnivaluePath(self, r: TreeNode) -> int:
        def dfs(R):
            if not R: return [None, 0]
            if not R.left and not R.right: return [R.val, 0]
            lf, s1 = dfs(R.left)
            rr, s2 = dfs(R.right)
            f = 0
            if lf ==rr ==R.val:
                self.mx, f = max(self.mx, s1+s2+2), max(s1, s2)+1
            elif rr ==R.val:
                self.mx, f = max(self.mx, s2+1), s2+1
            elif lf ==R.val:
                self.mx,f = max(self.mx, s1+1), s1+1
            return [R.val, f ]
        
        self.mx = 0 
        dfs(r)
        return self.mx
        
            
        
