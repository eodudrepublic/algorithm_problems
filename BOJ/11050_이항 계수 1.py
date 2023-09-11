# 2023-09-11
N, K = map(int, input().split())
if K > N / 2 : K = N - K
ans = 1
for n in range(K) : ans *= N - n
for k in range(1, K+1) : ans /= k
print(int(ans))