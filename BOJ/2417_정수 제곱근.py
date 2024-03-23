# 2024-03-23
import math
n = int(input())
sqrt = math.isqrt(n)
if sqrt**2 != n :
    print(int(sqrt) + 1)
else :
    print(int(sqrt))