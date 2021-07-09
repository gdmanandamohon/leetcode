'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
#O(N)
class Solution:
    def reverseBetween(self, H: ListNode, L: int, R: int) -> ListNode:
        H = ListNode(-1, H)
        L,R = L+1,R+1 
        t, c, d_node, d_node_e = H, 1, None, None
        while t and t.next and c<R:
            if L-1<= c < R:
                cur  = t.next
                t.next=t.next.next
                cur.next=None
                if not d_node:
                    d_node = cur
                    d_node_e = cur
                else:
                    cur.next = d_node
                    d_node = cur
            else:
                t=t.next
            c+=1
        d_node_e.next = t.next
        t.next = d_node
        return H.next
