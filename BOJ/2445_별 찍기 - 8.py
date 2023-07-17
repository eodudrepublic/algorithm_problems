# 2023-04-08 (04-09)
import sys

N = int(sys.stdin.readline())

for n in range(1, N+1) :
    print('*'*(n) + ' '*(N-n)*2 + '*'*(n))
for n in range(1, N) :
    print('*'*(N-n) + ' '*(n*2) + '*'*(N-n))