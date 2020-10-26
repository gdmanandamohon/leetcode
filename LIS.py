#LIS
n = [0,4,11,12,2,10,6,9,13,3,11,7,15]
dp = [1 for x in range(len(n))]
idx = [ '*' for x in range(len(n))]

for i in range(1, len(n)):
    for j in range(i):
        if n[j]< n[i]:
            if dp[j]+1>dp[i]:
                dp[i] = dp[j]+1
                idx[i] = j

print("max seq: ", max(dp))
print("dp Array ", dp)
print("idx array ", idx)

index = dp.index(max(dp))
while index!='*':
    print(n[index])
    index = idx[index]

