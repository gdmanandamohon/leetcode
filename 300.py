'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
#O(N*N)
class Solution:
    def lengthOfLIS(self, N: List[int]) -> int:
        dp = [1 for _ in N]
        for i in range(len(N)):
            for j in range(i+1, len(N)):
                if N[i]<N[j]:
                    dp[j] = max(dp[j], dp[i]+1)
        return max(dp)


#O(N.log(N))
class Solution:
    def lengthOfLIS(self, N: List[int]) -> int:
        ans =[]
        for n in N:
            idx = bisect_left(ans, n)
            if len(ans)<= idx:
                ans.append(n)
            else:
                ans[idx]=n
        return len(ans)
