# 2023-04-15 (04-16)
import sys
from collections import deque
    
N = int(sys.stdin.readline())

tn = 0
liN = deque([N])

while True :
    L = len(liN)
    for l in range(L) :
        n = liN.popleft()
        if n == 1 :
            print(tn)
            sys.exit()
        if n % 3 == 0 :
            liN.append(n//3)
        if n % 2 == 0 :
            liN.append(n//2)
        liN.append(n-1)     
    tn += 1