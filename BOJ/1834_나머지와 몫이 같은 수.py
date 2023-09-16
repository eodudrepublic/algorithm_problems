# 2023-09-16
N = int(input())
ans = 0
for _ in range(1, N) : ans += (N*_ + _)
print(ans)