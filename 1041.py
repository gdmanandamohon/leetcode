'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
"GLGLGGLGL"
class Solution:
    def isRobotBounded(self, i: str) -> bool:
        
        ax = [[1,0], [1,1], [-1,0], [-1, -1]]
        se = []
        d = 0
        cx, cy = 0,0
        for x in i: 
            if x =='L':
                d = (d+1)%4
            elif x == 'R':
                d = (d+3)%4
            else:
                cx, cy = cx +ax[d][0], cy+ax[d][1]
                #print(x, d, cx,cy)
        '''if cx == 0 ==cy:return True 
        if d ==0:return False
        return True'''
        if (cx != 0 or cy!=0) and d==0:return False
        return True
                
