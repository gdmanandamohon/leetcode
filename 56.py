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


#Choose the interval which has started first and also maximum length
class Solution:
    def merge(self, I: List[List[int]]) -> List[List[int]]:
        I.sort(key = lambda x:(x[0], x[1]-x[0]))
        i,l = 0,len(I) 
        st, en = 0,0
        ans =[]
        while i<l:
            st, en = I[i][0], I[i][1]
            #print(st,en)
            while (i+1<l) and (I[i+1][0]<=en ): 
                i+=1
                st = min(I[i][0], st)
                en = max(en, I[i][1])
            ans.append([st,en])
            i+=1
        return ans
