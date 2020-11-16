'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root: return 0
        res = 0
        if low<=root.val<=high:
            res = root.val
        return res + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high) 
