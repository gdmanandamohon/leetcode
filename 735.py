'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

#All the asteroids heats each other 
class Solution:
    def asteroidCollision(self, A: List[int]) -> List[int]:
        st = []
        for n in A:
            if not st:
                st.append(n)
            else:
                if n<0:
                    while st and abs(st[-1])< abs(n):
                        st.pop()
                    if (st and st[-1]<0) or not st:
                        st.append(n)
                    elif st and st[-1]+n==0:
                        st.pop()
                elif st[-1]<=n:
                    st.append(n)
        return st
                    
                
                
 #Similar direction asteroids will not heat each other
 #O(N)
 def asteroidCollision(self, A: List[int]) -> List[int]:
        res = []
        for x in A:
            if not res or x>0:
                res.append(x)
            else:
                while res and res[-1]>0 and res[-1]+x<0:
                    res.pop()
                if res and res[-1]+x == 0:
                    res.pop()
                    continue
                elif res and  res[-1]<0:res.append(x)
                elif not res:
                    res.append(x)
                #print(x, res)
        return res               
