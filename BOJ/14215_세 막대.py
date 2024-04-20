# 2024-04-20 (04-21)
a, b, c = map(int, input().split())
s = a + b + c
m = max(a, b, c)
t = s - m - 1
if m <= t :
    print(s)
else :
    print(t + t + 1)