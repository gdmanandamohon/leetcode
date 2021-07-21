'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
# O(N) * O(1)
class RandomizedSet:
    def __init__(self):
        self.li = []
        self.mp = {}
        
    def insert(self, val: int) -> bool:
        if val in self.mp:return False
        else:
            self.mp[val] = len(self.li)
            self.li.append(val)
            return True
            
    def remove(self, val: int) -> bool:
        if val in self.mp:
            idx = self.mp[val]   
            del self.mp[val]
            rep_val = self.li.pop()
            if idx==len(self.li):
                return True
            self.mp[rep_val] = idx
            self.li[idx] = rep_val
            return True
        else:return False
        
    def getRandom(self) -> int:
        return self.li[random.randint(1, len(self.li))-1]
