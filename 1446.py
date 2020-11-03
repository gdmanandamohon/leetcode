'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

#O(n) + O(n)
def maxPower(self, s: str) -> int:
    return max(len(list(x[1])) for x in itertools.groupby(s))

#O(n) + O(1)
def maxPower(self, s: str) -> int:
        mx,i = 0,0
        while i<len(s):
            j =i+1
            while j<len(s) and s[j] == s[i]: j+=1
            mx =max(mx, j-i)
            i=j
        return mx
