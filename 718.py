'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        #Rolling hash O(N lon(N))
        '''mod = 10**9+7
        base = 103
        def roll(d):
            sa = set()
            hashv = 0
            for i in range(len(A)):
                #if A[i] ==0: A[i] =11
                if i<d:
                    hashv = (hashv*base + A[i])%mod
                    if i == d-1:sa.add(hashv)
                else:
                    hashv = (hashv*base + A[i])%mod
                    hashv = (hashv - A[i-d]* pow(base, d, mod)+mod)%mod
                    sa.add(hashv)
            #print(sa)
            hashv = 0
            for i in range(len(B)):
                #if B[i] ==0: B[i] =11
                if i<d:
                    hashv = (hashv*base + B[i])%mod
                    if i == d-1:
                        if hashv in sa: return True
                else:
                    hashv = (hashv*base + B[i])%mod
                    hashv = (hashv - B[i-d]* pow(base, d, mod)+mod)%mod
                    if hashv in sa: return True
            return False
        
        l,h, c = 0, len(A), None
        while l<=h:
            m = l+(h-l)//2
            f =roll(m)
            if f: c =m
            if roll(m):l = m+1
            else:h = m-1
        return c'''
        
        #DP approach
        # M*N where M and n is the length of the array of A and B respectively 
        dp = [ [0 for _ in range(len(A)+1)] for _ in range(len(B)+1)]
        for i in range(1, len(B)+1):
            for j in range(1, len(A)+1):
                if A[j-1] ==B[i-1]:
                    dp[i][j] = dp[i-1][j-1]+1
        #print(dp)
        return max(max(a) for a in dp)
