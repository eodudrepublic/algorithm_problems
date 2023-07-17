# 2023-04-08 (04-09)
import sys

N = int(sys.stdin.readline())

for n in range(N) :
    print(' '*(n) + '*'*(N-n) + '*'*(N-n-1))
for n in range(2, N+1) :
    print(' '*(N-n) + '*'*(n) + '*'*(n-1))