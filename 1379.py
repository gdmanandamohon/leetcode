'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    def getTargetCopy(self, O: TreeNode, C: TreeNode, T: TreeNode) -> TreeNode:
        st = [[O, C]]
        while st:
            o, c = st.pop()
            if o==T:return c
            if o.left: st.append([o.left, c.left])
            if o.right: st.append([o.right, c.right])
