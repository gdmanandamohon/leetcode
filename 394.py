'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    def decodeString(self, s: str) -> str:
        i,l,st = 0, len(s),[]
        while i<l:
            if s[i] ==']':
                ts = ""
                while st and st[-1] != '[':
                    ts = st.pop()+ts
                st.pop()
                vl=""
                while st and st[-1].isnumeric():
                    vl = st.pop()+vl
                #print(s[i], ts, vl, st)
                vl = int(vl)
                st.append(ts*vl)
            else:st.append(s[i])
            i+=1
        return ''.join(st)
