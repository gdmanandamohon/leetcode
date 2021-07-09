'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
class Solution:
    def largestRectangleArea(self, H: List[int]) -> int:
        st, mx, i  = [], 0, 0
        while i<len(H):
            if len(st)==0 or H[st[-1]]<=H[i]:
                st.append(i)
                i+=1
            else:
                rb = i 
                h = H[st.pop()]
                lb = st[-1] if len(st) else -1
                mx = max(mx, (rb-lb-1)*h)
        while len(st):
            rb = len(H)
            h = H[st.pop()]
            lb = st[-1] if len(st) else -1
            mx = max(mx, (rb-lb-1)*h)
            
        return mx

    def maximalRectangle(self, M: List[List[str]]) -> int:
        if not M: return 0
        mx = 0
        dp=[  1 if v == '1' else 0 for v in M[0]]
        mx = max(mx, self.largestRectangleArea(dp))
        for i in range(1, len(M)):
            for j in range(len(M[0])):
                if M[i][j] == '1': dp[j]+=1
                else:dp[j] = 0
            mx = max(mx, self.largestRectangleArea(dp))
        return mx
