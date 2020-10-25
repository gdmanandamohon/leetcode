'''
l4zyc0d3r /// 1629 /// Sun Oct 25, 2020
'''
class Solution:
    def slowestKey(self, R: List[int], K: str) -> str:
        l = []
        R.insert(0,0)
        for i,x in enumerate(K):
            d = R[i+1] - R[i]
            l.append([d, x])
        l.sort(reverse= True) #, key = lambda x:-ord(x[1])
        return l[0][1]
