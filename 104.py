'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    def maxDepth(self, r: TreeNode) -> int:
        if not r: return 0
        if not r.left and not r.right: return 1
        return max(1+self.maxDepth(r.left), 1+ self.maxDepth(r.right))
