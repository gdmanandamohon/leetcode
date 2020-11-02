'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        sm,bs,po = 0,2,0
        while head:
            t= head.val
            head =head.next
            sm*=2
            sm+= t
        return sm
