'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.a = None
        self.b = None
        def dfs (r, l, p):
            if not r:
                return 
            if r.val ==x:
                self.a = [l, p.val if p else None]
            if r.val ==y:
                self.b = [l, p.val if p else None]
            dfs(r.left, l+1, r)
            dfs(r.right, l+1, r)
            return l
        dfs(root, 0, None)
        print(self.a, self.b)
        return self.a[0]==self.b[0] and self.a[1]!=self.b[1]
