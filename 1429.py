'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
class FirstUnique:

    def __init__(self, N: List[int]):
        self.m = collections.defaultdict(int)
        self.q = []
        for n in N:
            if n not in self.m:
                self.q.append(n)
            self.m[n]+=1

    def showFirstUnique(self) -> int:
        while self.q and self.m[self.q[0]]>1:
            self.q.pop(0)
        return self.q[0] if self.q else -1

    def add(self, value: int) -> None:
        if value not in self.m:
            self.q.append(value)
        self.m[value]+=1
