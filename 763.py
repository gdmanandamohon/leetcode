'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
		
		#O(N*N)
        '''i , l = 0, len(S)
        ans = []
        while i<l:
            c = S[i]
            c_r_idx = S.rfind(c)
            j=i+1
            while j<c_r_idx:
                t_c_r_idx = S.rfind(S[j])
                if t_c_r_idx>c_r_idx:
                    c_r_idx = t_c_r_idx
                j+=1
            ans.append(c_r_idx-i+1)
            i = c_r_idx+1
        return ans'''
    
		
		#O(N)
        ans = [] 
        mp = {}
        for i,c in enumerate(S): mp[c] = i
        print(mp)
        i=0
        while i<len(S):
            c_r_idx = mp[S[i]]
            j=i+1
            while j<c_r_idx:
                t_c_r_idx = mp[S[j]]
                if t_c_r_idx>c_r_idx:
                    c_r_idx = t_c_r_idx
                j+=1
            ans.append(c_r_idx-i+1)
            i = c_r_idx+1
        return ans
            
        
            
