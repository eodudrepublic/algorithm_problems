# 2024-02-16
from itertools import product

N, k = input().split()
L = len(N)
n = int(N)

arr = list(reversed(sorted(input().split())))
found = False
for l in range(L, 0, -1) :
    if found : break
    comb = product(arr, repeat=l)
    for _ in comb : 
        ans = int(''.join(_))
        if ans <= n : 
            found = True
            print(ans)
            break
