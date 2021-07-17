'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''
#More optimized in calculating
#can find max block
class Solution:
    def trap(self, H: List[int]) -> int:
        if len(H)<3:return 0
        mx_idx = H.index(max(H))
        i=0
        w, cur_max  = 0, 0
        while i<mx_idx:
            if H[i]>cur_max:
                cur_max = H[i]
            w += cur_max - H[i]
            i+=1

        i = len(H)-1
        cur_max  = 0
        while i>mx_idx:
            if H[i]>cur_max:
                cur_max = H[i]
            w += cur_max - H[i]
            i-=1
        return w
            




class Solution:
    def trap(self, H: List[int]) -> int:
        if len(H)<3:return 0
        mx = max(H)
        mx_idx = H.index(mx)
        i=0
        w, mx  = 0, 0
        while i<mx_idx:
            if H[i] ==0:
                pass
            elif mx<H[i]:
                w+= (mx_idx-i)*(H[i]-mx)
                mx = H[i]
                w-=H[i]
            else:
                w-=H[i]
            i+=1
            
        i = len(H)-1
        mx = 0
        while i>mx_idx:
            if H[i] ==0:
                pass
            elif mx<H[i]:
                w+= (i-mx_idx)*(H[i]-mx)
                mx = H[i]
                w-=H[i]  
            else:
                w-=H[i]
            i-=1
        return w
