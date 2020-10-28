'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        sp, fp = head, head
        while fp and fp.next:
            sp = sp.next
            fp=fp.next.next
            if sp==fp:
                sp = head
                while sp is not fp:
                    sp, fp = sp.next, fp.next
                return sp
                
        return None
