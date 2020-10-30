'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''


class Codec:
    def serialize(self, root: TreeNode) -> str:
        ans = []
        def dfs(r):
            if not r:return 
            ans.append(str(r.val))
            dfs(r.left)
            dfs(r.right)
        dfs(root)
        return ','.join(ans)
    
    def conBST(self, ar, st, en):
        if st>en: return None
        rt = TreeNode(ar[st])
        if st==en: return rt
        idx = st
        while idx<=en and int(ar[idx])<=int(ar[st]):idx+=1
        rt.right = self.conBST(ar, idx, en)
        rt.left = self.conBST(ar, st+1, idx-1)  
        return rt
        
    def deserialize(self, data: str) -> TreeNode:
        if not data: return 
        data = data.split(',')
        return self.conBST(data, 0, len(data)-1)
