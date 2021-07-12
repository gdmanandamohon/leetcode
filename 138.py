'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
class Solution:
    def copyRandomList(self, H1: 'Node') -> 'Node':
        H2, t1, t2 = None, H1, None
        mp, c = {}, 0
        while t1:
            if not H2:
                H2=t2 = Node(t1.val)
            else:
                t2.next= Node(t1.val)
                t2=t2.next
            mp[t1] = t2
            t1=t1.next
            c+=1
            
        t1, t2, c = H1, H2,0
        while t1:
            if t1.random:
                t2.random = mp[t1.random]
            t1= t1.next
            t2 = t2.next
        return H2
        
