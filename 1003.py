'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    def isValid(self, s: str) -> bool:
        st = [] 
        for x in s:
            if x == 'c':
                if len(st)<2:return False
                else:
                    b, a = st.pop(), st.pop()
                    if a != 'a' or b!='b':return False
            else:st.append(x)
        return False if st else True
