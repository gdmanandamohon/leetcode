
'''
@author: l4zyc0d3r 
People who are happy makes other happy. I am gonna finish it slowly but definitely.cdt
'''

A = [904,-40,523,-12,-335,-385,-124, -981,-31]
mx = ans = A[0]
csum = 0
for x in A:
    csum = max(csum+x, x)
    mx = max(mx, csum)
    print(x, mx, csum)
print(mx)
