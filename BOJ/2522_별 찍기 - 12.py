# 2023-04-10
import sys

N = int(sys.stdin.readline())

for n in range(1, N+1) :
    print(' '*(N-n) + '*'*(n))
for n in range(1, N) :
    print(' '*(n) + '*'*(N-n))