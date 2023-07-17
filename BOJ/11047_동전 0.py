# 2023-04-15 (04-16)
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

vl = deque()
for n in range(N) :
    v = int(sys.stdin.readline())
    vl.appendleft(v)
    
cn = 0
while K != 0 :
    c = vl.popleft()
    n = K//c
    if n == 0 :
        continue
    cn += n 
    K -= c*n

print(cn)