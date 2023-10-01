class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrom(sub_string):
            print('search for', sub_string)
            for i in range(len(sub_string)//2):
                if sub_string[i] != sub_string[~i]:return False
            return True
        lo, hi = 0, len(s)-1
        mx = ""
        while lo<=hi:
            md = lo + (hi-lo)//2 
            print("md", md)
            f = False
            for i in range(len(s)-md+1):
                if isPalindrom(s[i:md+i]):
                    f, mx  = True, s[i:md+i]
                    print("found", md)
                    break
            
            if f: 
                lo = md+1
            else: 
                hi = md-1
            print(md, mx, lo, hi )
        return mx

s = Solution()
#s.longestPalindrome("bkdsfkpdskfopdskpfksdpokfpodskopfkpdskfsdsfksdpkfpoksdopfkopdskfpksdpofksdpkfsdkb")
s.longestPalindrome("bkdkb")



