'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
#O(N*N)
class MedianFinder:

    def __init__(self):
        self.ar = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.ar, num)
        #print(self.ar)
    def findMedian(self) -> float:
        l = len(self.ar)
        
        if l ==0: return 0
        elif l ==1: return self.ar[0]
        elif l ==2: return sum(self.ar)/2
        elif l%2==0:
            return (self.ar[l//2-1]+self.ar[l//2])/2
        else:
            return self.ar[l//2]



#O(log(N))
class MedianFinder:

    def __init__(self):
        self.MNH =[]
        self.MXH =[]
        self.cnt=0
        
    def addNum(self, num: int) -> None:
        if self.cnt == 0:
            heapq.heappush(self.MNH,-num)
            self.cnt+=1
        elif num < -self.MNH[0]:
            heapq.heappush(self.MNH,-num)
        else:
            heapq.heappush(self.MXH,num)
            
        if len(self.MNH) - len(self.MXH) >=2:
            heapq.heappush(self.MXH, -heapq.heappop(self.MNH))
        elif len(self.MXH) - len(self.MNH) >=2:
            heapq.heappush(self.MNH, -heapq.heappop(self.MXH))
        #print(self.MNH, self.MXH)
        
        
    def findMedian(self) -> float:
        if len(self.MNH)>len(self.MXH):
            return -self.MNH[0]
        elif len(self.MNH)==len(self.MXH):
            return (self.MXH[0]-self.MNH[0])/2
        else: return self.MXH[0]

