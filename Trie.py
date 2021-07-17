class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    
    def _charToIndex(self,ch):
        return ord(ch)-ord('a')
    
    
    def insert(self, key):
        pCrawl = self.root
        
        for i,ch in enumerate(key):
            index = self._charToIndex(ch)
            if not pCrawl.children[index]:
                pCrawl.children[index] = TrieNode()
            pCrawl = pCrawl.children[index]
        pCrawl.isEndOfWord = True # mark last node as leaf
    
    def search(self, key):
        pCrawl = self.root
        for i,ch in enumerate(key):
            index = self._charToIndex(ch)
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
        return pCrawl.isEndOfWord
    
    
board = ['amdklas', 'asdas','asdwqrew']
root = Trie()
for wd in board:
    root.insert(wd)
            
print(root.search(board[0]))
print(root.search('board'))
