# 2023-04-15 (04-16)
import sys

N = int(sys.stdin.readline())

nl = list(map(int, sys.stdin.readline().split()))
nl.sort(reverse=True)

t = 0
for n in range(N) :
    t += nl[n]*(n+1)

print(t)