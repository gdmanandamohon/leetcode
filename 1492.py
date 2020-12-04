'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        for i in range(1, n+1):
            if n % i == 0:
                k-=1
            if k == 0: return i
        return -1
