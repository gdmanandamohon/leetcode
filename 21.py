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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:return l2
        if not l2: return l1
        if l1.val<l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        self.H, self.t = None, None
        def attach(node):
            if not self.H: 
                self.H = node
                self.t= node
            else:
                self.t.next = node
                self.t = node
        
        while l1 and l2:
            if l1.val>=l2.val:
                attach(l2)
                l2 = l2.next
            else:
                attach(l1)
                l1 = l1.next
        while l1 or l2:
            if l1:
                attach(l1)
                l1 = l1.next
            if l2:
                attach(l2)
                l2 = l2.next
        return self.H
                
                

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        h, c = None,None
        while l1 and l2:
            t=None
            if l1.val<=l2.val:
                t = l1
                l1=l1.next
            else:
                t=l2
                l2 = l2.next
            if not c:c=t
            else:h.next=t
            h = t
        if not c and l1:return l1
        if not c and l2:return l2
        if l1: h.next=l1
        if l2: h.next=l2
        return c
          
          
          
 class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        s=ListNode(0)
        t = s
        while l1 and l2:
            if l1.val>=l2.val:
                t.next=l2
                l2=l2.next
            else:
                t.next=l1
                l1=l1.next
            t=t.next
        if l1:
            t.next = l1
        if l2:
            t.next = l2
        return s.next        
