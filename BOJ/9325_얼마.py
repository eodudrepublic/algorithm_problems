# 2023-07-30
import sys

T = int(sys.stdin.readline())
for t in range(T) : 
    s = int(sys.stdin.readline())
    N = int(sys.stdin.readline())
    for n in range(N) :
        q, p = map(int, sys.stdin.readline().split())
        s += q*p
    print(s)