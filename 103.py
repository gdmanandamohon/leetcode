'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    
    def zigzagLevelOrder(self, R: TreeNode) -> List[List[int]]:
        def dfs(r, l):
            if not r:
                return 
            hm[l].append(r.val) if l%2==0 else hm[l].insert(0, r.val)
            dfs(r.left, l+1)
            dfs(r.right, l+1)
            
        hm = collections.defaultdict(list)
        dfs(R, 0)
        return [ hm[i] for i in hm.keys()]
        
