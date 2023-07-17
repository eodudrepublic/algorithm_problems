# 2023-04-08 (04-09)
import sys

N = int(sys.stdin.readline())

for n in range(N) :
    print(' '*(n) + '*'*(N-n) + '*'*(N-n-1))