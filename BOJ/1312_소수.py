# 2024-01-29
a, b, n = map(int, input().split())
a = a % b
ans = 0
for _ in range(n) :
    a *= 10
    ans = a // b
    a = a % b
print(ans)