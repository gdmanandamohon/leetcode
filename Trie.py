class Trie:
    def __init__(self):
        self.kids = [None for _ in range(26)]
        self.isEnd =False 
    
    def insert(self, key):
        cur = self
        for k in key:
            print(cur.kids[ord(k)-ord('a')])
            if not cur.kids[ord(k)-ord('a')]:
                cur.kids[ord(k)-ord('a')] =  Trie()
            cur = cur.kids
        cur.isEnd=True
    
    def search(self, key):
        cur = self
        for k in key:
            if cur.kids[ord(k)-ord('a')] != -1:
                return False
            cur = cur.kids[ord(k)-ord('a')] 
        return cur.isEnd
board = ['amdklas', 'asdas','asdwqrew']
root = Trie()
for wd in board:
    root.insert(wd)
            
print(root.search(board[0]))
print(root.search('board'))
