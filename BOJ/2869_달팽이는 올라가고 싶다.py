# 2023-09-10 (09-11)
a, b, v = map(int, input().split())
v -= a
t = v // (a-b)
if v % (a-b) != 0 : t += 1
print(t+1)