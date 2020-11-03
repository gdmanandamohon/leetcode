'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        def find(v):
            st,prv=head,None
            while st:
                if st.val< v.val:
                    prv=st
                    st=st.next
                else:return prv

        if not head:return head
        cur,fwd = head, head.next
        if not fwd:return head
        while fwd:
            if cur.val>fwd.val:
                t_n = fwd
                cur.next = fwd.next
                t_n.next =None
                pos = find(t_n)
                if not pos:
                    t_n.next=head
                    head =t_n
                else:
                    nxt = pos.next
                    pos.next=t_n
                    t_n.next =nxt
            cur=fwd
            fwd= fwd.next
        return head
