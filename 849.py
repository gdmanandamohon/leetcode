'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
class Solution:
    def maxDistToClosest(self, S: List[int]) -> int:
        i,mx,c,f,lv=0,0,0, True,0
        while i<len(S):
            if S[i] ==0:
                c+=1
                if f: lv = max(lv, c)
            else:
                f = False
                mx = max(mx, c)
                c = 0
            i+=1
        if c and c>(mx+1)//2 and c>lv: return c
        elif lv>(mx+1)//2:return lv
        else: return (mx+1)//2
        



class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        c,mx, f=0,0, False
        for i in range(len(seats)):
            if seats[i] ==0:
                c+=1
            else:
                if f:
                    c = (c+1)//2   
                mx = max(c, mx)
                c=0
                f = True
        if not seats[len(seats)-1]:
            return  max(mx, c)
        else:
            return mx
