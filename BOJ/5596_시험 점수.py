# 2023-08-31
mk = list(map(int, input().split()))
ms = list(map(int, input().split()))
a = sum(mk)
b = sum(ms)
if b > a : print(b)
else : print(a)