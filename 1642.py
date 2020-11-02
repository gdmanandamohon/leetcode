'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

'''
[4,12,15,16,18]
8
1
[4,2,7,6,9,14,12]
5
1
[4,12,2,7,3,18,20,3,19]
10
2
[14,3,19,3]
17
0'''
class Solution:
    def furthestBuilding(self, H: List[int], B: int, L: int) -> int:
        pq=[]
        import heapq
        heapq.heapify(pq)
        c, l = -1, H[0]
        for i,x in enumerate(H):
            if i ==0: c+=1
            elif x-H[i-1]<=0:c+=1
            else:
                d = x-H[i-1]
                heapq.heappush(pq, d)
                if len(pq)>L:
                    d = heapq.heappop(pq)
                    if d<=B:
                        B -=d
                        c+=1
                    else: return c+L
        return min(c+L, len(H)-1)
            
                
            
                    
            
