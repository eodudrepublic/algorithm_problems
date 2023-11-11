# 2023-11-11
a, b = map(int, input().split())
if b > a : print(-1)
elif (a + b) % 2 == 0 : print((a+b)//2, a - (a+b)//2)
else : print(-1)