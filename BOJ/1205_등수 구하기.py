# 2023-05-10 (05-11)
import sys
from collections import deque

N, nR, P = map(int, sys.stdin.readline().split())

if N == 0 :
    print(1)
    sys.exit()

rB = list(map(int, sys.stdin.readline().split())) + [-1]*(P-N)

r = -1
if nR <= rB[P-1] :
    print(-1)
    sys.exit()
for p in range(P) :
    if nR >= rB[p] :
        r = p+1
        break

print(r)