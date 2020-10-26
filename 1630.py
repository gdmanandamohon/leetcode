'''
l4zyc0d3r /// 1630 /// Sun Oct 25, 2020
'''
class Solution:
    def checkArithmeticSubarrays(self, N: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i in range(len(r)):
            t = N[l[i]:r[i]+1]
            t.sort()
            d, f=None, True
            for i in range(1,len(t)):
                if i==1: d = t[i] - t[i-1]
                else:
                    if t[i] - t[i-1] !=d:
                        f = False
                        break
            ans.append(f)
        return ans
