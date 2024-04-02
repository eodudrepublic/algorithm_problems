# 2024-04-02
ans = 1
N, M = map(int, input().split())
temp = N - M
M = min(temp, M)
for m in range(M) :
    ans *= N - m
for m in range(2, M+1) :
    ans //= m
print(ans)