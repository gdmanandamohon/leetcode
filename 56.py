'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    def merge(self, I: List[List[int]]) -> List[List[int]]:
        I.sort(key = lambda x : x[0],)
        i, st, en, l = 1, I[0][0],I[0][1], len(I)
        ans =[]
        while i<l:
            if I[i][0]<=en:
                if I[i][1] >= en: en = I[i][1]
            else:
                ans.append([st,en])
                st,en = I[i][0],I[i][1]
            i+=1
        ans.append([st,en])
        return ans
