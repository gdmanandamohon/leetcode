'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
#O(M*N)
class Solution:
    
    def dfs(self, r, t):
        if (not t and r) or (not r and t):return False
        if not r and not t: return True
        return r.val == t.val and self.dfs(r.left, t.left) and self.dfs(r.right, t.right)
    
    def isSubtree(self, r: TreeNode, s: TreeNode) -> bool:
        st= [r]
        while st:
            cur = st.pop()
            if cur.val == s.val:
                if self.dfs(cur, s):return True
            if cur.left:st.append(cur.left)
            if cur.right:st.append(cur.right)
        return False
