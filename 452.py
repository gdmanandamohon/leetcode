'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt

Examples(consider 4 cases of the following):

--------------------
     -----------
	----      ----
	     ---


[[10,16],[2,8],[1,6],[7,12]]
[[2,3],[2,3]]
[[1,2]]
[[1,2],[2,3],[3,4],[4,5]]
[[1,2],[3,4],[5,6],[7,8]]
[[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]'''
class Solution:
    def findMinArrowShots(self, P: List[List[int]]) -> int:
        P.sort(key = lambda x: x[1])
        #print(P)
        i, c = 0, 0
        while i<len(P):
            st, en = P[i]
            j = i+1
            while j<len(P) and (P[j][0]<=st or P[j][0]<=en):
                j+=1
            c+=1
            i=j
        return c
