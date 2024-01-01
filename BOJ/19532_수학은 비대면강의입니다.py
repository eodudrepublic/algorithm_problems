# 2024-01-01
a, b, c, d, e, f = map(int, input().split())
print((c*e - b*f) // (a*e - b*d), (a*f - c*d) // (a*e - b*d))