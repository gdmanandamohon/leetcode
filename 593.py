'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        l = [p1,p2,p3,p4]
        st = set()
        x,y = l[0][0],l[0][1]
        for i,[x,y] in enumerate(l):
            for j,[x1,y1] in enumerate(l):
                if i==j: continue
                elif x1==x and y ==y1: return False
                else:
                    st.add( (x-x1)*(x-x1)+  (y-y1)*(y-y1))
        return len(st)<=2
