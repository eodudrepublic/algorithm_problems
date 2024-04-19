# 2024-04-19
a, b, c, d = map(int, input().split())
ans = min(a, b, c-a, d-b)
print(ans)