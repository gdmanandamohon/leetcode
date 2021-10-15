'''
l4zyc0d3r /// 1629 /// Sun Oct 25, 2020
'''

class Solution:
    def slowestKey(self, R: List[int], K: str) -> str:
        k, t = None, 0
        st = 0 
        for i, x in enumerate(K):
            if i==0: k, t = x, R[i]
            elif R[i] -R[i-1]>t:
                k = x
                t = R[i] -R[i-1]
            elif R[i] -R[i-1]>=t and k<=x:
                k = x
                t = R[i] -R[i-1]
        return k


class Solution:
    def slowestKey(self, R: List[int], K: str) -> str:
        l = []
        R.insert(0,0)
        for i,x in enumerate(K):
            d = R[i+1] - R[i]
            l.append([d, x])
        l.sort(reverse= True) #, key = lambda x:-ord(x[1])
        return l[0][1]
