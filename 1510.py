'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        n+=1
        print(n)
        self.wl = [False for i in range(n)]
        self.wl[1] =True
        for i in range(2, n):
            root = int(pow(i, 0.5))
            #print(i,root)
            for j in range(root, 0, -1):
                t= i -j*j
                #print("  => ", j, t)
                if self.wl[t] == False:
                    self.wl[i] = True
                    break;
        return self.wl[n-1]
