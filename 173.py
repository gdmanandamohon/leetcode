'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class BSTIterator:

    def dfs(self, r):
        if not r: return 
        self.dfs(r.left)
        self.ar.append(r.val)
        self.dfs(r.right)
    def __init__(self, root: TreeNode):
        self.ar = []
        self.dfs(root)

    def next(self) -> int:
        t = self.ar.pop(0)
        return t

    def hasNext(self) -> bool:
        return len(self.ar) != 0
